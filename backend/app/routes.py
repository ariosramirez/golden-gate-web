import os
import requests
from flask import request, jsonify, current_app as app
from . import db
from .models import Image, Tag, Author, SyncStatus

UNSPLASH_API_URL = "https://api.unsplash.com/search/photos"
UNSPLASH_API_KEY = os.getenv("UNSPLASH_API_KEY")


current_page = 1  # Global variable to store the current page number


@app.route("/sync", methods=["GET"])
def sync_images():
    """
    Synchronize images from Unsplash API.

    This endpoint fetches 30 images from the Unsplash API based on the query parameter,
    and stores them in the local database, including the associated authors and tags.
    """
    sync_status = SyncStatus.query.first()
    current_page = sync_status.current_page

    query = request.args.get("query", "golden-gate")
    response = requests.get(
        UNSPLASH_API_URL,
        params={
            "query": query,
            "client_id": UNSPLASH_API_KEY,
            "per_page": 30,
            "page": current_page,
        },
    )
    data = response.json()

    for result in data["results"]:
        author_data = result["user"]
        author = Author.query.filter_by(id=author_data["id"]).first()
        if not author:
            profile_image = author_data["profile_image"]["large"]
            twitter_username = author_data.get("social", {}).get("twitter_username")
            author = Author(
                id=author_data["id"],
                username=author_data["username"],
                name=author_data["name"],
                profile_image=profile_image,
                twitter_username=twitter_username,
            )
            db.session.add(author)

        image = Image.query.filter_by(id=result["id"]).first()
        if not image:
            image = Image(
                id=result["id"], url=result["urls"]["regular"], author_id=author.id
            )
            db.session.add(image)

            for tag_data in result["tags"]:
                tag = Tag.query.filter_by(title=tag_data["title"]).first()
                if not tag:
                    tag = Tag(title=tag_data["title"])
                    db.session.add(tag)
                image.tags.append(tag)
        db.session.commit()

    sync_status.current_page += 1  # Increment the page number
    db.session.commit()  # Save the new page number

    return jsonify({"message": "Images synchronized successfully!"})


@app.route("/images", methods=["GET"])
def get_images():
    """
    Get images from the database with pagination.

    This endpoint returns a list of images stored in the local database,
    including the associated authors and tags.
    """
    page = request.args.get("page", 1, type=int)
    limit = request.args.get("limit", 30, type=int)
    offset = (page - 1) * limit
    images = Image.query.offset(offset).limit(limit).all()
    return jsonify([image.to_dict() for image in images])

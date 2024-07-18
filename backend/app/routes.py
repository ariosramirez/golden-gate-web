import os
import requests
from flask import request, jsonify, current_app as app
from . import db
from .models import Image, Tag, Author

UNSPLASH_API_URL = "https://api.unsplash.com/search/photos"
UNSPLASH_API_KEY = os.getenv('UNSPLASH_API_KEY')


@app.route('/sync', methods=['GET'])
def sync_images():
    """
    Synchronize images from Unsplash API.

    This endpoint fetches images from the Unsplash API based on the query parameter,
    and stores them in the local database, including the associated authors and tags.
    """
    query = request.args.get('query', 'golden-gate')
    response = requests.get(UNSPLASH_API_URL, params={'query': query, 'client_id': UNSPLASH_API_KEY})
    data = response.json()

    for result in data['results']:
        author_data = result['user']
        author = Author.query.filter_by(id=author_data['id']).first()
        if not author:
            author = Author(id=author_data['id'], username=author_data['username'], name=author_data['name'])
            db.session.add(author)

        image = Image.query.filter_by(id=result['id']).first()
        if not image:
            image = Image(id=result['id'], url=result['urls']['regular'], author_id=author.id)
            db.session.add(image)

            for tag_data in result['tags']:
                tag = Tag.query.filter_by(title=tag_data['title']).first()
                if not tag:
                    tag = Tag(title=tag_data['title'])
                    db.session.add(tag)
                image.tags.append(tag)
        db.session.commit()

    return jsonify({'message': 'Images synchronized successfully!'})


@app.route('/images', methods=['GET'])
def get_images():
    """
    Get all images from the database.

    This endpoint returns a list of all images stored in the local database,
    including the associated authors and tags.
    """
    images = Image.query.all()
    return jsonify([image.to_dict() for image in images])

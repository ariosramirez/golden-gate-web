import unittest
from app import db, create_app
from app.models import Image, Tag, Author, SyncStatus


class TestModels(unittest.TestCase):
    def setUp(self):
        self.app = create_app()
        self.app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///:memory:"
        self.app_context = self.app.app_context()
        self.app_context.push()
        db.create_all()

    def tearDown(self):
        db.session.remove()
        db.drop_all()
        self.app_context.pop()

    def test_image_model(self):
        author = Author(
            id="1",
            username="author1",
            name="Author One",
            profile_image="http://example.com/image.jpg",
        )
        tag1 = Tag(id=1, title="Tag1")
        tag2 = Tag(id=2, title="Tag2")
        image = Image(
            id="img1",
            url="http://example.com/image.jpg",
            author=author,
            tags=[tag1, tag2],
        )

        db.session.add(author)
        db.session.add(tag1)
        db.session.add(tag2)
        db.session.add(image)
        db.session.commit()

        self.assertEqual(image.url, "http://example.com/image.jpg")
        self.assertEqual(image.author.username, "author1")
        self.assertEqual(len(image.tags), 2)

    def test_image_to_dict(self):
        author = Author(
            id="1",
            username="author1",
            name="Author One",
            profile_image="http://example.com/image.jpg",
        )
        tag = Tag(id=1, title="Tag1")
        image = Image(
            id="img1", url="http://example.com/image.jpg", author=author, tags=[tag]
        )

        db.session.add(author)
        db.session.add(tag)
        db.session.add(image)
        db.session.commit()

        image_dict = image.to_dict()
        self.assertEqual(image_dict["url"], "http://example.com/image.jpg")
        self.assertEqual(image_dict["author"]["username"], "author1")
        self.assertEqual(len(image_dict["tags"]), 1)

    def test_tag_model(self):
        tag = Tag(id=1, title="Tag1")
        db.session.add(tag)
        db.session.commit()

        self.assertEqual(tag.title, "Tag1")

    def test_tag_to_dict(self):
        tag = Tag(id=1, title="Tag1")
        db.session.add(tag)
        db.session.commit()

        tag_dict = tag.to_dict()
        self.assertEqual(tag_dict["title"], "Tag1")

    def test_author_model(self):
        author = Author(
            id="1",
            username="author1",
            name="Author One",
            profile_image="http://example.com/image.jpg",
            twitter_username="author1_twitter",
        )
        db.session.add(author)
        db.session.commit()

        self.assertEqual(author.username, "author1")
        self.assertEqual(author.profile_image, "http://example.com/image.jpg")
        self.assertEqual(author.twitter_username, "author1_twitter")

    def test_author_to_dict(self):
        author = Author(
            id="1",
            username="author1",
            name="Author One",
            profile_image="http://example.com/image.jpg",
            twitter_username="author1_twitter",
        )
        db.session.add(author)
        db.session.commit()

        author_dict = author.to_dict()
        self.assertEqual(author_dict["username"], "author1")
        self.assertEqual(author_dict["profile_image"], "http://example.com/image.jpg")
        self.assertEqual(author_dict["twitter_username"], "author1_twitter")

    def test_sync_status_model(self):
        sync_status = SyncStatus(id=20, current_page=20)
        db.session.add(sync_status)
        db.session.commit()

        self.assertEqual(sync_status.current_page, 20)


if __name__ == "__main__":
    unittest.main()

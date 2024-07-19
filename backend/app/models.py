from . import db

image_tags = db.Table('image_tags',
    db.Column('image_id', db.String, db.ForeignKey('image.id'), primary_key=True),
    db.Column('tag_id', db.Integer, db.ForeignKey('tag.id'), primary_key=True)
)

class Image(db.Model):
    id = db.Column(db.String, primary_key=True)
    url = db.Column(db.String, nullable=False)
    author_id = db.Column(db.String, db.ForeignKey('author.id'), nullable=False)
    tags = db.relationship('Tag', secondary=image_tags, lazy='subquery',
                           backref=db.backref('images', lazy=True))

    def to_dict(self):
        return {
            'id': self.id,
            'url': self.url,
            'author': self.author.to_dict(),
            'tags': [tag.to_dict() for tag in self.tags]
        }

class Tag(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String, nullable=False)

    def to_dict(self):
        return {
            'id': self.id,
            'title': self.title
        }

class Author(db.Model):
    id = db.Column(db.String, primary_key=True)
    username = db.Column(db.String, nullable=False)
    name = db.Column(db.String, nullable=False)
    profile_image = db.Column(db.String, nullable=False)  # Profile image URL
    twitter_username = db.Column(db.String, nullable=True)  # Twitter username
    images = db.relationship('Image', backref='author', lazy=True)

    def to_dict(self):
        return {
            'id': self.id,
            'username': self.username,
            'name': self.name,
            'profile_image': self.profile_image,
            'twitter_username': self.twitter_username
        }

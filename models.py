"""Models for Blogly."""


"""Demo file showing off a model for SQLAlchemy."""


from flask_sqlalchemy import SQLAlchemy
import datetime
db = SQLAlchemy()


def connect_db(app):
    """Connect to database."""

    db.app = app
    db.init_app(app)


class User(db.Model):
    """User."""
    __tablename__ = "users"

    id = db.Column(db.Integer,
                   primary_key=True,
                   autoincrement=True)
    first_name = db.Column(db.String(50),
                           nullable=False)
    last_name = db.Column(db.String(50),
                          nullable=False)
    image_url = db.Column(db.String(2000),
                          nullable=False, default="https://cdn.pixabay.com/photo/2015/10/05/22/37/blank-profile-picture-973460_1280.png")

    posts = db.relationship('Post')

    def __repr__(self):
        return f"User {self.first_name} {self.last_name}>"

    @property
    def full_name(self):
        """Return full name of user."""
        return f"{self.first_name} {self.last_name}"


class Post(db.Model):
    """Post."""
    __tablename__ = "posts"

    id = db.Column(db.Integer,
                   primary_key=True,
                   autoincrement=True)
    title = db.Column(db.String(50),
                      nullable=False)
    content = db.Column(db.String(1000),
                        nullable=False)
    created_at = db.Column(db.DateTime,
                           nullable=False,
                           default=datetime.datetime.now)
    user_id = db.Column(db.Integer, db.ForeignKey(
        'users.id'))

    usr = db.relationship('User')

    def __repr__(self):
        return f"<Post {self.title} {self.content}>"

    @property
    def format_date(self):
        """Format the date-time to look readable"""
        return self.created_at.strftime("%a %b %-d %Y, %-I:%M %p")


class Tag(db.Model):
    """Tag."""
    __tablename__ = 'tags'

    id = db.Column(db.Integer,
                   primary_key=True,
                   autoincrement=True)
    name = db.Column(db.String(50), nullable=False)

    posts = db.relationship('Post', secondary='post_tags',
                            cascade="all,delete", backref='tags')

    def __repr__(self):
        return f"<Tag {self.id} {self.name}>"


class Post_Tag(db.Model):
    """Post_Tag."""
    __tablename__ = 'post_tags'

    post_id = db.Column(db.Integer,
                        db.ForeignKey('posts.id'), primary_key=True,)
    tag_id = db.Column(db.Integer,
                       db.ForeignKey('tags.id'), primary_key=True,)

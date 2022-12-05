"""Seed file to make sample data for user db."""

from models import User, Post, Tag, Post_Tag, db
from app import app


# Add users
user1 = User(first_name='Alan', last_name="Alda",
             image_url='https://img.freepik.com/free-photo/young-bearded-man-with-striped-shirt_273609-5677.jpg?size=626&ext=jpg')
user2 = User(first_name='Joel', last_name="Burton",
             image_url='https://cdn.pixabay.com/photo/2014/04/02/17/07/user-307993__340.png')
user3 = User(first_name='Jane', last_name="Smith")

# Add Posts
post1 = Post(title='First Post!', content='Oh, hai.', usr=user2)

post2 = Post(title='Yet Another Post',
             content='Here is the content.', usr=user2)

post3 = Post(title='Flask Is Awesome',
             content='Flask is a lovely framework for building cool things.', usr=user2)

# Add tags
tag1 = Tag(name='Fun')

tag2 = Tag(name='Crazy')

tag3 = Tag(name='Deep')


# Create all tables
with app.app_context():
    db.drop_all()
    db.create_all()
    User.query.delete()
    Post.query.delete()
    Tag.query.delete()
    Post_Tag.query.delete()

    # db.session.add_all([user1, user2, user3])
    db.session.add_all([user1, user2, user3, post1,
                       post2, post3, tag1, tag2, tag3])
    db.session.commit()

    post1.tags.append(tag1)
    post1.tags.append(tag2)
    post2.tags.append(tag3)
    post3.tags.append(tag1)
    db.session.commit()

    tag = Tag.query.get(1)
    post = tag.posts

    db.session.close()

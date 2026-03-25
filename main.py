from client import APIClient

client = APIClient()

# GET all posts
posts = client.get_posts()
print("First 2 posts:", posts[:2])

# GET single post
post = client.get_post_by_id(1)
print("Single post:", post)

# CREATE post
new_post = client.create_post({
    "title": "New Post",
    "body": "This is a test post",
    "userId": 1
})
print("Created:", new_post)

# UPDATE post
updated_post = client.update_post(1, {
    "title": "Updated Title",
    "body": "Updated content",
    "userId": 1
})
print("Updated:", updated_post)

# DELETE post
deleted = client.delete_post(1)
print("Deleted:", deleted)from client import APIClient

client = APIClient()

# GET all posts
posts = client.get_posts()
print("First 2 posts:", posts[:2])

# GET single post
post = client.get_post_by_id(1)
print("Single post:", post)

# CREATE post
new_post = client.create_post({
    "title": "New Post",
    "body": "This is a test post",
    "userId": 1
})
print("Created:", new_post)

# UPDATE post
updated_post = client.update_post(1, {
    "title": "Updated Title",
    "body": "Updated content",
    "userId": 1
})
print("Updated:", updated_post)

# DELETE post
deleted = client.delete_post(1)
print("Deleted:", deleted)

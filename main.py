from client import APIClient

client = APIClient()

posts = client.get_posts()
print(posts[:2])  # print first 2 posts

single_post = client.get_post_by_id(1)
print(single_post)
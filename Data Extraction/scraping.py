from mastodon import Mastodon
from dotenv import load_dotenv
import os
from hdfs import InsecureClient
import datetime
import json

load_dotenv()

# Connect to the mastodon API
mastodon = Mastodon(
    client_id=os.getenv('Client_key'),  # Your Client ID
    client_secret=os.getenv('Client_secret'),  # Your Client Secret
    access_token=os.getenv('Access_token'),  # Your Access Token
    api_base_url="https://mastodon.social"
)

# Initialize an HDFS client
hdfs_client = InsecureClient('http://localhost:9870', user='hadoop')

# Get current date and time
now = datetime.datetime.now()
directory_path = '/raw/' + str(now.year) + '-' + str(now.month) + '-' + str(now.day)

# Check if the directory already exists
if not hdfs_client.status(directory_path, strict=False):
    hdfs_client.makedirs(directory_path)

# Define the HDFS path where you want to save the data
hdfs_path = directory_path + '/' + str(now.hour) + '-' + str(now.minute) + '/mastodon.txt'

last_toot_id = None
public_posts = []

# Specify the number of runs
n = 200

for _ in range(n):
    # Retrieve public posts
    new = mastodon.timeline_public(limit=40, since_id=last_toot_id)

    # Append the current run's public posts to the list
    public_posts.extend(new)
    print(f'Number of posts retrieved: {str(len(public_posts))}', end='\r')

    # Update the last_toot_id
    if public_posts:
        latest_toot = public_posts[0]
        last_toot_id = str(latest_toot['id'])


# Create a text file to store the selected columns as JSON objects
with hdfs_client.write(hdfs_path) as writer:
    for i, post in enumerate(public_posts):
        formatted_post = {
            'account_id': post['account']['id'],
            'account_username': post['account']['username'],
            'account_followers_count': post['account']['followers_count'],
            'replies_count': post['replies_count'],
            'reblogs_count': post['reblogs_count'],
            'favourites_count': post['favourites_count'],
            'account_created_at': post['account']['created_at'].isoformat(),
            'url': post['url'],
            'language': post['language'],
            'content': post['content']
        }
        # Encode the JSON as bytes
        formatted_post_bytes = json.dumps(formatted_post).encode('utf-8')
        writer.write(formatted_post_bytes + b'\n')

print('Data saved successfully to HDFS: ' + hdfs_path)

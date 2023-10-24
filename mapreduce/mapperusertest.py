from hdfs import InsecureClient
import json

# Initialize an HDFS client
hdfs_client = InsecureClient('http://localhost:9870', user='hadoop')

# Specify the HDFS path to the file you want to read
hdfs_path = '/raw/2023-10-20/15-20/mastodon.txt'  # Update this path

# Mapper
def map_to_followers(data):
    for line in data:
        try:
            # Load the JSON data from the line
            post = json.loads(line)
            account_username = post.get('account_username')
            account_followers_count = post.get('account_followers_count')
            if account_username is not None and account_followers_count is not None:
                # Output the username and their number of followers
                print(f"Username: {account_username}, Followers: {account_followers_count}")
        except json.JSONDecodeError as e:
            print(f"Error decoding JSON: {e}")
        except KeyError as e:
            print(f"Key not found: {e}")

# Read the data from the specified HDFS file
with hdfs_client.read(hdfs_path, encoding='utf-8') as reader:
    data = reader.read().splitlines()

# Apply the mapper function to the data
map_to_followers(data)

## Initialize a dictionary to store usernames and their total followers
user_followers = {}

# Iterate through the mapped data
for line in data:
    try:
        username, followers_count = line.strip().split(',')
        username = username.strip()
        followers_count = int(followers_count.strip())

        if username in user_followers:
            # If the username is already in the dictionary, add the followers_count to the existing total
            user_followers[username] += followers_count
        else:
            # If the username is not in the dictionary, initialize the entry with the followers_count
            user_followers[username] = followers_count
    except ValueError:
        # Handle lines that don't match the expected format (e.g., missing data)
        pass

# Sort the user_followers dictionary by follower count in descending order
sorted_users = sorted(user_followers.items(), key=lambda x: x[1], reverse=True)

# Display the top 10 users with the most followers
for i, (username, total_followers) in enumerate(sorted_users[:10]):
    print(f"Top {i+1}: Username: {username}, Total Followers: {total_followers}")

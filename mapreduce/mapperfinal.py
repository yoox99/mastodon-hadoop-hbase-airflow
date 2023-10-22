import sys
import json
import re
from urllib.parse import urlparse

def process_data(input_data):
    pattern = r'http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+'
    
    for line in input_data:
        try:
            # Split the line based on the separator (tab in this example)
            parts = line.strip().split('\t')

            # Extract data from the TXT file
            created_at = parts[0]
            account_json = parts[1]
            media_attachments_json = parts[2]
            emojis_json = parts[3]
            content = parts[4]

            data = json.loads(account_json)  # Parse the JSON data in the account field

            toot_with_media_dict = {}
            toot_with_media_id = 'toot_with_media'
            
            followers = int(data.get('followers_count', 0))
            reblogs_count = int(data.get('reblogs_count', 0))
            favourites_count = int(data.get('favourites_count', 0))

            engagement_rate = (reblogs_count + favourites_count) / followers if followers > 0 else 0

            user_id = 'user:' + str(data.get('id'))
            user_data = {
                "date": created_at,
                "followers": followers,
                "engagement_rate": engagement_rate
            }

            croissance_id = "croissance:" + data.get('created_at').split('-')[0] + '-' + data.get('created_at').split('-')[1]
            croissance_data = {"value": 1, "user_id": user_id}

            # Emit key-value pairs for the reducer
            print(f"{user_id}\t{user_data}")
            print(f"{croissance_id}\t{croissance_data}")
            
            if media_attachments_json:
                toot_with_media_dict["value"] = 1
                print(f"{toot_with_media_id}\t{toot_with_media_dict}")

            language_id = "language:" + data.get('language')
            language_data = {"value": 1}
            print(f"{language_id}\t{language_data}")

            if emojis_json:
                emojis = json.loads(emojis_json)
                for emoji in emojis:
                    emoji_id = "emoji:" + emoji.get('shortcode')
                    emoji_data = {"value": 1}
                    print(f"{emoji_id}\t{emoji_data}")

            if content:
                urls = re.search(pattern, content)
                if urls:
                    website_id = "website:" + urlparse(urls.group(0)).netloc
                    website_data = {"value": 1}
                    print(f"{website_id}\t{website_data}")

        except Exception as e:
            # Log exceptions to standard error
            print(f"Error: {str(e)}", file=sys.stderr)

# Example usage of the process_data function
if __name__ == "__main__":
    input_data = sys.stdin
    process_data(input_data)

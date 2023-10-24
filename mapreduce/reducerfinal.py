# #!/usr/bin/env python3
# import sys

# # Initialize variables to keep track of different keys and their respective aggregates
# current_user = None
# current_croissance = None
# current_language = None
# current_toot_with_media = None
# current_emoji = None
# current_url = None

# earliest_followers = float('inf')
# old_time = "00:00:00"

# engagement_rate_sum = 0.0000
# croissance_sum = 0
# language_sum = 0
# toot_with_media_sum = 0
# emoji_sum = 0
# url_sum = 0
# count = 1

# unique_users_roissance = []

# user_dict = {}
# croissance_dict = {}
# language_dict = {}
# toot_with_media_dict = {}
# emoji_dict = {}
# url_dict = {}

# # Read input lines from standard input
# for line in sys.stdin:
#     key = line.strip().split('\t')[0]
#     key = key.strip()

#     # Check the key to determine the type of record

#     # If the key starts with "user," it's a user record
#     if key.startswith("user"):
#         user, strdata = line.strip().split('\t')
#         # Parse the JSON data in the record
#         data = eval(strdata.strip())
#         followers = int(data["followers"])
#         time = data['date']
#         engagement_rate = float(data["engagement_rate"])

#         # Process user records
#         if current_user == user:
#             if time > old_time:
#                 old_time = time
#                 earliest_followers = followers
#             engagement_rate_sum += engagement_rate
#             count += 1
#         else:
#             if current_user is not None:
#                 if count > 0:
#                     engagement_rate_avg = engagement_rate_sum / count
#                     user_dict["engagement_rate"] = engagement_rate_avg
#                     user_dict["followers"] = earliest_followers
#                     print(f"{current_user}\t{user_dict}")
#             current_user = user
#             earliest_followers = followers
#             old_time = time
#             engagement_rate_sum = engagement_rate
#             count = 1

#     # If the key starts with "croissance," it's a croissance record
#     elif key.startswith("croissance"):
#         croissance, strdata = line.strip().split('\t')
#         data = eval(strdata.strip())
#         user_id = data["user_id"]

#         # Process croissance records
#         if croissance == current_croissance:
#             if current_croissance is not None:
#                 if user_id not in unique_users_roissance:
#                     unique_users_roissance.append(user_id)
#                     croissance_sum += data["value"]
#         elif croissance != current_croissance:
#             if current_croissance is not None:
#                 croissance_dict["count"] = croissance_sum
#                 print(f"{current_croissance}\t{croissance_dict}")
#             current_croissance = croissance
#             croissance_sum = 1
#             unique_users_roissance = [user_id]

#     # If the key starts with "language," it's a language record
#     elif key.startswith("language"):
#         language, strdata = line.strip().split('\t')
#         data = eval(strdata.strip())

#         # Process language records
#         if language == current_language:
#             if current_language is not None:
#                 language_sum += data["value"]
#         elif language != current_language:
#             if current_language is not None:
#                 language_dict["count"] = language_sum
#                 print(f"{current_language}\t{language_dict}")
#             current_language = language
#             language_sum = 1

#     # If the key starts with "toot_with_media," it's a toot_with_media record
#     elif key.startswith("toot_with_media"):
#         toot_with_media, strdata = line.strip().split('\t')
#         data = eval(strdata.strip())

#         # Process toot_with_media records
#         if toot_with_media == current_toot_with_media:
#             if current_toot_with_media is not None:
#                 toot_with_media_sum += data["value"]
#         elif toot_with_media != current_toot_with_media:
#             if current_toot_with_media is not None:
#                 toot_with_media_dict["count"] = toot_with_media_sum
#                 print(f"{current_toot_with_media}\t{toot_with_media_dict}")
#             current_toot_with_media = toot_with_media
#             toot_with_media_sum = 1

#     # If the key starts with "emoji," it's an emoji record
#     elif key.startswith("emoji"):
#         emoji_id , strdata = line.strip().split('\t')
#         data = eval(strdata.strip())

#         # Process emoji records
#         if emoji_id == current_emoji:
#             if current_emoji is not None:
#                 emoji_sum += data["value"]
#         elif emoji_id != current_emoji:
#             if current_emoji is not None:
#                 emoji_dict["count"] = emoji_sum
#                 print(f"{current_emoji}\t{emoji_dict}")
#             current_emoji = emoji_id
#             emoji_sum = 1

#     # If the key starts with "website," it's a website record
#     elif key.startswith("website"):
#         website_id , strdata = line.strip().split('\t')
#         data = eval(strdata.strip())

#         # Process website records
#         if website_id == current_url:
#             if current_url is not None:
#                 url_sum += data["value"]
#         elif website_id != current_url:
#             if current_url is not None:
#                 url_dict["count"] = url_sum
#                 print(f"{current_url}\t{url_dict}")
#             current_url = website_id
#             url_sum = 1

# # Print the last data for each category

# # User records
# if current_user is not None:
#     if count > 0:
#         engagement_rate_avg = engagement_rate_sum / count
#         print(f"{current_user}\t{user_dict}")

# # Croissance records
# if current_croissance is not None:
#     croissance_dict["count"] = croissance_sum
#     print(f"{current_croissance}\t{croissance_dict}")

# # Language records
# if current_language is not None:
#     language_dict["count"] = language_sum
#     print(f"{current_language}\t{language_dict}")

# # Toot with media records
# if current_toot_with_media is not None:
#     toot_with_media_dict["count"] = toot_with_media_sum
#     print(f"{current_toot_with_media}\t{toot_with_media_dict}")

# # Emoji records
# if current_emoji is not None:
#     emoji_dict["count"] = emoji_sum
#     print(f"{current_emoji}\t{emoji_dict}")

# # Website records
# if current_url is not None:
#     url_dict["count"] = url_sum
#     print(f"{current_url}\t{url_dict}")


#!/usr/bin/env python3
import sys
import happybase
import ast
import json

# HBase connection settings
hbase_host = 'localhost'  # Replace with your HBase host
hbase_port = 9090  # Default HBase port

# Connect to HBase
connection = happybase.Connection(host=hbase_host, port=hbase_port)
create 'croissance_table', 'cf'
create 'language_table', 'cf'
create 'toot_with_media_table', 'cf'
create 'emoji_table', 'cf'
create 'website_table', 'cf'
# Open the tables
user_table = connection.table(f'user_table')
croissance_table = connection.table(f'croissance_table')
language_table = connection.table(f'language_table')
toot_with_media_table = connection.table(f'toot_with_media_table')
emoji_table = connection.table(f'emoji_table')
website_table = connection.table(f'website_table')

current_user = None
current_croissance = None
current_language = None
current_toot_with_media = None
current_emoji = None
current_website = None

earliest_followers = float('inf')
old_time = "00:00:00"

engagement_rate_sum = 0.0000
croissance_sum = 0
language_sum = 0
toot_with_media_sum = 0
emoji_sum = 0
website_sum = 0
count = 1

unique_users_roissance = []

for line in sys.stdin:
    key, strdata = line.strip().split('\t')
    data = ast.literal_eval(strdata)

    # Handle user data
    if key.startswith("user"):
        user_id = key
        followers = int(data["followers"])
        time = data['date']
        engagement_rate = float(data["engagement_rate"])

        if user_id == current_user:
            if time > old_time:
                old_time = time
                earliest_followers = followers
            engagement_rate_sum += engagement_rate
            count += 1
        else:
            if current_user is not None:
                if count > 0:
                    engagement_rate_avg = engagement_rate_sum / count
                    user_dict = {
                        "engagement_rate": engagement_rate_avg,
                        "followers": earliest_followers
                    }
                    # Store the user data as a JSON object
                    user_data = {
                        b'cf:json': json.dumps(user_dict).encode('utf-8')
                    }
                    user_table.put(current_user.encode('utf-8'), user_data)
            current_user = user_id
            earliest_followers = followers
            old_time = time
            engagement_rate_sum = engagement_rate
            count = 1

    # Handle other data types (croissance, language, toot_with_media, emoji, website)
    elif key.startswith("croissance"):
        croissance_id = key
        user_id = data["user_id"]
        if croissance_id == current_croissance:
            if current_croissance is not None:
                if user_id not in unique_users_roissance:
                    unique_users_roissance.append(user_id)
                    croissance_sum += data["value"]
        else:
            if current_croissance is not None:
                croissance_dict = {"count": croissance_sum}
                # Store the croissance data as a JSON object
                croissance_data = {
                    b'cf:json': json.dumps(croissance_dict).encode('utf-8')
                }
                croissance_table.put(current_croissance.encode('utf-8'), croissance_data)
            current_croissance = croissance_id
            croissance_sum = 1
            unique_users_roissance = [user_id]

    # Handle language data
    elif key.startswith("language"):
        language_id = key
        if language_id == current_language:
            if current_language is not None:
                language_sum += data["value"]
        else:
            if current_language is not None:
                language_dict = {"count": language_sum}
                # Store the language data as a JSON object
                language_data = {
                    b'cf:json': json.dumps(language_dict).encode('utf-8')
                }
                language_table.put(current_language.encode('utf-8'), language_data)
            current_language = language_id
            language_sum = 1

    # Handle toot_with_media data
    elif key.startswith("toot_with_media"):
        toot_with_media_id = key
        if toot_with_media_id == current_toot_with_media:
            if current_toot_with_media is not None:
                toot_with_media_sum += data["value"]
        else:
            if current_toot_with_media is not None:
                toot_with_media_dict = {"count": toot_with_media_sum}
                # Store the toot_with_media data as a JSON object
                toot_with_media_data = {
                    b'cf:json': json.dumps(toot_with_media_dict).encode('utf-8')
                }
                toot_with_media_table.put(current_toot_with_media.encode('utf-8'), toot_with_media_data)
            current_toot_with_media = toot_with_media_id
            toot_with_media_sum = 1

    # Handle emoji data
    elif key.startswith("emoji"):
        emoji_id = key
        if emoji_id == current_emoji:
            if current_emoji is not None:
                emoji_sum += data["value"]
        else:
            if current_emoji is not None:
                emoji_dict = {"count": emoji_sum}
                # Store the emoji data as a JSON object
                emoji_data = {
                    b'cf:json': json.dumps(emoji_dict).encode('utf-8')
                }
                emoji_table.put(current_emoji.encode('utf-8'), emoji_data)
            current_emoji = emoji_id
            emoji_sum = 1

    # Handle website data
    elif key.startswith("website"):
        website_id = key
        if website_id == current_website:
            if current_website is not None:
                website_sum += data["value"]
        else:
            if current_website is not None:
                website_dict = {"count": website_sum}
                # Store the website data as a JSON object
                website_data = {
                    b'cf:json': json.dumps(website_dict).encode('utf-8')
                }
                website_table.put(current_website.encode('utf-8'), website_data)
            current_website = website_id
            website_sum = 1

# Close the HBase connection
connection.close()
import requests
import json
import csv

api_key = "AIzaSyBUQO3iubK55sSOszhs7QKjiFIpODGDU5w"

def get_links(search_term, max_results=10000):
    links = []
    url = "https://www.googleapis.com/youtube/v3/search"
    page_token = None

    while len(links) < max_results:
        params = {
            "part": "snippet",
            "q": search_term,
            "type": "channel",
            "key": api_key,
            "maxResults": min(50, max_results - len(links)),
        }
        if page_token:
            params["pageToken"] = page_token

        response = requests.get(url, params=params)
        data = response.json()

        for item in data["items"]:
            channel_id = item["snippet"]["channelId"]
            links.append(f"https://www.youtube.com/channel/{channel_id}")

        page_token = data.get("nextPageToken")
        if not page_token:
            break

    return links
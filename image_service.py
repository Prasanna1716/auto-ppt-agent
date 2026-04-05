import requests

PEXELS_API_KEY = "TkBt6EBkSp6pVEDJ9wvwTIPEKmhCidwKQ0X7M05dli3yrVQ5LCNkM7Kn"


def fetch_image(query):
    url = "https://api.pexels.com/v1/search"

    headers = {
        "Authorization": PEXELS_API_KEY
    }

    params = {
        "query": query,
        "per_page": 1
    }

    response = requests.get(url, headers=headers, params=params)

    data = response.json()

    if data.get("photos"):
        return data["photos"][0]["src"]["medium"]

    return None
import os
import requests
from fastapi import HTTPException

GITHUB_API_BASE = os.getenv("GITHUB_API_BASE", "https://api.github.com")

def fetch_repo(owner: str, repo: str):
    url = f"{GITHUB_API_BASE}/repos/{owner}/{repo}"
    response = requests.get(url, timeout=5)

    if response.status_code != 200:
        raise HTTPException(status_code=404, detail="GitHub repo not found")

    data = response.json()

    return {
        "name": data["name"],
        "owner": data["owner"]["login"],
        "stars": data["stargazers_count"],
        "url": data["html_url"]
    }

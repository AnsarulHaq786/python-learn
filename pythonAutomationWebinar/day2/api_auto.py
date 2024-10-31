import requests
import json

username="amamulhaq"
url= f"https://api.github.com/users/{username}/repos"

response = requests.get(url)

repos_data = response.json()

all_repos_info = [{"name": repo.get("name"), "stars": repo.get("stargazers_count"), "language": repo.get("language"), "created_date": repo.get("created_at")} for repo in repos_data]


with open(f"{username}Github.json", "w", encoding="utf-8") as file:
    json.dump(all_repos_info, file, ensure_ascii=False, indent=4)

print(all_repos_info.count)
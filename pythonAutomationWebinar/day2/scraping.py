import requests
from bs4 import BeautifulSoup
import json

# Define the URL for the news page
url = "https://ekantipur.com/news"

# Send a GET request to the URL
response = requests.get(url)

# Check if the request was successful
if response.status_code == 200:
    # Parse the HTML content
    soup = BeautifulSoup(response.content, "html.parser")
    
    # Find all news article divs with the specific class "teaser offset"
    articles = soup.find_all("div", class_="teaser offset")
    
    # List to hold all news data
    news_data = []
    
    # Loop through each article and extract details
    for article in articles:
        title = article.find("h2").get_text(strip=True)
        author = article.find("div", class_="author").get_text(strip=True)
        summary = article.find("p").get_text(strip=True)
        
        # Append data as a dictionary to the news_data list
        news_data.append({
            "title": title,
            "author": author,
            "summary": summary
        })
    
    # Save data to a JSON file
    with open("news_data.json", "w", encoding="utf-8") as file:
        json.dump(news_data, file, ensure_ascii=False, indent=4)

    print("News data has been saved to news_data.json")
else:
    print("Failed to retrieve the webpage. Status code:", response.status_code)

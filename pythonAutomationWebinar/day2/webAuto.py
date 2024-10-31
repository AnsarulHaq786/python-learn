from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
import time
import json

opts = Options()
opts.headless = True
service = Service(ChromeDriverManager().install())
browser = webdriver.Chrome(service=service, options=opts)

search_results = []

try:
    browser.get("https:google.com")
    searchBox = browser.find_element("name", "q")
    searchBox.send_keys("pokhara university")
    searchBox.submit()
    time.sleep(5)
    results = browser.find_elements("css selector", "div.g")[:5]
    for i, result in enumerate(results, start=1):
        title = result.find_element("tag name", "h3").text
        url = result.find_element("tag name", "a").get_attribute("href")
        search_results.append({"title": title, "url": url})
finally:
    browser.quit()
    
with open("google_search_results.json", "w", encoding="utf-8") as f:
    json.dump(search_results, f, ensure_ascii=False, indent=4)
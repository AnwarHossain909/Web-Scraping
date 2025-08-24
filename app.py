'''
import requests
import json

# ---------- Function to fetch app data from iTunes API ----------
def get_app_data(app_id, country="us"):

    """
    Fetch app data (description, screenshots, URL, name, etc.) from iTunes API
    """
    url = f"https://itunes.apple.com/lookup?id={app_id}&country={country}"
    #url = f"https://itunes.apple.com/lookup?"
    response = requests.get(url)

    if response.status_code != 200:
        print(f"Failed to fetch data for App ID {app_id}")
        return {}

    try:
        data = response.json()
        if data.get("resultCount", 0) > 0:
            app_info = data["results"][0]
            # Select only useful fields
            result = {
                "app_id": app_info.get("trackId"),
                "app_name": app_info.get("trackName"),
                "description": app_info.get("description"),
                "app_url": app_info.get("trackViewUrl"),
                "icon_url": app_info.get("artworkUrl512"),
                "screenshots": app_info.get("screenshotUrls", []),
                "ipad_screenshots": app_info.get("ipadScreenshotUrls", []),
                #"appletv_screenshots": app_info.get("appletvScreenshotUrls", []),
                #"genres": app_info.get("genres", []),
                #"average_user_rating": app_info.get("averageUserRating"),
                #"user_rating_count": app_info.get("userRatingCount")
            }
            return result
        else:
            print(f"No results found for App ID {app_id}")
            return {}
    except Exception as e:
        print("JSON decode error:", e)
        return {}


# ---------- Main ----------
if __name__ == "__main__":
    # List of App IDs
    app_ids = [
        #"389801252",  # Instagram
        #"284882215",  # Facebook
        #"835599320",  # TikTok
        #"324684580",  # Spotify
        #"310633997",  # WhatsApp Messenger
        #"544007664",  # YouTube
        #"333903271",  # Twitter (X)
        #"6446124409", # GenAI AI Chatbot
        #"6473001180"    #booked ai(afzal)
        #"1668787639"
        "293301871"

    ]

    all_apps_data = []

    for app_id in app_ids:
        print(f"Fetching data for App ID: {app_id}")
        app_data = get_app_data(app_id)
        if app_data:
            all_apps_data.append(app_data)

    # Save all apps data to JSON
    with open("all_apps_data.json", "w", encoding="utf-8") as f:
        json.dump(all_apps_data, f, indent=4, ensure_ascii=False)

    print("All app data saved to all_apps_data.json")

    



#playstore theke data collect korar code
import json
from google_play_scraper import app

# ---------- Function to fetch app data ----------
def get_playstore_app_data(package_name, lang="en", country="us"):
    try:
        result = app(
            package_name,
            lang=lang,
            country=country
        )

        # Select useful fields
        app_data = {
            "app_id": package_name,
            "title": result.get("title"),
            "description": result.get("description"),
            #"summary": result.get("summary"),
            "app_url": f"https://play.google.com/store/apps/details?id={package_name}",
            #"developer": result.get("developer"),
            #"developer_email": result.get("developerEmail"),
            #"developer_website": result.get("developerWebsite"),
            #"icon": result.get("icon"),
            "header_image": result.get("headerImage"),
            "screenshots": result.get("screenshots", []),
            "genre": result.get("genre"),
            #"installs": result.get("installs"),
            #"min_installs": result.get("minInstalls"),
            #"released": result.get("released"),
            #"updated": result.get("updated"),
            #"rating": result.get("score"),
            #"ratings_count": result.get("ratings"),
            #"reviews_count": result.get("reviews"),
            #"size": result.get("size"),
            #"current_version": result.get("version"),
            #"content_rating": result.get("contentRating"),
            #"ad_supported": result.get("adSupported"),
            #"in_app_purchases": result.get("offersIAP"),
            #"free": result.get("free"),
            #"price": result.get("price")
        }
        return app_data
    except Exception as e:
        print(f"Failed to fetch data for {package_name}: {e}")
        return {}

# ---------- Main ----------
if __name__ == "__main__":
    # List of Play Store Package Names
    package_names = [
        #"com.facebook.katana",   # Facebook
        #"com.instagram.android", # Instagram
        #"com.zhiliaoapp.musically", # TikTok
        #"com.spotify.music",     # Spotify
        #"com.whatsapp",          # WhatsApp
        #"com.google.android.youtube", # YouTube
        #"com.twitter.android"    # Twitter (X)
        #"com.openai.chatgpt&hl",
        #"com/store/games?hl=en"
        "com.bd/products/24-i293301871-s1300643140.html?"
    ]

    all_apps_data = []

    for package in package_names:
        print(f"Fetching data for {package}")
        app_data = get_playstore_app_data(package)
        if app_data:
            all_apps_data.append(app_data)

    # ✅ Save all apps data to JSON
    with open("playstore_apps_data.json", "w", encoding="utf-8") as f:
        json.dump(all_apps_data, f, indent=4, ensure_ascii=False)

    print("✅ All Play Store app data saved to playstore_apps_data.json")

'''


#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
একটি URL থেকে:
- পেজ টাইটেল
- ভিজিবল টেক্সট (স্ক্রিপ্ট/স্টাইল বাদ)
- সব লিংক (a[href])
- সব ইমেজ (img[src])

ডেডুপ করে, অ্যাবসোলিউট URL বানিয়ে (base URL দিয়ে), JSON আউটপুট দেয়।
ব্যবহার:
    python scrape_to_json.py https://example.com -o output.json
"""

'''

import requests
from bs4 import BeautifulSoup
import json
from datetime import datetime
from urllib.parse import urljoin

def scrape_website(url):
    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()
    except requests.RequestException as e:
        print(f" Error fetching {url}: {e}")
        return None

    soup = BeautifulSoup(response.text, 'html.parser')

    # websites theke text
    text = soup.get_text(separator="\n", strip=True)

    # link
    links = [urljoin(url, a['href']) for a in soup.find_all('a', href=True)]

    # image
    images = [urljoin(url, img['src']) for img in soup.find_all('img', src=True)]

    # json bosab
    data = {
        "url": url,
        "fetched_at": datetime.utcnow().isoformat() + "Z",
        "title": soup.title.string.strip() if soup.title else "No Title",
        "scraped_text": text,
        "scraped_links": links,
        "scraped_images": images
    }

    return data


if __name__ == "__main__":
    
    url = "https://app.creatify.ai/tool/link-to-video/edit-product?flowId=4aff5041-bba5-4ca5-870d-6de51261560f"
    result = scrape_website(url)
    if result:
        with open("output.json", "w", encoding="utf-8") as f:
            json.dump(result, f, ensure_ascii=False, indent=4)
        print("Data saved to output.json")
    else:
        print("Failed to scrape website")

'''




# ei code diye sokol prokar website ,playstore theke data collect kore jai


from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
import time
import json

def scrape_dynamic_site(url):
    # Setup Chrome (auto download driver)
    options = webdriver.ChromeOptions()
    options.add_argument("--headless")   # Browser দেখাবে না (background এ run করবে)
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")

    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
    driver.get(url)

    # Wait for JS to load (change time if needed)
    time.sleep(5)

    data = {
        "url": url,
        "title": None,
        "description": None,
        "images": []
    }

    # Try to grab Title (example: first <h1>)
    try:
        data["title"] = driver.find_element(By.TAG_NAME, "h1").text
    except:
        pass

    # Try to grab Description (example: first <p>)
    try:
        data["description"] = driver.find_element(By.TAG_NAME, "p").text
    except:
        pass

    # Grab all <img> tags (screenshots, product images etc.)
    images = driver.find_elements(By.TAG_NAME, "img")
    for img in images:
        src = img.get_attribute("src")
        if src and src.startswith("http"):
            data["images"].append(src)

    driver.quit()
    return data


# ---------------- MAIN ----------------
target_url = input("Enter Website URL: ").strip()
scraped_data = scrape_dynamic_site(target_url)

# Save to JSON
with open("scraped_data.json", "w", encoding="utf-8") as f:
    json.dump(scraped_data, f, ensure_ascii=False, indent=4)

print(" Data successfully scraped and saved to scraped_data.json")


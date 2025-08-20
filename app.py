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
        "2036628890900837154"

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

    '''



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
        "com/store/games?hl=en"
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

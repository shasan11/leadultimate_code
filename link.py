from instagram_scraper import InstagramScraper

def scrape_followers(username):
    scraper = InstagramScraper(username)
    followers = scraper.get_followers()

    for follower in followers:
        username = follower["username"]
        full_name = follower["full_name"]
        follower_id = follower["id"]
        # Access other available attributes as needed
        # ...
        print(f"Username: {username}, Full Name: {full_name}, ID: {follower_id}")

# Specify the username of the account whose followers you want to scrape
target_username = "cortifoxsystems"
scrape_followers(target_username)

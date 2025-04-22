# scrap.py
import os
import csv
from urllib.parse import quote
from playwright.sync_api import sync_playwright

def run_scraper(search_query, max_sellers):
    safe_query = search_query.replace(" ", "_").lower()
    output_dir = r"C:\Users\Rehima\OneDrive\سطح المكتب\test\static"
    os.makedirs(output_dir, exist_ok=True)
    output_path = os.path.join(output_dir, f"{safe_query}_tiktok_sellers.csv")

    visited_profiles = set()

    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        context = browser.new_context(user_agent="Mozilla/5.0 Chrome/123 Safari/537.36")
        page = context.new_page()

        live_url = f"https://www.tiktok.com/search/live?q={quote(search_query)}"
        page.goto(live_url)
        page.wait_for_timeout(5000)

        for _ in range(30):
            page.mouse.wheel(0, 2000)
            page.wait_for_timeout(2000)
            profile_links = page.eval_on_selector_all(
                'a[data-e2e^="search-card-user-link"]',
                'els => els.map(el => ({username: el.href.split("/")?.pop(), url: el.href}))'
            )

            for seller in profile_links:
                visited_profiles.add((seller["username"], seller["url"]))
                if len(visited_profiles) >= max_sellers:
                    break
            if len(visited_profiles) >= max_sellers:
                break

        sellers = list(visited_profiles)[:max_sellers]
        with open(output_path, "w", newline="", encoding="utf-8") as f:
            writer = csv.writer(f)
            writer.writerow(["Seller Username", "Profile URL"])
            for username, url in sellers:
                writer.writerow([username, url])

        browser.close()
    return output_path
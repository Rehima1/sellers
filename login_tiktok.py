from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)
    context = browser.new_context(
        user_agent="Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123 Safari/537.36"
    )
    page = context.new_page()

    # Navigate to TikTok login
    page.goto("https://www.tiktok.com/login", timeout=60000)
    print("🔑 Please log in manually in the browser window.")
    input("✅ After login is complete, press Enter to save the session...")

    # Save session state after login
    context.storage_state(path="tiktok_session.json")
    print("💾 Session saved to tiktok_session.json")
    browser.close()




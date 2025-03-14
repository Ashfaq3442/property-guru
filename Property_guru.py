# from playwright.sync_api import sync_playwright
# from playwright_stealth import stealth
# import time
# import random
# import csv
# with open('Property Guru.csv', mode='w', newline='', encoding='utf-8') as file:
#     writer = csv.writer(file)
#     writer.writerow(["Title", "Link",])  # Write header

#     with sync_playwright() as playwright:
#         #launch a Browser
#         browser=playwright.chromium.launch(headless=False, slow_mo=1000)
#         time.sleep(random.uniform(1, 3))
#         #create a new page
#         page=browser.new_page() #(viewport={"width": 1020, "height": 1080})
#         page.set_extra_http_headers({
#         "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36"})
#         #visit any site
#         page.goto("https://www.propertyguru.com.sg/property-for-sale",wait_until="domcontentloaded")
#         page.mouse.move(50, 50, steps=25)
#         page.wait_for_load_state("domcontentloaded")
#         time.sleep(random.uniform(1, 3))
#         time.sleep(5)
#         accept_button = page.query_selector("div.cookie-banner-action button.btn-dark")
#         if accept_button:
#             page.mouse.move(100, 150, steps=25)
#             accept_button.click()#Accepted Cookies
#         time.sleep(5)
#         for _ in range(10):  # Adjust the range for longer scrolling
#             page.mouse.move(150, 200, steps=25)
#             page.evaluate("window.scrollBy(0, 1500)")  # Scrolls down 200 pixels
#             time.sleep(random.uniform(1, 1))  # Wait randomly to mimic human behavior

#         print("Scrolling completed!")
#         while True:
            # page.mouse.move(200, 250, steps=25)
            # links = page.query_selector_all("a.listing-card-link")
            # for link in links:
            #     href = link.get_attribute("href")
            #     title = link.get_attribute("title")
            #     print("Links =",href)
            #     print("\n\n\n")

            # Find and click the "Next" pagination button
            # next_button = page.query_selector("a[data-automation-id='hui-pagination-btn-next']")
            # if next_button:
            #     page.mouse.move(200, 300, steps=25)
            #     next_button.click()
            #     time.sleep(random.uniform(3, 5))  # Wait for next page to load
            #     page.wait_for_load_state("domcontentloaded")
            #     time.sleep(20)

            # else:
            #     print("No more pages found.")
            #     break  # Exit the loop if no "Next" button is found








# from playwright.sync_api import sync_playwright
# from playwright_stealth import stealth_sync
# import time
# import random
# import csv


# with open('Property Guru.csv', mode='w', newline='', encoding='utf-8') as file:
#     writer = csv.writer(file)
#     writer.writerow(["Title", "Link"])  # Write CSV header

#     with sync_playwright() as playwright:
#         browser = playwright.chromium.launch(headless=False, slow_mo=500, args=[
#             "--disable-blink-features=AutomationControlled",  # Hide automation flag
#             "--no-sandbox",
#             "--disable-setuid-sandbox",
#             "--disable-web-security",
#             "--disable-features=IsolateOrigins,site-per-process",
#             "--disable-dev-shm-usage",
#             "--enable-gpu",
#             "--disable-extensions"],
#             proxy={"server": "http://127.0.0.1:8082"}
            
#         )
#         page = browser.new_page()
#         time.sleep(60)
#         stealth_sync(page)  # Apply stealth mode
#         page.mouse.move(500, 600, steps=25)
#         time.sleep(random.uniform(5, 10))
#         time.sleep(1)

#         page.set_extra_http_headers({
#             "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36"
#         })
#         page.goto("https://www.propertyguru.com.sg/property-for-sale/20", wait_until="domcontentloaded")
        
        
#         page.mouse.move(50, 100, steps=25)
#         time.sleep(random.uniform(5, 10))
#         time.sleep(30)
#         # Accept Cookies
#         accept_button = page.query_selector("div.cookie-banner-action button.btn-dark")
#         if accept_button:
#             page.mouse.move(50, 100, steps=25)
#             page.wait_for_load_state("domcontentloaded")
#             accept_button.click()

#         for _ in range(7):  # Adjust the range for longer scrolling
#             page.evaluate("window.scrollBy(0, 2500)")  # Scrolls down 200 pixels
#             page.mouse.move(150, 200, steps=25)
#             time.sleep(random.uniform(1, 2))  # Wait randomly to mimic human behavior
#             page.wait_for_load_state("domcontentloaded")
#             time.sleep(1)

#         for page_num in range(2,22):
#             href=(f"/property-for-sale/{page_num}")
#             page.mouse.move(500, 600, steps=25)
#             #open new tab for each page
#             page.mouse.move(550, 650, steps=25)
#             profile_page = browser.new_page()
#             profile_page.set_extra_http_headers({
#                     "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36"
#                 })
#             page.mouse.move(600, 750, steps=25)
#             profile_page.goto(f"https://www.propertyguru.com.sg{href}", wait_until="domcontentloaded")
#             profile_page.wait_for_load_state("domcontentloaded")
#             time.sleep(random.uniform(1, 2))
#             time.sleep(1)
#             profile_page.close()
#             time.sleep(random.uniform(1, 2))
#             time.sleep(1)
#         page.close()







            
            # page.mouse.move(100, 150, steps=25)   
            # links = page.query_selector_all("a.listing-card-link")
            # for link in links:
            #     href = link.get_attribute("href")
            #     title = link.get_attribute("title")
            #     print("Links =",href)
            #     time.sleep(random.uniform(1, 1))
            #     print("\n\n\n")

            # Find and click the "Next" pagination button


            # next_button = page.get_by_role("a[data-automation-id='hui-pagination-btn-next']")
            # page.get_by_role("link", name="Next").click()
            # page.mouse.move(200, 250, steps=25)
            # page.wait_for_load_state("domcontentloaded")
            # time.sleep(random.uniform(3, 5))  # Wait for next page to load
            # time.sleep(10)

            # for page_number in range(2, 6):  # Adjust range as needed
            #     xpath = f"/html/body/div[1]/div/div/div[1]/div[6]/div[2]/div[1]/ul/li[{page_number}]"

            #     page.wait_for_selector(f"xpath={xpath}", timeout=500)  # Wait for the button
                
            #     page.locator(f"xpath={xpath}").click()  # Click on the page number
            #     page.mouse.move(200, 250, steps=25)
            #     page.wait_for_load_state("domcontentloaded")
            #     time.sleep(random.uniform(2, 3))
            #     print(f"Clicked on page {page_number}")

            # next_button = page.locator("i.pgicon-arrow-right").first

            # if next_button.is_visible():
            #     page.mouse.move(450, 550, steps=25)
            #     print("Clicking Next Button")
            #     next_button.click()
            #     page.mouse.move(500, 600, steps=25)
            #     page.wait_for_load_state("domcontentloaded")
            #     time.sleep(random.uniform(1, 3))
            #     page.mouse.move(600, 650, steps=25)
            #     time.sleep(40)  # Wait for the next page to load
            #     page.mouse.move(650, 700, steps=25)




                # previous_height = 0
                # while True:
                #     page.evaluate("window.scrollTo(0, document.body.scrollHeight)")
                #     page.mouse.move(350, 400, steps=25)
                #     page.wait_for_load_state("domcontentloaded")
                #     time.sleep(random.uniform(2, 3))  # Human-like delay
                #     new_height = page.evaluate("document.body.scrollHeight")
                #     if new_height == previous_height:
                #         break
                #     previous_height = new_height
   
                # browser.close()








from playwright.sync_api import sync_playwright
from playwright_stealth import stealth_sync
import time
import random
import csv

# List of User Agents for rotation
user_agents = [
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Edge/120.0.0.0 Safari/537.36",
    "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36",
]
x_target = random.randint(40, 60)  # Target around 50 with small variations
y_target = random.randint(380, 420)  # Target around 400 with small variations

steps = random.randint(20, 40)  # Random steps between 20 and 40 for smooth motion
with open('Property Guru.csv', mode='w', newline='', encoding='utf-8') as file:
    writer = csv.writer(file)
    writer.writerow(["Title", "Link"])  # Write CSV header

    with sync_playwright() as playwright:
        browser = playwright.chromium.launch(headless=False, slow_mo=500,proxy={"server": "http://127.0.0.1:8080"}, args=[
            "--disable-blink-features=AutomationControlled",
            "--no-sandbox",
            "--disable-setuid-sandbox",
            "--disable-web-security",
            "--disable-features=IsolateOrigins,site-per-process",
            "--disable-dev-shm-usage",
            "--enable-gpu",
            "--disable-extensions"
        ])
        
        page = browser.new_page()
        stealth_sync(page)  # Apply stealth mode
        page.mouse.move(x_target, y_target, steps=steps)
        
        # Rotate User-Agent for the main page
        random_user_agent = random.choice(user_agents)
        page.set_extra_http_headers({"User-Agent": random_user_agent,
        "Accept-Language": "en-US,en;q=0.9",
        "Referer": "https://www.google.com/",
        "Sec-Fetch-Mode": "navigate"})
        print(f"Using User-Agent: {random_user_agent}")

        page.goto("https://www.propertyguru.com.sg/property-for-sale/", wait_until="domcontentloaded")
        time.sleep(60)

        # Accept Cookies if banner exists
        # accept_button = page.query_selector("div.cookie-banner-action button.btn-dark")
        # if accept_button:
        #     page.mouse.move(x_target, y_target, steps=steps)
        #     accept_button.click()
        #     time.sleep(random.uniform(2, 4))

        # # Scroll multiple times
        # for _ in range(7):  
        #     page.evaluate("window.scrollBy(0, 2500)")
        #     page.mouse.move(x_target, y_target, steps=steps)
        #     time.sleep(random.uniform(1, 2))

        # # Iterate over pages 2-22
        # for page_num in range(2, 25):
        #     href = f"/property-for-sale/{page_num}"

        #     # Open a new tab for each page
        #     profile_page = browser.new_page()
        #     page.mouse.move(x_target, y_target, steps=steps)

        #     # Rotate User-Agent for each new page
        #     random_user_agent = random.choice(user_agents)
        #     page.mouse.move(x_target, y_target, steps=steps)
        #     profile_page.set_extra_http_headers({"User-Agent": random_user_agent})
        #     print(f"Using User-Agent: {random_user_agent}")

        #     profile_page.goto(f"https://www.propertyguru.com.sg{href}", wait_until="domcontentloaded")
        #     time.sleep(random.uniform(1, 2))

        #     profile_page.close()
        #     time.sleep(random.uniform(1, 2))

        # page.close()
        # browser.close()






# from playwright.sync_api import sync_playwright
# from playwright_stealth import stealth_sync
# import random
# import time

# # List of User Agents for rotation
# user_agents = [
#     "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36",
#     "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
#     "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Edge/120.0.0.0 Safari/537.36",
#     "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36",
# ]

# x_target = random.randint(40, 60)  # Target around 50 with small variations
# y_target = random.randint(380, 420)  # Target around 400 with small variations

# steps = random.randint(20, 40)  # Random steps between 20 and 40 for smooth motion

# # Move the mouse


# with sync_playwright() as playwright:
#     browser = playwright.chromium.launch(headless=False)
#     page = browser.new_page()
#     page.mouse.move(x_target, y_target, steps=steps)
#     time.sleep(random.uniform(5, 10))

#     # Apply stealth mode
#     stealth_sync(page)

#     # Rotate User-Agent and Set Extra Headers
#     random_user_agent = random.choice(user_agents)
#     page.set_extra_http_headers({
#         "User-Agent": random_user_agent,
#         "Accept-Language": "en-US,en;q=0.9",
#         "Referer": "https://www.google.com/",
#         "Sec-Fetch-Mode": "navigate"
#     })
#     page.mouse.move(x_target, y_target, steps=steps)
#     print(f"Using User-Agent: {random_user_agent}")

#     # Open the page
#     page.goto("https://www.propertyguru.com.sg/property-for-sale/", wait_until="domcontentloaded")

#     page.mouse.move(x_target, y_target, steps=steps)
#     time.sleep(random.uniform(5, 10))
#     time.sleep(10)
#     # Accept Cookies
#     accept_button = page.query_selector("div.cookie-banner-action button.btn-dark")
#     if accept_button:
#         page.mouse.move(50, 100, steps=25)
#         page.wait_for_load_state("domcontentloaded")
#         accept_button.click()

#     for _ in range(7):  # Adjust the range for longer scrolling
#         page.evaluate("window.scrollBy(0, 2500)")  # Scrolls down 200 pixels
#         page.mouse.move(150, 200, steps=25)
#         time.sleep(random.uniform(1, 2))  # Wait randomly to mimic human behavior
#         page.wait_for_load_state("domcontentloaded")
#         time.sleep(1)

#     for page_num in range(2,22):
#         href=(f"/property-for-sale/{page_num}")
#         page.mouse.move(500, 600, steps=25)
#         #open new tab for each page
#         page.mouse.move(550, 650, steps=25)
#         profile_page = browser.new_page()
#         profile_page.set_extra_http_headers({
#                 "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36"
#             })
#         page.mouse.move(600, 750, steps=25)
#         profile_page.goto(f"https://www.propertyguru.com.sg{href}", wait_until="domcontentloaded")
#         profile_page.wait_for_load_state("domcontentloaded")
#         time.sleep(random.uniform(1, 2))
#         time.sleep(1)
#         profile_page.close()
#         time.sleep(random.uniform(1, 2))
#         time.sleep(1)
#     page.close()

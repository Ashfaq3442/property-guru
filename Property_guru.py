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








from playwright.sync_api import sync_playwright
from playwright_stealth import stealth_sync
import time
import random
import csv


with open('Property Guru.csv', mode='w', newline='', encoding='utf-8') as file:
    writer = csv.writer(file)
    writer.writerow(["Title", "Link"])  # Write CSV header

    with sync_playwright() as playwright:
        browser = playwright.chromium.launch(headless=False, slow_mo=500)
        page = browser.new_page()
        stealth_sync(page)  # Apply stealth mode
        page.mouse.move(500, 600, steps=25)
        time.sleep(random.uniform(5, 10))
        time.sleep(1)

        page.set_extra_http_headers({
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36"
        })
        page.goto("https://www.propertyguru.com.sg/property-for-sale/", wait_until="domcontentloaded")
        
        
        page.mouse.move(50, 100, steps=25)
        time.sleep(random.uniform(1, 2))
        time.sleep(2)
        # Accept Cookies
        accept_button = page.query_selector("div.cookie-banner-action button.btn-dark")
        if accept_button:
            page.mouse.move(50, 100, steps=25)
            page.wait_for_load_state("domcontentloaded")
            accept_button.click()

        for _ in range(7):  # Adjust the range for longer scrolling
            page.evaluate("window.scrollBy(0, 2000)")  # Scrolls down 200 pixels
            page.mouse.move(150, 200, steps=25)
            time.sleep(random.uniform(1, 2))  # Wait randomly to mimic human behavior
            page.wait_for_load_state("domcontentloaded")
            time.sleep(1)

        for page_num in range(2,22):
            href=(f"/property-for-sale/{page_num}")
            page.mouse.move(500, 600, steps=25)
            #open new tab for each page
            page.mouse.move(550, 650, steps=25)
            profile_page = browser.new_page()
            profile_page.set_extra_http_headers({
                    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36"
                })
            page.mouse.move(600, 750, steps=25)
            profile_page.goto(f"https://www.propertyguru.com.sg{href}", wait_until="domcontentloaded")
            profile_page.wait_for_load_state("domcontentloaded")
            time.sleep(random.uniform(1, 2))
            time.sleep(1)
            profile_page.close()
            time.sleep(random.uniform(1, 2))
            time.sleep(1)
        page.close()







            
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

from playwright.sync_api import sync_playwright
import time
import random
import csv
with open('coaches_data.csv', mode='w', newline='', encoding='utf-8') as file:
    writer = csv.writer(file)
    writer.writerow(["Coach Name", "Website", "Email", "Coaching Themes"])  # Write header

    with sync_playwright() as playwright:
        #launch a Browser
        browser=playwright.chromium.launch(headless=False, slow_mo=500)
        time.sleep(random.uniform(1, 3))
        #create a new page
        page=browser.new_page() #(viewport={"width": 1020, "height": 1080})
        page.set_extra_http_headers({
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36"})
        #visit any site
        page.goto("https://coachingfederation.org/", wait_until="domcontentloaded")
        sign_in=page.get_by_role("link",name="sign in")#click on sign in button
        page.mouse.move(100, 100, steps=25)
        sign_in.click()
        page.wait_for_load_state("domcontentloaded")
        time.sleep(random.uniform(1, 3))
        time.sleep(1)
        page.mouse.move(200, 300, steps=25)
        page.locator("#user_login").fill("ashfaqm46@gmail.com")# fill in the username
        page.wait_for_load_state("domcontentloaded")
        time.sleep(random.uniform(1, 3))
        time.sleep(2)
        page.mouse.move(250, 350, steps=25)
        page.locator("#user_pass").fill("Ashfaqm46@3442")#fill the password
        page.wait_for_load_state("domcontentloaded")
        time.sleep(random.uniform(1, 3))
        time.sleep(3)
        page.mouse.move(300, 400, steps=25)
        page.locator("#wp-submit").click() #click on submit button
        page.wait_for_load_state("domcontentloaded")
        time.sleep(random.uniform(1, 3))
        time.sleep(4)
        page.get_by_role("link", name="Accept").click()#click on extra accept button
        page.wait_for_load_state("domcontentloaded")
        time.sleep(random.uniform(1, 3))
        time.sleep(5)
        page.mouse.move(400, 500, steps=25)
        find_coach=page.get_by_role("link", name="find a coach")#click on find a coach button
        find_coach.click()
        page.wait_for_load_state("domcontentloaded")
        time.sleep(random.uniform(1, 3))
        time.sleep(1)
        page.wait_for_load_state("domcontentloaded")
        page.get_by_role("link", name="i agree").click()#click the i accept button
        page.wait_for_load_state("domcontentloaded")
        time.sleep(random.uniform(1, 3))
        time.sleep(2)
        page.mouse.move(430, 520, steps=25)
        page.get_by_role("heading", name="Demographics").click() #Click on Demographics
        page.wait_for_load_state("domcontentloaded")
        time.sleep(random.uniform(1, 3))
        time.sleep(20)
        page.get_by_role("button", name="location").click() #click on add location
        page.wait_for_load_state("domcontentloaded")
        time.sleep(random.uniform(1, 3))
        time.sleep(3)
        page.get_by_role("button",name="united kingdom").click()# click on uk
        page.wait_for_load_state("domcontentloaded")
        time.sleep(random.uniform(1, 3))
        time.sleep(4)
        page.get_by_role("button",name="canada").click()#click on canda
        page.wait_for_load_state("domcontentloaded")
        time.sleep(5)
        page.locator('a[data-tab="countries"]').click()#clcik on countries tab
        page.wait_for_load_state("domcontentloaded")
        time.sleep(random.uniform(1, 3))
        time.sleep(1)
        page.get_by_role("button",name="united state").click() #click on us
        page.wait_for_load_state("domcontentloaded")
        time.sleep(random.uniform(1, 3))
        time.sleep(2)
        page.get_by_role("button", name="close").click()#click on close button
        page.wait_for_load_state("domcontentloaded")
        time.sleep(random.uniform(1, 3))
        time.sleep(3)
        for j in range(2,4):
            page.mouse.move(450, 550, steps=25)
            next_page = page.locator(f'a.icon.borderless.item[data-value="{j}"]')
            next_page.click()
            page.wait_for_load_state("domcontentloaded")
            time.sleep(random.uniform(1, 3))
            time.sleep(3)
            coach_count=page.locator(".ui.fluid.link.card") #coaches on a single page
            count=coach_count.count()
            for i in range(count):
                page.mouse.move(500, 600, steps=25)  # mouse movement
                card = page.locator(".ui.fluid.link.card").nth(i)  # Each Coach profile
                value = card.locator('input[name="compare"]').get_attribute("value")
                
                url = f"https://apps.coachingfederation.org/eweb/CCFDynamicPage.aspx?webcode=ccfcoachprofileview&coachcstkey={value}"

                # Open a new tab for each profile
                page.mouse.move(550, 650, steps=25)
                profile_page = browser.new_page()

                profile_page.set_extra_http_headers({
                    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36"
                })
                
                page.mouse.move(600, 700, steps=25)
                profile_page.goto(url, wait_until="domcontentloaded")
                profile_page.wait_for_load_state("domcontentloaded")
                coach_name =profile_page.locator("h2#coachName").inner_text()#coach name
                link_element = profile_page.locator('#webSiteLink')#website
                website= link_element.get_attribute('href')
                page.mouse.move(650, 750, steps=25)
                email_element = profile_page.locator('#emailLink')#eamil
                email= email_element.get_attribute("href")
                page.mouse.move(700, 800, steps=25)
                first_tr = profile_page.locator('table.ui.unstackable.very.basic.definition.table tr').first#coaching theme
                coachingtheme = first_tr.locator('td:nth-of-type(2)').inner_text().strip()



                # print("Caoch Name =", coach_name)
                # print("Web Site =",website)
                # print("Email =", email)
                # print("Coaching Themes =", coachingtheme,"\n\n\n")

                # Simulate some work on the profile page (replace this with your scraping logic)
                time.sleep(random.uniform(1, 3))  # Optional wait
                time.sleep(2)  # Your scraping or interaction time
                # Close the tab after work is done
                writer.writerow([coach_name, website, email, coachingtheme])
                profile_page.close()

        page.close()







# from playwright.sync_api import sync_playwright
# import time

# with sync_playwright() as playwright:
#     browser = playwright.chromium.launch(headless=False, slow_mo=500)
#     page = browser.new_page(viewport={"width": 1280, "height": 1024})

#     # Step 1 - Visit site and sign in
#     page.goto("https://coachingfederation.org/", wait_until="domcontentloaded")
#     page.get_by_role("link", name="sign in").click()
#     page.wait_for_load_state("domcontentloaded")

#     page.locator("#user_login").fill("ashfaqm46@gmail.com")
#     page.wait_for_load_state("domcontentloaded")
#     time.sleep(1)
#     page.locator("#user_pass").fill("Ashfaqm46@3442")
#     page.wait_for_load_state("domcontentloaded")
#     time.sleep(1)
#     page.locator("#wp-submit").click()
#     page.wait_for_load_state("domcontentloaded")
#     time.sleep(1)

#     page.wait_for_load_state("domcontentloaded")

#     page.get_by_role("link", name="Accept").click()
#     page.wait_for_load_state("domcontentloaded")

#     # Step 2 - Find a coach
#     page.get_by_role("link", name="find a coach").click()
#     page.wait_for_load_state("domcontentloaded")
#     time.sleep(2)

#     page.get_by_role("link", name="i agree").click()
#     page.wait_for_load_state("domcontentloaded")

#     # Step 3 - Demographics
#     page.get_by_role("heading", name="Demographics").click()
#     page.wait_for_load_state("domcontentloaded")
#     time.sleep(1)


#     page.get_by_role("button", name="location").click()
#     page.wait_for_load_state("domcontentloaded")
#     time.sleep(1)

#     # Fix for United Kingdom button (scroll and force click)
#     uk_button = page.get_by_role("button", name="united kingdom")
#     uk_button.scroll_into_view_if_needed()
#     uk_button.click
#     page.wait_for_load_state("domcontentloaded")
#     time.sleep(1)

#     # Same for Canada
#     canada_button = page.get_by_role("button", name="canada")
#     canada_button.scroll_into_view_if_needed()
#     canada_button.click
#     page.wait_for_load_state("domcontentloaded")
#     time.sleep(1)

#     # Click Countries Tab (with scroll fix)
#     countries_tab = page.locator('a[data-tab="countries"]')
#     countries_tab.scroll_into_view_if_needed()
#     countries_tab.click()
#     page.wait_for_load_state("domcontentloaded")
#     time.sleep(1)

#     # Select United States (similar force scroll and click just to be safe)
#     us_button = page.get_by_role("button", name="united state")
#     us_button.scroll_into_view_if_needed()
#     us_button.click
#     page.wait_for_load_state("domcontentloaded")
#     time.sleep(1)

#     page.get_by_role("button", name="close").click()
#     page.wait_for_load_state("domcontentloaded")
#     time.sleep(1)

#     page.locator(".ui.fluid.link.card").first.click()
#     page.wait_for_load_state("domcontentloaded")
#     time.sleep(1)

#     coach_name = page.locator("h2#coachName").inner_text()
#     print(coach_name)

#     page.go_back()
#     page.wait_for_load_state("domcontentloaded")
#     time.sleep(1)

#     input("Press Enter to close browser...")





from selenium import webdriver
import time

def open_firefox_and_fill_username(url):
    try:
        # Open Firefox using subprocess
        subprocess.Popen(["firefox"])

        # Wait for Firefox to start (you can adjust the sleep duration as needed)
        time.sleep(5)

        # Create a Firefox webdriver
        driver = webdriver.Firefox()

        # Navigate to the specified URL
        driver.get(url)

        # Wait for the page to load (you can adjust the sleep duration as needed)
        time.sleep(5)

        # Find the "Sign up" button by class name
        sign_up_button = driver.find_element_by_css_selector('.btn.primary.ms-2.btn-fs')

        # Click the "Sign up" button
        sign_up_button.click()

        # Wait for a moment to see the effect (you can adjust the sleep duration as needed)
        time.sleep(5)

        # Find the "username" input field by its ID
        username_input = driver.find_element_by_id('username')

        # Fill in the "username" input field with the value "abcd"
        username_input.send_keys('abcd')

        # Wait for a moment to see the effect (you can adjust the sleep duration as needed)
        time.sleep(5)

    except FileNotFoundError:
        print("Firefox not found. Make sure it is installed or provide the correct path.")

    finally:
        # Close the browser window
        driver.quit()

if __name__ == "__main__":
    url_to_open = "https://www.clickasnap.com"
    open_firefox_and_fill_username(url_to_open)

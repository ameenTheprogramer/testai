import subprocess
import time
from robobrowser import RoboBrowser

def open_firefox(url):
    try:
        # Open Firefox using subprocess
        subprocess.Popen(["firefox"])

        # Wait for Firefox to start (you can adjust the sleep duration as needed)
        time.sleep(5)

        # Navigate to clickasnap.com using RoboBrowser
        browser = RoboBrowser(parser='html.parser')
        browser.open(url)

        # Call the function to interact with the element
        interact_with_element(browser, 'btn.primary.ms-2.btn-fs')
    except FileNotFoundError:
        print("Firefox not found. Make sure it is installed or provide the correct path.")

def interact_with_element(browser, class_name):
    try:
        # Find the button with the specified class
        button = browser.find(class_=class_name)

        if button:
            # Click the button
            form = button.form
            browser.submit_form(form)
            print(f"Successfully clicked the button with class '{class_name}'.")
        else:
            print(f"Button with class '{class_name}' not found.")
    except Exception as e:
        print(f"Error interacting with element: {e}")

if __name__ == "__main__":
    url_to_open = "https://www.clickasnap.com"

    open_firefox(url_to_open)

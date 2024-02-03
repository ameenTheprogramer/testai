import subprocess
import webbrowser
import time
import pyautogui

def open_firefox(url):
    try:
        # Open Firefox using subprocess
        subprocess.Popen(["firefox"])

        # Wait for Firefox to start (you can adjust the sleep duration as needed)
        time.sleep(5)

        # Navigate to clickasnap.com using webbrowser
        webbrowser.open(url)

        # Wait for the page to load (you may need to adjust the sleep duration)
        time.sleep(10)

        # Call the function to click the element
        click_element_by_class_name('btn.primary.ms-2.btn-fs')
    except FileNotFoundError:
        print("Firefox not found. Make sure it is installed or provide the correct path.")

def click_element_by_class_name(class_name):
    try:
        # Find the location of the element by class name and click it
        element_location = pyautogui.locateCenterOnScreen('path/to/element.png')  # You need to capture the element image first
        pyautogui.click(element_location.x, element_location.y)
    except Exception as e:
        print(f"Error clicking element: {e}")

if __name__ == "__main__":
    url_to_open = "https://www.clickasnap.com"

    open_firefox(url_to_open)

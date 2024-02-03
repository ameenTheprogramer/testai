import subprocess
import webbrowser
import time
import requests
from bs4 import BeautifulSoup

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

        # Call the function to interact with the element
        interact_with_element('btn.primary.ms-2.btn-fs')
    except FileNotFoundError:
        print("Firefox not found. Make sure it is installed or provide the correct path.")

def interact_with_element(class_name):
    try:
        # Get the HTML content of the current page
        response = requests.get("http://localhost:7055/json/new/session")
        session_id = response.json()['sessionId']

        response = requests.get(f"http://localhost:7055/session/{session_id}/window")
        window_handle = response.json()['value']

        response = requests.get(f"http://localhost:7055/session/{session_id}/url")
        current_url = response.json()['value']

        # Perform your desired interaction with the element using the current_url and class_name
        print(f"Interacting with element '{class_name}' on '{current_url}'")

        # Example: You can perform a click by making a POST request to the 'element' endpoint
        payload = {
            'using': 'class name',
            'value': class_name
        }
        response = requests.post(f"http://localhost:7055/session/{session_id}/element", json=payload)
        
        if response.status_code == 200:
            element_id = response.json()['value']['ELEMENT']
            
            response = requests.post(f"http://localhost:7055/session/{session_id}/element/{element_id}/click")
            if response.status_code == 200:
                print("Successfully clicked the element.")
            else:
                print(f"Failed to click the element. Response: {response.text}")
        else:
            print(f"Failed to find the element. Response: {response.text}")

    except Exception as e:
        print(f"Error interacting with element: {e}")

if __name__ == "__main__":
    url_to_open = "https://www.clickasnap.com"

    open_firefox(url_to_open)

import subprocess
import webbrowser
import time

def open_firefox(url):
    try:
        # Open Firefox using subprocess
        subprocess.Popen(["firefox"])

        # Wait for Firefox to start (you can adjust the sleep duration as needed)
        time.sleep(5)

        # Navigate to clickasnap.com using webbrowser
        webbrowser.open(url)
    except FileNotFoundError:
        print("Firefox not found. Make sure it is installed or provide the correct path.")

if __name__ == "__main__":
    url_to_open = "https://www.clickasnap.com"
    open_firefox(url_to_open)

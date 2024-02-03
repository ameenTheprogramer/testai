from selenium import webdriver
from selenium.webdriver.firefox.service import Service

def main():
    # Path to the geckodriver executable
    geckodriver_path = "/usr/local/bin/geckodriver"

    # Create a Firefox webdriver
    service = Service(geckodriver_path)
    driver = webdriver.Firefox(service=service)

    try:
        # Navigate to clickasnap.com
        driver.get("https://www.clickasnap.com")

        # You can perform further actions here, like clicking buttons, filling forms, etc.

    finally:
        # Close the browser window
        driver.quit()

if __name__ == "__main__":
    main()

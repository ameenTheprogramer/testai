from selenium import webdriver

def main():
    # Create a Firefox webdriver
    driver = webdriver.Firefox()

    try:
        # Navigate to clickasnap.com
        driver.get("https://www.clickasnap.com")

        # You can perform further actions here, like clicking buttons, filling forms, etc.

    finally:
        # Close the browser window
        driver.quit()

if __name__ == "__main__":
    main()

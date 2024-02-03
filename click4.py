import time
from requests_html import HTMLSession

def open_firefox(url):
    try:
        session = HTMLSession()
        r = session.get(url)

        # Wait for the page to load (you may need to adjust the sleep duration)
        time.sleep(10)

        # Call the function to interact with the element
        interact_with_element(r, 'btn.primary.ms-2.btn-fs')

    except Exception as e:
        print(f"Error: {e}")

def interact_with_element(response, class_name):
    try:
        # Render the JavaScript on the page
        response.html.render(sleep=2)

        # Find the button with the specified class
        button = response.html.find(f'.{class_name}', first=True)

        if button:
            # Click the button
            button.click()
            print(f"Successfully clicked the button with class '{class_name}'.")
        else:
            print(f"Button with class '{class_name}' not found.")
    except Exception as e:
        print(f"Error interacting with element: {e}")

if __name__ == "__main__":
    url_to_open = "https://www.clickasnap.com"
    open_firefox(url_to_open)

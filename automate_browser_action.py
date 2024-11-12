import pyautogui
import time
import pygetwindow as gw
import keyboard
import pyperclip
from bs4 import BeautifulSoup

# switch to Google Chrome window
def switch_to_chrome():
    # Find the Chrome window and bring it to the foreground
    print("Switching to Chrome window...")
    chrome_window = gw.getWindowsWithTitle('Google Chrome')[0]
    chrome_window.activate()
    time.sleep(0.500)
    print("Switched to Chrome window.\n")

# open a new tab
def open_new_tab():
    # Simulate pressing Ctrl + T to open a new tab
    print("Opening a new tab...")
    pyautogui.hotkey('ctrl', 't')
    time.sleep(0.500)
    print("Opened a new tab.\n")

# enter the product page url in address bar
def enter_url_in_address_bar(url: str):
    # Simulate typing the URL into the address bar and press Enter
    print(f"URL: {url}")
    print("Started typing the URL into the address bar...")
    pyautogui.hotkey('ctrl', 'l')
    pyautogui.write(url)
    print("Finished typing the URL address bar.")
    print("Pressing Enter...")
    pyautogui.press('enter')
    print("Pressed Enter.\n")
    time.sleep(7)

# close the Translate popup window
def close_translate_popup():
    # Simulate pressing Esc to close the translate pop-up
    pyautogui.press('esc')
    time.sleep(0.5)

# scroll down and back up to load the whole page
def scroll_down_and_up(num_of_clicks: int):
    # Scroll down to the end of the page
    print(f"Scrolling towards the end of the page for {num_of_clicks} clicks...")
    pyautogui.scroll(num_of_clicks)
    time.sleep(10)
    print(f"Scrolled down for {num_of_clicks} clicks.")

    # Scroll up to the beginning of the page
    print(f"Scrolling towards the beginning of the page for {num_of_clicks} clicks...")
    pyautogui.scroll(-1 * num_of_clicks)
    time.sleep(1)
    print(f"Scrolled up for {num_of_clicks} clicks.\n")

# scroll down the page
def scroll_down(num_of_clicks: int):
    # Simulate pressing the down arrow key
    print(f"Scrolling towards the end of the page for {num_of_clicks} clicks...")
    for click in range(num_of_clicks):
        pyautogui.press('down')
        time.sleep(0.200)
    print(f"Scrolled down for {num_of_clicks} clicks.\n")

# scroll up the page
def scroll_up(num_of_clicks: int):
    # Simulate pressing the up arrow key
    print(f"Scrolling towards the beginning of the page for {num_of_clicks} clicks...")
    for click in range(num_of_clicks):
        pyautogui.press('up')
        time.sleep(0.200)
    print(f"Scrolled up for {num_of_clicks} clicks.\n")

# click on image carousal to get all images
def click_on_image(x_coordinate: int, y_coordinate: int, num_of_clicks: int):
    # Click on a particular point on the screen
    print(f"Clicking on coordinates ({x_coordinate}, {y_coordinate})...")
    pyautogui.moveTo(x=x_coordinate, y=y_coordinate)
    time.sleep(2)
    for click in range(num_of_clicks):
        pyautogui.click(x=x_coordinate + 5, y=y_coordinate - 5)
        time.sleep(1)
        print(f"Clicked on coordinates ({x_coordinate + 5}, {y_coordinate - 5}).")
    print()

# copy the page source code from Inspect to Clipboard
def retrieve_list_of_venues(page_title):
    # # Press Ctrl + Shift + I to open the Developer Tools
    # print("Opening Developer Tools...")
    # pyautogui.hotkey('ctrl', 'shift', 'i')
    # time.sleep(5)
    # print("Opened Developer Tools.")
    
    # Press Ctrl + U to view page source
    print("Viewing Page Source...")
    pyautogui.hotkey('ctrl', 'u')
    time.sleep(7)
    print("Viewed Page Source.")

    # Press Ctrl + A to select all, Ctrl + C to copy
    print("Selecting Source Code...")
    pyautogui.hotkey('ctrl', 'a')
    time.sleep(1)
    pyautogui.hotkey('ctrl', 'c')
    time.sleep(1)
    print("Copied Source Code.")

    # Store the copied source code in a variable
    print("Pasting Source Code...")
    source_code = pyperclip.paste()
    time.sleep(1)
    print("Pasted Source Code.\n")

    close_current_tab()

    # Parse the HTML content using BeautifulSoup
    soup = BeautifulSoup(source_code, "html.parser")
    # print(f"Page searched: {page_title}")
    # print(f"Page retrieved: {soup.title.string}\n")
    if soup.title.string != page_title:
        raise Exception(f"Invalid Page Title: {soup.title.string}")

    # Find all the <li> elements with class="list"
    venue_list = soup.find_all("li", class_="list")

    if venue_list:
        # Format venuelist to get only the data-name of the <li> element
        venue_list = [item.get('data-name') for item in venue_list if item.get('data-name') is not None]
        # print(venue_list)
        print("\nVenue List:")
        for sl_num, venue in enumerate(venue_list, start=1):
            print(f"{sl_num}. {venue}")
        print()

        return venue_list
    
    return None

# close the tab
def close_current_tab():
    # Simulate pressing Ctrl + W to close the current tab
    pyautogui.hotkey('ctrl', 'w')
    time.sleep(1)
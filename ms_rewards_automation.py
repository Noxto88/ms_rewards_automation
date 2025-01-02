"""This Module perform search operation in default browser"""

__version__ = 2.0

import time
import webbrowser
import pyautogui


def perform_search():
    """
    Automates opening a browser tab and performing the search.
    """
    for x in range(1, 35):
        # Open a new browser tab
        webbrowser.open_new_tab("https://www.bing.com")
        time.sleep(3)

        pyautogui.hotkey('alt', 'd')
        time.sleep(1)

        search_query = f"test_search_{x}"
        pyautogui.typewrite(search_query)
        time.sleep(1)

        pyautogui.press('enter')
        print(f"Performed search: {search_query}")
        time.sleep(5)


if __name__ == "__main__":
    perform_search()

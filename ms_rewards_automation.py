import time
import subprocess
import webbrowser

def perform_search():
    x = 0
    for x in range(35):
        url = f"https://www.bing.com/search?q={x}"
        webbrowser.open_new_tab(url)
        time.sleep(2)

if __name__ == "__main__":
    perform_search()
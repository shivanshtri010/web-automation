from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.edge.service import Service
import time

# Define the list of search items
search_items = [
    "History of Ancient Rome",
    "Photography tips for beginners",
    "Best hiking trails in the US",
    "Understanding quantum physics",
    "Top yoga practices for relaxation",
    "Exploring the deep sea",
    "Famous art museums in Europe",
    "How to grow your own vegetables",
    "The benefits of meditation",
    "Classic novels to read",
    "Home renovation ideas",
    "How to start a podcast",
    "Basics of financial investing",
    "Space exploration missions",
    "Eco-friendly living tips",
    "Learning a new language fast",
    "Tips for effective public speaking",
    "Best board games for families",
    "History of jazz music",
    "Understanding blockchain technology",
    "Tips for writing a novel",
    "How to brew your own beer",
    "Famous historical landmarks",
    "Simple DIY crafts",
    "Best practices for coding interviews",
    "The impact of climate change",
    "How to manage stress",
    "Basics of digital marketing",
    "Top mobile apps of the year",
    "Gardening tips for beginners"
]

# Path to the Edge WebDriver
edge_driver_path = r'C:\Users\shiva\Downloads\edgedriver_win32\msedgedriver.exe'

# Set up the Edge WebDriver service
service = Service(edge_driver_path)

# Create a new instance of the Edge driver
driver = webdriver.Edge(service=service)

# Iterate over the list of search items and perform the search
for item in search_items:  # Search for all items in the list
    # Open the search engine (e.g., Bing)
    driver.get("https://www.bing.com")

    # Find the search box element using By.NAME
    search_box = driver.find_element(By.NAME, "q")

    # Enter the search item and submit the search
    search_box.send_keys(item)
    search_box.send_keys(Keys.RETURN)

    # Wait for a few seconds to let the search results load
    time.sleep(5)

# Close the browser
driver.quit()

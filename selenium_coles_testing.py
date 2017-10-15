import os
import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

# Optional argument, add path to find your webdriver
chrome_options = Options()

# Making headless
chrome_options.add_argument("--headless")

#Specifying to use Chrome Canary by specifying the binary location of the same. Note that normal chrome build binary will be in different location.
chrome_options.binary_location = 'C:\\Users\\gagan\\AppData\\Local\\Google\\Chrome SxS\\Application\\chrome.exe'


#location of chromedriver. In this case, it is saved in the same location as this script is saved and running from.
driver = webdriver.Chrome(executable_path=os.path.abspath("chromedriver.exe"), chrome_options=chrome_options)

driver.get('https://www.coles.com.au')

oldtab = driver.current_window_handle

# example 1 - find and test the link for 'Catalogues & specials'
catalogues = driver.find_element_by_partial_link_text("Catalogues & specials")

if catalogues is not None:
    print("Found the right link for Catalogues & specials")
    catalogues.click()
    print("The description for this link is : " + str(catalogues.text))
    time.sleep(4)
else:
    print("Can't find the right link for Catalogues & specials")

# example 2 - find and test the link for 'Shop online'
online = driver.find_element_by_partial_link_text("Shop online")

if online is not None:
    print("Found the right link for Shop online")
    online.click()
    print("The description for this link is : " + str(online.text))
    time.sleep(4)
    driver.switch_to.window(oldtab)
    time.sleep(2)
else:
    print("Can't find the right link for Shop online")

# example 3 - find and test the link for 'Locations & hours'
locations = driver.find_element_by_partial_link_text("Locations & hours")

if locations is not None:
    print("Found the right link for Locations & hours")
    locations.click()
    print("The description for this link is : " + str(locations.text))
    time.sleep(4)
else:
    print("Can't find the right link for Locations & hours")

# example 4 - find and test the link for 'Recipes & tips'
recipes = driver.find_element_by_partial_link_text("Recipes & tips")

if recipes is not None:
    print("Found the right link for Recipes & tips")
    recipes.click()
    print("The description for this link is : " + str(recipes.text))
    time.sleep(4)
else:
    print("Can't find the right link for Recipes & tips")

# example 5 - find and test the link for 'Our Range'
range = driver.find_element_by_partial_link_text("Our Range")

if range is not None:
    print("Found the right link for Our Range")
    range.click()
    print("The description for this link is : " + str(range.text))
    time.sleep(4)
else:
    print("Can't find the right link for Our Range")

# example 6 - find and test the link for 'Corporate responsibility'
corporate = driver.find_element_by_partial_link_text("Corporate responsibility")

if corporate is not None:
    print("Found the right link for Corporate responsibility")
    corporate.click()
    print("The description for this link is : " + str(corporate.text))
    time.sleep(4)
else:
    print("Can't find the right link for Corporate responsibility")

time.sleep(4)
driver.quit()

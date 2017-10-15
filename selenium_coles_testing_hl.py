import time
import os
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys

# Optional argument, add path to find your webdriver
chrome_options = Options()

# Making headless
chrome_options.add_argument("--headless")

#Specifying to use Chrome Canary by specifying the binary location of the same. Note that normal chrome build binary will be in different location.
chrome_options.binary_location = 'C:\\Users\\gagan\\AppData\\Local\\Google\\Chrome SxS\\Application\\chrome.exe'


#location of chromedriver. In this case, it is saved in the same location as this script is saved and running from.
driver = webdriver.Chrome(executable_path=os.path.abspath("chromedriver.exe"), chrome_options=chrome_options)


#Launching the website.
driver.get('https://www.coles.com.au')

# step 1 : find the search bar and enter my favourite yogurt description
search_bar = driver.find_element_by_id("ctl19_ctl02_txtSearch")
search_bar.send_keys("Berry Punnet Yoghurt 6 pack")
time.sleep(4)

# step 2 : find my favourite yogurt
search_icon = driver.find_element_by_id("ctl19_ctl02_btnButtonSearch")
search_icon.click()
time.sleep(4)

found = False

try:
    assert "Berry Punnet Yoghurt 6 pack" in driver.page_source
    found = True
except:
    print("\n\n\nSeach Item not present in the page!\n\n\n")

if found:
    print ("\n\n\nYour item is available to place order for !\n\n\n")

# step 3 : select my favourite yogurt
driver.execute_script("window.scrollBy(0, 600);")
confirmation = driver.find_element_by_class_name("button-main-inner")
confirmation.click()
time.sleep(4)

# step 4 : sign in to order my favourite yogurt
login = driver.find_element_by_class_name("login")
login.click()
time.sleep(4)

time.sleep(4)
driver.close()

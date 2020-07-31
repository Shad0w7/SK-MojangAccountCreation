from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome('/Users/ayushnayak/Downloads/chromedriver')
driver.get("https://www.google.com")
parentGUID = driver.current_window_handle

# open a link in a new window
actions = ActionChains(driver)
about = driver.find_element_by_link_text('About')
actions.key_down(Keys.COMMAND).click(about).key_up(Keys.COMMAND).perform()

driver.switch_to.window(driver.window_handles[-1])


driver.get("https://stackoverflow.com")

childGUID = driver.current_window_handle

input()

driver.switch_to.window(parentGUID)

input()
driver.quit()
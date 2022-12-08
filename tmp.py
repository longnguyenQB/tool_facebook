from selenium import webdriver
from selenium.webdriver.chrome.options import Options
def launchBrowser():
    chrome_options = Options()
    chrome_options.binary_location="../Google Chrome"
    chrome_options.add_argument("start-maximized");
    driver = webdriver.Chrome(chrome_options=chrome_options)

    driver.get("http://www.google.com/")
    return driver
driver = launchBrowser()
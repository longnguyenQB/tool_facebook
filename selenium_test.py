from selenium import webdriver
from selenium.webdriver.chrome.options import Options

# options = [Options()]
# options[0].add_argument("user-data-dir=C:/Users/GroooDev/AppData/Local/Google/Chrome/User Data")
# options[0].add_argument("--profile-directory=Profile 2")

# drivers = [webdriver.Chrome(executable_path=r'C:/Development/chromedriver.exe', options=options[0]), webdriver.Chrome(executable_path=r'C:/Development/chromedriver.exe', options=options[0])]

# drivers[0].get("https://instagram.com")
def launchBrowser():
   chrome_options = Options()
   chrome_options.add_argument("user-data-dir=C:/Users/GroooDev/AppData/Local/Google/Chrome/User Data")
   chrome_options.add_argument("disable-infobars");
   chrome_options.add_argument("--profile-directory=Profile 3")
   driver = webdriver.Chrome(chrome_options=chrome_options)

   driver.get("http://www.facebook.com/")
   while(True):
       pass
launchBrowser()

import os
import sys
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options  

chrome_options = Options()
chrome_options.add_argument("--headless")
chrome_options.binary_location = '/usr/bin/google-chrome'

url = f"http://{sys.argv[1]}:82/devopsIQ/";
print(f"Testing Website: {url}")
driver = webdriver.Chrome(executable_path=os.path.abspath("/usr/local/bin/chromedriver"), chrome_options=chrome_options)
driver.get(url);
expectedTitle = "Cloudtrain Website";
actualTitle = driver.title;
print(actualTitle);
print(f"Website Title Expected: {expectedTitle}");
print(f"Website Title Actual: {actualTitle}");
if actualTitle == expectedTitle:
    print("TEST PASSED!");
else:
    print("TEST FAILED!");
driver.close()

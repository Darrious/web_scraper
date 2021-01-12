from selenium import webdriver

# This is the path I use
# DRIVER_PATH = '.../Desktop/Scraping/chromedriver 2'# Put the path for your ChromeDriver here
DRIVER_PATH = "C:/Users/Oreo/Desktop/Muad'DIb/Coding/Python/chromedriver.exe"
wd = webdriver.Chrome(executable_path=DRIVER_PATH)
wd.get('https://google.com/')

search_box = wd.find_element_by_css_selector('input.gLFyf')
search_box.send_keys('Dogs')

wd.implicitly_wait(10)

search_button = wd.find_elements_by_xpath("//input[@name='btnK' and @value='Google Search']")[0]
search_button.click()

 	



#wd.quit()
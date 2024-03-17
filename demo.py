import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By


#initialize web page

def futuratek():
    try:
        cService = webdriver.ChromeService(executable_path='C:/chromedriver-win64/chromedriver.exe')
        cOptions = webdriver.ChromeOptions()
        cOptions.add_argument("user-data-dir=/Users/Admin/AppData/Local/Google/Chrome/User Data")
        cOptions.add_argument("disable-infobars")
        cOptions.add_argument("--start-maximized")
        driver = webdriver.Chrome(service=cService, options=cOptions)
        
        driver.get("https://futuratek.com/")

        #get parent page
        parent_window = driver.current_window_handle

        #get all clickable elements or ads
        elems = driver.find_elements(By.CLASS_NAME, "prdocutname")
        links = []

            #1. store all the <a> tag and its links as a map
        for elem in elems: links.append(elem.get_attribute('href'))
            #2. click first element
        for link in links:
            #4. look for the <a> which href attr is the same as the next link
            clickable = driver.find_element(By.XPATH, f"//a[@href='{link}' and @class='prdocutname']")
                
            if clickable != None:
                clickable.click()
                print(link)
                time.sleep(1.5)
            #3. go one step back in the browser
                driver.back();
                time.sleep(1.5)
            #5. click and repeat process
    except Exception as err:
        print(err)
        driver.quit()


counter = 0
while(counter < 5):
    futuratek()
    counter += 1     

'''FIRST DEMO WITH OUR OWN WEBPAGE

////////////////////////////////

counter = 0

#initialize web page
driver = webdriver.Chrome()
driver.get("http://127.0.0.1:5500/index.html")

#get parent page
parent_window = driver.current_window_handle

time.sleep(10)
while(counter <= 5):

    #get all clickable elements or ads
    elems = driver.find_elements(By.CLASS_NAME, "ads")
    
    for elem in elems:
        #for each element find it's link
        link = elem.find_element(By.CLASS_NAME, 'ad_link')
        
        #click the link and then go back to parent window
        link.click()
        driver.switch_to.window(parent_window)
        
    #get all tabs handle and compare them to the parent handle
    all_windows = driver.window_handles
    for handle in all_windows:
        if handle != parent_window:
            driver.switch_to.window(handle)
            print(driver.title)
            driver.close()

    #swith again to parent window 
    driver.switch_to.window(parent_window)
    counter+=1

'''
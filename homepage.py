from preqreqs import *
from homepage_urls import *


# initialize the driver
options = webdriver.ChromeOptions()
options.add_argument("--disable-gpu")
options.add_argument("--disable-software-rasterizer")
driver = webdriver.Chrome(ChromeDriverManager().install())
parent_path = os.path.dirname(os.path.dirname(os.path.realpath(__file__)))


wait = None

def loadPage():
    # Load the page
    driver.get(HOMEPAGE_URL)
    
    global wait
    wait = WebDriverWait(driver, 5)
    #Wait for it to load
    driver.implicitly_wait(5)
    driver.maximize_window()
    
    return wait

def accessURL():
    wait = loadPage()

    # Get the shopping categories button
    button = driver.find_element_by_class_name(SHOPPING_CATEGORY_CLASS)
    button.click()

    
    time.sleep(5)

def main():
    accessURL()
    driver.close()


if __name__ == '__main__':
    main()
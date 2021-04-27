import time
from selenium import webdriver

browser = webdriver.Chrome("C:/Users/MarioJerez/Desktop/PythonProjects/mileageProgram/chromedriver/chromedriver_win32/chromedriver.exe")

#BestBuy RTX 3080 page
page = browser.get("https://www.bestbuy.com/site/nvidia-geforce-rtx-3080-10gb-gddr6x-pci-express-4-0-graphics-card-titanium-and-black/6429440.p?skuId=6429440")

#Surface test page
#page = browser.get("https://www.bestbuy.com/site/microsoft-surface-go-2-10-5-touch-screen-intel-pentium-gold-4gb-64gb-ssd-device-only-platinum/6408476.p?skuId=6408476")

q = False

while not q:
    try:
        addToCartBtn = addButton = browser.find_element_by_class_name("btn-disabled")

        print("Button is not ready yet")

        time.sleep(.5)
        browser.refresh()

    except:

        addToCartBtn = addButton = browser.find_element_by_class_name("btn-primary")
        print("Button was clicked")
        addToCartBtn.click()
        q = True

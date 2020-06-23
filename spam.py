from selenium import webdriver
from selenium.webdriver.firefox.firefox_binary import FirefoxBinary
import time
import platform

opr_sys = platform.system()

def initWebdriver():
    driver = None
    if opr_sys == 'Windows': driver = webdriver.Firefox(executable_path=r"./Resource/chromedriver.exe")
    if opr_sys == 'Linux': driver = webdriver.Firefox(executable_path=r"./Resource/geckodriver")
    driver.maximize_window()
    driver.switch_to_default_content
    time.sleep(2)
    return driver

def openPageFromUrl(driver, url):
    try:
        driver.get(url)
        print("Page opened")
    except Exception:
        print("Page failed to open.")
        exit(0)

def openPageInstagram(driver):
    try:
        driver.get("https://www.instagram.com")
        print("Page opened")
    except Exception:
        print("Page failed to open. Type the new URL of your page")
        newUrl = str(input())
        openPageFromUrl(driver,newUrl)

def openPageWhatsapp(driver):
    try:
        driver.get("https://web.whatsapp.com")
        print("Page opened")
    except Exception:
        print("Page failed to open. Type the new URL of your page")
        newUrl = str(input())
        openPageFromUrl(driver,newUrl)

def Login():
    print("Waiting for user to login")
    print("Type 's' when logged in and press enter")
    s = str(input())
    if s == 's': print("loggedIn")
    else : print("You should have typed 's'")

def OpenMessage():
    print("Open the person you want to spam to")
    print("Type 'm' when opened and press enter")
    s = str(input())
    if s == 'm': print("loggedIn")
    else: print("You should have typed 'm'")

def findTheFieldInstagram(driver):
    try:
        textArea = driver.find_element_by_xpath("/html/body/div[1]/section/div/div[2]/div/div/div[2]/div[2]/div/div[2]/div/div/div[2]/textarea")
        return textArea
    except Exception:
        return None

def findTheFieldWhatsapp(driver):
    try:
        textArea = driver.find_element_by_xpath("/html/body/div[1]/div/div/div[4]/div/footer/div[1]/div[2]/div/div[2]")
        return textArea
    except Exception:
        return None

def automateSpam(listObj, types):

    driver = initWebdriver()
    if types == 'W' or types == 'w': openPageWhatsapp(driver)
    if types == 'I' or types == 'i': openPageInstagram(driver)

    Login()
    OpenMessage()
    textArea = None
    if types == 'W' or types == 'w': textArea = findTheFieldWhatsapp(driver)
    if types == 'I' or types == 'i': textArea = findTheFieldInstagram(driver)
    if textArea == None: 
        print("Something went wrong. Try Again")
        exit(0)

    for i in listObj:
        textArea.send_keys(i)
        textArea.send_keys("\n")
        time.sleep(1)
    print("Spam ended")
    driver.close()

print('Enter the text you want to spam. When finished press Enter and then type "3TDone" without quotes and press Enter')
stuff = str("")
while True:
    temp = str(input())
    if temp == '3TDone' : break
    stuff= stuff +" " +temp
stuff_in_list =  stuff.split(sep = " ")
print("\nEnter the website you want to spam on \nW for Whatsapp, I for Instagram, F for facebook")
typeSite = str(input())

automateSpam(stuff_in_list, typeSite[0])

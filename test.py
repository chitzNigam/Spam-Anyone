# from selenium import webdriver
# from selenium.webdriver.firefox.firefox_binary import FirefoxBinary
# import time
# import platform

# opr_sys = platform.system()

# def initWebdriver():
#     driver = None
#     if opr_sys == 'Windows': driver = webdriver.Chrome(executable_path=r"./Resource/chromedriver.exe")
#     if opr_sys == 'Linux': driver = webdriver.Firefox(executable_path=r"./Resource/geckodriver")
#     driver.maximize_window()
#     driver.switch_to_default_content
#     time.sleep(2)
#     return driver
# def login(username,password):
#         driver.get("https://www.instagram.com/")

#         time.sleep(2)
#         username_field = driver.find_element_by_xpath(
#             "/html/body/div[1]/section/main/article/div[2]/div[1]/div/form/div[2]/div/label/input"
#             )

#         password_field = driver.find_element_by_xpath(
#             "/html/body/div[1]/section/main/article/div[2]/div[1]/div/form/div[3]/div/label/input"
#             )
#         username_field.send_keys(username)
#         password_field.send_keys(password)

#         driver.find_element_by_xpath(
#             "/html/body/div[1]/section/main/article/div[2]/div[1]/div/form/div[4]/button/div"
#             ).click()
#         time.sleep(2)

#         try:
#             driver.find_element_by_xpath(
#             "/html/body/div[1]/section/main/article/div[2]/div[1]/div/form/div[7]/p"
#             )
#             return False
#         except Exception:
#             return True

# driver = initWebdriver()
# login('the_original_chitz','[#!+R@~$# abcd 12349')
# time.sleep(2)
# driver.get('https://www.instagram.com/aadishasingh')
# time.sleep(2)
# driver.find_element_by_xpath('/html/body/div[1]/section/main/div/header/section/div[1]/div[1]/div/button').click()
# for i in range(10000000): 
#     try:
#         driver.find_element_by_xpath('/html/body/div[1]/section/div/div[2]/div/div/div[2]/div[2]/div/div[2]/div/div/div[2]/textarea')
#         success = True
#         break
#     except Exception:
#         pass
                
# name = driver.find_element_by_xpath('/html/body/div[1]/section/div/div[2]/div/div/div[2]/div[1]/div/div/div[2]/div/div[2]/button/div/div[1]/div')
# print(name.text)

from tkinter import *
root=Tk()
def retrieve_input():
    inputValue=textBox.get("1.0","end-1c")
    print(inputValue)

textBox=Text(root, height=2, width=10)
textBox.pack()
buttonCommit=Button(root, height=1, width=10, text="Commit", 
                    command=lambda: retrieve_input())
#command=lambda: retrieve_input() >>> just means do this when i press the button
buttonCommit.pack()

mainloop()
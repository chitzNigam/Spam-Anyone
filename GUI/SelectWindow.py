import tkinter as tk
import threading
import spam
from FacebookLogin import FacebookLogin
from InstagramLogin import InstagramLogin
from WhatsappLogin import WhatsappLogin
driver = None

def for_instagram():
    root.destroy()
    InstagramLogin(driver)

def for_facebook():
    root.destroy()
    FacebookLogin(driver)

def for_whatsapp():
    root.destroy()
    WhatsappLogin(driver)

if __name__ == "__main__":
    driver = spam.initWebdriver()
    root = tk.Tk()
    # root.geometry("400x200")
    root.configure(background = "#ffffff")
    root.title("Spam Anyone")
    label = tk.Label(root, text = "Select the application you want to spam on")
    facebook = tk.Button(root, text = 'Facebook', command = for_facebook)
    instagram = tk.Button(root, text = 'Instagram', command = for_instagram)
    whatsapp = tk.Button(root, text = 'Whatsapp', command = for_whatsapp)
    facebook.configure(background = "#ffffff")
    label.configure(background = "#ffffff")
    whatsapp.configure(background = "#ffffff")
    instagram.configure(background = "#ffffff")
    label.pack(pady=(20,10),padx = (50,50))
    facebook.pack(pady=(10,0))
    instagram.pack(pady=(10,0))
    whatsapp.pack(pady=(10,20))
    root.mainloop()


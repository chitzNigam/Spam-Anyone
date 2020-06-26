import sys

try:
    import Tkinter as tk
except ImportError:
    import tkinter as tk

try:
    import ttk
    py3 = False
except ImportError:
    import tkinter.ttk as ttk
    py3 = True
import requests
import spam
import time

class Instagram:

    driver = None
    def check_username(self):
        username = self.TEntry1.get()
        if username[0] == "@":
            username = username[1:]
        response = requests.get("https://www.instagram.com/"+username)
        if response.status_code == 200: return True
        else: return False
    
    def can_message(self):
        if not self.check_username(): return False
        username = self.TEntry1.get()
        if username[0] == "@":
            username = username[1:]
        self.driver.get("https://www.instagram.com/"+username)
        for i in range(10000000): 
            try:
                self.driver.find_element_by_xpath('/html/body/div[1]/section/main/div/header/section/div[1]/div[1]/div/button')
                return True
            except Exception:
                return False
        return False

    def change_status(self,status):
        if status == 0: #all conditions success start
            self.Button1.configure(text = "Stop")
            tk.messagebox.showinfo("Success","Your spam will start now")
        elif status == 1: #spam finished
            self.Button1.configure(text = "Start")
            tk.messagebox.showinfo("Finished","Your spam has finished now. Thank you!")
        elif status == 2: #bad username
            tk.messagebox.showerror("Error","Invalid username or you cannot chat with the person")

    def check_clicked(self):
        if self.can_message():
            self.Button2.configure(text = "Valid")
        else: 
            self.Button2.configure(text = "Not Valid")

    def listener(self):
        self.Button2.configure(text = "Check")

    def start_clicked(self):
        if self.Button1['text'] == 'Start':
            self.Button1.configure(text ='Stop')
            self.start_spam()
        else :
            #need to add Thread
            self.Button1.configure(text = 'Start')
            
    def start_spam(self):
        username = self.TEntry1.get()
        if username[0] == "@":
            username = username[1:]
        if not self.can_message(): 
            self.change_status(2)
            return "False"

        self.driver.get("https://www.instagram.com/"+username)
        button = None
        for i in range(10000000):
            try:
                button = self.driver.find_element_by_xpath('/html/body/div[1]/section/main/div/header/section/div[1]/div[1]/div/button')
                break
            except Exception:
                continue
        button.click()
        text = None
        for i in range(10000000): 
            try:
                text = self.driver.find_element_by_xpath('/html/body/div[1]/section/div/div[2]/div/div/div[2]/div[2]/div/div[2]/div/div/div[2]/textarea')
                break
            except Exception:
                continue
        
        name = self.driver.find_element_by_xpath('/html/body/div[1]/section/div/div[2]/div/div/div[2]/div[1]/div/div/div[2]/div/div[2]/button/div/div[1]/div')
        if not name.text == username: 
            self.change_status(2)
            return "False"
        spam_text = self.spam_text.get("1.0",'end-1c')
        spam_text_in_list =  spam_text.split(sep = " ")

        self.change_status(0)
        for i in spam_text_in_list:
            text.send_keys(i)
            text.send_keys("\n")
            time.sleep(1)
        print("Spam ended")
        self.change_status(1)
        return "success"

    def __init__(self, driver=None):
        '''This class configures and populates the toplevel window.
           top is the toplevel containing window.'''
        self.driver = driver
        self.top = tk.Tk()
        _bgcolor = '#d9d9d9'  # X11 color: 'gray85'
        _fgcolor = '#000000'  # X11 color: 'black'
        _compcolor = '#d9d9d9' # X11 color: 'gray85'
        _ana1color = '#d9d9d9' # X11 color: 'gray85'
        _ana2color = '#ececec' # Closest X11 color: 'gray92'
        font11 = "-family {Vemana2000} -size 10"
        font12 = "-family {Waree} -size 10 -weight bold"
        font13 = "-family {Waree} -size 9"
        self.style = ttk.Style()
        if sys.platform == "win32":
            self.style.theme_use('winnative')
        self.style.configure('.',background=_bgcolor)
        self.style.configure('.',foreground=_fgcolor)
        self.style.configure('.',font="TkDefaultFont")
        self.style.map('.',background=
            [('selected', _compcolor), ('active',_ana2color)])

        self.top.geometry("702x596+329+72")
        self.top.minsize(1, 1)
        self.top.maxsize(1351, 738)
        self.top.resizable(1, 1)
        self.top.title("Spam Anyone")
        self.top.configure(background="#5757ff")

        self.menubar = tk.Menu(self.top,font="TkMenuFont",bg=_bgcolor,fg=_fgcolor)
        self.top.configure(menu = self.menubar)

        self.Label1 = tk.Label(self.top)
        self.Label1.place(relx=0.078, rely=0.055, height=28, width=589)
        self.Label1.configure(background="#5757ff")
        self.Label1.configure(font=font12)
        self.Label1.configure(foreground="#ffffff")
        self.Label1.configure(text='''Insert the text you want to spam''')

        self.spam_text = tk.Text(self.top)
        self.spam_text.place(relx=0.313, rely=0.134, relheight=0.426
                , relwidth=0.379)
        self.spam_text.configure(font=font11)
        self.spam_text.configure(wrap="word")

        self.Label1_2 = tk.Label(self.top)
        self.Label1_2.place(relx=0.028, rely=0.57, height=72, width=673)
        self.Label1_2.configure(background="#5757ff")
        self.Label1_2.configure(font=font12)
        self.Label1_2.configure(foreground="#ffffff")
        self.Label1_2.configure(text='''Insert the username of person you want to spam.\nFormat- @username (make sure it is correct)''')

        self.TEntry1 = ttk.Entry(self.top)
        self.TEntry1.place(relx=0.313, rely=0.700, relheight=0.042
                , relwidth=0.276)

        self.Button1 = tk.Button(self.top, command = self.start_clicked)
        self.Button1.place(relx=0.313, rely=0.822, height=35, width=270)
        self.Button1.configure(background="#ffffff")
        self.Button1.configure(disabledforeground="#000000")
        self.Button1.configure(text='''Start''')

        self.Button2 = tk.Button(self.top,command = self.check_clicked)
        self.Button2.place(relx=0.584, rely=0.700, height=25, width=76)
        self.Button2.configure(background="#ffffff")
        self.Button2.configure(font=font13)
        self.Button2.configure(relief="groove")
        self.TEntry1.bind("<Key>",self.listener)
        self.Button2.configure(text='''Check''')
        self.top.mainloop()

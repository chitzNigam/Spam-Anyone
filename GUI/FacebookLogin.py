import sys
import time
import Facebook

try:
    import Tkinter as tk
    from Tkinter import messagebox
except ImportError:
    import tkinter as tk
    from tkinter import messagebox

try:
    import ttk
    py3 = False
except ImportError:
    import tkinter.ttk as ttk
    py3 = True


class FacebookLogin:

    def login(self,username,password):
        self.driver.get("https://www.facebook.com/")

        time.sleep(2)
        username_field = self.driver.find_element_by_xpath(
            "/html/body/div[1]/section/main/article/div[2]/div[1]/div/form/div[2]/div/label/input"
            )

        password_field = self.driver.find_element_by_xpath(
            "/html/body/div[1]/section/main/article/div[2]/div[1]/div/form/div[3]/div/label/input"
            )
        username_field.send_keys(username)
        password_field.send_keys(password)

        self.driver.find_element_by_xpath(
            "/html/body/div[1]/section/main/article/div[2]/div[1]/div/form/div[4]/button/div"
            ).click()
        time.sleep(2)

        try:
            self.driver.find_element_by_xpath(
            "/html/body/div[1]/section/main/article/div[2]/div[1]/div/form/div[7]/p"
            )
            return False
        except Exception:
            return True

    def loginsubmit(self):
        ret = self.login(self.TEntry1.get(),self.TEntry2.get())
        if ret: 
            messagebox.showinfo("", "Login Successful")
            self.top.quit()
            Facebook.Facebook(self.driver)
        else : messagebox.showinfo("","Login unsuccessful. Try again!")

    def __init__(self, driver=None):
        self.driver = driver
        self.top = tk.Tk()
        _bgcolor = '#d9d9d9'  # X11 color: 'gray85'
        _fgcolor = '#000000'  # X11 color: 'black'
        _compcolor = '#d9d9d9' # X11 color: 'gray85'
        _ana1color = '#d9d9d9' # X11 color: 'gray85'
        _ana2color = '#ececec' # Closest X11 color: 'gray92'
        self.style = ttk.Style()
        if sys.platform == "win32":
            self.style.theme_use('winnative')
        self.style.configure('.',background=_bgcolor)
        self.style.configure('.',foreground=_fgcolor)
        self.style.configure('.',font="TkDefaultFont")
        self.style.map('.',background=
            [('selected', _compcolor), ('active',_ana2color)])

        self.top.geometry("420x277+451+136")
        self.top.minsize(1, 1)
        self.top.maxsize(1351, 738)
        self.top.resizable(1, 1)
        self.top.title("Login to Facebook Account")
        self.top.configure(borderwidth="10")
        self.top.configure(background="#fdfdfd")

        self.Username = tk.Label(self.top)
        self.Username.place(relx=0.024, rely=0.289, height=15, width=199)
        self.Username.configure(activebackground="#ffffff")
        self.Username.configure(background="#fdfdfd")
        self.Username.configure(borderwidth="10")
        self.Username.configure(cursor="fleur")
        self.Username.configure(text='''Enter your email :''')

        self.Label1 = tk.Label(self.top)
        self.Label1.place(relx=0.024, rely=0.469, height=16, width=194)
        self.Label1.configure(background="#fdfdfd")
        self.Label1.configure(borderwidth="10")
        self.Label1.configure(text='''Enter your Password :''')

        self.TEntry1 = ttk.Entry(self.top)
        self.TEntry1.place(relx=0.5, rely=0.289, relheight=0.069, relwidth=0.438)

        username = self.TEntry1.register(self.top)
        self.TEntry1.configure(invalidcommand=(username))
        self.TEntry1.configure(takefocus="")
        self.TEntry1.configure(cursor="xterm")

        self.TEntry2 = ttk.Entry(self.top,show="*")
        self.TEntry2.place(relx=0.495, rely=0.469, relheight=0.069
                , relwidth=0.438)
        password = self.TEntry2.register(self.top)
        self.TEntry2.configure(invalidcommand=(password))
        self.TEntry2.configure(takefocus="")
        self.TEntry2.configure(cursor="fleur")

        self.TButton1 = ttk.Button(self.top, command = self.loginsubmit)
        self.TButton1.place(relx=0.236, rely=0.668, height=32, width=83)
        self.TButton1.configure()
        self.TButton1.configure(takefocus="")
        self.TButton1.configure(text='''Login''')

        self.TButton2 = ttk.Button(self.top, command = self.top.destroy)
        self.TButton2.place(relx=0.567, rely=0.668, height=32, width=83)
        self.TButton2.configure(takefocus="")
        self.TButton2.configure(text='''Cancel''')

        self.Label2 = tk.Label(self.top)
        self.Label2.place(relx=0.048, rely=0.108, height=25, width=370)
        self.Label2.configure(background="#fdfdfd")
        self.Label2.configure(text='''Log in to your Facebook Account''')
        self.top.mainloop()

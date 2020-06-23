import sys
import time
import Whatsapp

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


class WhatsappLogin:
    
    def get_qr(self):
        pass
        

    def __init__(self, driver=None):
        self.driver = driver
        self.top = tk.Tk()
        

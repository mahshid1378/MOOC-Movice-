import tkinter as tk
from tkinter import scrolledtext
from tkinter import filedialog,ttk
from tkinter import messagebox as mbox
import speech_recognition as sr

from VideoSeekUtils import test
class Mygui:
    def __init__(self, root):
        self.root = root
        root.title("A simple GUI")
        self.frame = tk.Frame(root, bg='yellow')
        self.root.grid_rowconfigure(1, weight=1)
        self.root.grid_columnconfigure(0, weight=1)
        self.filename=""
        self.stext=""
        self.frame.grid(row=0, sticky="ew")
    
        self.label = tk.Label(self.frame, text="Video-Seek",bg="yellow")
        self.label.config(font=("Courier", 44))
        self.label.pack()
    
        self.center = tk.Frame(self.root, bg='gray', width=50, height=40, padx=5, pady=5)
        self.center.grid(row=1, sticky="nsew")
    
        self.button = tk.Button(self.center,text="SelectFile",activebackground="green",activeforeground="white",font="Times",padx=10,pady=5,command=self.addApp).pack()
    
        self.label2 = tk.Label(self.center, text="Insert Youtube Url",bg="gray",fg="white")
        self.label2.config(font=("Times", 18))
        self.label2.pack()
        
        self.textFrame = scrolledtext.ScrolledText(self.center, height=2,width=25, bd=10, font="Times")
        self.textFrame.pack()
        
        self.label1 = tk.Label(self.center, text="Enter keywords",bg="gray",fg="white")
        self.label1.config(font=("Times", 18))
        self.label1.pack()
        
        self.entry = tk.Entry(self.center)
        self.entry.pack()
    
        self.result = tk.Button(self.center,text="Result",width=10,height=2,activebackground="green",activeforeground="white",font="Times",command=self.fresult).pack()
    
       
    def addApp(self):
        #if self.speech_status:
            #mbox.showwarning("Warning","You already selected Speech as input,Please select only one option for input")
            #return
        self.textFrame.configure(state='disabled')
        self.filename = filedialog.askopenfilename(initialdir="/",title="Select File",filetypes=(("videofiles",".mp4"),("all files","*.*")))
        if self.filename =="":
            self.textFrame.configure(state='normal')
            mbox.showwarning("Warning","No File Selected.Please Select file or enter video url")
        else:
            mbox.showinfo("Information","You Have selected "+self.filename)
        
    def fresult(self):
        keywor = self.entry.get()
        if len(self.filename)==0 and len(self.textFrame.get("1.0", tk.END))==1 and len(self.stext)==0:
            mbox.showerror("Error","Please select a Video file")
        ip=""
        if len(self.filename)!=0 and len(self.textFrame.get("1.0", tk.END))!=1 and len(self.stext)!=0:
            mbox.showerror("Error","Please select only Video or enter video url")
        if self.filename=="":
            ip = self.textFrame.get("1.0", tk.END)
        if self.stext!="":
            test(self.stext,keywor)
        if ip=="":
            test(self.openfile())
            import time 
            self.progress['value'] = 50
            self.center.update_idletasks() 
            time.sleep(1) 
        
            self.progress['value'] = 100
            self.center.update_idletasks() 
            time.sleep(1) 
        else:
            test(ip,keywor)
            
    def openfile(self):
        with open(self.filename,"r") as f:
            ip = f.read()
            ip = ip.lower()
        return ip
   
        
root = tk.Tk()
root.geometry("1540x785+0+0")
mygui = Mygui(root)
root.mainloop()
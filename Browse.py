from tkinter import *
from tkinter import ttk
from tkinter import filedialog
import PDFMerg
 
file = open('PDFMerg.txt','w')
class Root(Tk):
    def __init__(Shivam):
        super(Root, Shivam).__init__()
        Shivam.title("PDF Merg")
        Shivam.minsize(400, 400)
 
        Shivam.labelFrame = ttk.LabelFrame(Shivam, text = "Open File")
        Shivam.labelFrame.grid(column = 0, row = 1, padx = 20, pady = 20)
        Shivam.labelFrame2=ttk.LabelFrame(Shivam, text = "OK")
        Shivam.labelFrame2.grid(column = 2, row = 1, padx = 20, pady = 20)
        Shivam.button()
 
 
 
    def button(Shivam):
        Shivam.button = ttk.Button(Shivam.labelFrame, text = "Browse A File",command = Shivam.fileDialog)
        Shivam.button.grid(column = 1, row = 1)
        Shivam.button2 = ttk.Button(Shivam.labelFrame2, text = "Done",command = Shivam.destroy)
        Shivam.button2.grid(column = 3, row = 1)
    def fileDialog(Shivam):
        path=[]
        
        Shivam.filename = filedialog.askopenfilename(initialdir =  "/", title = "Select A File", filetype =[("PDF files","*.pdf")])
        Shivam.label = ttk.Label(Shivam.labelFrame, text = "")
        path.append('"'+Shivam.filename+'",')
        Shivam.label.grid(column = 1, row = 2)
        Shivam.label.configure(text = Shivam.filename)
        
        for i in path:
            PDFMerg.write(path)
            
 
 
 
 
 
root = Root()
root.mainloop()

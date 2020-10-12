import os
import time
from time import  strftime
SHIVAM=os.getcwd()
try:
    from PyPDF2 import PdfFileMerger, PdfFileReader
except ImportError:
    print(("Run __init__.py"))
    os.system("__init__.py")
def pm(x):
    mergedObject = PdfFileMerger()
    for i in range(0, len(x)):
        mergedObject.append(PdfFileReader(x[i], 'rb'))
    os.chdir(SHIVAM)
    file=("YourMergedPDF"+str(strftime("%a%d%b%Y%H%M%S"))+".pdf")
    mergedObject.write(str(file))
    os.system(str(file))
    print("\n your file is saved at location")
    print(str(os.getcwd()))
    time.sleep(10)
def write(y):
    file = open('PDFMerg.txt','a+')
    for i in y :
        file.write(i)

def read():
    file = open('PDFMerg.txt', "r") 
    return (file.read())
    print(file.read())
def list(l):
    L=[]
    for i in l:
        L.append(i)
    return(L)
    print(L)
def reverse(r):
    return(r[::-1])
    print(r[::-1])
def replace(p,b,c):
    file = open(p, "rt")
    data = file.read()
    data = data.replace(b,c)
    file.close()
    file = open(p, "wt")
    file.write(data)
    file.close()

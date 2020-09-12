import __init__
import Browse
import PDFMerg as PM
import os
import Merger as M
PM.replace('PDFMerg.txt','/','\\\\')
print("\nPath of Your File\n", PM.read())
print('''\nExample:= "C:\\Users\\Shivam\\Downloads\\CamScanner 07-28-2020 13.22.15.pdf","D:\\Users\\Shivam\\Downloads\\New Doc 2020-07-21 19.27.15.pdf" ''')
print("\nNote := The file In C Drive will be First And file in D drive will be Second")
print('''\nExample (only for one file):= "C:\\Users\\Shivam\\Downloads\\CamScanner 07-28-2020 13.22.15.pdf",''')
print("\nNote:= Protected Pdf Need To Be Decrepted First By User")
print("\n Any Error Will Exit The Program")
print("\n You Can Change the order of PDF Files to be Merged")
print(' remove "", or " ", from Path Pasted ')
M.merger()
os.system("YourMergedPDF.pdf")

import os
import time
try:
    from PyPDF2 import*
except ImportError:
    print("Pleace turn on internet in 30 secto install PyPDF2")
    time.sleep(30)
    os.system("pip install PyPDF2")

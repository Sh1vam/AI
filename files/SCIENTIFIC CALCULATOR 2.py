import  tkinter 
from tkinter import *
import tkinter.messagebox as msg
import math
from math import*
import os
import statistics
from statistics import*

os.system("msg * GUI SCIENTIFIC CALCULATOR")
msg.showinfo("",'''Made by - Shivam.P.Patel

Class   - 12 Science

Roll No.- 27''')
msg.showinfo("HELP",'''YOU SHOULD CLOSE ALL BRACKET AND STRING'
POW(NUMBER,POWER)
GCD(NUMBER_1,NUMBER_2)
LOG(NUMBER,BASE)
INT("NUMBER TO CONVERT INTO DECIMAL",2<=BASE<=36)
YOUR ANSWER WILL NOT BE CALCULATED IF YOUR INPUT IS WRONG
YOU CAM TYPE YOUR OWN INPUT FROM PYTHON MODULE MATH & STATISTICS AND OTHER FUNCTIONS USING GIVEN KEYBOARD''')

class Calculator:
        def __init__(self, master):
            self.master = master
            master.title("Python Calculator  Made by - Shivam.P.Patel")

            # create screen widget
            self.screen = Text(master, state='disabled', width=26, height=2,background="black", foreground="Yellow",font=' ArialBold 20')

            # position screen in window
            self.screen.grid(row=0,column=0,columnspan=5,padx=5,pady=5)
           # self.screen.configure(state='normal')

            # initialize screen value as empty
            self.equation = ''

            # create buttons using method createButton
            
            b1 =  self.createButton(0)
            b2 = self.createButton(1)
            b3 = self.createButton(2)
            b4 = self.createButton(3)
            b5 = self.createButton(4)
            b6 = self.createButton(5)
            b7 = self.createButton(6)
            b8 = self.createButton(7)
            b9 = self.createButton(8)
            b10 = self.createButton(9)
            b11 = self.createButton(u"\u00F7")
            b12 = self.createButton('*')
            b13 = self.createButton('.')
            b14 = self.createButton('+')
            b15 = self.createButton('-')
            b16 = self.createButton(u"\u232B",None)
            b17 = self.createButton('sin((pi/180)*')
            b18 = self.createButton('cos((pi/180)*')
            b19 = self.createButton('tan((pi/180)*')
            b20 = self.createButton('ANSWER',None)
            b21 = self.createButton('sqrt(')
            b22 = self.createButton('(')
            b23 = self.createButton(')')
            b24 = self.createButton("//")
            b25 = self.createButton('pow(')
            b26 = self.createButton(',')
            b27 = self.createButton('>')
            b28 = self.createButton('<')
            b29 = self.createButton('!=')
            b30 = self.createButton('factorial(')
            b31 = self.createButton('~')
            b32 = self.createButton('exp(')
            b33 = self.createButton(')**(1/')
            b34 = self.createButton('%')
            b35 = self.createButton('radians(')
            b36 = self.createButton('degrees(')
            b37 = self.createButton('gcd(')
            b38 = self.createButton('e')
            b39 = self.createButton('pi')
            b40 = self.createButton('tau')
            b41 = self.createButton('log(')
            b42 = self.createButton('log10(')
            b43 = self.createButton('hex(')
            b44 = self.createButton('oct(')
            b45 = self.createButton('bin(')
            b46 = self.createButton('"')
            b47 = self.createButton('|')
            b48 = self.createButton(' and ')
            b49 = self.createButton(' or ')
            b50 = self.createButton(' ')
            b51 = self.createButton(u"\u0026")
            b52 = self.createButton("^")
            b53 = self.createButton("[")
            b54 = self.createButton("]")
            b55 = self.createButton("{")
            b56 = self.createButton("}")
            b57 = self.createButton('=')
            b58 = self.createButton('int("')
            b59 = self.createButton('A')
            b60 = self.createButton('B')
            b61 = self.createButton('C')
            b62 = self.createButton('D')
            b63 = self.createButton('E')
            b64 = self.createButton('F')
            b65 = self.createButton('G')
            b66 = self.createButton('H')
            b67 = self.createButton('I')
            b68 = self.createButton('J')
            b69 = self.createButton('K')
            b70 = self.createButton('L')
            b71 = self.createButton('M')
            b72 = self.createButton('N')
            b73 = self.createButton('O')
            b74 = self.createButton('P')
            b75 = self.createButton('Q')
            b76 = self.createButton('R')
            b77 = self.createButton('S')
            b78 = self.createButton('T')
            b79 = self.createButton('U')
            b80 = self.createButton('V')
            b81 = self.createButton('W')
            b82 = self.createButton('X')
            b83 = self.createButton('Y')
            b84 = self.createButton('Z')
            b85 = self.createButton('a')
            b86 = self.createButton('b')
            b87 = self.createButton('c')
            b88 = self.createButton('d')
            b89 = self.createButton('e')
            b90 = self.createButton('f')
            b91 = self.createButton('g')
            b92 = self.createButton('h')
            b93 = self.createButton('i')
            b94 = self.createButton('j')
            b95 = self.createButton('k')
            b96 = self.createButton('l')
            b97 = self.createButton('m')
            b98 = self.createButton('n')
            b99= self.createButton('o')
            b100 = self.createButton('p')
            b101 = self.createButton('q')
            b102 = self.createButton('r')
            b103 = self.createButton('s')
            b104 = self.createButton('t')
            b105 = self.createButton('u')
            b106 = self.createButton('v')
            b107 = self.createButton('w')
            b108 = self.createButton('x')
            b109 = self.createButton('y')
            b110 = self.createButton('z')
            # buttons stored in list
            buttons = [b1,b2,b3,b4,b5,b6,b7,b8,b9,b10,
                       b11,b12,b13,b14,b15,b16,b17,b18,b19,b20,
                       b21,b22,b23,b24,b25,b26,b27,b28,b29,b30,
                       b31,b32,b33,b34,b35,b36,b37,b38,b39,b40,
                       b41,b42,b43,b44,b45,b46,b47,b48,b49,b50,
                       b51,b52,b53,b54,b55,b56,b57,b58,b59,b60,
                       b61,b62,b63,b64,b65,b66,b67,b68,b69,b70,
                       b71,b72,b73,b74,b75,b76,b77,b78,b79,b80,
                       b81,b82,b83,b84,b85,b86,b87,b88,b89,b90,
                       b91,b92,b93,b94,b95,b96,b97,b98,b99,b100,
                       b101,b102,b103,b104,b105,b106,b107,b108,b109,b110]
            try:
                # intialize counter
                count = 0
                # arrange buttons with grid manager
                for row in range(1,110):
                    for column in range(5):
                        buttons[count].grid(row=row,column=column)
                        count += 1
            except:pass
        def createButton(self,val,write=True,width=9):
            # this function creates a button, and takes one compulsory argument, the value that should be on the button

            return Button(self.master, text=val,font='ArialBold 10',command = lambda: self.click(val,write), width=width,background="black",foreground="gold")

        def click(self,text,write):
            try:
            # this function handles what happens when you click a button
            # 'write' argument if True means the value 'val' should be written on screen, if None, should not be written on screen
                if write == None:

                    #only evaluate code when there is an equation to be evaluated
                    if text == 'ANSWER' and self.equation: 
                        # replace the unicode value of division ./.with python division symbol / using regex
                        self.equation= re.sub(u"\u00F7", '/', self.equation)
                        print(self.equation)
                        answer = str(eval(self.equation))
                        self.clear_screen()
                        self.insert_screen(answer,newline=True)
                    elif text == u"\u232B":
                        self.clear_screen()
                    
                else:
                    # add text to screen
                    self.insert_screen(text)
            except:pass
            else:pass
        def clear_screen(self):
            #to clear screen
            #set equation to empty before deleting screen
            self.equation = ''
            self.screen.configure(state='normal')
            self.screen.delete('1.0', END)

        def insert_screen(self, value,newline=False):
            self.screen.configure(state='normal')
            self.screen.insert(END,value)
            # record every value inserted in screen
            self.equation += str(value)
            self.screen.configure(state ='disabled')
  
root = Tk()
my_gui = Calculator(root)
root.mainloop()
    




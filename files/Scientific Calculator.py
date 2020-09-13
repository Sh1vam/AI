import math
from math import*
import os
import time
import statistics
print()
print('''Made by - Shivam.P.Patel

Class   - 11 Science

Roll No.- 27''')

time.sleep(2)

os.system('cls')

try:
    def menu():
              os.system("cls")
              print()
              print("MENU")
              print()
              print("Enter srno. to choose")
              print()
              print("0)  MODULUS")
              print("1)  ADDITION")
              print("2)  SUBTRACTION")
              print("3)  MULTIPLICATION")
              print("4)  DIVISION")
              print("5)  FLOOR DIVISION")
              print("6)  TRIGONOMETRIC FUNCTION")
              print("7)  EXPONENTIATION")
              print("8)  BASE CONVERSION")
              print("9)  FACTORIAL")
              print("10) PERMUTATION")
              print("11) COMBINATION")
              print("12) ROOTING")
              print("13) REMAINDER")
              print("14) LOG")
              print("15) ANGULAR CONVERSION")
              print("16) STATISTICS (for ungrouped data)")
              print("17) GREATEST COMMON DIVISOR")
              print("18) FACTOR FINDING")
              print("19) GREATEST AMONG THE THREE ")
              print("20) EXIT")
              print()
              list=['0','1','2','3','4','5','6','7','8','9','10','11','12','13','14','15','16','17','18','19','20']
              input0=input("ENTER YOUR CHOICE : ")
              print()
              if (input0=='0'):
                  def Modulus():
                      print("0)  MODULUS")
                      print()
                      a=eval(input("Enter no.: "))
                      print()
                      print('ANS = ',fabs(a))
                  Modulus()
              if (input0=='1'):
                  def Add():
                      print("1) ADDITION")
                      print()
                      a=eval(input("Enter all nos. with (',') : "))
                      print()
                      print('ANS = ',fsum(a))
                  Add()
              if(input0=='2') :
                  def Subtract():
                      print("2) SUBTRACTION")
                      print()
                      a=eval(input("Enter no. with ('-') : "))
                      print()
                      print('ANS = ',a)
                  Subtract()
              if(input0=='3'):
                  def Mutiply():
                      print("3) MULTIPLICATION")
                      print()
                      a=eval(input("Enter no. with('*'): "))
                      print()
                      print('ANS = ',a)
                  Mutiply()
              if(input0=='4'):
                  def Divide():
                      print("4) DIVISION")
                      print()
                      a=eval(input("Enter no. one : "))
                      b=eval(input("Enter no. two : "))
                      print()
                      if (b==0):
                          print("Zero Division Error : Division with ZERO is Not-Possible")
                          Divide()
                      else:
                          print('ANS = ',a/b)
                  Divide()
              if(input0=='5'):
                  def FloorDivision():
                      print("5) FLOOR DIVISION DIVISION")
                      print()
                      a=eval(input("Enter no. one : "))
                      b=eval(input("Enter no. two : "))
                      print()
                      if (b==0):
                          print("Zero Division Error : Division with ZERO is Not-Possible")
                          FloorDivision()
                      else:
                          print('ANS = ',a//b)
                  FloorDivision()
              if(input0=='6'):          
                  def TRIGONOMETRICFUNCTION():
                      list2=['1','2','3','4','5','6','7']
                      print("6) TRIGONOMETRIC FUNCTION")
                      print()
                      print("1) Sin")
                      print("2) Cos")
                      print("3) Tan")
                      print("4) Cot")
                      print("5) Sec")
                      print("6) Cosec")
                      print("7) Exit To Main-Menu")
                      print()
                      input1=input("Enter choice : ")
                      print()
                      if input1 not in list2 :
                          print("Enter Valid Choice")
                          TRIGONOMETRICFUNCTION()
                      if (input1=='1') :
                          print("1) Sin")
                          print()
                          x=eval(input("Enter angle : "))
                          print()
                          print('ANS = ',sin((pi/180)*x))
                      if (input1=='2') :
                          print("2) Cos")
                          print()
                          x=eval(input("Enter angle : "))
                          print()
                          print('ANS = ',cos((pi/180)*x))
                      if (input1=='3') :
                          print("3) Tan")
                          print()
                          x=eval(input("Enter angle : "))
                          print()
                          print('ANS = ',sin((pi/180)*x)/cos((pi/180)*x))
                      if (input1=='4') :
                          print("4) Cot")
                          print()
                          x=eval(input("Enter angle : "))
                          print()
                          print('ANS = ',cos((pi/180)*x)/sin((pi/180)*x))
                      if (input1=='5') :
                          print("5) Sec")
                          print()
                          x=eval(input("Enter angle : "))
                          print()
                          print('ANS = ',1/(cos((pi/180)*x)))
                      if (input1=='6') :
                          print("6) Cosec")
                          print()
                          x=eval(input("Enter angle : "))
                          print()
                          print('ANS = ',1/(cos((pi/180)*x)))
                      if(input1=='7'): 
                          time.sleep(1)
                          menu()
                      if input1!="7":
                          time.sleep(0.2)
                          print()
                          TRIGONOMETRICFUNCTION()
                  TRIGONOMETRICFUNCTION()
              if(input0=='7'):
                  def Power():
                      print("7) EXPONENTIATION")
                      print()
                      no=eval(input("Enter no. for Exponentiation: "))
                      sq=eval(input("Enter power :"))
                      print()
                      print('ANS = ',(no)**(sq))
                  Power()
              if(input0=='8'):
                  def base():
                      list2=['1','2','3','4','5','6','7']
                      print("8) BASE CONVERSION (Enter Integer)")
                      print()
                      print("1) Decimal to Binary")
                      print("2) Decimal to Octadecimal")
                      print("3) Decimal to Hexadecimal")
                      print("4) Binary to Decimal")
                      print("5) Octadecimal to Decimal")
                      print("6) Hexadecimal to Decimal")
                      print("7) Exit To Main-Menu")
                      print()
                      input2=input("Enter choice : ")
                      print()
                      if input2 not in list2 :
                          print("Enter Valid Choice")
                          base()
                      if (input2=='1') :
                          print("1) Decimal to Binary")
                          print()
                          n=int(input("Enter Decimal No.: "))
                          n=fabs(n)
                          print()
                          a=0
                          m=0
                          c=1
                          while n>0:
                              a=n%2
                              m=m+(a*c)
                              c=c*10
                              n=int(n/2)
                          print('ANS = ',m)    
                      if (input2=='2') :
                          print("2) Decimal to Octadecimal")
                          print()
                          n = int(input('Enter Decimal No.: '))
                          d=fabs(n)
                          print()
                          o = oct(n)
                          o=str (o)
                          o=o[2:]
                          print('ANS = ',o)
                      if (input2=='3') :
                          print("3) Decimal to Hexadecimal")
                          print()
                          n = int(input('Enter Decimal No.: '))
                          d=fabs(n)
                          print()
                          h = hex(n).split('x')[-1]
                          print('ANS = ',h)
                      if (input2=='4') :
                          print("4) Binary to Decimal")
                          print()
                          n=int(input("Enter Binary No.: "))
                          binary=fabs(n)
                          print()
                          decimal,i=0,0
                          while binary!=0:
                                  dec=binary%10
                                  decimal=decimal+dec*pow(2,i)
                                  binary=binary//10
                                  i+=1
                          print('ANS = ',decimal)
                      if (input2=='5') :                      
                          print("5) Octadecimal to Decimal")
                          print()
                          n=int(input("Enter Octadecimal No.: "))
                          octa=fabs(n)
                          print()
                          decimal,i=0,0
                          while octa!=0:
                              dec=octa%10
                              decimal=octa+dec*pow(8,i)
                              octa=octa//10
                              i+=1
                          print('ANS = ',decimal)
                      if (input2=='6') :                       
                          print("6) Hexadecimal to Decimal")
                          print()
                          hexdec = input("Enter Hexadecimal number : ");
                          dec = int(hexdec, 16);
                          print('ANS=',str(dec));
                      if(input2=='7'): 
                          time.sleep(1)
                          menu()
                      if input2!="7":
                          time.sleep(0.2)
                          print()
                          base()
                  base()  
              if(input0=='9'):
                  def Factorial():
                    print("9) FACTORIAL")
                    print()
                    factorial=1
                    num=int(input("Enter a number:"))
                    print()
                    if(num<0):
                        print("Sorry, factorial of negative number does not exist.")
                    elif(num==0):
                        print("Factorial of 0 is 1.")
                    else:
                        for i in range(1,num+1):
                            factorial=factorial*i
                            i=i+1
                        print("Factorial of",num,"is",factorial)
                  Factorial()
              if(input0=='10'):
                  def PERMUTATION():
                      print("10) PERMUTATION")
                      print()
                      n=int(input("Enter positive integer 0<=n: "))
                      while n<0:
                                    print()
                                    PERMUTATION()
                                    break
                      r=int(input("Enter positive integer 0<=r<=n: "))
                      while r>n:
                                   print()
                                   PERMUTATION()
                                   break
                      while r<0:
                                    print()
                                    PERMUTATION()
                                    break
                      while n<r:
                          print()
                          PERMUTATION()
                          break
                      print()
                      print('ANS = ',(factorial(n))/(factorial(n-r)))
                  PERMUTATION()
              if(input0=='11'):
                  def COMBINATION():
                      print("11)COMBINATION")
                      print()
                      n=int(input("Enter positive integer 0<=n: "))
                      while n<0:
                                    print()
                                    COMBINATION()
                                    break
                      r=int(input("Enter positive integer 0<=r<=n: "))
                      while r>n:
                                   print()
                                   COMBINATION()
                                   break
                      while r<0:
                                    print()
                                    COMBINATION()
                                    break
                      while n<r:
                          print()
                          COMBINATION()
                          break
                      print()
                      ans=(((factorial(n))/((factorial(n-r))*(factorial(r)))))
                      print('ANS = ',ans)
                  COMBINATION()
              if(input0=='12'):
                  def Root():
                      print("12) ROOTING ")
                      print()
                      no=eval(input("Enter No. for Rooting: "))
                      sqrt=eval(input("Enter Root :"))
                      print()
                      print('ANS = ',(no)**(1/sqrt))
                  Root()
              if(input0=='13'):
                  def Remainder():
                      print("13) REMAINDER ")
                      print()
                      a=eval(input("Enter no one: "))
                      b=eval(input("Enter no two :"))
                      print()
                      if (b==0):
                          print("Zero Division Error : Division with ZERO is Not-Possible")
                          Remainder()
                      else:
                         print('ANS = ',a%b)
                  Remainder()
              if(input0=='14'):
                  def Log():
                      print("14) LOG")
                      print()
                      a=eval(input("Enter no one: "))
                      print()
                      print('ANS = ',log10(a))
                  Log()
              if(input0=='15'):
                  def Angularconversion():
                      print("15) ANGULAR CONVERSION ")
                      list2=['1','2','3']
                      print()
                      print("1) Degree to Radians")
                      print("2) Radians to Degree")
                      print("3) Exit To Main-Menu")
                      print()
                      input3=input("Enter choice : ")
                      print()
                      if input3 not in list2 :
                          print("Enter Valid Choice")
                          Angularconversion()
                      if (input3=='1') :
                          print("1) Degree to Radians")
                          print()
                          x=eval(input("Enter angle : "))
                          print()
                          print('ANS = ',radians(x))
                      if (input3=='2') :
                          print("2) Radians to Degree")
                          print()
                          x=eval(input("Enter angle : "))
                          print()
                          print('ANS = ',degrees(x))
                      if(input3=='3'): 
                          time.sleep(1)
                          menu()
                      if input3!="3":
                          time.sleep(0.2)
                          print()
                          Angularconversion()
                  Angularconversion()
              if (input0=='16'):
                  def Statistics():
                      list2=['1','2','3','4','5','6','7']
                      print("16) STATISTICS \n( EX : 1,3,2,4,5,8 etc or 'red','blue','red' 'etc'(for mode only) \nor (for entering only one no. ) 1, 'r'")
                      print()
                      print("1) Mean")
                      print("2) Median")
                      print("3) Mode")
                      print("4) Standard Deviation")
                      print("5) Variance")
                      print("6) Coefficient of Variance")
                      print("7) Exit To Main-Menu")
                      print()
                      input1=input("Enter choice : ")
                      print()
                      if input1 not in list2 :
                          print("Enter Valid Choice")
                          Statistics()
                      if (input1=='1') :
                          print("1) Mean")
                          print()
                          x=eval(input("Enter data : "))
                          print()
                          print('ANS = ',statistics.mean(x) )
                      if (input1=='2') :
                          print("2) Median")
                          print()
                          x=eval(input("Enter data : "))
                          print()
                          print('ANS = ',statistics.median(x))
                      if (input1=='3') :
                          print("3) Mode")
                          print()
                          x=eval(input("Enter data : "))
                          print()
                          print('ANS = ',statistics.mode(x))
                      if (input1=='4') :
                          print("4) Standard Deviation")
                          print()
                          x=eval(input("Enter fi : "))
                          xi=eval(input("Enter xi : "))
                          print()
                          print('ANS = ',statistics.stdev(x,xbar=statistics.mean(xi)))
                      if (input1=='5') :
                          print("5) Variance")
                          print()
                          x=eval(input("Enter fi : "))
                          xi=eval(input("Enter xi : "))
                          print()
                          print('ANS = ',statistics.variance(x,xbar=statistics.mean(xi)))
                      if (input1=='6') :
                          print("6) Coefficient of Variance")
                          print()
                          x=eval(input("Enter fi : "))
                          xi=eval(input("Enter xi : "))
                          print()
                          print('ANS = ',statistics.variance(x,xbar=statistics.mean(xi)*100/statistics.mean(x)))
                      if(input1=='7'): 
                          time.sleep(1)
                          menu()
                      if input1!="7":
                          time.sleep(0.2)
                          print()
                          Statistics()
                  Statistics()
              if(input0=='17'):
                  def GCD():
                      print("17) GREATEST COMMON DIVISOR")
                      print()
                      a=int(input("Enter integer no. one : "))
                      b=int(input("Enter integer no. two : "))
                      print()
                      print('ANS = ',gcd(a, b) )
                  GCD()
              if(input0=='18'):
                  def FACTOR():
                    print("18) FACTOR FINDING")  
                    print()
                    n=int(input("Enter integer to find its factors: "))
                    n=fabs(n)
                    print()
                    print('ANS = (+,-)',1,end=',')
                    f=2
                    while f<=n/2:
                        if n%f==0:
                            print(f,end=',')
                        f+=1
                    print(n)
                  FACTOR()
              if(input0=='19'):
                def Great():
                    print("19) GREATEST AMONG THE THREE ")
                    print()
                    print(' For Square-Root Enter sqrt() Ex-sqrt(9) ')
                    print()
                    num_1 = eval(input("Enter no. 1 : "))
                    num_2 = eval(input("Enter no. 2 : "))
                    num_3 = eval(input("Enter no. 3 : "))
                    print()
                    if (num_1>num_2) and (num_1>num_3) :
                              print ('ANS = ',num_1," is greater ( no.1 )")
                    elif (num_2>num_1)and (num_2>num_3):
                              print ('ANS = ',num_2," is greater ( no.2 )")
                    elif (num_3>num_1)and (num_3>num_2):
                              print ('ANS = ',num_3," is greater ( no.3 )")
                    elif (num_3>=num_1>=num_2):
                              print ('ANS = ',num_1,num_2,num_3," all are equal ")
                Great()
              if(input0=='20'): 
                  print("20) EXIT")
                  time.sleep(1)
                  exit()
              if  input0 not in list:
                      print("Please enter a valid choice")
                      time.sleep(0.5)
                      os.system("cls")
                      menu()
              if input0!="20":
                  time.sleep(2)
                  print()
                  c=input("For clearing the screen press 'C' ")
                  if( c=='c' or c=='C'):
                      os.system("cls")
                      menu()
                  else:
                      menu()
    menu()
    print()
except SyntaxError: print("SyntaxError:An Error Has Occured \n\n Enter All the Values \n\n Or Check Entered Values")
except ValueError: print("ValueError:An Error Has Occured \n\n Enter All the Values \n\n Or Check Entered Values")
except NameError: print("NameError:An Error Has Occured \n\n Enter All the Values \n\n Or Check Entered Values")
except TypeError: print("TypeError:An Error Has Occured \n\n Enter All the Values \n\n Or Check Entered Values")
except ZeroDivisionError: print("ZeroDivisionError:Division With Zero is Not-Possible")
except IndexError: print("IndexError:An Error Has Occured \n\n Enter All the Values \n\n Or Check Entered Values")
else:print("An Error Has Occured \n\n Enter All the Values \n\n Or Check Entered Values")
time.sleep(3)
menu()


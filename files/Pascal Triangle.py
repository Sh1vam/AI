def pascal(p):
    r=[1]
    s=[0]
    for t in range(max(p,0)):
        print(r)
        r=[q+r for q,r in zip(r+s,s+r)]
    global x
    x=int(input("Enter Number To Get Pascal Triangle : "))
    pascal(x)
global x
x=int(input("Enter Number To Get Pascal Triangle : "))
pascal(x)

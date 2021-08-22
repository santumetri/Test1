import os
from src.live import live1
from src.textfile import textfile

d1 = live1()
tf = textfile()
try:
    input1 = (input("""select the options below 
1.Write a paragraph 
2.Select the file\n """))
    input1 = int(input1)
except :
    print("invalid input")
    print ("Enter number")
    input1 =0

while input1:
    if input1==1:
        rtr = d1.getinput()
        rtr = list(rtr.split())
        d1.compare(rtr)
        break
    elif input1==2:
        file1 = str(input("Enter the file path: "))
        print(file1)
        file = open(file1)
        txt=file.read()
        rtr = list(txt.split())
        rtr1 = tf.compare(rtr)
        break


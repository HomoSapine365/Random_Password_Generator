import random as r
import string
Alphabets=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
Numbers=[0,1,2,3,4,5,6,7,8,9]
Special_Symbols=['!','@','#','$','%','^','&','*']
length_of_Password = int(input("Enter the length of your password you want:"))
No_of_Alphabets = int(input("Enter Number of Alphabets you want :"))
No_of_SpecialCharacters = int(input("Enter Number of Special Characters you want :"))
No_of_numbers = int(input("Enter Number of Integer Numbers you want :"))
password= [ ]
#For Required number of Alphabets into the password
for i in range(No_of_Alphabets):
    letter=r.choice(Alphabets)
    password.append(letter)
#For Required number of Special Characters into the password
for i in range(No_of_SpecialCharacters):
    letter=r.choice(Special_Symbols)
    password.append(letter)
#For Required number of Integer Numbers into the password
for i in range(No_of_numbers):
    letter= str (r.choice(Numbers))
    password.append(letter)
r.shuffle(password)
password = "".join(password)
print("The random Passord is:" + password)
#Final_Password=" "
#for i in password:
    #Final_Password += string.i
#print(Final_Password)
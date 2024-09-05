#Password Generator
import random
symbols=["!","@","#","$","%","^","&","*","(",")"]
letters=["q","w","e","r","t","y","u","i","i","o","p","a","s","d","f","g","h","j","k","l","z","x","c","v","b","n","m","Q","W","E","R","T","Y","U","I","O","O","P","A","S","D","F","G","H","J","K","L","Z","X","C","V","B","N","M"]
numbers=[1,2,3,4,5,6,7,8,9,0]
x=int(input("How many letters do you want in your password:"))
a=[]
b=[]
c=[]

for i in range(x):
    a.append(random.choice(letters)) # a+=random.choice(letters)
y=int(input("How many numbers do you want in your password:"))
for i in range(y):
    b.append(random.choice(numbers))
z=int(input("How many symbols do you want in your password:"))
for i in range(z):
    c.append(random.choice(symbols))
#list comprehension to append multiple lists
[a.extend(i)for i in (b,c)]
#print(a)
'''a=a+b+c
print(a)'''
random.shuffle(a)
#print(a)
print("Generated Password is:")
for i in a:
    print(i,end="")
print("\n")




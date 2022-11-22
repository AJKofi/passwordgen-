import random
letters=['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z','A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers=['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols=['@', '#', '$', '%', '^', '&', '*', '!']
print("We are glad you chose us to help you cr4eate a password\n")
print("Please input various requests below\n")
nofletters=int(input("How many letters would you like to use in your password\n"))
nofnumbers=int(input("How many numbers would you like to use in your password\n"))
nofsymbols=int(input("How many symbols would you like to use in your password\n"))

#Eazy password generator
#using a for loop
# password=""
# for char in range(1,nofletters+1):
#     password = password+random.choice(letters)

# for char in range(1,nofnumbers+1):
#     password = password+random.choice(numbers)   

# for char in range(1,nofsymbols+1):
#     password = password+random.choice(symbols)     
# print(password)
#shuffle can only be utilised on a list therefore for anything you woud to shuffle you will need to make it a list first
#therefore create a list
#note also strings cannot be concactenated into a list unless you use append
password_list=[]    
for char in range(1,nofletters+1):
    password_list.append(random.choice(letters))

for char in range(1,nofnumbers+1):
    password_list.append(random.choice(numbers)) 

for char in range(1,nofsymbols+1):
    password_list.append(random.choice(symbols)) 

print(password_list)
random.shuffle(password_list)
print(password_list)

password=""
for char in (password_list):
    password=password+char

print(f"Your pasword is : {password}")
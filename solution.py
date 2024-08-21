                             #first solution by using Slicing


# Name = input('name: ') #save the name or whatever the user type and store it in a variable "name"

# print( Name[::-1] )# print out whatever we saved in "name" in a reversed way using the [::-1]method


                             #second solution by using  swaping


# def myreverse(name):      #we make like a manual reverse Function
#  
#     name = list(name)     # knowing that Strings in python are immutable so we make a list of characters in order to later in the code return  like a new empty string to join the list 
#  
#     left = 0              # herre we intialize a pointers, one for the 1st charcter and the other for last charcter
#     right = len(name) - 1 

#   
#     while left < right:   # aloop for swaping pointers(or charcters) untile the left = right        

#         name[left], name[right] = name[right], name[left] 
#         left += 1
#         right -= 1

#     return "".join(name)  # as mentioned in line 11


# name = input("What's your name: ")
# print(myreverse(name))




    # okay so in this 3rd solution, as a guy intersted in the cybersecurty field iam trying to make the required task by adding some sort of securty to it
    # by experincing penteration testing knowing that SQL injection or command injectionattaks uses like sympols so i tried my best adding another function 
    # that dont accept these kind of sympols by showing its like an invalid name if it doesnt follow the rule or the function            
    #at the end I hope it works to prevent such attaks and i am looking forward to hear your openions and how to improve it 
import re

def valid_name(name):
    if not re.match(r"^[a-zA-Z .'-]+$", name):
        raise ValueError("Invalid name.")
    return name 

def myreverse(name):
    try:
        name = valid_name(name)
        name = list(name)
        left = 0
        right = len(name) - 1   
        while left<right:
            name[left],name[right] = name[right],name[left] 
            left+=1
            right-=1
        return "".join(name)
    except ValueError as E:
        print(E)
x = myreverse("#/@Mina")
print(x)
    
name = input("what's ur name: ")
print(myreverse(name))




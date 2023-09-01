import random                     

def generate_password(len):  
    list = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz1234567890!@#$%&*"  
    selected = random.sample(list, len)  
    pass_str = "".join(selected)  
    return pass_str  
  

if __name__ == "__main__":   
    while True:  
    
        userSelection = input("Do you wish to generate a Password?\nPress 'Y/y' to Continue, or 'N/n' to Exit: ")  
        if userSelection == 'N' or userSelection == 'n':  
            print("Thank You! See You Next Time.")  
            break  
        elif userSelection == 'Y' or userSelection == 'y':          
            len = int(input("Enter the length of the Password: "))  
            pass_str = generate_password(len)  
            print("A Randomly Generated Password is:", pass_str)  
            print("") 
        else:  
            print("Invalid Input! Try Again.")  
            print("") 
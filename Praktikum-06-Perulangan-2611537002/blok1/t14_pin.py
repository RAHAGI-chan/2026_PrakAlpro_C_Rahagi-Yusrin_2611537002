correct_pin = "1234"                 
max_attempts = 3                     
attempt = 1                          
pin = input("Enter PIN: ")           

while pin != correct_pin and attempt < max_attempts:  
    print("Incorrect PIN.")          
    attempt += 1                     
    pin = input("Enter PIN: ")       

if pin == correct_pin:               
    print("Access granted")          
else:                                
    print("Account locked")       


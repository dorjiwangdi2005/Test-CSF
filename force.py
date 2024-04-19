print ("Mewton's second law of motion")
print ("--------------------------------")

#determining the missing values
print ("select the missing values")
print ("1. mass (m)")
print ("2. acceleration (a)")
print ("3. force (f)")
missing_value_choice = input ("enter the option number for the missing value: ")

if missing_value_choice == "1":
    a = float(input("enter the value of acceleration(a) in m/s :  "))
    f = float(input("enter the value of force (f) in N : ")) 
    m = f/a
    print (f"mass (m) = {m} kg ")

elif missing_value_choice == "2":
    m = float(input("enter the value of mass (m) in kg : "))
    f = float (input("enter the value of force(f) in N : "))
    a = f / m
    print (f"acceleratin (a) = {a} m/s")

elif missing_value_choice == "3":
    a = float(input("enter the value of acceleration(a) in m/s :  "))
    m = float (input("enter the value of mass (m) in kg : "))
    f = m * a
    print (f"force (f) = {f} N ")

else:
    print("invalid option selected for the missing option!")
    


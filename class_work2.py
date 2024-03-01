user_age = int(input("enter your age: "))

question_ = input("are you a student?(  yes/no): ")

if user_age < 12 or question_ == "no":
    print ("you are eligible for a discount on a movie ticket.")

elif user_age > 13 or user_age <18 and question_== "yes":
    print ("you are eligible for a discount on a movie ticket.")


elif user_age > 13 or user_age < 18 and question_== "no":
    print ("you are not eligible for a discount on a movie ticket.")

else:
    print ("you are not eligible for a discount on a movie ticket.")
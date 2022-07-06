# Account Opening App
# Usable commands = if, print(), input(), def, variables, comments

# talking
print("Welcome to KSZ account opener")
def account():
    name = input("Name: ")
    email = input("Email: ")
    password = input("Password: ")
    wanting = input("Do you want to restart from the beginning? Y/N: ")
    if(wanting == "Y"):
        account()
    elif(wanting == "N"):
        print("You name is " + name + ", your email is " + email + " and your password is " + password + ".")
    else:
        wanting = input("Do you want to restart from the beginning? Y/N: ")
        if (wanting == "Y"):
            print("You name is " + name + ", your email is " + email + " and your password is " + password + ".")
        elif (wanting == "N"):
            account()

account()

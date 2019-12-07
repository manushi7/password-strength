#python program for checking password strength
def password_check(pw):
    Symbol=['@','#']
    value=True
    if len(pw) < 2:
        print('the length of password should be at least 2 characters long')
        value=False
    if len(pw) > 7:
        print('the length of password shouldnot be greater than 7')
        value=False
    if not(digit() for character in pw):
        print('the password should have at least one numeral')
        value=False
    if not(Symbol() for character in pw):
        print('the password should have at least two of the symbols @,#')
        value=False
    else:
        print('password is accessible')
        return value
pw= input('enter the password : ')
print(password_check(pw))


#-------------------------------------------------------------------------------------------------------------#



def check_alphanumeric_count(a):
    chars = ['@', '$', '%', '#', '&', '"', '!', '*', '^', "'"]
    s = []
    for i in a:
        for j in chars:
            if i == j:
                s.append(True)
    if len(s) >= 2:
        return True
    else:
        return False


def check_num_count(a):
    num = [(i+1) for i in range(10)] # [1, 2 , 3, 4, 5 ,6, 7, 8, 9, 10]
    s = []
    for i in a:
        for n in num:
            if i == str(n):
                s.append(True)
    if len(s) >= 2:
        return True
    else:
        return False        


def check_password_strength(password):
    if len(password) >= 7:
        if check_alphanumeric_count(password) and check_num_count(password):
            return True
        else:
            print("More alphanumeric or num req")
            return False
    else:
        print("Too less characters : MIN 7 required")
        return False

user_input = input("Please enter your password : ")
while not check_password_strength(user_input):
    user_input = input("Please enter another password : ")
print("Password is good")
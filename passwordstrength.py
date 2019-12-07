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

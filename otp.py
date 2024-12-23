import random
def genotp():
    otp=''
    for i in range(2):
        otp+=random.choice([chr(i) for i in range(ord('A'),ord('Z')+1)])
        otp+=random.choice([chr(i) for i in range(ord('a'),ord('z')+1)])
        otp+=str(random.randint(0,10))
    return otp
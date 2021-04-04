def setPassword():
    n1=int(input('Set Password'))
    n2=int(input('Confirm Password'))
    if n2==n1:
        print('Password set')
        return n1
    else:
        print('''Sorry password is not matching.
Please try again''')
        return(setPassword())



import time
n=setPassword()
print('Phone Locked')
c1=4
while True:
    print('Enter password to unlock')
    e=int(input())
    if e==n:
        print('Access Permitted')
        break
    else:
        print('You have',c1,'more attempts')
        c1-=1
    if c1==-1:
        print('Try again after 10 seconds')
        time.sleep(10)
        c1=4

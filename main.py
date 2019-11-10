import random
import string

def GeneratePassword(count,kirill):
    Symbs = []
    for i in string.ascii_letters:
        Symbs.append(i)
    Symbs.extend(['!','#','1','2','3','4','5','6','7','8','9','0','%','$','@'])
    if kirill:
        start = ord('а')
        for i in range(start,start+32):
            Symbs.append(chr(i))
    password = ''
    for i in range(count):
        RandSymb = random.randint(0,len(Symbs)-1)
        password += Symbs[RandSymb]
    return(password) 




try:
    CountSymb = int(input('Введите количество символов в пароле :\n'))
except:
    while True:
        try:
            CountSymb = int(input('Пожалуйста, введите число :\n'))
            break
        except:
            continue

UseKiril = input('Введите Yes, если в пароле нужно использовать кириллицу и No, если не нужно :\n')
while True:
    if UseKiril == 'Yes':
        UseKiril = True
        break
    elif UseKiril == 'No':
        UseKiril = False
        break
    else:
        UseKiril = input('Пожалуйста, введите Yes или No :\n')

password = GeneratePassword(CountSymb,UseKiril)
with open('Password.txt','w') as fl:
    fl.write(password)
print(password)
n = input('Нажмите Enter чтобы закрыть')

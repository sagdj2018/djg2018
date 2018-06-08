#1
print('Hello, Django girls!')

#2
if 3 > 2:
    print('It works!')

#3
if 5 > 2:
    print('5 est effectivement plus grand que 2')
else:
    print("5 n'est pas plus grand que 2")

#4
def hi(name):
    if name == 'Ola':
        print('Hi Ola!')
    elif name == 'Sonja':
        print('Hi Sonja!')
    else:
        print('Hi anonymous!')

hi("")  #vide ou autre prénom non déclaré >> affiche anonymous

#5
def hi(name):
    print('Hi ' + name + '!')

hi("Rachel")

#6

def hi(name):
    print('Hi ' + name + '!')

girls = ['Rachel', 'Monica', 'Phoebe', 'Ola', 'You']
for name in girls:
    hi(name)
    print('----')

#7
    for i in range(1, 6):
        print(i)

a, b = 1, 1

for i in range(101):
    A = a 
    a = b 
    b = A+b 

    print('{}th Pib. Number is {}'.format(i+2, b))

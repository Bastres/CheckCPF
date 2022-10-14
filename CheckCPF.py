num2 = input('Digite os 6 últimos números dos 9 primeiros números do CPF: ')

def digito(a):
    b = len(a) + 1
    c = 0
    for i in range(b - 1):
        d = b*int(a[i])
        c = c + d
        b = b - 1
    if c % 11 < 2:
        return 0
    if c % 11 >= 2:
        return 11 - (c % 11)

for i in range(0, 1000):
    num1 = str(i)
    while len(num1) < 3:
        num1 = '0' + num1    
    num = num1 + num2       
    num = num + str(digito(num))
    num = num + str(digito(num))
    print(num)
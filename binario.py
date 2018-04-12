num =int(input('decimal number: '))
#put some number

c = 1

bin = 0

list = []
#list to sum the binary numbers
while num >= 1:
    b = num%2

    num = num//2

    bin = b*c

    list.append(bin)

    c = c*10

sum = sum(list)
print('Your decimal number in binary numbers is: {}'.format(sum))

#You'll input 3 numbers between 100 and 999
num = int(input('three-digit number: '))
u = num%10
#unit
d = int((num%100)//10)
#dozen
c = num//100
#hundred
inv =int(u*100+d*10+c)
#the account number upside down
#the sum between the account number and inverse account number
sum = num + inv
#the multiplication of each digit according to your positional order
sum_u = (sum%10)*3
#unity of sum
sum_d =  ((sum%100)//10)*2
#dozen of sum
sum_c = (sum//100)
#hundred of sum
realn = sum_u + sum_d+ sum_c
#the sum of digit of sum
n = realn%10
#unity of realn
print('The number verified is {}.'.format(n))
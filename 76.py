num = int(input('Put some number: '))
##i'll change the number to your sucessor, but the number will stay between 0 and 60
suc = (num + 1)% 61
#the sucessor between 0 and 60
#even if the number is greater than 60, the sucessor will stay between 0 and 60
print('The number: {}. '
      'The sucessor: {}'.format(num, suc))

a = b = 0

# _a =  8
# __a = 10

title = "Calulator" # comment
print(title)
# 

a = int(input('Enter a = '))
b = int(input('Enter b = '))
operation = input('Enter operation = ')
# * / // % **
if operation == '+':
    print(a + b)
elif operation == '-':
    print(a - b)
else:
    print('Bad operation')

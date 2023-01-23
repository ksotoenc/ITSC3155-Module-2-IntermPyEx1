#Kelvin Soto
#Reference for try-except blocks: https://www.w3schools.com/python/python_try_except.asp
i = 1
number = 0
sum = 0
while i <= 5:
    number = input('Enter number ' + str(i) + ': ')
    try:
        int(number)
    except ValueError:
        print('Invalid input. Please enter an int')
    else:
        sum+= int(number)
        i+= 1
print('The sum is ' + str(sum))

    


    
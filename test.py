

# # print('hello world')

# # enterName = input('enter your name: ')
# # print('yoyo', enterName)


# hours = input('enter hours: ')
# rate = input('enter rate: ')
# print('pay', float(hours) * float(rate))


# # run using the button in the right hand side corner
# # use the terminal 'python3 demo.py'

# # define a variable, name
# msg = 'Hello'
# # print the content () on the terminal
# print(msg)

# my_name = 'Nathalie'
# my_name = 'Anna'
# # print the value of a variable
# print(my_name)

# # string
# print('Ivonita')

# # Number: Integer or Float
# my_age = 36

# # or Float
# temp = 2.2

# # <class 'int>  
# print(type(my_age))
 
## Calculate the year I was born:
# my_birthyear = 2023 - 36

# current_year = 2023
# my_birthyear = current_year - my_age
# print(my_birthyear)


guests = ['Isa', 'Toto', 'Heike', 'Edith']
bill = 30
tip_percentage = 10
tip_amount = (bill * tip_percentage) / 100
individual_cost = (bill + tip_amount) / float(len(guests))

for guest in guests:
    print(guest + ' pays: ' + str(individual_cost) + ' ' + 'EUR')
    
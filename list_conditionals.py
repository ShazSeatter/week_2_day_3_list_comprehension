# starts at 1 finishes at 10, should be numbers only. different kinds of class , not the same as a list class. 
# can be a quick way to create a sequence of numbers
# numbers = range(1, 11)

even_squared = [ number * number for number in range(1,11) if number % 2 == 0 ]

# for number in numbers: # the loop
#     if number % 2 == 0: # the condition 
#         even_squared.append(number * number)
        # 'evens_squared.append' - appending something to the list (it is an action)
        # 'number * number' - what gets added to the list 


print(even_squared)




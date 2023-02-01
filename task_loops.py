# for number in numbers: # the loop
#     if number % 2 == 0: # the condition 
#         even_squared.append(number * number)
        # 'evens_squared.append' - appending something to the list (it is an action)
        # 'number * number' - what gets added to the list

even_squared = [ number * number for number in range(1,11) if number % 2 == 0 ]

# Part 1

ages = [5, 15, 64, 27, 84, 26]

# Return a list of only the odd ages

odd_ages = [ age for age in ages if age % 2 != 0 ]

print(odd_ages)

# Part 2

chicken_names = ["Hen Solo", "Cluck Norris", "Hennifer Lopez", "ChewPekka", "Feather Locklear"]

# Return a list with chickens whose names are more than 10 characters
# Return a list of chickens whose names start with the letter H

long_chicken_names = [chicken for chicken in chicken_names if len(chicken) > 10]

chicken_letter_h = [chicken_name for chicken_name in chicken_names if chicken_name[0] == "H"]

print(long_chicken_names)
print(chicken_letter_h)

# Part 3

words = ["The", "quick", "brown", "fox", "jumped", "over", "the", "lazy", "dog"]

# Build a new list with the first letter from each word
# Convert each letter to lower case

# Expectedd output: ["t", "q", "b", "f", "j", "o", "t", "l", "d"]

# Hint : Strings in Python work as if they were a tuple full of characters.
#        How would you get the first element from a tuple or list?

first_letter = [letter[0].lower() for letter in words]
print(first_letter)
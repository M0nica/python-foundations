# Grade: 12.5 / 15

# Monica Powell
# May, 25th, 2016
# Homework 2

# 1) Make a list of the following numbers: 22, 90, 0, -10, 3, 22, and 48
numbers = [22, 90, 0, -10, 3, 22, 48 ]

# 1) Display the number of elements in the list
print("number of elements on list", len(numbers))

# 2) Display the 4th element of this list.
print("fourth element", numbers[3])

# 3) Display the sum of the 2nd and 4th element of the list.
print("sum of 2nd and 4th element", numbers[1] + numbers[3])

#prints the second largest number of a sorted list
print(sorted(numbers)[-2])

# 5) Display the last element of the original unsorted list

print(numbers[len(numbers)-1])

# 6) For each number, display a number: if your original number
# is less than 10, multiply it by thirty. If it's also even,
# add six. If it's greater than 50 subtract ten. If it's not
#negative ten, subtract one. (For example: 2 is less than
# 10, so 2 * 30 = 60, 2 is also even, so 60 + 6 = 66,
#2 is not negative ten, so 66 - 1 = 65.)

# TA-COMMENT: (-1) The code below manipulates your original number and then after the first if condition, the other if conditions check the manipulated number, rather than the original number. It should be checking the original number. Also, it does not have the > 50 condition included at all.

sum = 0
for number in numbers:
    if number < 10:
        number = number * 30
        if number % 2 == 0:
            number = number + 6
        if number != - 10:
            number = number - 1
    sum = sum + number
    print(number)

# TA-COMMENT: A solution for Question 6 could look like this:

for number in numbers:
	original = number

	if original < 10:
		number = number * 30

		if (original%2) == 0:
			number = number + 6

	elif original > 50:
		number = number - 10

	if original != -10:
		number = number - 1

	print(number)

# 7) Sum the result of each of the numbers divided by two.

# TA-COMMENT: (-1) You're summing the manipulated numbers, not the original list.

print(sum/2)


movies = [
 # cat_info[0]
   { 'title': 'What I Like About You', 'year': 2006, 'director': "Amanda Bynes", 'budget':1000, 'revenue':5000}

# TA-COMMENT: (-0.5) We can add entries to a dictionary AFTER making it. We wanted to see:
    # name_of_dictionary['budget'] = 1000
# rather than "hard coding" budget and revenue into the initial dictionary. This is trickier to do because you have put your dictionary in a list, but it's not necessary to do that (and in this case, it makes the solution harder for yourself).


 # cat_info[1]
#   { 'name': 'Callery', 'age': 2 },
 # cat_info[2]
 #  { 'name': 'Naples', 'age': 'unknown' }
]

for movie in movies:
# TA-COMMENT: Again, you should not make a list if you know you will only have one object. This prints fine, but the for loop is unnecessary when there is only one item.

    print("My favorite movie is", movie['title'], "which was released in", movie['year'], "and was directed by", movie['director'])
    profit = movie['revenue'] - movie['budget']
    print("$", profit)
    if(profit < 0):
        print("It was a flop")
    elif (movie['revenue']/5) >= movie['budget']:
        print("That was a good investment")


# TA-COMMENT: This works; we weren't looking for a list of dictionaries, but rather a dictionary that looks something like this:

    # populations = { 'Manhattan': 1600000, 'Brooklyn': 2600000, etc. ...}

# TA-COMMENT: However, the point was to see if you can access values out of dictionaries using its keys and I do see that you do that here. I think the structure you used just made it a bit harder, but it also forced you to practice for loops!

boroughs = [
 # cat_info[0]
{ 'name': 'Brooklyn', 'population': 2600000},
{ 'name': 'Manhattan', 'population': 1600000},
{ 'name': 'Bronx', 'population': 1400000},
{ 'name': 'Queens', 'population': 2300000},
{ 'name': 'Staten Island', 'population': 470000}

]

Brooklyn = boroughs[0]



print("The population of Brooklyn is ", Brooklyn['population'])
population = 0
for borough in boroughs:
    population = population + borough['population']
print("Total population across boroughs is", population)

Manhattan = boroughs[1]

print("Manhattan is", (Manhattan['population']/population)*100, "% of the NYC total population")

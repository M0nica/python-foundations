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

sum = 0
for number in numbers:


    if number < 10:
        newnumber = number * 30
        if number % 2 == 0:
            newnumber = number + 6
    if number > 50:
        newnumber - 10
    if number != - 10:
        newnumber = number - 1
    sum = sum + newnumber
    print(newnumber)

# 7) Sum the result of each of the numbers divided by two.



print(sum/2)


movies = [
 # cat_info[0]
   { 'title': 'What I Like About You', 'year': 2006, 'director': "Amanda Bynes", 'budget':1000, 'revenue':5000}
 # cat_info[1]
#   { 'name': 'Callery', 'age': 2 },
 # cat_info[2]
 #  { 'name': 'Naples', 'age': 'unknown' }
]

for movie in movies:

    print("My favorite movie is", movie['title'], "which was released in", movie['year'], "and was directed by", movie['director'])
    profit = movie['revenue'] - movie['budget']
    print("$", profit)
    if(profit < 0):
        print("It was a flop")
    elif (movie['revenue']/5) >= movie['budget']:
        print("That was a good investment")


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

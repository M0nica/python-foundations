# Monica Powell
# May, 23rd, 2016
# Homework 1

year_of_birth = input("What year were you born?")
age = 2016 - int(year_of_birth)

if age < 0:
    year_of_birth = input("Give me a year that is not in the future! What year were you really born?")
    age = 2016 - int(year_of_birth)

print("You are approximately ", age, "years old")


# http://wonderopolis.org/wonder/how-many-times-does-your-heart-beat-in-a-lifetime
hheartbeat = age * 42048000

print("Your heart has beat approximately",  hheartbeat,  " times")

# 4. How many times a blue whale's heart has beaten
# http://www.whalefacts.org/blue-whale-heart/

min_in_year = 525600
bpm = 9
bwheartbeat = bpm * min_in_year * age
print("A blue whale's heart has beat approximately",  bwheartbeat ,  " times")
# 5. How many times a rabbit's heart has beaten
#http://rabbit.org/temperature-and-respiration-rates

bpm = 135
rheartbeat = bpm * min_in_year * age


# 6. If the answer to (5) is more than a billion, say "XXX billion" instead of the very long raw number
if rheartbeat >= 1000000000:
    print("A rabbit's heart has beat approximately", (rheartbeat/1000000000), " billion times" )
else:
    print("A rabbit's heart has beat approximately",  rheartbeat ,  " times")


# 7. How old they are in Venus years
# http://spaceplace.nasa.gov/all-about-venus/en/
# http://www.universetoday.com/14319/how-long-is-a-year-on-venus/
venusyears = (age * 365) / 243
print("venus years", venusyears)
# another way to calulate with slighlty different results
# venusyears = (age) / .62
# print("venus years", venusyears)



# 8. How old they are in Neptune years

# http://www.universetoday.com/22064/how-long-is-a-year-on-neptune/
# a year in neptune is 60,190
neptuneyears = (age * 365) / 60190
print("neptune years", neptuneyears)
# 9. Whether they are the same age as you, older or younger

if age > 22:
    print("You are older than me")
elif age == 22:
    print("We are the same age")
else:
    print("You are younger than me!")

# 10. If older or younger, how many years difference

if age != 22:
    print("There is a ", abs(22 - age), "year difference between us.")

# 11. If they were born in an even or odd year

if (int(year_of_birth)% 2) == 0:
    print("You were born in an even year.")

else:
    print("You were born in an odd year.")

# 12. How many times the Pittsburgh Steelers have won the Superbowl since their birth.
if int(year_of_birth) <= 1974:
  steelerwins = 6
elif int(year_of_birth) <= 1975:
  steelerwins = 5
elif int(year_of_birth) <= 1978:
  steelerwins = 4
elif int(year_of_birth) <= 1979:
  steelerwins = 3
elif int(year_of_birth) <= 2005:
  steelerwins = 2
elif int(year_of_birth) <= 2008:
    steelerwins = 1
elif int(year_of_birth) <= 2016:
    steelerwins = 0

print("The steelers have won ", steelerwins, " since your birth")

# 13. Which US President was in office when they were born (FDR onward)
# http://www.ipl.org/div/potus/

if 1933 <= int(year_of_birth) <= 1945:
    print("Franklin Delano Roosevelt was in office when you were born")
elif int(year_of_birth) <= 1953:
    print("Harry S. Truman was in office")
elif int(year_of_birth) <= 1961:
    print("Dwight David Eisenhower was in office when you were born")
elif int(year_of_birth) <= 1963:
    print("John Fitzgerald Kennedy was in office when you were born")


elif int(year_of_birth) <= 1969:
    print("Lyndon Baines Johnson was in office when you were born")

elif int(year_of_birth) <= 1974:
    print("Richard Milhous Nixon was in office when you were born")

elif int(year_of_birth) <= 1977:
    print("Gerald Rudolph Ford was in office when you were born")

elif int(year_of_birth) <= 1981:
    print("James Earl Carter, Jr. was in office when you were born")

elif int(year_of_birth) <= 1989:
    print("Ronald Wilson Reagan was in office when you were born")

elif int(year_of_birth) <= 1993:
    print("George Herbert Walker Bush was in office when you were born")
elif int(year_of_birth) <= 2001:
    print("William Jefferson Clinton was in office when you were born")
elif int(year_of_birth) <= 2009:
    print("George Walker Bush was in office when you were born")
elif int(year_of_birth) <= 2016:
    print("Barack Hussein Obama  was in office when you were born")

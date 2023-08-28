# write your code here
favorite_animals=["cat","seal","horse","dog"]

print(favorite_animals)
print(favorite_animals[1])
favorite_animals.pop(2)

favorite_animals.append("bird")
for animal in favorite_animals :
    print(f"I love  {animal}")

numbers=[1,2,3,4,5]
number_sum=[0]

for num in numbers :
    number_sum.append (num+num)
print(number_sum)
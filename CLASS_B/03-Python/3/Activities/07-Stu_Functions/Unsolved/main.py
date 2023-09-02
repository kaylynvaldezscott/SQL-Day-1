# @TODO: Write a function that returns the arithmetic average for a list of numbers


# Test your function with the following:
# print(average([1, 5, 9]))
# print(average(range(11)))
# numbers=[1,5,9]
# s=sum(numbers)   #15
# l=len(numbers) 
# avg=s/l
# print(avg)

def average(numbers):

    s=sum(numbers)   #15
    l=len(numbers) 
    avg=s/l
    return avg

# print(average([1,5,9]))

# print(average([1,5,9,100]))


numbers=[1,5,9]
s=0
for i in numbers:
    s=s+i
l=len(numbers) 
avg=s/l
print(avg)


def average(numbers):
    s=0
    for i in numbers:
        s=s+i
    l=len(numbers) 
    avg=s/l
    return avg

print(average([1,5,9,5,30]))











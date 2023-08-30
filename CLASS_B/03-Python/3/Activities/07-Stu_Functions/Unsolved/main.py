# @TODO: Write a function that returns the arithmetic average for a list of numbers


# Test your function with the following:
# print(average([1, 5, 9]))
# print(average(range(11)))
#numbers=[1,5,9]
def average(numbers):
    total=0
    for i in numbers:
        total=total+i
        # total*=i

    avg=total/len(numbers)

    return total,avg,len(numbers)


print(average([1,5,9,5,30]))











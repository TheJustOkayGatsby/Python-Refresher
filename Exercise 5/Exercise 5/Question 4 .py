def AvgAge(list):
    count = 0
    total = 0
    while count <10:
        total = total + list[count]
        count= count +1
    mean = total / 10
    return mean

ages = [1,1,1,1,1,9,9,9,9,9]
average = AvgAge(ages)
print(average)
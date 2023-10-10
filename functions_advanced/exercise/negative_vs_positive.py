def sum_nums(*args):
    sum_negative = 0
    sum_positive = 0
    for num in args:
        if num > 0:
            sum_positive += num
        else:
            sum_negative += num
    return sum_negative, sum_positive


numbers = [int(x) for x in input().split()]

print(sum_nums(*numbers)[0])
print(sum_nums(*numbers)[1])
if abs(sum_nums(*numbers)[0]) > sum_nums(*numbers)[1]:
    print("The negatives are stronger than the positives")
else:
    print("The positives are stronger than the negatives")

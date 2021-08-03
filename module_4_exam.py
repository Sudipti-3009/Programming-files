'''
inventory = {'apples': 430, 'bananas': 312, 'oranges': 525, 'pears': 217}

print(inventory.get("apples"))
alist = [4,2,8,6,5]
blist = [num*2 for num in alist if num%2==1]
print(blist)
inventory = {'apples': 430, 'bananas': 312, 'oranges': 525, 'pears': 217}

ks = list(inventory.keys())

print(ks)
'''
def keep_evens(nums):

    new_seq = filter(lambda num: num % 2 == 0, nums)

    return list(new_seq)



print(keep_evens([3, 4, 6, 7, 0, 1]))
numbers = [17, 123, 87, 34, 66, 8398, 44]

print(numbers[-2])

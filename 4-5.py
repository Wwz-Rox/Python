nums = [1,2,3,4,5,6]
# for name in names:
#     print(name)
sum = 0
for num in nums:
    sum = sum + num
print(sum)

sum = 0
list = range(101)
for n in list:
    sum += n
print(sum)

sum = 0
n = 100
while n >= 0:
    sum += n
    n -= 1
print(sum)

names = ['1','2','3']
for name in names:
    print("hello,",name+"!")
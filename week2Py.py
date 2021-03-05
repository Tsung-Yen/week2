#Part1
def calculate(min,max):
    sum=0
    for n in range(min,max+1):
        sum+=n
    print(sum)
calculate(1,3)
calculate(4,8)

#Part2
import json
import math
def avg(data):
    r = json.dumps(data)
    load_r = json.loads(r)
    count = len(data["employees"])
    sum = 0
    for x in range(count):
        sum = sum + data["employees"][x]["salary"]
        result = math.floor(sum/count)
    print(result)
avg({
        "count":3,
        "employees":[
            {   
                "name":"John",
                "salary":30000
            },
            {   
                "name":"Bob",
                "salary":60000
            },
            {
                "name":"Jenny",
                "salary":50000
            }
        ]
    })

    #Part3
import sys
def maxProduct(nums):
    count=len(nums)   
    maxNum = nums[0]
    secLarNum = -sys.maxsize-1
    for i in range(count):
        if nums[i] > maxNum:
            maxNum = nums[i]
            secLarNum = maxNum
        elif nums[i] < maxNum:
            secLarNum = nums[i]
        ans = maxNum * secLarNum
    print(ans) 
maxProduct([5,20,2,6])
maxProduct([10,-20,0,3])

#Part4
def twoSums(nums,target):
    count = len(nums)
    for x in range(count):
        for y in range(1,count):
            sum = nums[x]+nums[y]
            if sum ==target:
                return [x , y]

result=twoSums([2,11,7,15],9)
print(result)
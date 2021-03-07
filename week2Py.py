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
def maxProduct(nums):
    list = []
    count = len(nums)
    max = nums[0]
    min = nums[0]
    for i in range(0,count):
        for j in range(i+1,count):
            ans = nums[i]*nums[j]
            list.append(ans)
    listCount = len(list)
    for x in range(0,listCount):
        if list[x] > max:
            max = list[x]
        elif list[x]<max:
            min = list[x]
    print(max)
                
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
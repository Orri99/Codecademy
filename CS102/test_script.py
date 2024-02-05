
testSet = """['one', 'two', 'three']"""

testSet = testSet.replace('[','')
testSet = testSet.replace(']','')
testSet = testSet.replace('\'','')
testSet = testSet.replace(',','')
print(testSet)
fixed = testSet.split()

print(type(fixed))
print(fixed)

for i in fixed:
    print(i)
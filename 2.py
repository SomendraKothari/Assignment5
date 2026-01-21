import random
l = []
for i in range(10):
    l.append(random.randint(1, 10))
print(f"Original List : {l}")
l1=[]
for i in range(5):
    l1.append(l[i])
print(f"Extracted first five elements : {l1}")
l1.sort(reverse=True)
print(f"Reversed extracted elements : {l1}")
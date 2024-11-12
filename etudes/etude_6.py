# Сортировка пузырьком

a = [1,6,8,2,4,9,5]

for i in range(len(a)-1):
    for j in range(len(a)-1-i):
        if a[j] > a[j+1]:
            a[j], a[j+1] = a[j+1], a[j]

print(a)

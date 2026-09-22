arr = [12, 5, 78, 34, 9, 56]

largest = arr[0]
smallest = arr[0]

for i in arr:
    if i > largest:
        largest = arr

    if i < smallest:
        smallest = i

print("Maximum =", largest)
print("Minimum =", smallest)
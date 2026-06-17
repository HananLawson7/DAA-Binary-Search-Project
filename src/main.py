from binary_search import binary_search

numbers = [2, 5, 8, 12, 16, 23, 38, 56]

target = int(input("Enter number to search: "))

result = binary_search(numbers, target)

if result != -1:
    print(f"Element found at index {result}")
else:
    print("Element not found")
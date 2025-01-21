def extract_and_sort(data):
    # main program
    up = sorted((char for char in data if char.isupper()), reverse=True)
    ll= sorted((char for char in data if char.islower()))
    odd = sorted((int(char) for char in data if char.isdigit() and int(char) % 2 != 0))
    even = sorted((int(char) for char in data if char.isdigit() and int(char) % 2 == 0),reverse=True)

    return up, ll, odd, even

# ----->input:
data1 = "756tars&&*&^In5G8"
uppercase, lowercase, odd, even = extract_and_sort(data1)
print("Uppercase letters (descending):", uppercase)
print("Lowercase letters (ascending):", lowercase)
print("Odd numbers (ascending):", odd)
print("Even numbers (descending):",even)
# using the filter
print("Enter the line")
# data1 = "756tarsIn5G8"
lst=[val for val in input()]

# Filter
up = list(filter(lambda x: x.isupper(), sorted(lst, reverse=True)))
ll = list(filter(lambda x: x.islower(), sorted(lst)))
odd = list(filter(lambda x: x.isdigit() and int(x) % 2 != 0, sorted(lst)))
even = list(filter(lambda x: x.isdigit() and int(x) % 2 == 0, sorted(lst, reverse=True)))

# Print results
print("Uppercase letters (descending):", up)
print("Lowercase letters (ascending):", ll)
print("Odd numbers (ascending):", odd)
print("Even numbers (descending):", even)

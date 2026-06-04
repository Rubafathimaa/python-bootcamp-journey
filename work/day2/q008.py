s = input("enter a string: ")
count = 0

for i in s.lower():
    if i in "aeiou":
        count += 1
print(f"Number of vowels in the string: {count}")

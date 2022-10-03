# list to search through
numbers = [5, 104, 401, 28, 60, 48, 4, 681, 3, 6, 9, 10, 46, 20]

number = int(input())

# write solution here
for y in numbers:
  if number == y:
    match_found = True
    break

print(match_found)
match_found = False

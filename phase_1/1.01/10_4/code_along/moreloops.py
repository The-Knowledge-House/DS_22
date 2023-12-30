
print("count by 2's")
x = 0
while x <= 10:
    print(x)
    x += 2

print("count backwards")
x = 10
while x > 0:
    print(x)
    x -= 1

print("count until I'm told not to")
answer = input("stop?")
times = 1
while answer != "stop":
    print("I asked", times, "times")
    answer = input("stop?")

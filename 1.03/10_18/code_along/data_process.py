data = [130, 500, 1000, "404", 530, 200, 150_000, 100_000,
        "404", 80_000, 30_000, 2000]

retention_rate = 0.03

# TODO: run this code
for pop in data:
    print(f"we retained {retention_rate * pop} users")

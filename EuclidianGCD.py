def gcd_algorithm(a, b, r):
    iteration = 0
    while b != 0:
        print(f"Iteration {iteration}: a={a}, b={b}, r={r}")

        r = a % b
        a = b
        b = r
        iteration += 1
    gcd = a
    print(f"\nGCD: {gcd}")

# Initial values
a = 5870
b = 1236
r = 1236

gcd_algorithm(a, b, r)

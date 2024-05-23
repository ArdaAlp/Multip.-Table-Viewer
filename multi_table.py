num = int(input("Number for multiplication table: "))
print(f"*** The Multiplication Table of {num} ***")

def multi(num):
    for i in range(1, 11):
        print(f"{i} x {num} = {i * num}")

multi(num)
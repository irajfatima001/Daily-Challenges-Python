
num = int(input("Enter a number: "))


binary = bin(num)[2:]


if binary == binary[::-1]:
    print(f"📌 Binary: {binary}")
    print("✅ Output: Palindrome")
else:
    print(f"📌 Binary: {binary}")
    print("❌ Output: Not a Palindrome")

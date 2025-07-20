import random
import string

def generate_password(length=12, use_upper=True, use_lower=True, use_digits=True, use_symbols=True):
    if not (use_upper or use_lower or use_digits or use_symbols):
        return "⚠️ You must select at least one character type."

    characters = ''
    if use_upper:
        characters += string.ascii_uppercase
    if use_lower:
        characters += string.ascii_lowercase
    if use_digits:
        characters += string.digits
    if use_symbols:
        characters += string.punctuation

    password = ''.join(random.choice(characters) for _ in range(length))
    return password

def get_user_input():
    print("\n🔐 Password Generator Settings:")
    try:
        length = int(input("Enter password length (e.g., 12): "))
    except ValueError:
        print("❌ Invalid input. Using default length 12.")
        length = 12

    use_upper = input("Include UPPERCASE letters? (y/n): ").lower() == 'y'
    use_lower = input("Include lowercase letters? (y/n): ").lower() == 'y'
    use_digits = input("Include digits? (y/n): ").lower() == 'y'
    use_symbols = input("Include symbols? (y/n): ").lower() == 'y'

    password = generate_password(length, use_upper, use_lower, use_digits, use_symbols)
    print(f"\n🔑 Generated Password: {password}")

def main():
    print("=== 💻 Python Password Generator ===")
    while True:
        get_user_input()
        again = input("\nGenerate another? (y/n): ").lower()
        if again != 'y':
            print("👋 Exiting Password Generator. Stay secure!")
            break

if __name__ == "__main__":
    main()

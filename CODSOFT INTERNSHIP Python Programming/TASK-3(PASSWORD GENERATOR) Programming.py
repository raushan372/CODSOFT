import string
import random

def generate_password(length):
    """Generate a secure password of given length."""
    if length < 4:
        return "❌ Password length should be at least 4 characters."

    # Characters: lowercase + uppercase + digits + punctuation
    characters = string.ascii_letters + string.digits + string.punctuation

    # Use random.choices for secure random selection
    password = ''.join(random.choices(characters, k=length))
    return password

def main():
    print("🔐 Welcome to the Password Generator!")

    try:
        length = int(input("Enter desired password length: "))
    except ValueError:
        print("❌ Please enter a valid number.")
        return

    password = generate_password(length)
    print(f"\n✅ Generated Password: {password}")

# Run the main function
main()

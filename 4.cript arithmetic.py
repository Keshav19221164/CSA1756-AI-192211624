import random

# Function to generate a basic arithmetic problem
def generate_problem():
    num1 = random.randint(1, 100)
    num2 = random.randint(1, 100)
    operation = random.choice(['+', '-', '*', '/'])
    return num1, num2, operation

# Function to encrypt the problem using a basic Caesar cipher
def encrypt(text, shift=3):
    encrypted_text = ''
    for char in text:
        if char.isalpha():
            shift_base = ord('A') if char.isupper() else ord('a')
            encrypted_text += chr((ord(char) - shift_base + shift) % 26 + shift_base)
        elif char.isdigit():
            encrypted_text += str((int(char) + shift) % 10)
        else:
            encrypted_text += char
    return encrypted_text

# Main function to create and encrypt the problem
def main():
    num1, num2, operation = generate_problem()
    problem = f"{num1} {operation} {num2}"
    encrypted_problem = encrypt(problem)
    print("Original Problem:", problem)
    print("Encrypted Problem:", encrypted_problem)

if __name__ == "__main__":
    main()

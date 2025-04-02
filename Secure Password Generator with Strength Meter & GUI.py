import random
import string
import tkinter as tk

def generate_password(min_length=12, numbers=True, special_characters=True, exclude_ambiguous=True):
    letters = string.ascii_letters
    digits = string.digits
    special = string.punctuation
    ambiguous_chars = "O0l1I"
    
    characters = letters
    password = []

    if numbers:
        characters += digits
        password.append(random.choice(digits))

    if special_characters:
        characters += special
        password.append(random.choice(special))

    if exclude_ambiguous:
        characters = "".join(char for char in characters if char not in ambiguous_chars)

    while len(password) < min_length:
        password.append(random.choice(characters))

    random.shuffle(password)
    return "".join(password)

def check_password_strength(password):
    length = len(password)
    has_digits = any(char.isdigit() for char in password)
    has_special = any(char in string.punctuation for char in password)
    has_upper = any(char.isupper() for char in password)
    has_lower = any(char.islower() for char in password)

    if length < 8:
        return "Weak"
    elif length >= 8 and (has_digits or has_special):
        return "Medium"
    elif length >= 10 and has_digits and has_special and has_upper and has_lower:
        return "Strong"
    elif length >= 12 and has_digits and has_special and has_upper and has_lower:
        return "Very Strong"
    else:
        return "Medium"

def generate_and_display():
    password = generate_password()
    strength = check_password_strength(password)
    password_display.config(text=f"Generated Password:\n{password}")
    strength_display.config(text=f"Strength: {strength}")

root = tk.Tk()
root.title("Password Generator")

tk.Label(root, text="Click the button to generate a strong password!", font=("Arial", 12)).pack(pady=10)
tk.Button(root, text="Generate Password", command=generate_and_display, font=("Arial", 12), bg="lightblue").pack(pady=5)
password_display = tk.Label(root, text="", font=("Courier", 14), fg="blue")
password_display.pack(pady=10)
strength_display = tk.Label(root, text="", font=("Arial", 12), fg="green")
strength_display.pack(pady=5)

root.mainloop()


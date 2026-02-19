import secrets
import string
import argparse


def generate_password(length: int, use_lower=True, use_upper=True,
                      use_digits=True, use_special=True) -> str:
    """Generate a strong random password based on selected criteria."""
    character_sets = []

    if use_lower:
        character_sets.append(string.ascii_lowercase)
    if use_upper:
        character_sets.append(string.ascii_uppercase)
    if use_digits:
        character_sets.append(string.digits)
    if use_special:
        character_sets.append(string.punctuation)

    if not character_sets:
        raise ValueError("No character types selected for the password.")

    all_chars = ''.join(character_sets)

    # Ensure at least one character from each selected set
    password = [
        secrets.choice(s) for s in character_sets
    ]

    # Fill the rest of the length
    password += [secrets.choice(all_chars) for _ in range(length - len(password))]

    # Shuffle to avoid predictable placement
    secrets.SystemRandom().shuffle(password)

    return ''.join(password)


def main():
    parser = argparse.ArgumentParser(description="Secure Python Password Generator")
    parser.add_argument("-l", "--length", type=int, default=12,
                        help="Length of the password (default: 12)")
    parser.add_argument("--no-lower", action="store_true", help="Exclude lowercase letters")
    parser.add_argument("--no-upper", action="store_true", help="Exclude uppercase letters")
    parser.add_argument("--no-digits", action="store_true", help="Exclude digits")
    parser.add_argument("--no-special", action="store_true", help="Exclude special characters")

    args = parser.parse_args()

    try:
        pwd = generate_password(
            length=args.length,
            use_lower=not args.no_lower,
            use_upper=not args.no_upper,
            use_digits=not args.no_digits,
            use_special=not args.no_special
        )
        print(f"\n🔐 Generated Password:\n{pwd}\n")
    except Exception as e:
        print("Error:", e)


if __name__ == "__main__":
    main()

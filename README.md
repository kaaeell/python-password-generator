# Python Password Generator

A simple and flexible Python script to generate strong passwords.

---

## Features

-  Generates random passwords with strong entropy
-  Customizable: include or exclude
  - lowercase letters
  - uppercase letters
  - digits
  - special characters
-  Uses `secrets` module for better security
-  Command-line arguments support

---

## Installation

```bash
git clone https://github.com/kaaeell/python-password-generator.git
cd python-password-generator
```

---

## Usage

### Basic

```bash
python password_generator.py
```

Generates a 12-character password.

---

### Custom length

```bash
python password_generator.py -l 16
```

---

### Exclude character types

```bash
python password_generator.py --no-special --no-upper
```

---

## Tips

- Use longer passwords (15+ chars) for better security.:contentReference[oaicite:2]{index=2}
- Try different combinations of character sets for strong randomness.

---

## Example Output

```
🔐 Generated Password:
x4!Bf8$zUqT2mL%
```

---

## Future Ideas

- Build a simple GUI version
- Save passwords to a file or clipboard
- Add strength scoring

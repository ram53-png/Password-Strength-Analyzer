# Password Strength Analyzer & Custom Wordlist Generator

## Objective
To build a simple tool that:
1. Evaluates the strength of passwords using zxcvbn.
2. Generates custom password wordlists based on user info (name, DOB, pet).

## Tools Used
- Python
- `zxcvbn` (for strength analysis)
- Custom functions for leetspeak and combinations

## Files Included
- `analyzer.py` – Checks password strength and gives suggestions.
- `wordlist_generator.py` – Generates a password wordlist.
- `wordlist.txt` – Output file with generated passwords.

## How It Works
- User enters personal info (name, DOB, pet).
- Script generates variants and saves them as a wordlist.
- Password entered is evaluated and scored (0 to 4) with recommendations.

## Conclusion
This tool helps users test password strength and understand how attackers might use personal info to guess passwords.

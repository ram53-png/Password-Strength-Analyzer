import zxcvbn
from zxcvbn import zxcvbn

password = input("Enter a password to test strength: ")
results = zxcvbn(password)

print(f"Score: {results['score']} (0=Weak, 4=Strong)")
print(f"Crack Time: {results['crack_times_display']['offline_fast_hashing_1e10_per_second']}")
print("Feedback:")
print(" - Warnings:", results['feedback']['warning'])
print(" - Suggestions:", ', '.join(results['feedback']['suggestions']))

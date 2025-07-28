def leetspeak(word):
    return word.replace("a", "@").replace("s", "$").replace("o", "0").replace("i", "1")

def generate_wordlist(name, dob, pet):
    base = [name, dob, pet]
    combos = []
    for word in base:
        combos.extend([
            word,
            word + "123",
            word + "2025",
            leetspeak(word),
            leetspeak(word) + "123"
        ])
    return combos

if __name__ == "__main__":
    name = input("Enter name: ")
    dob = input("Enter date of birth (e.g. 1999): ")
    pet = input("Enter pet name: ")
    wordlist = generate_wordlist(name, dob, pet)
    with open("wordlist.txt", "w") as file:
        for word in wordlist:
            file.write(word + "\n")
    print("Custom wordlist saved as wordlist.txt")

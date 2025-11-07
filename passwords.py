#Author: David Owolabi
#Creativity: Added customized feedback messages for each password strength level, along with input validation for empty passwords and spaces to enhance user experience.

LOWER=["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
UPPER=["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
DIGITS=["0","1","2","3","4","5","6","7","8","9"]
SPECIAL=["!", "@", "#", "$", "%", "^", "&", "*", "(", ")", "-", "_", "=", "+", "[", "]", "{", "}", "|", ";", ":", """, """, ",", ".", "<", ">", "?", "/", "`", "~"]      
        
    
def word_in_file(word,filename,case_sensitive=False):
    """Checks if a word is in a file."""
    with open(filename, "r",encoding="utf-8") as file:
        word_list = file.readlines()
        for line in word_list:
            word = word.lower()
            line = line.strip().lower()
            if word == line:
                return True
        else:
            return False

def word_has_character(word,character_list):
    """Checks if a word has at least one character from a list."""
    for character in word:
         if character in character_list:
            return True
    return False


def word_complexity(word):
    """Calculates the complexity score of a word based on character types."""
    complexity = 0
    if word_has_character(word, LOWER):
        complexity += 1
    if word_has_character(word, UPPER):
        complexity += 1
    if word_has_character(word, DIGITS):
        complexity += 1
    if word_has_character(word, SPECIAL):
        complexity += 1
    return complexity

def password_strength (password,min_length=10,strong_length=16):
    """Evaluates the strength of a password and provides feedback."""
    password_strength = 0
    if password == "":
        print("Password cannot be empty")
        return 0
    if " " in password:
        print("Password should not contain spaces")
        return 0
    if word_in_file(password,"wordlist.txt"):
        print("Password is a dictionary word and is not secure.")
        return 0
    if word_in_file(password, "toppasswords.txt", case_sensitive=True):
        print("Password is a commonly used password and is not secure.")
        return 0
    elif len(password) < min_length:
        print("Password is too short and is not secure.")
        return 1
    elif len(password) >= strong_length:
        print("Password is long, length trumps complexity this is a good password")
        return 5
    elif len(password) >= strong_length and word_complexity(password) >= 3:
        print("Password is very strong due to excellent length and high complexity.")
        return 5
    elif len(password) >= min_length and word_complexity(password) >= 3:
        print("Password is strong due to good length and high complexity.")
        return 5
    elif len(password) == min_length and word_complexity(password) == 1:
        print("Password is weak due to low complexity.")
        return 2
    elif len(password) >= min_length and word_complexity(password) == 2:
        print("Password is fair due to medium complexity.")
        return 3
    elif len(password) >= min_length and word_complexity(password) == 3:
        print("Password is moderate due to medium complexity.")
        return 4
    
    return password_strength

def main():
    """Main function to test password strength evaluation."""
    print("Welcome to the password strength checker, press q to quit")
    while True:
        password = input("Enter a password to evaluate its strength: ")
        if password.strip().lower() != "q":
            strength = password_strength(password)
            print(f"Password strength: {strength}/5\n")
        else:
            print("Goodbye!")
            break

if __name__ == "__main__":
    main()
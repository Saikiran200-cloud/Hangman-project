hangman_parts = [ "head", "left arm", "torso", "right arm", "left leg", "right leg" ]
num_wrong_guesses_allowed = len(hangman_parts)
words = [
    "apple",
    "butterfly",
    "car",
    "pajama",
    "kayak",
    "zigzag",
    "zombie",
    "oxygen",
    "able",
    "baby",
    "lock",
    "ornament",
    "quality",
    "liquid",
    "suggestion",
    "weather",
    "twist"
    ]

def draw_hangman(num_wrong_guesses):
    if num_wrong_guesses > num_wrong_guesses_allowed:
        num_wrong_guesses = num_wrong_guesses_allowed

    hangman_characters = {
        "head" : "  O",
        "left arm" : " /",
        "torso" : "|",
        "right arm" : "\\",
        "left leg" : " /",
        "right leg" : " \\"
    }
    hangman_newlines = [ "head", "right arm", "right leg" ]

    output = " _____\n |   |\n | "
    num_newlines = 0
    for i in range(num_wrong_guesses):
        output = output + hangman_characters[hangman_parts[i]]
        if hangman_parts[i] in hangman_newlines:
            output = output + "\n | "
            num_newlines = num_newlines + 1
    for i in range(len(hangman_newlines) - num_newlines):
        output = output + "\n |"
    output = output + "____\n\n"
    print(output)

# check for a win condition
def check_if_done(word, guesses):
    for character in word:
        if not character in guesses:
            return False
        return True

word = "test"
wrong_guesses = 0
guesses = []
done = False

name = input("What is your name? ")
print("Hello, " + name + "! Time to play hangman!")

while wrong_guesses < num_wrong_guesses_allowed:
    guess = input("What is your guess? ").lower()
    if guess in word:
        print("Correct!")
    else:
        print("Wrong!")
        wrong_guesses = wrong_guesses + 1
    
    draw_hangman(wrong_guesses)
    guesses.append(guess)
    print("guessed:" + str(guesses))

    done = check_if_done(word, guesses)

if wrong_guesses == num_wrong_guesses_allowed:
    print("Sorry, you lost!")
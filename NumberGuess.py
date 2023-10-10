import random
def generate_seq(length):
    sequence = []
    for _ in range(length):
        sequence.append(random.randint(1,9))
    return sequence


def display_seq(sequence):
    print("Här är sekvensen:")
    for item in sequence:
        print(item,end=" ")
    print()

def get_player_guess(length):
    print("Gissa ordningen:")
    guess= []
    for _ in range(length):
        guess.append(int(input()))
    return guess

def check_guess(sequence, guess):
    return sequence == guess

def play_game():
    difficulty = int(input("Välja svårighetsrad:"))
    if difficulty < 2:
        print("Svårighetsgraden måste vara minst 2.")
        return
    sequence = generate_seq(difficulty)
    display_seq(sequence)
    input("Tryck Enter för att blanda sekvensen...")
    random.shuffle(sequence)
    display_seq(sequence)

    while True:
        player_guess = get_player_guess(difficulty)
        if check_guess(sequence,player_guess ):
            print("Grattis")
            break
        else:
            print("Fel ordning, Försök igen.")
if __name__ == "__main__":
    play_game()


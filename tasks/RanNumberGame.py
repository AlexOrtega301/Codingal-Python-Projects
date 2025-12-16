import random

# Game data stored in a dictionary
game = {
    "min": 1,
    "max": 10,
    "secret": random.randint(1, 10),
    "attempts": 0,
    "running": True
}

print("🎮 Guess the Number Game")
print(f"I'm thinking of a number between {game['min']} and {game['max']}")

while game["running"]:
    guess = input("Your guess: ")

    # Basic input check
    if not guess.isdigit():
        print("⚠️ Please enter a number.")
        continue

    guess = int(guess)
    game["attempts"] += 1

    if guess < game["secret"]:
        print("📉 Too low!")
    elif guess > game["secret"]:
        print("📈 Too high!")
    else:
        print(f"🎉 Correct! You guessed it in {game['attempts']} tries.")
        game["running"] = False

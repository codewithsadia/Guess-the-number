import random  # Random number banane ke liye
from colorama import Fore, Style  # type: ignore # Color text ke liye

secret_number = random.randint(1, 10)  # Secret number (1-10)
guess = None
tries = 5  # Sadia ke paas 5 chances hain!

print(Fore.CYAN + "🎯 Welcome Sadia! Guess a number between 1 and 10!")
print(f"You have {tries} tries! Good Luck! 🍀" + Style.RESET_ALL)

while guess != secret_number and tries > 0:
    try:
        guess = int(input(Fore.YELLOW + "👉 Enter your guess: " + Style.RESET_ALL))
    except ValueError:
        print(Fore.RED + "Please enter a valid number! 🚫" + Style.RESET_ALL)
        continue

    if guess < secret_number:
        print(Fore.BLUE + "Too low! 🌧️ Try a bigger number!" + Style.RESET_ALL)
    elif guess > secret_number:
        print(Fore.MAGENTA + "Too high! 🎈 Try a smaller number!" + Style.RESET_ALL)
    else:
        print(Fore.GREEN + "🎉 Yayyy Sadia! You guessed it right! You are awesome! 🌟" + Style.RESET_ALL)
        break  # Correct guess, loop se bahar niklo

    tries -= 1  # Har galat guess ke baad tries kam hongi
    if tries > 0:
        print(Fore.CYAN + f"⚡ Tries left: {tries}" + Style.RESET_ALL)
    else:
        print(Fore.RED + f"😢 Oh no Sadia! You ran out of tries! The number was {secret_number}." + Style.RESET_ALL)


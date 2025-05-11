import re, random
from colorama import Fore, init

# Initialize colorama
init(autoreset=True)

# Data
destinations = {
    "beaches": ["Bali", "Maldives", "Phuket"],
    "mountains": ["Swiss Alps", "Rocky Mountains", "Himalayas"],
    "cities": ["Tokyo", "Paris", "New York"]
}

jokes = [
    "Why don't programmers like nature? Too many bugs!",
    "Why did the computer go to the doctor? Because it had a virus!",
    "Why do travelers always feel warm? Because of all their hot spots!"
]
last_joke = None

# Utility functions
def normalize_input(text):
    return re.sub(r"\s+", " ", text.strip().lower())

def get_yes_no_input(prompt):
    response = normalize_input(input(Fore.YELLOW + prompt))
    return "yes" if "yes" in response else "no" if "no" in response else "unknown"

# Core functions
def recommend_destination(preference):
    if preference not in destinations:
        print(Fore.RED + "TravelBot: Sorry, I don't have suggestions for that category.")
        return
    
    while True:
        suggestion = random.choice(destinations[preference])
        print(Fore.GREEN + f"TravelBot: How about {suggestion}?")
        user_response = get_yes_no_input("Do you like it? (yes/no): ")
        
        if user_response == "yes":
            print(Fore.GREEN + f"TravelBot: Awesome! Enjoy your time in {suggestion}!")
            break
        elif user_response == "no":
            print(Fore.CYAN + "TravelBot: No worries, let me suggest another one...")
        else:
            print(Fore.RED + "TravelBot: I didn't get that. Let's try again.")

def recommend():
    print(Fore.CYAN + "\nTravelBot: Do you prefer beaches, mountains, or cities?")
    preference = normalize_input(input(Fore.YELLOW + "You: "))
    recommend_destination(preference)

def packing_tips():
    print(Fore.CYAN + "\nTravelBot: Where are you headed?")
    location = normalize_input(input(Fore.YELLOW + "You: "))
    
    print(Fore.CYAN + "TravelBot: For how many days?")
    try:
        days = int(input(Fore.YELLOW + "You: "))
    except ValueError:
        days = 3  # default value
        print(Fore.RED + "TravelBot: Couldn't understand. Defaulting to 3 days.")

    print(Fore.GREEN + f"\nTravelBot: Packing tips for {days} days in {location.capitalize()}:")
    print(Fore.GREEN + "- Pack versatile clothes.")
    print(Fore.GREEN + "- Bring chargers and adapters.")
    print(Fore.GREEN + "- Check the weather forecast.")

    if days >= 7:
        print(Fore.GREEN + "- Don't forget laundry supplies or access to laundry service.")
    elif days <= 2:
        print(Fore.GREEN + "- Travel light! Consider a backpack instead of a suitcase.")

def tell_joke():
    global last_joke
    available_jokes = [j for j in jokes if j != last_joke]
    joke = random.choice(available_jokes) if available_jokes else random.choice(jokes)
    last_joke = joke
    print(Fore.YELLOW + f"\nTravelBot: {joke}")

def show_help():
    print(Fore.MAGENTA + "\nWhat I can do:")
    print(Fore.GREEN + "- Suggest travel destinations → say 'recommend' or 'suggest'")
    print(Fore.GREEN + "- Offer packing tips → say 'pack' or 'packing'")
    print(Fore.GREEN + "- Tell a joke → say 'joke' or 'funny'")
    print(Fore.CYAN + "Type 'exit' or 'bye' to end the conversation.\n")

# Main chat loop
def chat():
    print(Fore.CYAN + "Hello! I'm TravelBot — your virtual travel buddy.")
    name = input(Fore.YELLOW + "What's your name? ")
    print(Fore.GREEN + f"Nice to meet you, {name}!")
    
    show_help()
    
    while True:
        user_input = normalize_input(input(Fore.YELLOW + f"{name}: "))
        
        if "recommend" in user_input or "suggest" in user_input:
            recommend()
        elif "pack" in user_input or "packing" in user_input:
            packing_tips()
        elif "joke" in user_input or "funny" in user_input:
            tell_joke()
        elif "help" in user_input:
            show_help()
        elif "exit" in user_input or "bye" in user_input:
            print(Fore.CYAN + "\nTravelBot: Safe travels! Goodbye!")
            break
        else:
            print(Fore.RED + "TravelBot: Hmm, I didn't quite get that. Try 'help' to see what I can do.")

# Run the bot
if __name__ == "__main__":
    chat()

print("Hello! I am A Bot. What's your name? ")
name = input()
print("Nice to meet you,", name)
print("How are you feeling today? (good/bad): ")
mood = input().lower()

if mood == "good":
    print("I am glad to hear that! ☺️")
elif mood == "bad":
    print("I am sorry to hear that. Hope your day gets better!")  
else:
    print("I see. Sometmes, it's hard to put feelings into words.")   

print(f"It was nice chatting with you, {name}. Have a nice day!")       
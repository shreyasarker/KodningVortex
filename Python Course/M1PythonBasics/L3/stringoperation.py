#input a word
text = str(input("Enter a string: "))

# Reverse String 
revText = text[::-1] 
text = revText

print("Reverse of Given String is:")
print(text)
# 1

while True:
    word_input = input("Please enter two words: ").strip()

    if not word_input:
        break
    elif word_input.lower() == "done":
        print("Bye!")
        break

    words = word_input.split()
    
    if len(words) == 2:
        word1, word2 = words
        if word1 < word2:
            print(f"{word1} comes first")
        else:
            print(f"{word2} comes first")
    elif len(words) == 1:
        print("Please enter two words separated by a space.")
    else:
        print("Invalid input. Please enter two words separated by a space.")




# 2

word_input = input("Enter a string: ")
length = len(word_input)
index = length - 1

print("Input string =", word_input)
while index >= 0:
    print(word_input[index])
    index -= 1




# 3

word_input = input("Please enter a string: ")
 
upper_count = 0
lower_count = 0
number_count = 0
other_count = 0

for i in word_input:
    if i.isupper():
        upper_count += 1
    elif i.islower():
        lower_count += 1
    elif i.isdigit():
        number_count += 1
    else:
        other_count += 1
        
print("Uppercase letters:", upper_count)
print("Lowercase letter:", lower_count)
print("Numbers:", number_count)
print("Other characters:", other_count)




# 4

while True:
    word_input = input("Please enter a string: ")
    
    if word_input.lower() == "done":
        print("Bye!")
        break
    
    special_char = [',','.',':','!','?']
    for i in special_char:
        word_input = word_input.replace(i, '')
        
    word_input = word_input.upper()
    
    print(word_input)
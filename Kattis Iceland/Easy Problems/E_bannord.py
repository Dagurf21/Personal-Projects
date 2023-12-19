banned_letter = (list(input()))
string = input().split(" ")

new_str = ""

for word in string:
    word_length = len(word)

    for letter in banned_letter:
    
        if letter in word:
            new_str = (new_str + ("*"*word_length) + " ")
            break
    
    else:
        new_str = (new_str + word + " ")
        
print (new_str)
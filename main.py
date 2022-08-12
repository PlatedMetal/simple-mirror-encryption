
def convertLetter(letter, shift): 
    if shift > 26:
        rshift = shift - 26
    if shift < -26:
        rshift = shift + 26
    
    # converts letter to num, returns if not lowercase to conserve spaces in the text, then shifts using shift value
    num = ord(letter) - 96
    if num < 0 or num > 26:
        return letter
    rnum = num + shift
    
    # constrains rnum value so you don't get weird unicode characters
    if rnum > 26:
        rnum = rnum - 26
    if rnum < 0:
        rnum = rnum + 26
    
    returnvalue = str(chr(rnum + 96))
    return returnvalue
    
# calls convertLetter() on all text that isn't null
def interpretText(interpreted, shift):
    final = ""
    for character in interpreted: # loops through each character
        if character != "" and character != None:
            final = final + convertLetter(character, shift)
        else:
            final = final + character # if it is null, just add to the string
    return final

while True:
    print("Enter alphabetical ciphertext, plaintext, or press enter to exit: ")
    cipher = str(input()).lower()
    if cipher != None and cipher != "" and cipher != " ": # catches enter (for exits)
    
        print("Enter shift value between 0 and 25 (negative if decrypting):")
        shift = int(input())
        
        if shift < 0:
            cipher = interpretText(cipher, shift) #if decrypting
            
        finaltext = ""
        
        # top, mid, and bottom row reflection of keyboard characters
        cipher1 = cipher.translate(str.maketrans({'q': 'p', 'w': 'o', 'e': 'i', 'r': 'u', 't': 'y', 'y': 't', 'u': 'r', 'i': 'e', 'o': 'w', 'p': 'q'}))
        cipher2 = cipher1.translate(str.maketrans({'a': 'l', 's': 'k', 'd': 'j', 'f': 'h', 'h': 'f', 'j': 'd', 'k': 's', 'l': 'a'}))
        cipher3 = cipher2.translate(str.maketrans({'z': 'm', 'x': 'n', 'c': 'b', 'b': 'c', 'n': 'x', 'm': 'z'}))
        
        
        if shift > 0:
            finaltext = interpretText(cipher3, shift) # if encrypting
        else:
            finaltext = cipher3 # if decrypting
        
        print(finaltext)
    else:
        print("Are you sure? Y/N")
        choice = str(input()).lower()
        
        if choice == "y":
            break
        else:
            choice = choice # random placeholder line of code
    
    
    
    
    
    
    
    
    
    
    
    

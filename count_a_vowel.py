def isVowel(ch):
    return ch.upper() in ['A', 'E', 'I', 'O', 'U']
 
def countVowels(str):
    count = 0
    for i in range(len(str)):
 
        # Check for vowel
        if isVowel(str[i]):
            count += 1
    return count
 
str = input()
 
print(countVowels(str))

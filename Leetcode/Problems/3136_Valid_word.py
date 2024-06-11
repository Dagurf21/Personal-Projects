class Solution:
    def isValid(self, word: str) -> bool:
        vowels = 'aeiouAEIOU'
        has_vowel = False
        has_consonant = False
        valid = True if len(word) >= 3 else False

        for char in word:
            if char in vowels:
                has_vowel = True
            elif char.isalpha() and char not in vowels:
                has_consonant = True
            elif char in '0123456789':
                check_numbers = True
            elif char in '@#$':
                return False
            
        if has_vowel and has_consonant and valid:
            return True 
        return False

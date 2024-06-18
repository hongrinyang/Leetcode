class Solution:
    def toGoatLatin(self, sentence: str) -> str:
        def is_vowel(char: str) -> bool:
            return char.lower() in 'aeiou'

        words = sentence.split()
        goat_latin_words = []

        for i, word in enumerate(words):
            if is_vowel(word[0]):
                goat_word = word + "ma"
            else:
                goat_word = word[1:] + word[0] + "ma"
            goat_word += "a" * (i + 1)
            goat_latin_words.append(goat_word)
        
        return " ".join(goat_latin_words)
class Solution:
    def countValidWords(self, sentence: str) -> int:
        def is_valid(word):
            n = len(word)
            if n == 0:
                return False

            if any(char.isdigit() for char in word):
                return False

            hyphen_count = word.count('-')
            if hyphen_count > 1:
                return False
            if hyphen_count == 1:
                hyphen_index = word.index('-')
                if hyphen_index == 0 or hyphen_index == n-1:
                    return False
                if not (word[hyphen_index-1].isalpha() and word[hyphen_index+1].isalpha()):
                    return False

            if word[-1] in "!,.":
                word = word[:-1]

            if any(char in "!,." for char in word):
                return False
            
            return True

        tokens = sentence.split()
        valid_word_count = sum(is_valid(word) for word in tokens)
        return valid_word_count
from collections import defaultdict
class Words:
    def __init__(self,words_file="/usr/share/dict/words"):
        with open(words_file) as file:
            words_by_length=defaultdict(list)
            for word in file:
                word=word.rstrip("\n")
                if not word.isalpha() or not word.islower():
                    continue
                words_by_length[len(word)].append(word)
                words_by_length[1]=list("IOa")
                self.words_by_length=words_by_length


    def possibilities(self,num_letters,num_words):
        words_by_length=self.words_by_length
        if num_words==1:
            for word1 in words_by_length[num_letters]:
                yield(word1,)
            return

        for length in range(1,num_letters-num_words+2):
            for word1 in words_by_length[length]:
                for rest in self.possibilities(num_letters-length,num_words-1):
                    yield(word1,)+rest

def main():
    words=Words()
    for sentence in words.possibilities(8,3):
        if "love" in sentence:
            print(*sentence)


if __name__=="__main__":
    main()

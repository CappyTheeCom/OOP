even_list = [2,3,4,5,6,7,8,9,10]
user_input = input("Enter a word: ")

class CustomReverse:

    def __init__(self,even_list,word):
        self.word = word
        self.even = even_list

    def word_reverse(self):
        word_list = []
        for word in reversed(self.word):
            word_list.append(word)

        for reWord in word_list:
            print(reWord,end="")
    
    def reverse_list(self):
        print(list(reversed(self.even)))

Custom = CustomReverse(even_list,user_input)
Custom.word_reverse()
Custom.reverse_list()
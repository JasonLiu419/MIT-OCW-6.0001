# Problem Set 4C
# Name: <Yuyang liu>
# Collaborators:
# Time Start ：20210405
# Time Spent: x:xx

import string
from ps4a import get_permutations

### HELPER CODE ###
def load_words(file_name):
    '''
    file_name (string): the name of the file containing 
    the list of words to load    
    
    Returns: a list of valid words. Words are strings of lowercase letters.
    
    Depending on the size of the word list, this function may
    take a while to finish.
    '''
    
    print("Loading word list from file...")
    # inFile: file
    inFile = open(file_name, 'r')
    # wordlist: list of strings
    wordlist = []
    for line in inFile:
        wordlist.extend([word.lower() for word in line.split(' ')])
    print("  ", len(wordlist), "words loaded.")
    return wordlist

def is_word(word_list, word):
    '''
    Determines if word is a valid word, ignoring
    capitalization and punctuation

    word_list (list): list of words in the dictionary.
    word (string): a possible word.
    
    Returns: True if word is in word_list, False otherwise

    Example:

    False
    '''
    word = word.lower()
    word = word.strip(" !@#$%^&*()-_+={}[]|\:;'<>?,./\"")
    return word in word_list


### END HELPER CODE ###

WORDLIST_FILENAME = 'words.txt'

# you may find these constants helpful
VOWELS_LOWER = 'aeiou'
VOWELS_UPPER = 'AEIOU'
CONSONANTS_LOWER = 'bcdfghjklmnpqrstvwxyz'
CONSONANTS_UPPER = 'BCDFGHJKLMNPQRSTVWXYZ'

class SubMessage(object):
    def __init__(self, text):
        '''
        Initializes a SubMessage object
                
        text (string): the message's text

        A SubMessage object has two attributes:
            self.message_text (string, determined by input text)
            self.valid_words (list, determined using helper function load_words)
        '''
        self.message_text = text
        self.valid_words = load_words(WORDLIST_FILENAME)
    
    def get_message_text(self):
        '''
        Used to safely access self.message_text outside of the class
        
        Returns: self.message_text
        '''
        return self.message_text

    def get_valid_words(self):
        '''
        Used to safely access a copy of self.valid_words outside of the class.
        This helps you avoid accidentally mutating class attributes.
        
        Returns: a COPY of self.valid_words
        '''
        return self.valid_words
                
    def build_transpose_dict(self, vowels_permutation):
        '''
        vowels_permutation (string): a string containing a permutation of vowels (a, e, i, o, u)
        
        Creates a dictionary that can be used to apply a cipher to a letter.
        The dictionary maps every uppercase and lowercase letter to an
        uppercase and lowercase letter, respectively. Vowels are shuffled 
        according to vowels_permutation. The first letter in vowels_permutation 
        corresponds to a, the second to e, and so on in the order a, e, i, o, u.
        The consonants remain the same. The dictionary should have 52 
        keys of all the uppercase letters and all the lowercase letters.

        Example: When input "eaiuo":
        Mapping is a->e, e->a, i->i, o->u, u->o
        and "Hello World!" maps to "Hallu Wurld!"

        Returns: a dictionary mapping a letter (string) to 
                 another letter (string). 
        '''
        # 只有元音根据输入顺序进行改变，辅音不发生变化
        dict = {}
        # 将所有的特殊字符形成列表，之后列出对应关系，自己对应自己
        punc = list(" !@#$%^&*()-_+={}[]|\:;'<>?,./\"")
        for i, item in enumerate(vowels_permutation.lower()):
            dict[VOWELS_LOWER[i]] = item
        for i, item in enumerate(vowels_permutation.upper()):
            dict[VOWELS_UPPER[i]] = item
        for item in CONSONANTS_LOWER:
            dict[item] = item
        for item in CONSONANTS_UPPER:
            dict[item] = item
        for pun in punc:
            dict[pun] = pun
        return dict
    
    def apply_transpose(self, transpose_dict):
        '''
        transpose_dict (dict): a transpose dictionary
        
        Returns: an encrypted version of the message text, based 
        on the dictionary
        '''
        # enc_message 代表的是加密后的信息
        enc_message = []
        for i in self.message_text:
            enc_message.append(transpose_dict[i])
        return ''.join(enc_message)
        
class EncryptedSubMessage(SubMessage):
    def __init__(self, text):
        '''
        Initializes an EncryptedSubMessage object

        text (string): the encrypted message text

        An EncryptedSubMessage object inherits from SubMessage and has two attributes:
            self.message_text (string, determined by input text)
            self.valid_words (list, determined using helper function load_words)
        '''
        self.message_text = text
        self.valid_words = load_words(WORDLIST_FILENAME)

    def decrypt_message(self):
        '''
        Attempt to decrypt the encrypted message 
        
        Idea is to go through each permutation of the vowels and test it
        on the encrypted message. For each permutation, check how many
        words in the decrypted text are valid English words, and return
        the decrypted message with the most English words.
        
        If no good permutations are found (i.e. no permutations result in 
        at least 1 valid word), return the original string. If there are
        multiple permutations that yield the maximum number of words, return any
        one of them.

        Returns: the best decrypted message    
        
        Hint: use your function from Part 4A
        '''
        tranpose_dict_list = []
        de_message_list = []
        # 得到 aeiou 的全排列
        perm_list = get_permutations('aeiou')
        # 将全排列中的所有对应加入字典列表中
        for perm in perm_list:
            tranpose_dict_list.append(self.build_transpose_dict(perm))
        for dic in tranpose_dict_list:
            de_message = self.apply_transpose(dic)
            de_message_list.append(de_message)
        test = []
        big_test = []
        word_list = self.get_valid_words()
        for mes in de_message_list:
            de_words = mes.split()
            for word in de_words:
                if is_word(word_list, word):
                    test.append(1)
                else:
                    test.append(0)
            # big_test 中存放着每一种排列方式，对应的得分（有效单词，得分加一）
            big_test.append((sum(test), mes))
            del test[0:len(test)]
        # best_choice 就是得分最高者
        best_choice = max(big_test)
        possible_de_message = []
        for tup in big_test:
            # tup[0] == best_choice[0]用于找到最高分所在得位置。并且排列方式不存在于已有方式中，则保存该排列
            if tup[0] == best_choice[0] and tup[1] not in possible_de_message:
                possible_de_message.append(tup[1])
        de_string = ''
        for mes in possible_de_message:
            de_string = de_string + ', ' + mes
        return de_string[1:]
    

if __name__ == '__main__':

    # Example test case
    message = SubMessage("Hello World!")
    permutation = "eaiuo"
    enc_dict = message.build_transpose_dict(permutation)
    print("Original message:", message.get_message_text(), "Permutation:", permutation)
    print("Expected encryption:", "Hallu Wurld!")
    print("Actual encryption:", message.apply_transpose(enc_dict))
    enc_message = EncryptedSubMessage(message.apply_transpose(enc_dict))
    print("Decrypted message:", enc_message.decrypt_message())
     
    #TODO: WRITE YOUR TEST CASES HERE
    message = SubMessage('Happy New Year!')
    permutation = 'iauoe'
    enc_dict = message.build_transpose_dict(permutation)
    print("Original message:", message.get_message_text(), "Permutation:", permutation)
    print("Expected encryption:", "Hippy Naw Yair!")
    print("Actual encryption:", message.apply_transpose(enc_dict))
    enc_message = EncryptedSubMessage(message.apply_transpose((enc_dict)))
    print('Decrypted message:', enc_message.decrypt_message())
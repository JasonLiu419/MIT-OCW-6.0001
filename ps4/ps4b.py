# Problem Set 4B
# Name: <Yuyang Liu>
# Collaborators:
# Time Start: 20210404
# Time Spent: x:xx

import string

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

    '''
    word = word.lower()
    # 存疑！！  word.strip() 应该只能是在首尾操作
    word = word.strip(" !@#$%^&*()-_+={}[]|\:;'<>?,./\"")
    return word in word_list

def get_story_string():
    """
    Returns: a story in encrypted text.
    """
    f = open("story.txt", "r")
    story = str(f.read())
    f.close()
    return story

### END HELPER CODE ###

WORDLIST_FILENAME = 'words.txt'

class Message(object):
    def __init__(self, text):
        '''
        Initializes a Message object
                
        text (string): the message's text

        a Message object has two attributes:
            self.message_text (string, determined by input text)
            self.valid_words (list, determined using helper function load_words)
        '''

        #delete this line and replace with your code here
        self.message_text = text
        self.valid_word = load_words(WORDLIST_FILENAME)



    def get_message_text(self):
        '''
        Used to safely access self.message_text outside of the class
        
        Returns: self.message_text
        '''
        # delete this line and replace with your code here
        return self.message_text

    def get_valid_words(self):
        '''
        Used to safely access a copy of self.valid_words outside of the class.
        This helps you avoid accidentally mutating class attributes.
        
        Returns: a COPY of self.valid_words
        '''
        # delete this line and replace with your code here

        return self.valid_word

    def build_shift_dict(self, shift):
        '''
        Creates a dictionary that can be used to apply a cipher to a letter.
        The dictionary maps every uppercase and lowercase letter to a
        character shifted down the alphabet by the input shift. The dictionary
        should have 52 keys of all the uppercase letters and all the lowercase
        letters only.        
        
        shift (integer): the amount by which to shift every letter of the 
        alphabet. 0 <= shift < 26

        Returns: a dictionary mapping a letter (string) to 
                 another letter (string). 
        '''
        # delete this line and replace with your code here
        import string
        # 为了使得超出26个字母的移动范围后仍然有匹配，现在使用将大小写字母生成两遍，前后相连
        lower_letters = string.ascii_lowercase * 2
        upper_letters = string.ascii_uppercase * 2
        dict = {}
        # 使用enumerate函数，在返回列表中参数同时返回索引，一次既获得位置信息又获得取值信息，便于操作
        for i, item in enumerate(lower_letters[:26]):
            dict[item] = lower_letters[i + shift]
        for i, item in enumerate(upper_letters[:26]):
            dict[item] = upper_letters[i + shift]


        return dict

    def apply_shift(self, shift):
        '''
        Applies the Caesar Cipher to self.message_text with the input shift.
        Creates a new string that is self.message_text shifted down the
        alphabet by some number of characters determined by the input shift        
        
        shift (integer): the shift with which to encrypt the message.
        0 <= shift < 26

        Returns: the message text (string) in which every character is shifted
             down the alphabet by the input shift
第一次使用的方法：（实际采用为第二种，直接保留原特殊字符）
        dict = self.build_shift_dict(shift)
        shift_message_text = []
        num = 0
        for i in range(len(self.message_text)):
            # 这里判断的引入是为了如果text中存在！等特殊字符，用于保留
            if self.message_text[i].isalpha():
                shift_message_text.append(dict[self.message_text[i]])
            else:
                num = i
                member = self.message_text[num]
                i += 1
                continue
        if num > 0:
            shift_message_text.insert(num, member)
        # 这时返回的字符都是分开的，单独存在与各个引号中，只用''.join(sequence), 把分开的字符连接起来
        return ''.join(shift_message_text)
        '''

        dict = self.build_shift_dict(shift)
        shift_message_text = []

        for i in range(len(self.message_text)):
            # 这里判断的引入是为了如果text中存在！等特殊字符，用于保留
            if self.message_text[i].isalpha():
                shift_message_text.append(dict[self.message_text[i]])
            else:
                shift_message_text.append(self.message_text[i])

        # 这时返回的字符都是分开的，单独存在与各个引号中，只用''.join(sequence), 把分开的字符连接起来
        return ''.join(shift_message_text)



class PlaintextMessage(Message):
    def __init__(self, text, shift):
        '''
        Initializes a PlaintextMessage object        
        
        text (string): the message's text
        shift (integer): the shift associated with this message

        A PlaintextMessage object inherits from Message and has five attributes:
            self.message_text (string, determined by input text)
            self.valid_words (list, determined using helper function load_words)
            self.shift (integer, determined by input shift)
            self.encryption_dict (dictionary, built using shift)
            self.message_text_encrypted (string, created using shift)

        '''

        self.message_text = text
        self.valid_words = load_words(WORDLIST_FILENAME)
        self.shift = shift
        # 因为 class PlaintextMessage(Message): 是class Message 的继承，所以可以直接调用class Message 中的函数
        self.encryption_dict = self.build_shift_dict(shift)
        self.message_text_encrypted = self.apply_shift(shift)

    def get_shift(self):
        '''
        Used to safely access self.shift outside of the class
        
        Returns: self.shift
        '''
        return self.shift

    def get_encryption_dict(self):
        '''
        Used to safely access a copy self.encryption_dict outside of the class
        
        Returns: a COPY of self.encryption_dict
        '''
        return self.encryption_dict

    def get_message_text_encrypted(self):
        '''
        Used to safely access self.message_text_encrypted outside of the class
        
        Returns: self.message_text_encrypted
        '''
        return self.message_text_encrypted

    def change_shift(self, shift):
        '''
        Changes self.shift of the PlaintextMessage and updates other 
        attributes determined by shift.        
        
        shift (integer): the new shift that should be associated with this message.
        0 <= shift < 26

        Returns: nothing
        '''

        self.get_encryption_dict = self.build_shift_dict(shift)
        self.message_text_encrypted = self.apply_shift(shift)
        self.shift = shift



class CiphertextMessage(Message):
    def __init__(self, text):
        '''
        Initializes a CiphertextMessage object
                
        text (string): the message's text

        a CiphertextMessage object has two attributes:
            self.message_text (string, determined by input text)
            self.valid_words (list, determined using helper function load_words)
        '''
        self.message_text = text
        self.valid_words = load_words(WORDLIST_FILENAME)

    def decrypt_message(self):
        '''
        Decrypt self.message_text by trying every possible shift value
        and find the "best" one. We will define "best" as the shift that
        creates the maximum number of real words when we use apply_shift(shift)
        on the message text. If s is the original shift value used to encrypt
        the message, then we would expect 26 - s to be the best shift value 
        for decrypting it.

        Note: if multiple shifts are equally good such that they all create 
        the maximum number of valid words, you may choose any of those shifts 
        (and their corresponding decrypted messages) to return

        Returns: a tuple of the best shift value used to decrypt the message
        and the decrypted message text using that shift value
        '''
        '''
             word_list = self.valid_words
        score = []
        num = 0
        for i in range(0, 26):
            de_text = self.apply_shift(i)
            de_words = de_text.split()
            for word in de_words:
                if is_word(word_list, word):
                    num += 1
                score.append(num)
        best_shift = score.index(max(score))
        return best_shift
        '''

        word_list = self.valid_words
        test = []
        big_test = []
        for s in range(26):
            de_text = self.apply_shift(s)
            de_words = de_text.split()
            for word in de_words:
                if is_word(word_list, word):
                    test.append(1)
                else:
                    test.append(0)
            # 将(sum(test), s, de_text)三个元素放在一起，存为一个元素
            big_test.append((sum(test), s, de_text))
            del test[0:len(test)]
        best_shift = max(big_test)
        answer = best_shift[1:3]
        return answer


if __name__ == '__main__':
    # Example test case (PlaintextMessage)
    plaintext = PlaintextMessage('hello!', 2)
    print('Expected Output: jgnnq!')
    print('Actual Output:', plaintext.get_message_text_encrypted())

    # Example test case (CiphertextMessage)
    ciphertext = CiphertextMessage('jgnnq')
    print('Expected Output:', (24, 'hello'))
    print('Actual Output:', ciphertext.decrypt_message())

    # TODO: WRITE YOUR TEST CASES HERE
    plaintext = PlaintextMessage('hairy balls', 1)
    print('Expected Output: ibjsz cbmmt')
    print('Actual Output:', plaintext.get_message_text_encrypted())
    # TODO: best shift value and unencrypted story
    story = get_story_string()
    ciphertext = CiphertextMessage(story)
    print('Unencypted story:', ciphertext.decrypt_message())

'''
#    #Example test case (PlaintextMessage)
#    plaintext = PlaintextMessage('hello', 2)
#    print('Expected Output: jgnnq')
#    print('Actual Output:', plaintext.get_message_text_encrypted())
     plaintext = PlaintextMessage('hello!', 2)
     print('Expected Output: jgnnq!')
     print('Actual Output:', plaintext.get_message_text_encrypted())
#    #Example test case (CiphertextMessage)
#    ciphertext = CiphertextMessage('jgnnq')
#    print('Expected Output:', (24, 'hello'))
#    print('Actual Output:', ciphertext.decrypt_message())
     ciphertext = CiphertextMessage('jgnnq')
     print('Expected Output:', (24, 'hello'))
     print('Actual Output:', ciphertext.decrypt_message())

    #TODO: WRITE YOUR TEST CASES HERE 
    plaintext = PlaintextMessage('hairy balls', 1)
    print('Expected Output: ibjsz cbmmt')
    print('Actual Output:', plaintext.get_message_text_encrypted())

    #TODO: best shift value and unencrypted story 
'''

    

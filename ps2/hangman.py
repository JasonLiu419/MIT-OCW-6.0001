# Problem Set 2, hangman.py
# Name: 
# Collaborators:
# Time spent:

# Hangman Game
# -----------------------------------
# Helper code
# You don't need to understand this helper code,
# but you will have to know how to use the functions
# (so be sure to read the docstrings!)
import random
import string

WORDLIST_FILENAME = "words.txt"


def load_words():
    """
    Returns a list of valid words. Words are strings of lowercase letters.
    
    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print("Loading word list from file...")
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r')
    # line: string
    line = inFile.readline()
    # wordlist: list of strings
    wordlist = line.split()
    print("  ", len(wordlist), "words loaded.")
    return wordlist



def choose_word(wordlist):
    """
    wordlist (list): list of words (strings)
    
    Returns a word from wordlist at random
    """
    return random.choice(wordlist)

# end of helper code

# -----------------------------------

# Load the list of words into the variable wordlist
# so that it can be accessed from anywhere in the program
wordlist = load_words()


def is_word_guessed(secret_word, letters_guessed):
    '''
    secret_word: string, the word the user is guessing; assumes all letters are
      lowercase
    letters_guessed: list (of letters), which letters have been guessed so far;
      assumes that all letters are lowercase
    returns: boolean, True if all the letters of secret_word are in letters_guessed;
      False otherwise
    '''
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    for i in range(len(secret_word)):
        if secret_word[i] in letters_guessed:
            continue
        else:
            return False
    return True




def get_guessed_word(secret_word, letters_guessed):
    '''
    secret_word: string, the word the user is guessing
    letters_guessed: list (of letters), which letters have been guessed so far
    returns: string, comprised of letters, underscores (_), and spaces that represents
      which letters in secret_word have been guessed so far.
    '''
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    new = secret_word
    for i in range(len(secret_word)):
        if secret_word[i] not in letters_guessed:
            new = new.replace(secret_word[i],'_ ')

        else:

           continue
    return new



def get_available_letters(letters_guessed):
    '''
    letters_guessed: list (of letters), which letters have been guessed so far
    returns: string (of letters), comprised of letters that represents which letters have not
      yet been guessed.
    '''
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    import string
    available_letters = string.ascii_lowercase
    for i in range(len(letters_guessed)):
        if letters_guessed[i] in available_letters:
            available_letters = available_letters.replace(letters_guessed[i] , '')
            continue
    return available_letters

    
    

def hangman(secret_word):
    '''
    secret_word: string, the secret word to guess.
    
    Starts up an interactive game of Hangman.
    
    * At the start of the game, let the user know how many 
      letters the secret_word contains and how many guesses s/he starts with.
      
    * The user should start with 6 guesses

    * Before each round, you should display to the user how many guesses
      s/he has left and the letters that the user has not yet guessed.
    
    * Ask the user to supply one guess per round. Remember to make
      sure that the user puts in a letter!
    
    * The user should receive feedback immediately after each guess 
      about whether their guess appears in the computer's word.

    * After each guess, you should display to the user the 
      partially guessed word so far.
    
    Follows the other limitations detailed in the problem write-up.
    '''
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    import os
    print(secret_word)
    num = 6
    letters_guessed = []
    warn = 3
    vowel_list = ['a', 'e', 'i', 'o', 'u']
    print('Welcome to the game Hangman!')
    print('I am thinking of a word that is ' + str(len(secret_word)) + ' letters long.')
    print('You have 3 warnings left')
    print('----------------------------')
    while num > 0:
        while warn > 0:
            #首先判断是否已经猜出正确答案
            if is_word_guessed(secret_word, letters_guessed):
                print('Congratulations, you won!')
                unique = count_secret_word(secret_word)
                score = unique * (num)
                print('You total score for this game is :', score)
                os._exit(0)
            #还没有猜出答案
            else:
                print('You have ', num, ' guesses left.')
                print('Available letters: ', get_available_letters(letters_guessed))
                in_word = input('Please guess a letter:')

                warn_new = test_inword(in_word, warn, letters_guessed)

                if warn_new < warn:
                    warn = warn_new
                    print(' You have ', warn, 'warnings left:', get_guessed_word(secret_word, letters_guessed))
                    print('----------------------------')
                else:
                    letters_guessed.append(in_word)
                    if in_word in secret_word:
                        print('Good guess:', get_guessed_word(secret_word, letters_guessed))
                        print('----------------------------')
                    #检查是否是元音
                    else:
                        if in_word in vowel_list:
                            print('Oops! That word is not in my word, meanwhile, that a Vowel, you will lose two guesses:', get_guessed_word(secret_word, letters_guessed))
                            num -= 2
                            print('----------------------------')
                        else:
                            print('Oops! That word is not in my word, meanwhile, that a Consonants, you will lose one guess:',
                                  get_guessed_word(secret_word, letters_guessed))
                            num -= 1
                            print('----------------------------')
        #warn 的3次机会使用完后，再次出现猜测问题则减少guess的机会，使得num减少
        else:
            # 首先判断是否已经猜出正确答案
            if is_word_guessed(secret_word, letters_guessed):
                print('Congratulations, you won!')
                unique = count_secret_word(secret_word)
                score = unique * (num)
                print('You total score for this game is :', score)
                os._exit(0)
            # 还没有猜出答案
            else:
                print('You have ', num, ' guesses left.')
                print('Available letters: ', get_available_letters(letters_guessed))
                in_word = input('Please guess a letter:')
                warn_new = test_inword(in_word, warn, letters_guessed)
                if warn_new < warn:
                    warn = warn_new
                    print(' You have no warnings left so you lose one guess',
                          get_guessed_word(secret_word, letters_guessed))
                    num -= 1
                    print('----------------------------')
                else:
                    letters_guessed.append(in_word)
                    if in_word in secret_word:
                        print('Good guess:', get_guessed_word(secret_word, letters_guessed))
                        print('----------------------------')

                    else:
                        if in_word in vowel_list:
                            print('Oops! That word is not in my word, meanwhile, that a Vowel, you will lose two guesses:',
                                  get_guessed_word(secret_word, letters_guessed))
                            num -= 2
                            print('----------------------------')
                        else:
                            print(
                                'Oops! That word is not in my word, meanwhile, that a Consonants, you will lose one guess:',
                                get_guessed_word(secret_word, letters_guessed))
                            num -= 1
                            print('----------------------------')
    else:
        print('Sorry, you run out of guesses. The word was ', secret_word)
        os._exit(0)



# When you've completed your hangman function, scroll down to the bottom
# of the file and uncomment the first two lines to test
#(hint: you might want to pick your own
# secret_word while you're doing your own testing)


# -----------------------------------
#判断输入的字符是否是字母，是否出现过(是否是元音),多传输过来一个可以进行判断*的分支
##配合具有*触发hits的功能

def test_inword(in_word, warn, letters_guessed,guessed_word):
    word = in_word.lower()
    my_word = guessed_word
    if word.isalpha():
        if word in letters_guessed:
            print('Oops! You\'ve already guessed that letter.', end='')
            warn -= 1
        else:
            warn = warn
    else:
        if word == '*':
            print('Possible word matches are:')
            show_possible_matches(my_word)
            warn += 1
        else:
            warn -= 1
            print('Oops! That is not a vaild letter.', end='')
    return warn


##不具有*触发hits的功能
'''
def test_inword(in_word, warn, letters_guessed,guessed_word):
    word = in_word.lower()
    my_word = guessed_word
    if word.isalpha():
        if word in letters_guessed:
            print('Oops! You\'ve already guessed that letter.', end='')
            warn -= 1
        else:
            warn = warn
    else:
            warn -= 1
            print('Oops! That is not a vaild letter.', end='')
    return warn

'''



#计算输出的结果 成绩
def count_secret_word(secret_word):
    unique = []
    for i in range(len(secret_word)):
        secret_word.replace(secret_word[i], '')
        if secret_word[i] not in unique:
            unique.append(secret_word[i])
        else:
            continue
    return (len(unique))


def match_with_gaps(my_word, other_word):
    '''
    my_word: string with _ characters, current guess of secret word
    other_word: string, regular English word
    returns: boolean, True if all the actual letters of my_word match the
        corresponding letters of other_word, or the letter is the special symbol
        _ , and my_word and other_word are of the same length;
        False otherwise: 
    '''
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    if len(my_word.strip()) == len(other_word.strip()):
        for each in range(len(my_word)):
            if my_word[each] != '_':
                if my_word[each] == other_word[each]:
                    continue
                else:
                    return False
            else:
                continue
        return True
    else:
        return False


def show_possible_matches(my_word):
    '''
    my_word: string with _ characters, current guess of secret word
    returns: nothing, but should print out every word in wordlist that matches my_word
             Keep in mind that in hangman when a letter is guessed, all the positions
             at which that letter occurs in the secret word are revealed.
             Therefore, the hidden letter(_ ) cannot be one of the letters in the word
             that has already been revealed.

    '''
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    #利用上一个match_with_gaps的函数进行判断


    possible_words = []
    word_list = load_words1()
    my_word = my_word.replace(' ', '')
    for i in range(len(word_list)):
        other_word = word_list[i]
        if match_with_gaps(my_word, other_word):
                possible_words.append(word_list[i])
        else:
            continue
    for each in range(len(possible_words)):
        print(possible_words[each], end=' ')



'''
     ##不使用match_with_gaps
    num = 0
    possible_words = []
    word_list = load_words1()
    print(word_list)
    my_word = my_word.replace(' ', '')
    print(my_word)
    for i in range(len(word_list)):
        if len(my_word.strip()) == len(word_list[i].strip()):
            for j in range(len(my_word)):
                if my_word[j] == '_':
                    num = j
                    continue
                else:
                    if my_word[j] == word_list[i][j]:
                        num = j
                        continue
                    else:
                        break
            if (num + 1 ) == len(my_word):

                possible_words.append(word_list[i])
            else:
                continue
    print(possible_words)

'''







def hangman_with_hints(secret_word):
    '''
    secret_word: string, the secret word to guess.
    
    Starts up an interactive game of Hangman.
    
    * At the start of the game, let the user know how many 
      letters the secret_word contains and how many guesses s/he starts with.
      
    * The user should start with 6 guesses
    
    * Before each round, you should display to the user how many guesses
      s/he has left and the letters that the user has not yet guessed.
    
    * Ask the user to supply one guess per round. Make sure to check that the user guesses a letter
      
    * The user should receive feedback immediately after each guess 
      about whether their guess appears in the computer's word.

    * After each guess, you should display to the user the 
      partially guessed word so far.
      
    * If the guess is the symbol *, print out all words in wordlist that
      matches the current guessed word. 
    
    Follows the other limitations detailed in the problem write-up.
    '''
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    import os
    print(secret_word)
    num = 6
    letters_guessed = []
    warn = 3
    vowel_list = ['a', 'e', 'i', 'o', 'u']
    print('Welcome to the game Hangman!')
    print('I am thinking of a word that is ' + str(len(secret_word)) + ' letters long.')
    print('You have 3 warnings left')
    print('----------------------------')
    while num > 0:
        while warn > 0:
            # 首先判断是否已经猜出正确答案
            if is_word_guessed(secret_word, letters_guessed):
                print('Congratulations, you won!')
                unique = count_secret_word(secret_word)
                score = unique * (num)
                print('You total score for this game is :', score)
                os._exit(0)
            # 还没有猜出答案
            else:
                print('You have ', num, ' guesses left.')
                print('Available letters: ', get_available_letters(letters_guessed))
                in_word = input('Please guess a letter:')
                guessed_word = get_guessed_word(secret_word, letters_guessed)
                warn_new = test_inword(in_word, warn, letters_guessed, guessed_word)
                if warn_new > warn:
                    print('\n----------------------------')
                elif warn_new < warn:
                    warn = warn_new
                    print(' You have ', warn, 'warnings left:', get_guessed_word(secret_word, letters_guessed))
                    print('----------------------------')
                elif warn == warn_new:
                    letters_guessed.append(in_word)
                    if in_word in secret_word:
                        print('Good guess:', get_guessed_word(secret_word, letters_guessed))
                        print('----------------------------')
                    # 检查是否是元音
                    else:
                        if in_word in vowel_list:
                            print(
                                'Oops! That word is not in my word, meanwhile, that a Vowel, you will lose two guesses:',
                                get_guessed_word(secret_word, letters_guessed))
                            num -= 2
                            print('----------------------------')
                        else:
                            print(
                                'Oops! That word is not in my word, meanwhile, that a Consonants, you will lose one guess:',
                                get_guessed_word(secret_word, letters_guessed))
                            num -= 1
                            print('----------------------------')
        # warn 的3次机会使用完后，再次出现猜测问题则减少guess的机会，使得num减少
        else:
            # 首先判断是否已经猜出正确答案
            if is_word_guessed(secret_word, letters_guessed):
                print('Congratulations, you won!')
                unique = count_secret_word(secret_word)
                score = unique * (num)
                print('You total score for this game is :', score)
                os._exit(0)
            # 还没有猜出答案
            else:
                print('You have ', num, ' guesses left.')
                print('Available letters: ', get_available_letters(letters_guessed))
                in_word = input('Please guess a letter:')
                guessed_word = get_guessed_word(secret_word, letters_guessed)
                warn_new = test_inword(in_word, warn, letters_guessed, guessed_word)
                if warn_new < warn:
                    warn = warn_new
                    print(' You have no warnings left so you lose one guess',
                          get_guessed_word(secret_word, letters_guessed))
                    num -= 1
                    print('----------------------------')
                else:
                    letters_guessed.append(in_word)
                    if in_word in secret_word:
                        print('Good guess:', get_guessed_word(secret_word, letters_guessed))
                        print('----------------------------')

                    else:
                        if in_word in vowel_list:
                            print(
                                'Oops! That word is not in my word, meanwhile, that a Vowel, you will lose two guesses:',
                                get_guessed_word(secret_word, letters_guessed))
                            num -= 2
                            print('----------------------------')
                        else:
                            print(
                                'Oops! That word is not in my word, meanwhile, that a Consonants, you will lose one guess:',
                                get_guessed_word(secret_word, letters_guessed))
                            num -= 1
                            print('----------------------------')
    else:
        print('Sorry, you run out of guesses. The word was ', secret_word)
        os._exit(0)


# When you've completed your hangman_with_hint function, comment the two similar
# lines above that were used to run the hangman function, and then uncomment
# these two lines and run this file to test!
# Hint: You might want to pick your own secret_word while you're testing.

#为了在使用*显示出其余内容的时候不再有：Loading word list from file... 和"  ", len(wordlist), "words loaded."，故写一个新的
def load_words1():
    """
    Returns a list of valid words. Words are strings of lowercase letters.

    Depending on the size of the word list, this function may
    take a while to finish.
    """

    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r')
    # line: string
    line = inFile.readline()
    # wordlist: list of strings
    wordlist = line.split()

    return wordlist

if __name__ == "__main__":
    # pass

    # To test part 2, comment out the pass line above and
    # uncomment the following two lines.

    #secret_word = choose_word(wordlist)
    #hangman(secret_word)



###############
    
    # To test part 3 re-comment out the above lines and 
    # uncomment the following two lines. 
    #Hits的方法是具有*触发提示的功能

    secret_word = choose_word(wordlist)
    hangman_with_hints(secret_word)

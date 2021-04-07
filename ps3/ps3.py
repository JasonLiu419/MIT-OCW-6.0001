# 6.0001 Problem Set 3
#
# The 6.0001 Word Game
# Created by: Kevin Luu <luuk> and Jenna Wiens <jwiens>
#
# Name          : <Yuyang Liu>
# Collaborators : <your collaborators>
# Time start    : <20210330>

import math
import random
import string

VOWELS = 'aeiou'
CONSONANTS = 'bcdfghjklmnpqrstvwxyz'
HAND_SIZE = 7
LETTER = 'aeioubcdfghjklmnpqrstvwxyz'
HAND_SIZE = 7
#SCRABBLE_LETTER_VALUES:recording the scores of each letter

SCRABBLE_LETTER_VALUES = {
    'a': 1, 'b': 3, 'c': 3, 'd': 2, 'e': 1, 'f': 4, 'g': 2, 'h': 4, 'i': 1, 'j': 8, 'k': 5, 'l': 1, 'm': 3, 'n': 1, 'o': 1, 'p': 3, 'q': 10, 'r': 1, 's': 1, 't': 1, 'u': 1, 'v': 4, 'w': 4, 'x': 8, 'y': 4, 'z': 10
}

# -----------------------------------
# Helper code
# (you don't need to understand this helper code)

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
    # wordlist: list of strings
    wordlist = []
    for line in inFile:
        wordlist.append(line.strip().lower())
    print("  ", len(wordlist), "words loaded.")
    return wordlist

def get_frequency_dict(sequence):

    """
    输入一个字符串，输出每个字符串中的单词对应的出现次数

    Returns a dictionary where the keys are elements of the sequence
    and the values are integer counts, for the number of times that
    an element is repeated in the sequence.

    sequence: string or list
    return: dictionary
    """
    
    # freqs: dictionary (element_type -> int)
    freq = {}
    for x in sequence:
        freq[x] = freq.get(x,0) + 1
        # 这里不是递归，freq[x]就是新建一个字典中的元素 x ,之后对于这个元素进行赋值
    return freq
	

# (end of helper code)
# -----------------------------------

#
# Problem #1: Scoring a word
#
def get_word_score(word, n):
    """
    Returns the score for a word. Assumes the word is a
    valid word.

    You may assume that the input word is always either a string of letters, 
    or the empty string "". You may not assume that the string will only contain 
    lowercase letters, so you will have to handle uppercase and mixed case strings 
    appropriately. 

	The score for a word is the product of two components:

	The first component is the sum of the points for letters in the word.
	The second component is the larger of:
            1, or
            7*wordlen - 3*(n-wordlen), where wordlen is the length of the word
            and n is the hand length when the word was played

	Letters are scored as in Scrabble; A is worth 1, B is
	worth 3, C is worth 3, D is worth 2, E is worth 1, and so on.

    word: string
    n: int >= 0
    returns: int >= 0
    """
    
   # pass # TO DO... Remove this line when you implement this function


    first_component = 0
    in_word = word.lower()
    word_length = len(in_word)

    for i in range(word_length):
        first_component += SCRABBLE_LETTER_VALUES.get(in_word[i], 0)
    test_score = (7 * word_length) - 3 * (n - word_length)
    if test_score > 1:
        second_component = test_score
    else:
        second_component = 1
    score = first_component * second_component
    return score




#
# Make sure you understand how this function works and what it does!
#
def display_hand(hand):
    """
    实现的目的就是：
    For example:
       display_hand({'a':1, 'x':2, 'l':3, 'e':1})
    Should print out something like:
       a x x l l l e


    Displays the letters currently in the hand.

    For example:
       display_hand({'a':1, 'x':2, 'l':3, 'e':1})
    Should print out something like:
       a x x l l l e
    The order of the letters is unimportant.

    hand: dictionary (string -> int)
    """
    
    for letter in hand.keys():
        # hand.keys()：取出字典hand里面的单词，形成一个新的字典集
        for j in range(hand[letter]):
            # 获取每一个单词后对应的key值，即打印出来的次数
             print(letter, end=' ')      # print all on the same line
    print()                              # print an empty line

#
# Make sure you understand how this function works and what it does!
# You will need to modify this for Problem #4.
#
def deal_hand(n):
    """
    Returns a random hand containing n lowercase letters.
    ceil(n/3) letters in the hand should be VOWELS (note,
    ceil(n/3) means the smallest integer not less than n/3).

    Hands are represented as dictionaries. The keys are
    letters and the values are the number of times the
    particular letter is repeated in that hand.

    n: int >= 0
    returns: dictionary (string -> int)
    """
    
    hand={}
    num_vowels = int(math.ceil(n / 3))
    # math.ceil():向上取整，括号内的内容含义是>=（）的数值，math.cell(3.5) = 4

    for i in range(num_vowels-1):
        x = random.choice(VOWELS)
        hand[x] = hand.get(x, 0) + 1
    hand['*'] = 1
    for i in range(num_vowels, n):    
        x = random.choice(CONSONANTS)
        hand[x] = hand.get(x, 0) + 1
    
    return hand

#
# Problem #2: Update a hand by removing letters
#
def update_hand(hand, word):
    """
    Does NOT assume that hand contains every letter in word at least as
    many times as the letter appears in word. Letters in word that don't
    appear in hand should be ignored. Letters that appear in word more times
    than in hand should never result in a negative count; instead, set the
    count in the returned hand to 0 (or remove the letter from the
    dictionary, depending on how your code is structured). 

    Updates the hand: uses up the letters in the given word
    and returns the new hand, without those letters in it.

    Has no side effects: does not modify hand.

    word: string
    hand: dictionary (string -> int)    
    returns: dictionary (string -> int)
    """

    # TO DO... Remove this line when you implement this function
    # 获取hand中展开的字母组成的列表 成为list_hand_word

    new_hand = {}
    list_hand_word = []
    word = word.lower()
    for letter in hand.keys():
        # hand.keys()：取出字典hand里面的单词，形成一个新的字典集
        for j in range(hand[letter]):
            # 获取每一个单词后对应的key值，即打印出来的次数
            list_hand_word.append(letter)
    # 判断对于word中的单词在hand中的存在情况，存在的话list中内容相应减少为new_hand做准备，不存在的话list的值相应减少（error）
    for each in range(len(word)):
        if word[each] in list_hand_word:
            list_hand_word.remove(word[each])
        else:
            if hand[word[each]] > 0:
                hand[word[each]] -= 1
            else:
                continue
    new_hand = get_frequency_dict(list_hand_word)
    return new_hand




#
# Problem #3: Test word validity
#
def is_valid_word(word, hand, word_list):
    """
    Returns True if word is in the word_list and is entirely
    composed of letters in the hand. Otherwise, returns False.
    Does not mutate hand or word_list.
   
    word: string
    hand: dictionary (string -> int)
    word_list: list of lowercase strings
    returns: boolean
    """

    # TO DO... Remove this line when you implement this function

    def generate_words_replacing_wildcard_with_vowels(word):
        list_of_word = []
        for vowel in VOWELS:
            index_of_wildcard = word.find('*')

            new_word = word[0:index_of_wildcard] + vowel
            if index_of_wildcard < len(word) - 1:
                new_word += word[index_of_wildcard + 1:]

            list_of_word.append(new_word.lower())

        return list_of_word

    # 检查word或者*替换后的word是否在word_list中
    if '*' in word:
        words_that_replace_wildcard = generate_words_replacing_wildcard_with_vowels(word)
        if_the_generated_words_is_in_dictionary = False

        for w in words_that_replace_wildcard:
            if w.lower() in word_list:
                if_the_generated_words_is_in_dictionary = True
                break
        if if_the_generated_words_is_in_dictionary:
            return True
        else:
            return False


    else:
    # 如果word中没有*
        # 检查word是否每个元素都在hand中
        list_hand_word = []
        word = word.lower()
        for letter in hand.keys():
            # hand.keys()：取出字典hand里面的单词，形成一个新的字典集
            for j in range(hand[letter]):
                # 获取每一个单词后对应的key值，即打印出来的次数
                list_hand_word.append(letter)
        if word in word_list:
            for each in word:
                if each in list_hand_word:
                    list_hand_word.remove(each)
                    # 在数量不足的情况下也应该报错
                    continue
                else:
                    return False
            return True
        else:
            return False
    '''
     hand_copy = hand.copy()
    for char in word.lower():
        if char not in hand_copy.keys():
            return False
        else:
            hand_copy[char] -= 1
            if hand_copy[char] < 0:
                return False
    '''


    # if it got to this point (e.g. it passed all tests of validity), then it is a valid word
    #return True

# 获取*用vowel代替后，在列表中的实际存在word
def generate_words_replacing_wildcard_with_vowels_inlist(word, word_list):

    list_of_word = []
    for vowel in VOWELS:
        index_of_wildcard = word.find('*')

        new_word = word[0:index_of_wildcard] + vowel + word[index_of_wildcard + 1:]

        if new_word in word_list:
            list_of_word.append(new_word.lower())
        else:
            continue
    return list_of_word


#
# Problem #5: Playing a hand
#
def calculate_handlen(hand):
    """ 
    Returns the length (number of letters) in the current hand.
    
    hand: dictionary (string-> int)
    returns: integer
    """

    # TO DO... Remove this line when you implement this function
    number_of_letters = 0
    for value in hand.values():
        # hand.keys() 用于提取hand这个字典类型中元素情况     hand.values()用于提取hand这个字典类型中取值情况
        number_of_letters += value

    return number_of_letters



def play_hand(hand, word_list):

    """
    Allows the user to play the given hand, as follows:

    * The hand is displayed.
    
    * The user may input a word.

    * When any word is entered (valid or invalid), it uses up letters
      from the hand.

    * An invalid word is rejected, and a message is displayed asking
      the user to choose another word.

    * After every valid word: the score for that word is displayed,
      the remaining letters in the hand are displayed, and the user
      is asked to input another word.

    * The sum of the word scores is displayed when the hand finishes.

    * The hand finishes when there are no more unused letters.
      The user can also finish playing the hand by inputing two 
      exclamation points (the string '!!') instead of a word.

      hand: dictionary (string -> int)
      word_list: list of lowercase strings
      returns: the total score for the hand
      
    """
    
    # BEGIN PSEUDOCODE <-- Remove this comment when you implement this function
    # Keep track of the total score
    a = 0
    total_score = 0
    # As long as there are still letters left in the hand:
    while calculate_handlen(hand) > 0:
        # Display the hand
        print('Current Hand:', end='')
        display_hand(hand)
        # Ask user for input
        in_word = input('Enter word, or "!!" to indicate that you are finished:')
        # If the input is two exclamation points:
        if in_word == '!!':
            # End the game (break out of the loop)

            break
            
        # Otherwise (the input is not two exclamation points):
        else:
            # If the word is valid:
            if is_valid_word(in_word, hand, word_list):
                # Tell the user how many points the word earned,
                n = len(in_word)
                print("\"%s\""%in_word, 'earned ', get_word_score(in_word, n), 'points', end=' ')
                # 每次结束加一个换行

                # and the updated total score
                total_score += get_word_score(in_word, n)
                print('Total:', total_score, 'points')
                print()
            # Otherwise (the word is not valid):
                # Reject invalid word (print a message)
            else:
                print('That is not a valid word. Please choose another word.')
            # update the user's hand by removing the letters of their inputted word
            hand = update_hand(hand, in_word)

    # Game is over (user entered '!!' or ran out of letters),

    else:
        print()
        print('Ran out of letters.', "Total score:", total_score, 'points')
    # so tell user the total score
    # Return the total score as result of function
    return total_score


#
# Problem #6: Playing a game
# 


#
# procedure you will use to substitute a letter in a hand
#

def substitute_hand(hand, letter):
    """ 
    Allow the user to replace all copies of one letter in the hand (chosen by user)
    with a new letter chosen from the VOWELS and CONSONANTS at random. The new letter
    should be different from user's choice, and should not be any of the letters
    already in the hand.

    If user provide a letter not in the hand, the hand should be the same.

    Has no side effects: does not mutate hand.

    For example:
        substitute_hand({'h':1, 'e':1, 'l':2, 'o':1}, 'l')
    might return:
        {'h':1, 'e':1, 'o':1, 'x':2} -> if the new letter is 'x'
    The new letter should not be 'h', 'e', 'l', or 'o' since those letters were
    already in the hand.
    
    hand: dictionary (string -> int)
    letter: string
    returns: dictionary (string -> int)
    """
    
    # TO DO... Remove this line when you implement this function
    hand_copy = hand.copy()
    value = hand[letter]
    get_random_letter = random.choice(LETTER)
    # 找到一个不在hand中的任意字母
    while True:
        if get_random_letter not in hand_copy:
            break
        else:
            get_random_letter = random.choice(LETTER)
    # 替换掉选中的letter
    hand_copy.pop(letter)
    hand_copy.update({get_random_letter: value})
    return hand_copy



       
    
def play_game(word_list):
    """
    Allow the user to play a series of hands

    * Asks the user to input a total number of hands

    * Accumulates the score for each hand into a total score for the 
      entire series
 
    * For each hand, before playing, ask the user if they want to substitute
      one letter for another. If the user inputs 'yes', prompt them for their
      desired letter. This can only be done once during the game. Once the
      substitue option is used, the user should not be asked if they want to
      substitute letters in the future.

    * For each hand, ask the user if they would like to replay the hand.
      If the user inputs 'yes', they will replay the hand and keep 
      the better of the two scores for that hand.  This can only be done once 
      during the game. Once the replay option is used, the user should not
      be asked if they want to replay future hands. Replaying the hand does
      not count as one of the total number of hands the user initially
      wanted to play.

            * Note: if you replay a hand, you do not get the option to substitute
                    a letter - you must play whatever hand you just had.
      
    * Returns the total score for the series of hands

    word_list: list of lowercase strings
    """
    
    # TO DO... Remove this line when you implement this function
    # 输入hands的长度大小
    number_of_hands = int(input('Enter total number of hands'))
    total_score = 0
    judge = 0
    judge_new = 0
    while number_of_hands > 0:
        if judge == judge_new:
            # 打印 生成的hand
            hand = deal_hand(HAND_SIZE)
        else:
            judge = judge
            hand = hand
        print('Current hand:', end='')
        display_hand(hand)
        # 判断是否想要替换letter
        judge_letter = str(input('Would you like to substitute a letter'))
        print()
        if judge_letter == 'no':
            round_score = play_hand(hand, word_list)
        else:
            replace_letter = str(input('Which letter would you like to replace:'))
            round_score = play_hand(substitute_hand(hand, replace_letter), word_list)
        print('Total score for this hand: ', round_score)
        print('------------------------------------------------')
        total_score += round_score
        number_of_hands -= 1
        if number_of_hands > 0:
            judge_replay = str(input('Would you like to replay the hand?'))
            print()
        if judge_replay == 'yes':
            judge_new = judge + 1


    print('Total score over all hands:', total_score)


#
# Build data structures used for entire session and play game
# Do not remove the "if __name__ == '__main__':" line - this code is executed
# when the program is run directly, instead of through an import statement
#
if __name__ == '__main__':
    word_list = load_words()
    play_game(word_list)

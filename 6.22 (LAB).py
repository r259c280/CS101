# Type all other functions here
#shorten_space() function.
def shorten_space(usrStr):
    split = usrStr.split()
    return ( " ".join(split) )
#replace_punctuation() function.
def replace_punctuation(usrStr):
    return usrStr.count("!"), usrStr.count(";"), usrStr.replace("!",".").replace(";",",")
#fix_capitilization() function.   
def fix_capitilization(usrStr):
    numberOfSentencesCapitalized = 0
    sentences = usrStr.split('.')   
    # looping through sentence list so we can modify the sentence in the collection
    for number in range(len(sentences ) ):
        sentence = sentences[number]
        # don't process the empty string if sentence ends with .
        if len( sentence ) > 0:
            # loops throug string so we can find the first non space
            for index in range(len(sentence) ):
                if not sentence[index].isspace():
                    # first non space character, fix or not
                    if not sentence[index].isupper():
                        sentences[number] = sentence[:index] + sentence[index].upper() + sentence[index + 1:]
                        numberOfSentencesCapitalized += 1                       
                    #break out of the range loop so we don't capitialize anything else
                    break
    capitalizedString = ".".join(sentences)
    return numberOfSentencesCapitalized, capitalizedString
def get_num_of_words(usrStr):
    return len( usrStr.split() )
#print_menu() to frint the menu.
def print_menu(usrStr):
   print( 'You entered:', usrStr )
   validOptions = ( 'c', 'w', 'f', 'r', 's', 'q' )
   menuOp = ' '
   while menuOp not in validOptions:
       print('MENU')
       print('c - Number of non-whitespace characters')
       print('w - Number of words')
       print('f - Fix capitalization')
       print('r - Replace punctuation')
       print('s - Shorten spaces')
       print('q - Quit')
       print()
       print('Choose an option: ')
       menuOp = input()
       if menuOp == 'c':
           print('Number of non-whitespace characters: %d' % get_num_of_non_WS_characters(usrStr) )
       elif menuOp == 'w':
           print( 'Number of words: %d' % get_num_of_words(usrStr) )
       elif menuOp == 'f':
           print( 'Number of letters capitalized: %d\nEdited text: %s' % fix_capitilization(usrStr) )
       elif menuOp == 'r':
           print( 'Punctuation replaced\nexclamationCount: %d\nsemicolonCount: %d\nEdited text: %s' % replace_punctuation(usrStr) )
       elif menuOp == 's':
            print( 'Edited text: %s' % shorten_space(usrStr) )
   return menuOp, usrStr
#get_num_of_non_WS_characters() function
def get_num_of_non_WS_characters(userInput):
    numberOfNonWhiteSpaceCharacters = 0
    for character in userInput:
        if not character.isspace():
            numberOfNonWhiteSpaceCharacters += 1
    return numberOfNonWhiteSpaceCharacters
if __name__ == '__main__':
    # Complete main section of code
    menuOption = ''
    userInput = input('Enter a sample text: ')
    while ( menuOption != 'q' ):
        menuOption, userInput = print_menu(userInput)

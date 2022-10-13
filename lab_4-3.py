#author: RED 10/13/22
# set my variables
first_word_first_letter = input("Who asked me to do this?")
second_word_first_letter = input("How do you do this?")

#if statements
if first_word_first_letter < second_word_first_letter:
    print('First letter of first word comes before in alphabet')
elif first_word_first_letter > second_word_first_letter:
    print('First letter of frist word comes after in the alphabet')
else:
    print('They are the same letter')

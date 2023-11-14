"""
As a user
So that I can manage my time
I want to see an estimate of reading time for a text, assuming that I can read 200 words a minute.
"""

"""
function - speed_reader()
take in some text as an argument
count the words in that text
divide that word count by 200 to get minutes (* 60 to get seconds?)
return that number ( maybe in an easy to read format?) - 
e.g 'It will take you approximately {number} minutes to read this text

def speed_reader(text):
    input - text from a document etc
    return:
        a float representing the time / formatted string

"""


def speed_reader(text):
    words = text.split()
    word_count = len(words)
    return word_count / 200

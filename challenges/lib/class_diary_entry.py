import math


class DiaryEntry:
    def __init__(self, title, contents):
        if title == "" or contents == "":
            raise Exception("Missing Data!")
        self.title = title
        self.contents = contents
        self.words_read_so_far = 0

    def format(self):
        return f"{self.title}: {self.contents}"

    def count_words(self):
        words = self.format().split()
        return len(words)

    def reading_time(self, wpm):
        if wpm == 0:
            raise Exception("Unable to calculate reading time. Please re-enter.")
        number_of_words = len(self.contents.split())
        return math.ceil(number_of_words / wpm)

    def reading_chunk(self, wpm, minutes):
        # work out how many words user can read per minute
        words_user_can_read = wpm * minutes
        # split the content into single words
        words = self.contents.split()
        if self.words_read_so_far >= len(words):
            self.words_read_so_far = 0
        # mark the start of the chunk as the word at the index after
        # the last word read - default is index 0
        chunk_start = self.words_read_so_far
        # mark the end of the chunk at the index of the word
        # the user can read up to
        chunk_end = self.words_read_so_far + words_user_can_read
        # create a chunk of the words between those two
        chunk_words = words[chunk_start:chunk_end]
        # set the new start of the chunk at that point for the next repetition
        self.words_read_so_far = chunk_end
        # return the 'chunk' as a string
        return " ".join(chunk_words)

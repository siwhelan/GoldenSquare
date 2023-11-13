def count_words(text):
    words = text.split()
    if len(words) > 0:
        return len(words)
    else:
        return ""

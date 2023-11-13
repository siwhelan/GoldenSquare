# A function called make_snippet that takes a string as an argument and
# returns the first five words and then a '...' if there are more than that.


def make_snippet(string):
    words = string.split(" ")
    if len(words) <= 5:
        return " ".join(words)
    else:
        return " ".join(words[:5]) + " ..."

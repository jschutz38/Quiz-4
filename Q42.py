#authors' name is Julia Schutz
def count_substring(string, hashtag):
    index = 0
    total = 0
    while index < len(string):
        if string[index: index + len(hashtag)] == hashtag:
            total += 1
            index += len(hashtag)
        else:
            index += 1
    return total
m = count_substring("I like # because # to # and #", "#")
def hash_spam():
    if m >= 4:
        print("This tweet will be considered as a spam!")
    else:
        print("None")
hash_spam()

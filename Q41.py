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


count_substring("I like to use a # in every sentence because #'s are cool #.", "#")

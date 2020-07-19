def no_dups(s):
    # Your code here
    new_string = ""

    if len(s) == 0:
        return new_string
    else:

        uncounted = s.split()
        found_words = dict.fromkeys(uncounted)

        # print(uncounted)

        # print(list(found_words))
        step = 1
        for key in list(found_words):
            if step == 1:
                new_string = key
            else:
                new_string = new_string + " " + key
            step += 1
        return new_string

        # for word in uncounted:
        #     if word not in found_words:
        #         found_words[word] = 1


if __name__ == "__main__":
    print(no_dups(""))
    print(no_dups("hello"))
    print(no_dups("hello hello"))
    print(no_dups("cats dogs fish cats dogs"))
    print(no_dups("spam spam spam eggs spam sausage spam spam and spam"))

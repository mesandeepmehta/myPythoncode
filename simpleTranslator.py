#this program replaces each vovel by g

def translate(phrase):
    word=""
    for letter in phrase:
        if letter in "aeiouAEIOU":
            word = word + "g"
        else:
            word = word + letter
    return word
print(translate("make me move"))

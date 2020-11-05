from isbnlib import isbn_from_words, meta, classify

s = isbn_from_words("I'm Nobody! Who Are You?: Poems of Emily Dickinson for Children (Poetry for Young People Series)")

print(s)
print(classify(s))
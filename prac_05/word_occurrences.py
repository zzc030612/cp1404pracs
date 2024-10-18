# this is a collection of words of nice words this is a fun thing it is

text = input("Text: ")
words = text.split(" ")

max_string_length = max(len(word) for word in words)
max_occurrence_length = max(len(str(words.count(word))) for word in words)

for word in sorted(set(words)):
    print(f"{word:{max_string_length}} : {words.count(word):{max_occurrence_length}}")

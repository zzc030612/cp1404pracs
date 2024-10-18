# this is a collection of words of nice words this is a fun thing it is

string = input("Text: ")
strings = string.split(" ")

max_string_length = max(len(string) for string in strings)
max_occurrence_length = max(len(str(strings.count(string))) for string in strings)

for string in sorted(set(strings)):
    print(f"{string:{max_string_length}} : {strings.count(string):{max_occurrence_length}}")

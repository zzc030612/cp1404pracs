# this is a collection of words of nice words this is a fun thing it is

string = input("Text: ")
strings = string.split(" ")
comparing_strings = set(strings)

max_string_length = max(len(string) for string in comparing_strings)
max_occurrence_length = max(len(str(strings.count(string))) for string in comparing_strings)

for string in sorted(comparing_strings):
    print(f"{string:{max_string_length}} : {strings.count(string):{max_occurrence_length}}")

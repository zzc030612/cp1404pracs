"""
Time started: 9:35
Time finished: 10:37
"""

from prac_06.programming_language import ProgrammingLanguage

programming_languages = [ProgrammingLanguage("Python", "Dynamic", True, 1991),
                         ProgrammingLanguage("Ruby", "Dynamic", True, 1995),
                         ProgrammingLanguage("Visual Basic", "Static", False, 1991)]

print("The dynamically typed languages are:")
dynamic_languages = [programming_language.language for programming_language in programming_languages if
                     programming_language.is_dynamic()]
print("\n".join(dynamic_languages))

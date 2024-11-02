"""
Time started: 9:35
Time finished: 10:37
"""


class ProgrammingLanguage:
    def __init__(self, language="", typing="", reflection="", year=0):
        """Initialise variables"""
        self.language = language
        self.typing = typing
        self.reflection = reflection
        self.year = year

    def __str__(self):
        """Return a string representation of the object"""
        return f"{self.language}, {self.typing} Typing, Reflection={self.reflection}, First appeared in {self.year}"

    def is_dynamic(self):
        """Check if the language is dynamic"""
        return self.typing == "Dynamic"

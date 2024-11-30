"""
Programming Language
Estimate:   20 minutes
Start Time: 2235
End Time:   2249
Time Taken: 14 minutes
"""


class ProgrammingLanguage:
    """Represent a Programming Language object."""

    def __init__(self, name, typing, reflection, year):
        """Initialise a Programming Language instance.

        name: string
        typing: string
        reflection: boolean
        year: int
        """
        self.name = name
        self.typing = typing
        self.reflection = reflection
        self.year = year

    def __str__(self):
        """String to represent a Programming Language instance."""
        return f"{self.name}, {self.typing} Typing, Reflection={self.reflection}, First appeared in {self.year}"

    def is_dynamic(self):
        """Determine if a Programming Language is dynamic."""
        return self.typing == "Dynamic"

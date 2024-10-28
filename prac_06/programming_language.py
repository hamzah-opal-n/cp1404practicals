"""
Programming Language
Estimate:   20 minutes
Start Time: 2235
End Time:   22xx
Time Taken: ?? minutes
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

    def is_dynamic(self):
        """Determine if a Programming Language is dynamic."""
        return self.typing == "Dynamic"

"""Band class for CP1404"""


class Band:
    """Band class"""

    def __init__(self, name=""):
        """Construct a Band with a name and empty list of members."""
        self.name = name
        self.members = []

    def __str__(self):
        """Return a string representation of a Band."""
        member_strings = []
        for member in self.members:
            member_strings.append(str(member))
        return f"{self.name} ({', '.join(member_strings)})"

    def __repr__(self):
        """Return a string representation of a Band, showing the variables."""
        return str(vars(self))

    def add(self, member):
        """Add a member to the band."""
        self.members.append(member)

    def play(self):
        """Return a string showing the band members playing their first (or no) instrument."""
        if not self.members:
            return f"{self.name} has no band members!"
        play_strings = []
        for member in self.members:
            play_strings.append(member.play())
        return "\n".join(play_strings)

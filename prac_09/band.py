class Band:
    """A band that has multiple musicians (association)."""

    def __init__(self, name):
        """Initialise a Band with a name and an empty list of members."""
        self.name = name
        self.members = []

    def add(self, musician):
        """Add a musician to the band."""
        self.members.append(musician)

    def play(self):
        """Simulate the band playing by calling play() on each musician."""
        for member in self.members:
            member.play()

    def __str__(self):
        """Return string representation of the band with its members."""
        member_strs = ", ".join(str(member) for member in self.members)
        return f"{self.name} ({member_strs})"

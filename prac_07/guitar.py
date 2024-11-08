"""Guitar Class."""


class Guitar:
    """Define Guitar class."""

    def __init__(self, name="", year=0, cost=0):
        """Initialise guitar instance."""
        self.name = name
        self.year = year
        self.cost = cost

    def __str__(self):
        """Return string version of guitar instance."""
        return f"{self.name} ({self.year}) : ${self.cost}"

    def __repr__(self):
        """Return string version of guitar instance."""
        return f"{self.name} ({self.year}) : ${self.cost}"

    def __lt__(self, other):
        """Determine if guitar instances are less than others."""
        return self.year < other.year

    def get_age(self):
        """Get age of guitar instance."""
        return 2024 - self.year

    def is_vintage(self):
        """Get if guitar instance is vintage."""
        return self.get_age() > 50

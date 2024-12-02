class Place:
    """Represents a place with name, country, priority, and visited status."""

    def __init__(self, name: str, country: str, priority: int, visited: bool = False):
        """
        Initialize a Place object.
        :param name: Name of the place.
        :param country: Country where the place is located.
        :param priority: Priority of the place (lower is more important).
        :param visited: Whether the place has been visited (default: False).
        """
        self.name = name
        self.country = country
        self.priority = priority
        self.visited = visited

    def __str__(self):
        """Return a string representation of the place."""
        status = "visited" if self.visited else "not visited"
        return f"{self.name} in {self.country}, priority {self.priority} ({status})"

    def mark_as_visited(self):
        """Mark the place as visited."""
        self.visited = True

    def mark_as_unvisited(self):
        """Mark the place as not visited."""
        self.visited = False

    def is_important(self):
        """
        Determine if the place is considered important.
        A place is important if its priority is 2 or less.
        :return: True if the place is important, False otherwise.
        """
        return self.priority <= 2

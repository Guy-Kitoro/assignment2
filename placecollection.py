import json
from place import Place  # Import the Place class

class PlaceCollection:
    """Manages a collection of Place objects."""

    def __init__(self):
        """Initialize a PlaceCollection object."""
        self.places = []

    def load_places(self, filename: str):
        """
        Load places from a JSON file into the collection.
        :param filename: The name of the JSON file to load.
        """
        with open(filename, "r") as file:
            data = json.load(file)
            self.places = [Place(**item) for item in data]

    def save_places(self, filename: str):
        """
        Save all places in the collection to a JSON file.
        :param filename: The name of the JSON file to save to.
        """
        with open(filename, "w") as file:
            json.dump([place.__dict__ for place in self.places], file, indent=4)

    def add_place(self, place: Place):
        """
        Add a new Place to the collection.
        :param place: The Place object to add.
        """
        self.places.append(place)

    def get_number_of_unvisited_places(self):
        """
        Get the number of unvisited places in the collection.
        :return: The count of unvisited places.
        """
        return sum(1 for place in self.places if not place.visited)

    def sort(self, key: str):
        """
        Sort places by a specified key (attribute).
        :param key: The attribute to sort by (e.g., 'name', 'country', 'priority').
        """
        self.places.sort(key=lambda place: getattr(place, key))

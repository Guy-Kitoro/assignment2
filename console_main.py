from place import Place
from placecollection import PlaceCollection

def main():
    """Test the Place and PlaceCollection classes."""
    # Create some places
    place1 = Place("Paris", "France", 1)
    place2 = Place("Tokyo", "Japan", 3, visited=True)
    place3 = Place("Cairns", "Australia", 2)

    print("Testing Place class:")
    print(place1)
    print(place2)
    print(place3)
    place1.mark_as_visited()
    print("After marking Paris as visited:", place1)
    print("Is Cairns important?", place3.is_important())

    # Test PlaceCollection class
    print("\nTesting PlaceCollection class:")
    collection = PlaceCollection()
    collection.add_place(place1)
    collection.add_place(place2)
    collection.add_place(place3)
    print(f"Number of unvisited places: {collection.get_number_of_unvisited_places()}")

    # Sort places by name and print
    collection.sort("name")
    print("Places sorted by name:")
    for place in collection.places:
        print(place)

    # Save and load places
    print("\nSaving and loading places from file:")
    collection.save_places("places.json")
    collection.load_places("places.json")
    for place in collection.places:
        print(place)

if __name__ == "__main__":
    main()

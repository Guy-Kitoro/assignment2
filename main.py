from kivy.app import App
from kivy.lang import Builder
from kivy.uix.button import Button
from placecollection import PlaceCollection
from place import Place

KV = """
BoxLayout:
    orientation: "vertical"
    BoxLayout:
        size_hint_y: None
        height: "40dp"
        Spinner:
            id: sort_spinner
            text: "Sort by"
            values: ["name", "country", "priority", "visited"]
            on_text: app.sort_places(self.text)
        TextInput:
            id: name_input
            hint_text: "Place Name"
        TextInput:
            id: country_input
            hint_text: "Country"
        TextInput:
            id: priority_input
            hint_text: "Priority"
        Button:
            text: "Add Place"
            on_press: app.add_place()
    ScrollView:
        GridLayout:
            id: places_layout
            cols: 1
            size_hint_y: None
            height: self.minimum_height
"""

class TravelTrackerApp(App):
    def build(self):
        self.title = "Travel Tracker 2.0"
        self.place_collection = PlaceCollection()
        self.place_collection.load_places("places.json")
        return Builder.load_string(KV)

    def sort_places(self, key):
        self.place_collection.sort(key)
        self.update_places()

    def add_place(self):
        name = self.root.ids.name_input.text
        country = self.root.ids.country_input.text
        try:
            priority = int(self.root.ids.priority_input.text)
            if priority <= 0:
                raise ValueError("Priority must be > 0")
            new_place = Place(name, country, priority)
            self.place_collection.add_place(new_place)
            self.update_places()
            self.clear_inputs()
        except ValueError:
            self.root.ids.priority_input.text = ""
            self.root.ids.priority_input.hint_text = "Invalid Priority"

    def clear_inputs(self):
        self.root.ids.name_input.text = ""
        self.root.ids.country_input.text = ""
        self.root.ids.priority_input.text = ""

    def update_places(self):
        layout = self.root.ids.places_layout
        layout.clear_widgets()
        for place in self.place_collection.places:
            button = Button(
                text=str(place),
                size_hint_y=None,
                height="40dp",
                background_color=(0, 1, 0, 1) if not place.visited else (1, 0, 0, 1),
                on_press=lambda instance, p=place: self.mark_place_visited(p)
            )
            layout.add_widget(button)

    def mark_place_visited(self, place):
        if not place.visited:
            place.mark_as_visited()
        else:
            place.mark_as_unvisited()
        self.update_places()

    def on_stop(self):
        self.place_collection.save_places("places.json")

if __name__ == "__main__":
    TravelTrackerApp().run()

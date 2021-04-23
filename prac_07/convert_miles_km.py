from kivy.app import App
from kivy.lang import Builder
from kivy.app import StringProperty

CONVERSION = 1.60934


class ConvertMtoKm(App):
    result = StringProperty()

    def build(self):
        self.title = "Convert Miles to Km"
        self.root = Builder.load_file("convert_miles_km.kv")
        return self.root

    def handle_convert(self, miles):
        miles = self.try_miles(miles)
        self.result = str(miles * CONVERSION)

    def handle_increment(self, value, miles):
        miles = self.try_miles(miles)
        self.root.ids.input_miles.text = str(miles + value)

    def try_miles(self, miles):
        try:
            miles = int(miles)
        except ValueError:
            miles = 0
        return miles


ConvertMtoKm().run()

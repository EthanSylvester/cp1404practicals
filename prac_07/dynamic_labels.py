from kivy.app import App
from kivy.lang import Builder
from  kivy.uix.label import Label


class DynamicLabels(App):
    def __init__(self):
        super().__init__()
        self.names = ["Ethan", "David", "Joel"]

    def build(self):
        self.title = "Dynamic Labels"
        self.root = Builder.load_file("dynamic_labels.kv")
        for name in self.names:
            temp_label = Label(text=name)
            self.root.ids.entries_box.add_widget(temp_label)
        return self.root


DynamicLabels().run()

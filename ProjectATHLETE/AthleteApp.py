import kivy
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput
from kivy.uix.dropdown import DropDown
from kivy.uix.button import Button
from kivy.uix.floatlayout import FloatLayout

import matplotlib.pyplot as plt
from kivy.garden.matplotlib.backend_kivyagg import FigureCanvasKivyAgg

class AthleteApp(App):
    def build(self):
        dropdown = DropDown()

        for item in ["60M", "100M", "200M", "400M"]:
            listbuton = Button(text=item, size_hint_y=None, height=44)
            dropdown.add_widget(listbuton)
        mainbutton = Button(text="Yarışlar", size_hint=(None, None))
        mainbutton.bind(on_release=dropdown.open)
        dropdown.bind(on_select=lambda instance, x: setattr(mainbutton, 'text', x))

        # Çizelge
        table = GridLayout(cols=3, rows=4, size_hint=(1, 0.4), pos_hint={'center_x': 0.5, 'center_y': 0.35})
        for i in range(12):
            label = Label(text=f'Hücre {i}')
            table.add_widget(label)

        # Grafik tablosu
        fig, ax = plt.subplots()
        ax.plot([1, 2, 3, 4, 5], [1, 2, 3, 4, 5])
        graph = FigureCanvasKivyAgg(fig)

        layout = FloatLayout()
        layout.add_widget(mainbutton)
        layout.add_widget(table)
        layout.add_widget(graph)
        mainbutton.pos_hint = {'center_x': 0.5, 'center_y': 0.92}

        return layout

if __name__ == "__main__":
    AthleteApp().run()

import kivy
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput



class SpartanGrid(GridLayout):
    def __init__(self,**kwargs):
        super(SpartanGrid, self).__init__()
        self.cols = 1
        self.add_widget((Label(text="Student Name:")))
        self.s_name = TextInput()
        self.add_widget(self.s_name)
class SpartanApp(App):
    def build(self):
        return SpartanGrid()
if __name__ == "__main__":
    SpartanApp().run()
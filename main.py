import kivy
from kivy.app import App
from kivy.uix.floatlayout import FloatLayout


class Interface(FloatLayout):

    def button_clicked(self):

        test_input_in_window=self.ids.first_textinput.text
        display_label=self.ids.first_label
        display_label.text=test_input_in_window

        return

    pass

class ProjectApp(App):

    pass
if __name__=="__main__":
    ProjectApp().run()

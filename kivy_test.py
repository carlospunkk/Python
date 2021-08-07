import kivy
from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout

kivy.require('1.9.1')

class btnApp(App):
    def build(self):
        box = BoxLayout()
        botao = Button(text='botao1')
        box.add_widget(botao)
        return box
btnApp().run()





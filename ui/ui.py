from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button

class ChatApp(App):
    def build(self):
        layout = BoxLayout(orientation='vertical')
        self.chat_log = Label(size_hint_y=8)
        layout.add_widget(self.chat_log)

        self.message_input = TextInput(size_hint_y=1, multiline=False)
        layout.add_widget(self.message_input)

        send_button = Button(text="Send", size_hint_y=1)
        send_button.bind(on_press=self.send_message)
        layout.add_widget(send_button)

        return layout

    def send_message(self, instance):
        message = self.message_input.text
        self.chat_log.text += f"\n{message}"
        self.message_input.text = ""

if __name__ == "__main__":
    ChatApp().run()

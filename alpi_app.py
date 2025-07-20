# alpi_app.py (All code in one file)

from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.lang import Builder
from kivy.core.window import Window

# જરૂરી લાઇબ્રેરીઓ
from gtts import gTTS
from kivy.core.audio import SoundLoader

# કીબોર્ડ દેખાય તે માટે
Window.softinput_mode = 'below_target'

# --- TTS Function (લખાણને અવાજમાં ફેરવવાનું કામ) ---
def speak(text):
    try:
        tts = gTTS(text=text, lang='gu')
        tts.save("response.mp3")
        sound = SoundLoader.load('response.mp3')
        if sound:
            sound.play()
    except Exception as e:
        print(f"TTS માં ભૂલ આવી: {e}")

# --- Command Logic (કમાન્ડને સમજવાનું કામ) ---
def process_command_logic(command):
    command_lower = command.lower() if command else ""
    
    if not command_lower:
        return "કૃપા કરીને કંઈક લખો."
    if "હવામાન" in command_lower or "weather" in command_lower:
        return "આજનું હવામાન સરસ અને વાદળછાયું છે જાનુ ❤️"
    elif "સંગીત" in command_lower or "music" in command_lower:
        return "તમારા માટે મનપસંદ સંગીત વગાડી રહી છું 🎶"
    elif "કેમ છો" in command_lower or "how are you" in command_lower:
        return "હું મજામાં છું, તમે કેમ છો?"
    else:
        return "માફ કરશો જાનુ, હું આ સમજી ન શકી 😔"

# --- Kivy App Layout (એપનો દેખાવ) ---
KV = """
BoxLayout:
    orientation: 'vertical'
    padding: 20
    spacing: 10
    Label:
        id: response_label
        text: "Alpi ને શું કહેવા માંગો છો?"
        font_size: '20sp'
        size_hint_y: 0.4
        halign: 'center'
    TextInput:
        id: command_input
        hint_text: 'અહીં તમારો કમાન્ડ લખો...'
        multiline: False
        font_size: '18sp'
        size_hint_y: 0.2
    Button:
        text: "પૂછો (Ask)"
        font_size: '20sp'
        size_hint_y: 0.2
        on_press: app.handle_command()
    Label:
        size_hint_y: 0.2
"""

# --- Main App Class (મુખ્ય એપ) ---
class AlpiApp(App):
    def build(self):
        return Builder.load_string(KV)

    def handle_command(self):
        user_command = self.root.ids.command_input.text
        response_text = process_command_logic(user_command)
        self.root.ids.response_label.text = response_text
        speak(response_text)
        self.root.ids.command_input.text = ""

# --- Run the App (એપ ચલાવો) ---
if __name__ == "__main__":
    AlpiApp().run()

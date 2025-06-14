import pyjokes
import cowsay
from textual.app import App, ComposeResult
from textual.widgets import Static

class CowJokeApp(App):
    def compose(self) -> ComposeResult:
        joke = pyjokes.get_joke()
        ascii_joke = cowsay.get_output_string("milk", joke)
        yield Static(f"[bold green]{ascii_joke}[/]", markup=True)
CowJokeApp().run()
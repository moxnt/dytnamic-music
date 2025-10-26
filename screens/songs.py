from textual.screen import Screen
from textual.widgets import Static


class Songs(Screen):
    def compose(self):
        yield Static("Song screen")

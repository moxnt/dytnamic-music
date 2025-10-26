from textual.screen import Screen
from textual.widgets import Static


class Mix(Screen):
    def compose(self):
        yield Static("Mix screen")

from textual.screen import Screen
from textual.widgets import Static


class Playlists(Screen):
    def compose(self):
        yield Static("Playlist screen")

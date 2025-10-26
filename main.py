from textual import on
from screens.playlists import Playlists
from screens.songs import Songs
from screens.mix import Mix
from textual.app import App
from textual.events import Load
from textual.widgets import Static, Header, Footer
from textual.screen import Screen


class Default(Screen):
    # A blank screen that will be pushed so the stack isn't empty when the user
    # wants so switch
    pass


class Shuffler(App):
    SCREENS = {
        "playlists": Playlists,
        "songs": Songs,
        "mix": Mix,
        "default": Default
    }
    BINDINGS = [
        ("d", "toggle_dark_mode", "Toggle dark mode"),
        ("1", "switch_screen('playlists')", "My playlists"),
        ("2", "switch_screen('songs')", "My songs"),
        ("3", "switch_screen('mix')", "Mix"),
    ]

    greeting = """
    Welcome to dytnamic music v0!
    Press 1 to go to your playlists
    Press 2 to go to your songs
    Press 3 to make a new mix
    Ctrl + q to exit
    """

    def action_toggle_dark_mode(self):
        self.theme = (
            "textual-dark" if self.theme == "textual-light"else "textual-light"
        )

    def compose(self):
        yield Header(show_clock=True)
        yield Static(self.greeting)
        yield Footer()

    @on(Load)
    def initial_screen(self):
        self.push_screen(Default())


if __name__ == "__main__":
    app = Shuffler()
    app.run()

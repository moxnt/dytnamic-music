from textual.app import App
from textual.widgets import Header, Footer


class Shuffler(App):
    BINDINGS = [
        ("d", "toggle_dark_mode", "Toggle dark mode")
    ]

    def compose(self):
        yield Header(show_clock=True)
        yield Footer()

    def action_toggle_dark_mode(self):
        self.theme = (
            "textual-dark" if self.theme == "textual-light" else "textual-light"
        )


if __name__ == "__main__":
    Shuffler().run()

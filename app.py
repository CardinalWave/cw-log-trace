import threading
from src.log_file_handler import filter_file, count_status
from textual.app import App, ComposeResult
from textual.containers import Horizontal, Vertical
from textual.widgets import Header, Footer, Log, Input, Static


class Main(App):
    BINDINGS = [('d', 'toggle_dark', 'Toggle dark mode')]

    CSS_PATH = "src/style.css"

    def compose(self) -> ComposeResult:
        yield Header(show_clock=True)
        yield Footer()
        with Horizontal():
            with Vertical(classes="column"):
                yield Input(classes="search")
                yield Log()
                # yield Static("Six", classes="box")

    def action_toggle_dark(self) -> None:
        self.dark = not self.dark

    def on_input_submitted(self, event: Input.Submitted):
        threading.Thread(target=self.update_log, daemon=True).start()

    def on_ready(self) -> None:
        threading.Thread(target=self.update_log, daemon=True).start()

    def update_log(self):
        log = self.query_one(Log)
        log.clear()
        param = self.query_one(Input).value
        line_log = filter_file("./log_service.txt", param)
        for line in line_log:
            log.write_line(line)


if __name__ == "__main__":
    app = Main()
    app.run()

import threading
from log_server import start_server, LOG_FILE
from concurrent.futures import ThreadPoolExecutor
from log_file_handler import filter_file, count_status
from textual.app import App, ComposeResult
from textual.containers import Horizontal, Vertical
from textual.widgets import Header, Footer, Log, Input, Static
from textual_plotext import PlotextPlot

TEXT = """2024-07-23 15:30:45,152 - INFO - Servidor HTTP iniciado na porta 8000
2024-07-23 15:30:55,891 - INFO - Recebida requisição para processar o item com ID: 123
2024-07-23 15:31:02,406 - INFO - Recebida requisição para processar o item com ID: 456
2024-07-23 15:31:12,802 - WARNING - Requisição recebida sem parâmetro 'id'
2024-07-23 15:31:12,802 - ERROR - Falha ao processar requisição: KeyError - 'id' não encontrado
2024-07-23 15:32:00,000 - INFO - Encerrando servidor HTTP
2024-07-23 15:32:00,001 - INFO - Servidor HTTP parado
"""


class Main(App):
    BINDINGS = [('d', 'toggle_dark', 'Toggle dark mode')]

    CSS_PATH = "style.css"

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.executor = ThreadPoolExecutor(max_workers=2)

    def compose(self) -> ComposeResult:
        yield Header(show_clock=True)
        yield Footer()
        with Horizontal():
            with Vertical(classes="column"):
                yield PlotextPlot(classes="bar")
                yield PlotextPlot(classes="plot")
            with Vertical(classes="column"):
                yield Input(classes="search")
                yield Log()
                yield Static("Six", classes="box")

    def action_toggle_dark(self) -> None:
        self.dark = not self.dark

    def on_mount(self):
        plt = self.query_one('.plot', PlotextPlot).plt
        y = plt.sin()
        plt.scatter(y, marker="braille")

        plt = self.query_one('.bar', PlotextPlot).plt
        pizzas = ["Sausage", "Pepperoni", "Mushrooms", "Cheese", "Chicken", "Beef"]
        male_percentages = [14, 36, 11, 8, 7, 4]
        female_percentages = [12, 20, 35, 15, 2, 1]

        plt.multiple_bar(pizzas, [male_percentages, female_percentages])
        plt.title("Most Favored Pizzas in the World by Gender")
        plt.show()
        plt.title("cw-message-service")

    def on_input_submitted(self, event: Input.Submitted):
        threading.Thread(target=self.update_log, daemon=True).start()

    def on_ready(self) -> None:
        threading.Thread(target=self.update_log, daemon=True).start()

    def update_log(self):
        log = self.query_one(Log)
        log.clear()
        param = self.query_one(Input).value
        line_log = filter_file(LOG_FILE, param)
        for line in line_log:
            log.write_line(line)


if __name__ == "__main__":
    app = Main()
    server_thread = threading.Thread(target=start_server, daemon=True)
    server_thread.start()
    app_thread = threading.Thread(target=app.run(), daemon=True)
    app_thread.start()

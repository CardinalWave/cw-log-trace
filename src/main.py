from textual import on
from textual.app import App, ComposeResult
from textual.containers import Horizontal, Vertical, Container
from textual.widgets import Header, Footer, Button, Label, Log, Input, Static
from textual_plotext import PlotextPlot, themes
from components.charts.plot import ChartPlot

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

    def compose(self) -> ComposeResult:
        with Horizontal():
            with Vertical(classes="column"):
                yield PlotextPlot(classes="bar")
                yield PlotextPlot(classes="plot")
            # with Vertical(classes="column"):
            with Vertical(classes="column"):
                yield Input()
                yield Log()
                yield Static("Six", classes="box")

    def action_toggle_dark(self) -> None:
        self.dark = not self.dark

    def on_mount(self):
        plt1 = self.query_one('.plot', PlotextPlot).plt
        y = plt1.sin()  # sinusoidal test signal
        plt1.scatter(y, marker = "braille")

        plt = self.query_one('.bar', PlotextPlot).plt
        pizzas = ["Sausage", "Pepperoni", "Mushrooms", "Cheese", "Chicken", "Beef"]
        male_percentages = [14, 36, 11, 8, 7, 4]
        female_percentages = [12, 20, 35, 15, 2, 1]

        plt.multiple_bar(pizzas, [male_percentages, female_percentages])
        plt.title("Most Favored Pizzas in the World by Gender")
        plt.show()
        plt.title("cw-message-service")

    def on_ready(self) -> None:
        log = self.query_one(Log)
        for _ in range(10):
            log.write_line(TEXT)


if __name__ == "__main__":
    app = Main()
    app.run()

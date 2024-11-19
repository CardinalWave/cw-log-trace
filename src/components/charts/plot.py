from textual_plotext import PlotextPlot
from textual.widget import Widget

class ChartPlot():

    def __init__(self):
        PlotextPlot(classes="plot")
        super().__init__()

    def on_mount(self):
        plt = self.query_one(PlotextPlot).plt
        pizzas = ["Sausage", "Pepperoni", "Mushrooms", "Cheese", "Chicken", "Beef"]
        male_percentages = [14, 36, 11, 8, 7, 4]
        female_percentages = [12, 20, 35, 15, 2, 1]

        plt.multiple_bar(pizzas, [male_percentages, female_percentages])
        plt.title("Most Favored Pizzas in the World by Gender")
        plt.show()
        plt.title("cw-message-service")

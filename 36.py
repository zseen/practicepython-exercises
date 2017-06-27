# TODO:
# 1. Change import to "import bokeh.plotting" and "import collectons.Counter"
# 2. No members needed
# 3. Create a class PlotData, which has two fields: xAxis and yAxis
# 4. Refactor data creation to a method, which returns a PlotData object

from bokeh.plotting import figure, show, output_file
import json
from collections import Counter

class MonthFigure(object):
    ALL_MONTHS = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October",
                  "November", "December", "Unknown"]

    def __init__(self):
        self.months = []
        self.birthdaysDict = {}
        self.month = []

    def countTheMonths(self):
        with open("info.json", "r") as f:
            self.birthdaysDict = json.load(f)

        for key, value in self.birthdaysDict.items():
            splitValue = value.split(" ")
            self.month = splitValue[len(splitValue) - 1]
            self.months.append(self.month)

        return Counter(self.months)

    def showFigure(self):
        monthsCounter = self.countTheMonths()

        x = []             # ["Jan", "Feb", "March", "Unknown"]
        y = []              # [3,     3,     2,       1]

        for key, value in monthsCounter.items():
            x.append(key)
            y.append(value)

        output_file("plot.html")

        p = figure(x_range=MonthFigure.ALL_MONTHS)
        p.vbar(x=x, top=y, width=0.5)

        show(p)

def main():
    m = MonthFigure()
    m.showFigure()

if __name__ == "__main__":
    main()

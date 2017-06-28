# TODO:
# 1. Change import to "import bokeh.plotting" and "import collectons.Counter"
# 2. No members needed
# 3. Create a class PlotData, which has two fields: xAxis and yAxis
# 4. Refactor data creation to a method, which returns a PlotData object

import bokeh.plotting as bk
import json
import collections


class PlotData(object):

    def __init__(self):
        self.xAxis = []
        self.yAxis = []


class MonthFigure(object):
    ALL_MONTHS = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October",
                  "November", "December", "Unknown"]

    def __init__(self):
        pass

    def countTheMonths(self):
        with open("info.json", "r") as f:
            birthdaysDict = json.load(f)

        months = []
        for key, value in birthdaysDict.items():
            splitValue = value.split(" ")
            month = splitValue[len(splitValue) - 1]
            months.append(month)

        return collections.Counter(months)

    def showFigure(self):
        data = self.getData()
        self.drawPlot(data)

    def drawPlot(self, data):
        bk.output_file("plot.html")
        p = bk.figure(x_range=MonthFigure.ALL_MONTHS)
        p.vbar(x=data.xAxis, top=data.yAxis, width=0.5)
        bk.show(p)

    def getData(self):
        monthsCounter = self.countTheMonths()
        data = PlotData()
        for key, value in monthsCounter.items():
            data.xAxis.append(key)
            data.yAxis.append(value)
        return data


def main():
    m = MonthFigure()
    m.showFigure()

if __name__ == "__main__":
    main()

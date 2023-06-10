import matplotlib.pyplot as plot

def generatePieChart():
    labels = ["A", "B", "C"]
    values = [100, 300, 600]

    fig, ax = plot.subplots()
    ax.pie(values, labels=labels)
    plot.savefig("pie.png")
    plot.close()

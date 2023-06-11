import matplotlib.pyplot as plot

def generarGraficaBarras(labels, values, name):
  fig, ax = plot.subplots()
  ax.bar(labels, values)
  plot.savefig(f"./imgs/{name}Bar.png")
  plot.close()

def generarGraficaPie(labels, values, name):
  ig, ax = plot.subplots()
  ax.pie(values, labels = labels)
  ax.axis("equal")
  plot.savefig(f"./imgs/{name}Pie.png")
  plot.close()

if __name__ == "__main__":
  labels = ['a', 'b', 'c']
  values = [10, 200, 60]
  generarGraficaBarras(labels, values)

import matplotlib.pyplot as plt

def generarGraficaBarras(labels, values):
  fig, ax = plt.subplots()
  ax.bar(labels, values)
  plt.show()

def generarGraficaPie(labels, values):
  ig, ax = plt.subplots()
  ax.pie(values, labels = labels)
  ax.axis("equal")
  plt.show()

if __name__ == "__main__":
  labels = ['a', 'b', 'c']
  values = [10, 200, 60]
  generarGraficaBarras(labels, values)

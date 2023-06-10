import csv
import matplotlib.pyplot as plt

def readCSV(path, collum):
  with open(path, 'r') as csvfile:
    reader = csv.reader(csvfile, delimiter=',')
    header = next(reader)
    data = []
    infoCountry = {}
    labelsCountry = []
    countryDigits = []
    
    for row in reader:
      iterable = zip(header, row)
      countryDict = {key: value for key, value in iterable}
      data.append(countryDict)
      
    for country in data:
      labelsCountry.append(country.get("Country/Territory"))
      countryDigits.append(country.get(collum))

    infoCountry = dict(zip(labelsCountry, countryDigits))
    #generarGraficaPie(labelsCountry, countryDigits)

  return infoCountry

def generarGraficaPie(labels, values):
  ig, ax = plt.subplots()
  ax.pie(values, labels = labels)
  ax.axis("equal")
  plt.show()

if __name__ == "__main__":
  data = readCSV("./app/data.csv", "1980 Population")
  print(data)

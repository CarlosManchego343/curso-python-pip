import csv
import matplotlib.pyplot as plt

def readCSV(path, countryInput):
  with open(path, 'r') as csvfile:
    reader = csv.reader(csvfile, delimiter=',')
    header = next(reader)
    data = []
    infoCountry = {}
    labelsCountryDigits = []
    countryDigits = []
    
    for row in reader:
      iterable = zip(header, row)
      countryDict = {key: value for key, value in iterable}
      data.append(countryDict)
      
    for country in data:
      if country.get("Country/Territory") == countryInput:
        infoCountry = country

    for value in infoCountry.values():
      if value.isdigit():
        countryDigits.append(int((value)))
    countryDigits.pop(0)
    countryDigits.pop(8)

    for key in infoCountry.keys():
      if key[0:4].isdigit():
        labelsCountryDigits.append(key[0:4])

    infoCountry = dict(zip(labelsCountryDigits, countryDigits))
    generarGraficaPie(labelsCountryDigits, countryDigits)

  return infoCountry

def generarGraficaPie(labels, values):
  ig, ax = plt.subplots()
  ax.pie(values, labels = labels)
  ax.axis("equal")
  plt.show()

if __name__ == "__main__":
  data = readCSV("./app/data.csv", "Colombia")
  print(data)

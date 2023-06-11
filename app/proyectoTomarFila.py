import csv
import charts
import matplotlib.pyplot as plot

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

    countryDigits = [int(value) for value in infoCountry.values() if value.isdigit()]
    
    '''for value in infoCountry.values():
      if value.isdigit():
        countryDigits.append(int((value)))'''

    countryDigits.pop(0)
    countryDigits.pop(8)

    labelsCountryDigits = [key[0:4] for key in infoCountry.keys() if key[0:4].isdigit()]
    
    '''for key in infoCountry.keys():
      if key[0:4].isdigit():
        labelsCountryDigits.append(key[0:4])'''

    infoCountry = dict(zip(labelsCountryDigits, countryDigits))
    charts.generarGraficaBarras(labelsCountryDigits, countryDigits, countryInput)
    charts.generarGraficaPie(labelsCountryDigits, countryDigits, countryInput)
   

  return infoCountry


if __name__ == "__main__":
  country = input("Digita un pais => ")
  data = readCSV("data.csv", country)
  print(data)

import csv

def readCSV(path):
  with open(path, 'r') as csvfile:
    reader = csv.reader(csvfile, delimiter = ',')
    header = next(reader)
    data = []
    for row in reader:
      iterable = zip(header, row)
      countryDict = {key: value for key, value in iterable}
      data.append(countryDict)
  return data

if __name__ == "__main__":
  data = readCSV("./app/data.csv")
  print(data[0])
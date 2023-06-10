import utils

data = [
    {
      'Country': 'Colombia',
      'Population': 300
    },
    {
      'Country': 'Irlanda',
      'Population': 400
    }
  ]

def run():
  keys, values = utils.getPopulation()
  print(keys, values)

  country = input("Digita el pais: ")

  result = utils.populationByCountry(data, country)

  print(result)

#Si es ejecutado desde la terminal se ejecuta el metodo que hay debajo, si es ejecutado y llamado desde otro archivo solo se ejecuta lo que necesita de este archivo
if __name__ == '__main__':
  run()
import readCSV as read_csv
import pandas as pd
import charts

def run():
    df = pd.read_csv("data.csv")
    df = df[df["Continent"] == "South America"]

    countries = df['Country'].values
    percentages = df['World Population Percentage'].values

    charts.generarGraficaPie(countries, percentages, "South America")

if __name__ == "__main__":
  run()
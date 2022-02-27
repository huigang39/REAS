import numpy as np
import pandas as pd


def readCSV(fileName):
    data = pd.read_csv(fileName)
    return data


def main(fileName):
    data = readCSV(fileName)


if __name__ == "__main__":
    fileName = input("Enter the file name: ")
    main(fileName)

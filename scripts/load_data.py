import pandas

def loadData():
    data_frame = pandas.read_csv('data/pokemon.csv')
    for index, row in data_frame.iterrows():


if __name__ == "__main__":
    loadData()
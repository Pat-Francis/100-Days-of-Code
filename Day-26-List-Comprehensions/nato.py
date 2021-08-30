import pandas
# Load CSV into Pandas Dataframe
data = pandas.read_csv("nato_phonetic_alphabet.csv")
# Iterates through data and appends to data_dict in the format 'A': 'Alfa'
data_dict = {row.letter: row.code for (index, row) in data.iterrows()}


def get_nato():
    # Ask user for word input
    word = input("Please input your word: ")
    try:
        # Iterate through word letter by letter and add corresponding code word
        nato_phonetic = [data_dict[letter] for letter in word.upper()]
    except KeyError:
        print("Please use letters only")
        get_nato()
    else:
        print(nato_phonetic)


get_nato()

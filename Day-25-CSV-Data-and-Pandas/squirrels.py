import pandas

# Load CSV into Pandas
data = pandas.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")

# Get the counts for each fur color
gray_squirrels = len(data[data["Primary Fur Color"] == "Gray"])
cinnamon_squirrels = len(data[data["Primary Fur Color"] == "Cinnamon"])
black_squirrels = len(data[data["Primary Fur Color"] == "Black"])

# Create dictionary
data_dict = {
    "Fur Color": ["Gray", "Cinnamon", "Black"],
    "Count": [gray_squirrels, cinnamon_squirrels, black_squirrels]
}

# Create dataframe from data_dict and export to CSV
data_frame = pandas.DataFrame(data_dict)
data_frame.to_csv("squirrel_count.csv")

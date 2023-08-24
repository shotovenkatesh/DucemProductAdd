import pandas as pd
import csv


df = pd.read_csv("vegan.csv")
# print(df)
df['Name'] = df['Name'].str.title()
df['Price'] = df['Price'].astype(float)
increase_percentage = 20
df['Price'] = df['Price'] * (1 + increase_percentage / 100)

# df['Description'] = df['Description'].str.title()

data_dict = df.to_dict('records')

names = [item['Name'] for item in data_dict]
price = [item['Price'] for item in data_dict]
meta_titles = [item['Name'] for item in data_dict]


try:
    barcodes = [item['Barcode'] for item in data_dict]
except KeyError:
    barcodes = ""

try:
    categories = [item['Category'] for item in data_dict]
except KeyError:
    categories = ""

try:
    weights = [item['Weight'] for item in data_dict]
except KeyError:
    weights = ""


def get_names():
    return names


def get_prices():
    return price


def get_barcodes():
    return barcodes


def get_meta_titles():
    return meta_titles


def get_categories():
    return categories


def get_weights():
    return weights

print(names[0])
print(type(names))
print(len(names))
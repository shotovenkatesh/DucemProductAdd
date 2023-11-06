import pandas as pd
import csv


#name of the csv that has the data
df = pd.read_csv("n.csv")
# print(df)
df['Name'] = df['Name'].astype(str)
df['Name'] = df['Name'].str.title()
try:
    df['Brand'] = df['Brand'].astype(str)
except:
    print("Brand details is not available for this csv")
else:
    df['Brand'] = df['Brand'].str.title()


df['Price'] = df['Price'].astype(float)
df['Price'] = df['Price'] * 1.35
df['Price'] = df['Price'].round(1)

# df['Description'] = df['Description'].str.title()

data_dict = df.to_dict('records')

names = [item['Name'] for item in data_dict]
price = [item['Price'] for item in data_dict]
meta_titles = [item['Name'] for item in data_dict]

try:
    brands = [item['Brand'] for item in data_dict]
except:
    brands = []

try:
    brands = [item['Brand'] for item in data_dict]
except KeyError:
    brands = ""



try:
    description = [item['Description'] for item in data_dict]
except KeyError:
    description = ""


try:
    barcodes = [str(item['Barcode']) for item in data_dict]
    barcodes = [s.rstrip('.0') if s.endswith('.0') else s for s in barcodes]
    barcodes = [str(barcode).rstrip('.0') for barcode in barcodes]
except KeyError:
    barcodes = ""



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





def get_weights():
    return weights

def get_des():
    return description


def get_brands():
    return brands

print(price)
print(barcodes)
print(names)
print(brands)
import csv
import read_csv
from slugify import slugify
from unidecode import unidecode

row_list = [
    ["Product ID", "Name", "Model", "SKU", "Description", "Meta Tag Description", "Meta Tag Keywords", "Tags", "UPC",
     "EAN", "JAN",
     "ISBN", "MPN", "Price", "Location", "Status", "Tax Class", "Quantity", "Minimum Quantity", "Image",
     "Subtract Stock", "Out Of Stock Status", "Requires Shipping", "SEO Keyword", "Date Available", "Length", "Width",
     "Height", "Length Class", "Weight", "Weight Class", "Sort Order", "Reward Points", "Manufacturer", "Categories",
     "Filters", "Stores", "Downloads", "Related Products", "Meta Title"], ]

# name of new file
with open('NCH.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerows(row_list)

# This should be changed
# manufacturer is supplier name
# location is company name
# MANUFACTURER = "Gulf International"
location = "NEW COUNTRY HEALTHCARE LLC"
si_tag = "NCHNEW"
date = "2023-11-06"

# Name ✅
# MODEL: si number ✅
# SKU: Barcode ✅
# Price: Increase by 20% ✅
# Date available
# sort order: increment by 1✅
# meta title same as the title✅
# seo:slug ✅
# location : ✅
# TAX_CLASS : ✅
# Quantity : ✅
# Store : ✅
# min_Quantity : ✅


names = read_csv.get_names()
price = read_csv.get_prices()
barcodes = read_csv.get_barcodes()
meta_titles = read_csv.get_meta_titles()
categories = 250
description = read_csv.get_des()
brands = read_csv.get_brands()

si_number = [f"{si_tag}{num:03}" for num in range(0, len(names))]
sort_number = [num for num in range(0, len(names))]
weights = read_csv.get_weights()
TAX_CLASS = "Taxable Goods"
seo = [slugify(name) for name in names]

# These should not be changed
QUANTITY = 100
MIN_QUANTITY = 1
SUBTRACT_STOCK = "Yes"
STORE = 0
index = 0
last_number = names

while index != len(names):
    name_tw = unidecode(names[index])
    price_tw = price[index]
    barcode_tw = barcodes[index]
    image = f"catalog/2023/nch01/{barcode_tw}.jpg"
    meta_title_tw = unidecode(meta_titles[index])
    si_number_tw = si_number[index]
    sort_number_tw = sort_number[index]
    seo_tw = seo[index]
    try:
        manu_f = brands[index]
    except IndexError:
        manu_f = ""

    if weights == "":
        weight_tw = ""
    else:
        weight_tw = weights[index]

    if barcodes == "":
        barcode_tw = ""
    else:
        barcode_tw = barcodes[index]

    if description == "":
        description_tw = name_tw
    else:
        description_tw = description[index]

    lines = description_tw.split('\n')  # Split the sentence into lines using '\n' as the delimiter
    meta_tag_tw = '\n'.join(lines[:2])

    # name of new file(same as above)
    f = open('NCH.csv', 'a')
    writer = csv.writer(f)
    row = ["", name_tw, si_number_tw, barcode_tw, description_tw, meta_tag_tw, name_tw, " ", "", "", "", "", "",
           price_tw,
           location, "Enabled", TAX_CLASS,
           QUANTITY, MIN_QUANTITY, image, SUBTRACT_STOCK, "", "", seo_tw, date, "", "", "", "", weight_tw, "",
           sort_number_tw,
           "", manu_f, categories, "", STORE, "", "", meta_title_tw]
    writer.writerow(row)
    print(f"{name_tw} has been added to the csv")
    index += 1

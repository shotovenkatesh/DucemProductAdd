import csv
import read_from_csv
from slugify import slugify
import chatgpt

row_list = [
    ["Product ID", "Name", "Model", "SKU", "Description", "Meta Tag Description", "Meta Tag Keywords", "Tags", "UPC",
     "EAN", "JAN",
     "ISBN", "MPN", "Price", "Location", "Status", "Tax Class", "Quantity", "Minimum Quantity", "Image",
     "Subtract Stock", "Out Of Stock Status", "Requires Shipping", "SEO Keyword", "Date Available", "Length", "Width",
     "Height", "Length Class", "Weight", "Weight Class", "Sort Order", "Reward Points", "Manufacturer", "Categories",
     "Filters", "Stores", "Downloads", "Related Products", "Meta Title"], ]

with open(f'test.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerows(row_list)


# This should be changed
#manufacturer is supplier name
#location is company name
MANUFACTURER = "Vegan Way"
location = "Vegan Way"
si_tag = "VW"
date = "24/08/2023"



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


names = read_from_csv.get_names()
price = read_from_csv.get_prices()
barcodes = read_from_csv.get_barcodes()
meta_titles = read_from_csv.get_meta_titles()
categories = read_from_csv.get_categories()
si_number = [f"{si_tag}{num:03}" for num in range(0, len(names))]
sort_number = [num for num in range(0, len(names))]
weights = read_from_csv.get_weights()
TAX_CLASS = "Taxable Good"
seo = [slugify(name) for name in names]

# These should not be changed
QUANTITY = 100
MIN_QUANTITY = 1
SUBTRACT_STOCK = "Yes"
STORE = 0
# print(seo)
index = 0
last_number = names



while index != len(names):
    name_tw = names[index]
    price_tw = price[index]
    meta_title_tw = meta_titles[index]
    si_number_tw = si_number[index]
    sort_number_tw = sort_number[index]
    seo_tw = seo[index]

    if weights == "":
        weight_tw = ""
    else:
        weight_tw = weights[index]

    if barcodes == "":
        barcode_tw = ""
    else:
        barcode_tw = barcodes[index]
    if categories == "":
        category_tw = ""
    else:
        category_tw = categories[index]
    description = chatgpt.get_description(f"Give me a description about {MANUFACTURER}'s {name_tw}")
    lines = description.split('\n')  # Split the sentence into lines using '\n' as the delimiter
    meta_tag_tw = '\n'.join(lines[:2])

    f = open(f'test.csv', 'a')
    writer = csv.writer(f)
    row = ["", name_tw, si_number_tw, barcode_tw, description, meta_tag_tw, " ", " ", "", "", "", "", "", price_tw,
           location, "", TAX_CLASS,
           QUANTITY, MIN_QUANTITY, "", SUBTRACT_STOCK, "", "", seo_tw, date, "", "", "", "", weight_tw, "",
           sort_number_tw,
           "", MANUFACTURER, category_tw, "", STORE, "", "", meta_title_tw]
    writer.writerow(row)
    print(f"{name_tw} has been added to the csv")
    index += 1

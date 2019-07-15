# importing libraries

import pandas as pd
import numpy as np


# getting user input

budget = input("Enter your Budget 'ex: 10000' : ")
max_rating = input("Enter Your Max Rating from 1-5 'ex: 4/3.5' : ")
vendor_type = input("Enter vendor Type 'ex: photographer/event planner/birthday planner/catering' : ")


# reading the files
lists = pd.read_csv('listing.csv')
vendors = pd.read_csv('vendors.csv')

# finding user input values in csv file : this has errors
for i, row in vendors.iterrows():
    if row["budget"] == budget or row["vendor_rating"] == max_rating or row["vendor_type"] == vendor_type:
        print(row)



# # Getting recommendation based on No. Of ratings
# ratings = pd.DataFrame(vendors, columns=['vendor_id', 'no_of_rating'])
#
# # print(ratings)
#
#
# # Sorting and dropping the duplicates
# sorted_rating = ratings.sort_values('no_of_rating', ascending=False).drop_duplicates().head(5)
#
# # print(sorted_rating)
#
#
# # getting 5 most rated vendors
# most_rated_vendors = pd.DataFrame([4, 5, 8, 1, 10], index=np.arange(5), columns=['vendor_id'])
# detail = pd.merge(most_rated_vendors, lists, on='vendor_id')
#
# # getting the most rated vendor
#
# most_rated_vendor = pd.DataFrame(vendors, columns=['vendor_id', 'vendor_rating', 'no_of_rating'])

# print(most_rated_vendor.max())






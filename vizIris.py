
import numpy as np
import pdb
import csv as csv


csv_file_object = csv.reader(open('train.csv', 'rb')) 
header = csv_file_object.next()  # The next() command just skips the 
                                 # first line which is a header
data=[]                          # Create a variable called 'data'.
for row in csv_file_object:      # Run through each row in the csv file,
    pdb.set_trace()
    data.append(row)             # adding each row to the data variable
data = np.array(data) 	         # Then convert from a list to an array
			  

print header
pdb.set_trace()
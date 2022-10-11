import csv
import json

#input the csv file
input_file_path = "< Input csv file path >"
output_file = "< Output file path >"

#Open and read the csv file
inp_file = open(input_file_path)
reader = csv.reader(inp_file)

#write into the output file
writer_file = open(output_file, "w")
writer = csv.writer(writer_file)

#extracting the headers from the original csv
for header in reader:
    headers = header
    break

headers.insert(7, 'Tags')   #adding the parsed data header in the final output

next(reader, 0)
writer.writerow(headers)

count = 0 

#loading the json column
for row in reader:
    value_str = ''
    json_data = json.loads(row[17])
    
    tags = json_data.get("Tags", "")    #add the attribute which you want to extract from the json in place of Tags. 
    if tags:
        for tag in tags:
            if tag.get("Key", "").lower() in ["team", "product", "owner", "project"]:    #list of key and values want to extract from the tags dict
                value = tag.get("Value", "")
                if value:
                    value_str += tag.get("Key", "") + ':' + value + '\n'   #store the key and value into a variable

    row.insert(7, value_str) #inserting the parsed output into a row 
    writer.writerow(row)
    count += 1
    print(count)
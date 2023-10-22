import happybase

connection = happybase.Connection('127.0.0.1', 9090)
table_name = 'test_table'

# Open the output.txt file for reading
with open("output.txt", "r") as f:
    table = connection.table(table_name)

    for x in f:
        item = x.split('"')
        key = item[1]
        value = item[2].strip()
        row_key = key.split(':')[0]
        column_family = key.split(':')[1]  # Assuming key format is "column_family:column_qualifier"
        data = {column_family: value}

        # Put the data into the HBase table
        table.put(row_key, data)

    print("Data inserted into HBase table")

connection.close()

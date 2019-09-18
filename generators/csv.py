def generate(data_list):
    csv_data = ''
    
    column_names = list(data_list[0].keys())
    csv = list_to_string(column_names)
    csv_data += csv

    for data in data_list:
        camps = list(data.values())
        csv = list_to_string(camps)
        csv_data += '\n'+csv
    
    return csv_data
    
def list_to_string(camps):
    csv = str(camps[0])
    for i in range(1, len(camps)):
        csv += ',{}'.format(camps[i])
    return csv
    
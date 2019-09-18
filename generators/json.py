def generate(data_list):
    dict1 = data_list[0]
    keys = list(dict1.keys())
    json_str = ''
    len_keys = len(keys)
    len_data_list = len(data_list)
    if len_data_list > 1:
        for i in dict1:
            keys.append(i)
        json_str2 = ('')
        json_str += '['
        cont1 = 1
        for i in range(len(data_list)):
            json_str += ('\n    {')
            cont2 = 1
            for j in data_list[i].keys():
                json_str2 = ('')
                k = (data_list[i])[j]
                json_str2 += ('\n        "{}": "{}"'.format(j, k))
                if cont2 < (len_keys):
                    json_str2 += (',')
                    cont2 += 1
                json_str += json_str2
                json_str2 = ('')
            if cont1 < len_data_list:
                json_str += ('\n    },\n')
                cont1 += 1
        json_str += ('\n    }')
        json_str += ('\n]')
    if len_data_list == 1:
        for i in dict1:
            keys.append(i)
        json_str2 = ('')
        cont1 = 1
        for i in range(len(data_list)):
            json_str += ('{')
            cont2 = 1
            for j in data_list[i].keys():
                json_str2 = ('')
                k = (data_list[i])[j]
                json_str2 += ('\n    "{}": "{}"'.format(j, k))
                if cont2 < (len_keys):
                    json_str2 += (',')
                    cont2 += 1
                json_str += json_str2
                json_str2 = ('')
            if cont1 < len_data_list:
                json_str += ('\n},\n')
                cont1 += 1
        json_str += ('\n}')
    return json_str
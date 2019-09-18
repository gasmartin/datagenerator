# MODIFICAR
def generate(data_list):
    sql = ""
    for data in data_list:
        sql += 'INSERT' + '\n'
        sql += 'INTO' + '\n'
        sql += '\t' + 'DataGen.Person' + '\n'
        sql += '\t' + '(name, address, phone, country, city, cep, uf)\n'
        sql += 'VALUES' + '\n'
        sql += '\t' + '("{0}", "{1}", "{2}", "{3}", "{4}", "{5}", "{6}");'.format(
            data["name"], data["address"], data["phone"], 
            data["country"], data["city"], data["cep"], data["uf"]
        )
        sql += '\n'
    return sql
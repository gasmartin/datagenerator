from random import choice, randint
from sys import argv, exit, path

from generators import csv, html, insert, json
from utils import show_error_log, show_help_information

#Caminho para a pasta que contém os arquivos de texto
path_to_files = path[0] + "/data/"

names = []
surnames = []
addresses = []
cities = []
ufs = []
countries = []
ceps = []

# Função usada para ler o conteúdo dos arquivos e
# colocá-los em suas respectivas listas
def read_files():
    with open(path_to_files + "names.txt", "r") as names_file:
        global names
        names = [name.rstrip() for name in names_file.readlines()]
    with open(path_to_files + "surnames.txt", "r") as surnames_file:
        global surnames
        surnames = [surname.rstrip() for surname in surnames_file.readlines()]
    with open(path_to_files + "addresses.txt", "r") as addresses_file:
        global addresses
        addresses = [address.rstrip() for address in addresses_file.readlines()]
    with open(path_to_files + "cities.txt", "r") as cities_file:
        global cities
        cities = [city.rstrip() for city in cities_file.readlines()]
    with open(path_to_files + "ufs.txt", "r") as ufs_file:
        global ufs
        ufs = [uf.rstrip() for uf in ufs_file.readlines()]
    with open(path_to_files + "countries.txt", "r") as countries_file:
        global countries
        countries = [country.rstrip() for country in countries_file.readlines()]
    with open(path_to_files + "ceps.txt", "r") as ceps_file:
        global ceps
        ceps = [cep.rstrip() for cep in ceps_file.readlines()]

# Função de gerar dados de uma pessoa
def generate_data():
    person = {} # Cria um dicionário vazio
    person["name"] = choice(names) # Escolhe um nome aleatório
    # Define aleatoriamente o número de sobrenomes que a pessoa terá
    # (1 ou 2)
    number_of_surnames = randint(1, 2)
    for _ in range(number_of_surnames):
        person["name"] += " " + choice(surnames)
    person["address"] = choice(addresses) # Escolhe um endereço aleatório
    person["phone"] = repr(randint(1000, 9999)) + "-" + repr(randint(1000, 9999))
    person["city"] = choice(cities) # Escolhe uma cidade aleatória
    person["uf"] = choice(ufs) # Escolhe uma UF aleatória
    person["country"] = choice(countries) # Escolhe um país aleatório
    person["cep"] = choice(ceps) # Escolhe um CEP aleatório
    return person

parameters = argv[1:]
number_of_parameters = len(parameters)
if number_of_parameters == 1:
    arg = ""
    try:
        arg = argv[1]
    except Exception:
        show_error_log()
        exit()

    if arg == "-help":
        show_help_information()
    else:
        show_error_log()
elif number_of_parameters == 2:
    try:
        size, output_format = parameters[0], parameters[1]
        size = int(size)
    except ValueError:
        show_error_log()
        exit()

    read_files()
    person_data = []
    for _ in range(size):
        person_data.append(generate_data())

    module = None
    if output_format == "-csv":
        module = csv
    elif output_format == "-json":
        module = json
    elif output_format == "-sql":
        module = insert
    elif output_format == "-html":
        module = html
    else:
        show_error_log()
        exit()

    person_data = module.generate(person_data)
    print(person_data)
else:
    show_error_log()

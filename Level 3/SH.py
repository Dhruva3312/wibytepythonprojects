import csv

print("Welcome to the Sports Heroes project")
print("We are going to do some analysis on Wimbledon and French Open Men's singles champions")

def print_line(report_line):
    filename = 'analysis.dat'
    with open(filename, mode='a', encoding='utf-8') as file:
        file.write(report_line)

def print_table(table):
    filename = 'analysis.dat'
    with open(filename, mode='a', encoding='utf-8') as file:
        if not table:
            return
        all_keys = list(table[0].keys())
        keys_line = ''
        for key in all_keys:
            keys_line = keys_line + key + (20 - len(key)) * ' '
        file.write(keys_line + '\n')
        
        for data in table:
            values_line = ''
            for values in data.values():
                val_str = str(values)
                values_line = values_line + val_str + (20 - len(val_str)) * ' '
            file.write(values_line + '\n')
        file.write('\n')

def initialize():
    filename = 'analysis.dat'
    with open(filename, mode='w', encoding='utf-8') as file:
        file.write('Analysis Results \n\n')

def print_set(winner_set):
    filename = 'analysis.dat'
    with open(filename, mode='a', encoding='utf-8') as file:
        # Sort members alphabetically for clean organization
        sorted_winners = sorted(list(winner_set))
        for winner in sorted_winners:
            file.write(winner + ' , ')
        file.write('\n \n')

def readcsvdata(tournament_name):
    filename = 'Level 3/' + tournament_name + '.csv'
    tournament_data = []
    with open(filename, mode='r', encoding='utf-8') as file:
        csvFile = csv.DictReader(file)
        for row in csvFile:
            # Data cleaning: filter out rows where Champion is missing/NaN (e.g. 2020 COVID cancellation)
            if row.get('Champion') and row.get('Champion').strip():
                tournament_data.append(row)
    return tournament_data

# Initialize the analysis file
initialize()

# Load CSV data with correct lowercase names
wimbledon_data = readcsvdata('wimbledon')
french_open_data = readcsvdata('frenchopen')

# Load CSV data
wimbledon_data = readcsvdata('wimbledon')
french_open_data = readcsvdata('frenchopen')

# Print the data to your analysis file
print_line("Wimbledon Champions:\n")
print_table(wimbledon_data)

print_line("French Open Champions:\n")
print_table(french_open_data)

print("Please see the file analysis.dat for the results")
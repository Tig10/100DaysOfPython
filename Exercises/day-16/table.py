from prettytable import PrettyTable

table = PrettyTable()
table.add_column('Pokemon Name', ['Pikachu', 'Weedle', 'Pansage', 'Mothin', 'Marill', 'Fennekin', 'Scatterbug', 'Charmander'])
table.add_column('Type', ['Electric', 'Poison', 'Grass', 'Water', 'Water Fairy', 'Fire', 'Bug', 'Fire'])
table.align = 'r'
print(table)

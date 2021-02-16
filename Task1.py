from sys import argv

script_name, output_in_hours, rate_per_hour, prize = argv
output_in_hours = int(output_in_hours)
rate_per_hour = int(rate_per_hour)
prize = int(prize)
print(f'Заработная плата сотрудника: {(output_in_hours * rate_per_hour) + prize}')

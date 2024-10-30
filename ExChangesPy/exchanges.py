import requests 
from bs4 import BeautifulSoup
import pandas as pd 
from datetime import datetime
import os

# The URL from which the exchange rates will be obtained is defined
url = "https://www.x-rates.com/table/?from=CLP&amount=1" 
clear_console = 'cls' if os.name == 'nt' else 'clear'

# An HTTP request is made to obtain the content of the page
response = requests.get(url)

# BeautifulSoup is used to process the HTML content of the page
soup = BeautifulSoup(response.content, 'html.parser')

# Two empty lists are defined where the exchange rates will be stored.
rates1 = []
rates2 = []

# All tables within the HTML content are searched.
tables = soup.find_all('table')

# The tables found are assigned to two different variables.
table1 = tables[0]
table2 = tables[1]

# We obtain the rows of both 
rows1 = table1.find_all('tr')
rows2 = table2.find_all('tr')

# We go through the rows of both tables
for row in rows1[1:]:  
    columns = row.find_all('td')
    if columns:
        currency_code1 = columns[0].text.strip()
        country1 = columns[1].text.strip()
        rate1 = float(columns[2].text.strip())
        rates1.append({'codigo': currency_code1, 'pais': country1, 'tasa': rate1})

for row in rows2[1:]:  
    columns = row.find_all('td')
    if columns:
        currency_code2 = columns[0].text.strip()
        country2 = columns[1].text.strip()
        rate2 = float(columns[2].text.strip())
        rates2.append({ 'codigo': currency_code2, 'pais': country2, 'tasa': rate2})

# Two dataframes (tables) are created from the rate lists obtained.
data1 = pd.DataFrame(rates1)
data2 = pd.DataFrame(rates2)

def check_input_currency(check):
    while True:
        os.system(clear_console)
        try:
            check = check
            if check in data2['codigo'].values or check in data1['codigo'].values:
                return check
            else:
                raise ValueError

        except ValueError:
            print("--------------------------------------------------------")
            print(f"Currency {check} not found is an invalid option please try again.")
            print("--------------------------------------------------------")
            check = input("What currency do you want to convert(e.g. US Dollar, Euro): ")
            
def check_input(check):
    while True:
        os.system(clear_console)
        try:
            if check.lower() == 'y':
                return check
            elif check.lower() == 'n':
                os.system(clear_console)
                print("--------------------------------------------------------")
                print("You have left the program")
                print("For more information you can visit the following page:")
                print("https://www.x-rates.com/table/?from=CLP&amount=1")
                print("SEE YOU SOON!")
                print("--------------------------------------------------------")
                exit()
            else:
                raise ValueError

        except ValueError:
            print("--------------------------------------------------------")
            print("Invalid option. Please try again.")
            print("--------------------------------------------------------")
            check = input("Try again (y/n): ")

def check_input_amount(check):
    while True:
        os.system(clear_console)
        try:
            check = float(check)
            if check <= 0 or not check.is_integer():
                raise ValueError
            return check
        except ValueError:
            print("The amount entered is not valid. It must be greater than 0 and an integer.")
            check = input("Enter the amount to convert:  ")

def show_menu():
    print("--- Options menu ---")
    print("1. Show Top 10 exchange rates")
    print("2. Show all exchange rates")
    print("3. Convert amount between two currencies")
    print("4. Convert amount to all available currencies")
    print("5. Show best conversion rate for a currency")
    print("6. Exit")

# This function converts an amount from a source currency to all available currencies.
def convert_amount_all_currencies(amount, original_currency, data):
    origin_rate = data.loc[data['codigo'] == original_currency, 'tasa'].values[0]
    for index, row in data.iterrows():
        destination_currency = row['codigo']
        destination_rate = row['tasa']
        amount_converted = (amount / origin_rate) * destination_rate
        print(f"{amount} {original_currency} = {amount_converted:.2f} {destination_currency}")
    print("Date and time of conversion:", datetime.now().strftime('%Y-%m-%d %H:%M:%S'))

# This function converts an amount between two specified currencies.
def convert_amount(amount, original_currency, destination_currency, data):
    origin_rate = data.loc[data['codigo'] == original_currency, 'tasa'].values[0]
    destination_rate = data.loc[data['codigo'] == destination_currency, 'tasa'].values[0]
    amount_converted = (amount / origin_rate) * destination_rate
    return amount_converted

# This function shows the best conversion rate for a specific currency.
def show_best_rate(currency, data):
    best_rate = data.loc[data['codigo'] == currency, 'tasa'].max()
    return best_rate

#Main function that controls user interaction with the program.
def run_program():
    follow = True 
    while follow:
        os.system(clear_console)
        show_menu() 
        option = input("Select an option: ")

        if option == '1':
            os.system(clear_console)
            print("--------------------------------------------------------")
            top_10 = data1.nlargest(10, 'tasa')
            print("Top 10 exchange rates:")
            print(top_10)
            print("--------------------------------------------------------")

        elif option == '2':
            os.system(clear_console)
            print("--------------------------------------------------------")
            print("All exchange rates:")
            print(data2)
            print("--------------------------------------------------------")

        elif option == '3':
            os.system(clear_console)
            print("--------------------------------------------------------")
            amount = input("Enter the amount to convert:  ")
            amount = float(check_input_amount(amount))
            print("Amount entered:", amount)
            original_currency = check_input_currency(input("Enter the currency of origin (e.g. US Dollar): "))
            destination_currency = check_input_currency(input("Enter the destination currency (e.g. Euro): "))      
            amount_converted = convert_amount(amount, original_currency, destination_currency, data2)
            print("--------------------------------------------------------")
            print(f"{amount} {original_currency} = {amount_converted:.2f} {destination_currency}")
            print("--------------------------------------------------------")

        elif option == '4':
            os.system(clear_console)
            print("--------------------------------------------------------")
            amount = input("Enter the amount to convert: ")
            amount = float(check_input_amount(amount))
            original_currency = check_input_currency(input("Type the name of the source currency: "))
            print("--------------------------------------------------------")
            convert_amount_all_currencies(amount, original_currency, data2)
            print("--------------------------------------------------------")

        elif option == '5':
            os.system(clear_console)
            print("--------------------------------------------------------")
            currency = check_input_currency(input("Type the name of the destination currency (You must consider that the current currency is Chilean):"))
            best_rate = show_best_rate(currency, data2)
            print("--------------------------------------------------------")
            print(f"The best conversion rate for {currency} is: {best_rate:.2f}")
            print("--------------------------------------------------------")

        elif option == '6':
            os.system(clear_console)
            print("--------------------------------------------------------")
            print("You have left the program")
            print("For more information you can visit the following page:")
            print("https://www.x-rates.com/table/?from=CLP&amount=1")
            print("SEE YOU SOON!")
            print("--------------------------------------------------------")
            break

        else:
            os.system(clear_console)
            print("--------------------------------------------------------")
            print("Invalid option. Please try again.")
            print("--------------------------------------------------------")
            follow_codigo = input("Try again (y/n): ")
            check_input(follow_codigo)
            continue
            
            
        # The user is asked if he/she wants to perform another action.
        follow_codigo = input("Do you wish to perform another action (y/n): ")
        check_input(follow_codigo)

# The main function is called to start the program.
run_program()

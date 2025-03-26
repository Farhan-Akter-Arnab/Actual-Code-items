print("Disclaimer: This is the list of country codes of 10 countries...")
country_code = {'Bangladesh': '0088',
                'India': '0091',
                'Turkey': '0090',
                'Norway': '0047',
                'Egypt': '0020',
                'Palestine': '00972',
                'Saudi Arabia': '00966',
                'Russia': '0074',
                'Azerbaijan': '00994',
                'Uzbekistan': '00998'}
#search dictionary for country codes
#search dictionary for country code of Bangladesh
print("Country code for Bangladesh -")
print(country_code.get('Bangladesh', 'Not found'))
#search dictionary for country code of Mongolia
print("Country code for Mongolia -")
print(country_code.get('Mongolia', 'Not found'))
#search dictionary for country code of Bangladesh
print("Country code for Uzbekistan -")
print(country_code.get('Uzbekistan', 'Not found'))
#search dictionary for country code of Mongolia
print("Country code for Norway -")
print(country_code.get('Norway', 'Not found'))
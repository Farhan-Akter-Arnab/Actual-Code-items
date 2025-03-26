country_code = {'Bangladesh': '0088',
                'India': '0091',
                'Turkey': '0090',
                'Norway': '0047'}
#search dictionary for country code of Bangladesh
print("Country code for Bangladesh -")
print(country_code.get('Bangladesh', 'Not found'))
#search dictionary for country code of Mongolia
print("Country code for Mongolia -")
print(country_code.get('Mongolia', 'Not found'))
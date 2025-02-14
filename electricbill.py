kWperh = float(input("Please enter your energy consumption in kW/h [units]: "))
if (kWperh < 50):
    amount = kWperh * 2.60
    surcharge = 25
elif (kWperh <= 100):
    amount = 130 + ((kWperh - 50) * 3.25)
    surcharge = 35
elif (kWperh <= 200):
    amount = 130 + 162.50 + ((kWperh - 100) * 5.26)
    surcharge = 45
else:
    amount = 130 + 162.50 + 526 + ((kWperh - 200) * 8.45)
    surcharge = 75
total = amount + surcharge
print("\nElectricity Bill : ", total)
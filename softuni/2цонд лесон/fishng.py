scumriq_kg_price = float(input())
caca_kg_price = float(input())
kg_pamud = float(input())
kg_safrid = float(input())
kg_midi = int(input())

price_of_pamud = scumriq_kg_price + scumriq_kg_price * 0.60
safrid_price = caca_kg_price + caca_kg_price * 0.80

suma_pamud = price_of_pamud * kg_pamud
suma_safrid = kg_safrid * safrid_price
suma_midi = kg_midi * 7.50
all_suma = suma_midi + suma_safrid + suma_pamud
print(f'{all_suma:.2f}')

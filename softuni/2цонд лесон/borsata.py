price_for_kg_zel = float(input())
price_for_kg_plod = float(input())
kg_zel = int(input())
kg_plod = int(input())

price_for_zel = price_for_kg_zel * kg_zel
price_for_plod = price_for_kg_plod * kg_plod

price_in_euro = (price_for_plod + price_for_zel) / 1.94

print(f'{price_in_euro:.2f}')
orders = [(102, "Ali"), (99, "Vali"), (150, "Sami")]

juft_buyurtmalar = []

for buyurtma in orders:
    if buyurtma[0] % 2 == 0:
        juft_buyurtmalar.append(buyurtma)

print(juft_buyurtmalar)
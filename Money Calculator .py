diez = int(input("Ingresa los de $10: "))
veinte = int(input("Ingresa los $20: "))
cincuenta = int(input("Ingresa los de $50: "))
cien = int(input("Ingresa los de $100: "))
doscientos = int(input("Ingresa los de $200: "))
quinientos = int(input("Ingresa los $500: "))
mil = int(input("Ingresa los $1000: "))


def calculator(diez, veinte, cincuenta, cien, doscientos, quinientos, mil):
    diez_b = (diez * 10)
    veinte_b = (veinte * 20)
    cincuenta_b = (cincuenta * 50)
    cien_b = (cien * 100)
    doscientos_b = (doscientos * 200)
    quinientos_b = (quinientos * 500)
    mil_b = (mil * 1000)
    total_tips = diez_b + veinte_b + cincuenta_b + cien_b + quinientos_b + mil_b

    return total_tips, diez_b, veinte_b, cincuenta_b, cien_b, dosciento_b, quinientos_b, mil_b


total_tips, diez_b, veinte_b, cincuenta_b, cien_b, dosciento_b, quinientos_b, mil_b = calculator(diez, veinte,
                                                                                                 cincuenta, cien,
                                                                                                 quinientos, mil)

print()
print(f" Total Tips: {total_tips} ")
print()
print(f"Cantidad en $10 {diez} ")
print(f" Total en billetes de $10: {diez_b} ")
print()
print(f"Cantidad en $20 {veinte} ")
print(f" Total en billetes de $20: {veinte_b} ")
print()
print(f"Cantidad en $50 {cincuenta} ")
print(f" Total en billetes de $50: {cincuenta_b} ")
print()
print(f"Cantidad en $100 {cien} ")
print(f" Total en billetes de $100: {cien_b} ")
print()
print(f"Cantidad en $200 {dlscientos} ")
print(f" Total en billetes de $100: {doscientos_b} ")
print()
print(f"Cantidad en $500 {quinientos} ")
print(f" Total en billetes de $500: {quinientos_b} ")
print()
print(f"Cantidad en $1000 {mil} ")
print(f" Total en billetes de $1000: {mil_b} ")
print()
print("♫♪♬🎶 Vaya por mas money Mr. ♫♪♬🎶")
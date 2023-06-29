diez = int(input("Ingresa los de $10: "))
veinte = int(input("Ingresa los $20: "))
cincuenta = int(input("Ingresa los de $50: "))
cien = int(input("Ingresa los de $100: "))
quinientos = int(input("Ingresa los $500: "))
mil = int(input("Ingresa los $1000: "))


def calculator(diez, veinte, cincuenta, cien, quinientos, mil):
    diez_b = (diez * 10)
    total_tips = diez + veinte + cincuenta + cien + quinientos + mil

    return total_tips, diez_b


diez_b, total_tips = calculator(diez, veinte, cincuenta, cien, quinientos, mil)

print(total_tips)
print()
print(f" Cantidad en $10 {diez} ")
print(f"Total en billetes de $10: {diez_b} ")
print()
print(f"Total en billetes de $20: {veinte} ")
print()
print(f"Total en billetes de $50: {cincuenta} ")
print(f"Total en billetes de $100: {cien} ")
print(f"Total en billetes de $500: {quinientos} ")
print(f"Total en billetes de $1000: {mil} ")
print("♫♪♬🎶 Paga lo que debe come Chocolate ♫♪♬🎶")
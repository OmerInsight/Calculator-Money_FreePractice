diez = int(input("Ingresa los de $10: "))
veinte = int(input("Ingresa los $20: "))
cincuenta = int(input("Ingresa los de $50: "))
cien = int(input("Ingresa los de $100: "))
quinientos = int(input("Ingresa los $500: "))
mil = int(input("Ingresa los $1000: "))


def calculator(t, v, w, x, y, z):
    total_tips = t + v + w + x + y + z

    return total_tips


total_tips = calculator(diez, veinte, cincuenta, cien, quinientos, mil)

print(total_tips)
print()
print(f"Total en billetes de $10: {diez} ")
print()
print(f"Total en billetes de $20: {veinte} ")
print()
print(f"Total en billetes de $50: {cincuenta} ")
print(f"Total en billetes de $100: {cien} ")
print(f"Total en billetes de $500: {quinientos} ")
print(f"Total en billetes de $1000: {mil} ")
print("♫♪♬🎶 Paga lo que debe come Chocolate ♫♪♬🎶")

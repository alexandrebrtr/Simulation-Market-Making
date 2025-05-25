import random
import matplotlib.pyplot as plt

# Paramètres de base
initial_price = 100.0
spread = 0.5
inventory = 0
cash = 0
price = initial_price
price_history = []
inventory_history = []
cash_history = []

# Simulation de 1000 ticks de marché
for t in range(1000):
    mid_price = price

    # Market maker place ses ordres
    bid = mid_price - spread / 2
    ask = mid_price + spread / 2

    # Simuler une interaction client : un ordre frappe bid ou ask (ou rien)
    action = random.choices(["hit_bid", "hit_ask", "none"], weights=[0.4, 0.4, 0.2])[0]

    if action == "hit_bid":
        # Client vend, market maker achète
        inventory += 1
        cash -= bid
        price = bid
    elif action == "hit_ask":
        # Client achète, market maker vend
        inventory -= 1
        cash += ask
        price = ask
    else:
        # Pas de transaction
        price += random.uniform(-0.1, 0.1)  # petite variation aléatoire

    # Historique
    price_history.append(price)
    inventory_history.append(inventory)
    cash_history.append(cash + inventory * price)  # valeur portefeuille = cash + inventaire * prix

# Résultats
plt.figure(figsize=(12, 6))
plt.subplot(2, 1, 1)
plt.plot(price_history, label="Prix")
plt.plot(cash_history, label="Valeur portefeuille")
plt.legend()
plt.title("Prix et PnL")

plt.subplot(2, 1, 2)
plt.plot(inventory_history, label="Inventaire")
plt.legend()
plt.title("Inventaire du market maker")
plt.tight_layout()
plt.show()

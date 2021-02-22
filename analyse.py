import matplotlib.pyplot as plt

plt.title("Danger de la vitesse")
plt.plot([50, 100, 150, 200], [1, 2, 3, 4], "r--", linewidth=5)
plt.plot([50, 100, 150, 200], [2, 3, 7, 10], "b", linewidth=3)
plt.plot([50, 100, 150, 200], [2, 7, 9, 10], "g", linewidth=10)
plt.grid(True)
plt.xlabel('Vitesse')
plt.ylabel('Temps')
plt.show()

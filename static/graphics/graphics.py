import matplotlib.pyplot as plt
import matplotlib.image as mpimg

pets = ["Suns", "Kaķis", "Grauzējis"]
descriptions = [
    "Uzticams draugs un kompanjons",
    "Neatkarīgs un mīlīgs mājdzīvnieks",
    "Mazi, bet interesanti"
]
suitability = [
    "Aktīviem cilvēkiem, ģimenēm ar bērniem",
    "Cilvēkiem, kuri novērtē mājīgumu un klusumu",
    "Cilvēkiem ar nelielu dzīves telpu"
]
considerations = [
    "Nepieciešama uzmanība, apmācība, pastaigas",
    "Patstāvīgs, bet arī prasa uzmanību",
    "Aizņem maz vietas, bet prasa rūpes"
]

fig, ax = plt.subplots(figsize=(8, 5))

ax.axis("off")

plt.text(0.5, 1.1, "Kāds mājdzīvnieks jums ir piemērots?", fontsize=20, ha="center", fontweight="bold")

for i, pet in enumerate(pets):
    y_pos = 1 - (i + 1) * 0.3  

    plt.text(0.15, y_pos, pet, fontsize=15, fontweight="bold")
    plt.text(0.35, y_pos, descriptions[i], fontsize=7)
    plt.text(0.55, y_pos, suitability[i], fontsize=7)
    plt.text(0.75, y_pos, considerations[i], fontsize=7)

plt.show()

import matplotlib.pyplot as plt


categories = ["Uzturs", "Higiēna", "Veselība", "Aktivitāte"]
pets = ["Kaķi", "Suni", "Grauzēji"]


care_data = [
    ["Sausa/mitra barība", "Sausa/mitra barība", "Graudi"],  # Uzturs
    ["Jāpārbauda ausis, acis, zobus", "Nagi jāapgriež reizi 2 nedēļās", "Pakaišus jāmaina pēc 3 dienām"],  # Higiēna
    ["Vakcinācija reizi gadā", "Vakcinācija reizi gadā", "Nepieciešami kociņi"],  # Veselība
    ["Spēlēt ar rotaļlietam", "Jāizveid pastaigā 2 reizes dienā", "Skriešanas ritenis"]   # Aktivitāte
]


fig, ax = plt.subplots(figsize=(8, 4))
ax.axis("tight")
ax.axis("off")


table_data = [[""] + pets]  


for i in range(len(categories)):
    row = [categories[i]] + care_data[i]  
    table_data.append(row)


table = ax.table(cellText=table_data, cellLoc="center", loc="center")


table.auto_set_font_size(False)
table.set_fontsize(14)


for i in range(len(pets) + 1):
    table[(0, i)].set_fontsize(16)
    table[(0, i)].set_text_props(weight="bold")

for i in range(len(categories)):
    table[(i + 1, 0)].set_fontsize(16)
    table[(i + 1, 0)].set_text_props(weight="bold")


plt.title("Mājdzīvnieku kopšanas ceļvedis", fontsize=16, fontweight="bold")
plt.show()
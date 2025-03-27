import matplotlib.pyplot as plt


regions = ["Rīga", "Pierīga", "Jūrmala", "Vidzeme", "Latgale"]
shelter_counts = [2, 2, 1, 1, 1]  


plt.figure(figsize=(7, 7))
plt.pie(shelter_counts, labels=regions, autopct="%1.1f%%", startangle=140, 
        colors=["lightblue", "lightgreen", "orange", "red", "purple"])


plt.title("Dzīvnieku patversmju sadalījums pa reģioniem Latvijā")


plt.show()
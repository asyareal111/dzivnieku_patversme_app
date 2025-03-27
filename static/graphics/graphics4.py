import pandas as pd


data = {
    "Nosaukums": [
        "Dzīvnieku draugs", "Juglas suņu patversme", "Dzīvnieku pansija Ulubele",
        "Slokas dzīvnieku patversme", "Mežavairogi", "Ogres Ķepas", "Otrā māja"
    ],
    "Adrese": [
        "Fridriha Candera iela 4, Rīga", "Juglas iela 18, Rīga", "Līči, Stopiņu novads",
        "Dzirnavu iela 8, Sloka, Jūrmala", "Mežavairogi, Ķekavas novads", "Indrānu iela 9/11, Ogre",
        "Vezi-1, Demenes pagasts, Daugavpils novads"
    ],
    "Telefons": [
        "67500491", "67532630, 22493377", "20203333, 67705593",
        "26134093", "29139149", "26342330, 65044224", "20045442, 29790219"
    ],
    "Vietne": [
        "dzd.lv", "patversme.lv", "ulubele.org", 
        "slokaspatversme.lv", "mezavairogi.lv", "ogreskepas.lv", "otramaja.lv"
    ]
}

df = pd.DataFrame(data)


filtered_df = df[df["Adrese"].str.contains("Jūrmala")]


print(filtered_df)
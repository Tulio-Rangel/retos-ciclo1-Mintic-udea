import random

balotas = [
    "B1",
    "B2",
    "B3",
    "B4",
    "B5",
    "B6",
    "B7",
    "B8",
    "B9",
    "B10",
    "B11",
    "B12",
    "B13",
    "B14",
    "B15",
    "I16",
    "I17",
    "I18",
    "I19",
    "I20",
    "I21",
    "I22",
    "I23",
    "I24",
    "I25",
    "I26",
    "I27",
    "I28",
    "I29",
    "I30",
    "N31",
    "N32",
    "N33",
    "N34",
    "N35",
    "N36",
    "N37",
    "N38",
    "N39",
    "N40",
    "N41",
    "N42",
    "N43",
    "N44",
    "N45",
    "G46",
    "G47",
    "G48",
    "G49",
    "G50",
    "G51",
    "G52",
    "G53",
    "G54",
    "G55",
    "G56",
    "G57",
    "G58",
    "G59",
    "G60",
    "O61",
    "O62",
    "O63",
    "O64",
    "O65",
    "O66",
    "O67",
    "O68",
    "O69",
    "O70",
    "O71",
    "O72",
    "O73",
    "O74",
    "O75",
]

letras_b = []
letras_i = []
letras_n = []
letras_g = []
letras_o = []

a = 0
for i in range(10):
    a = random.choice(balotas)
    if "B" in a:
        letras_b.append(a)
    elif "I" in a:
        letras_i.append(a)
    elif "N" in a:
        letras_n.append(a)
    elif "G" in a:
        letras_g.append(a)
    elif "O" in a:
        letras_o.append(a)

print(letras_b)
print(letras_i)
print(letras_n)
print(letras_g)
print(letras_o)

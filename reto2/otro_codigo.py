def calcular_promedio_y_cuadro_honor(grupo):
    # ACÁ INICIA LA FUNCIÓN SOLUCIÓN (En este espacio debes entregar tu solución)
    honor_student = []
    cuadro_honor = []
    listaNotas = []
    pos1 = []
    pos2 = []
    pos3 = []
    acum_nota = 0.0
    puesto1 = 0.0
    puesto2 = 0.0
    puesto3 = 0.0
    # ****************************************
    for a in grupo:
        listaNotas.append(float(a["nota_fundamentos"]))
    listaNotas.sort(reverse=True)
    # ****************************************
    for i in range(len(listaNotas)):

        nota = float(listaNotas.pop(0))
        acum_nota += nota
        # Obtenemos el puesto N° 1
        if nota > puesto1:
            puesto1 = nota
            honor_student.append(nota)
            nota = 0
        if nota == puesto1 and nota > 0:
            if nota == puesto1:
                nota = 0
        # Obtenemos el puesto N° 2
        if nota > puesto2 and puesto2 < puesto1:
            puesto2 = nota
            honor_student.append(nota)
            nota = 0
        if nota == puesto2 and nota > 0:
            nota = 0
        # Obtenemos el puesto N° 3
        if nota > puesto3 and puesto3 < puesto2:
            puesto3 = nota
            honor_student.append(nota)
            nota = 0

    # ****************************************
    for i in grupo:
        cuadro_honor.append(i["nota_fundamentos"])
        cuadro_honor.append(i["cédula"])
    # ****************************************
    for i in range(0, len(cuadro_honor), 2):
        if float(cuadro_honor[i]) == honor_student[0]:
            pos1.append(cuadro_honor[(i + 1)])
        if float(cuadro_honor[i]) == honor_student[1]:
            pos2.append(cuadro_honor[(i + 1)])
        if float(cuadro_honor[i]) == honor_student[2]:
            pos3.append(cuadro_honor[(i + 1)])
    # ****************************************
    promedio = acum_nota / len(grupo)
    cuadro_honor = {1: pos1, 2: pos2, 3: pos3}
    return promedio, cuadro_honor


# ****************************************
estudiante1 = {"cédula": "00032145678", "nombre": "Valen", "nota_fundamentos": 3}

estudiante2 = {"cédula": "1067678654", "nombre": "Cris", "nota_fundamentos": 4.5}

estudiante3 = {"cédula": "45677890", "nombre": "John", "nota_fundamentos": 4.5}

estudiante4 = {"cédula": "72033405", "nombre": "Carmen", "nota_fundamentos": 4.5}

estudiante5 = {"cédula": "89245678", "nombre": "Jordan", "nota_fundamentos": 4.5}

estudiante6 = {"cédula": "89766345", "nombre": "Pedro", "nota_fundamentos": 2.3}

estudiante7 = {"cédula": "1045789098", "nombre": "Camilo", "nota_fundamentos": 3.7}

grupo = [
    estudiante1,
    estudiante2,
    estudiante3,
    estudiante4,
    estudiante5,
    estudiante6,
    estudiante7,
]
print(calcular_promedio_y_cuadro_honor(grupo))

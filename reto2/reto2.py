estudiante1 = {
    'cédula': '1',
    'nombre': 'Juancho',
    'nota_fundamentos': 4.5
}
estudiante2 = {
    'cédula': '2',
    'nombre': 'Pedro',
    'nota_fundamentos': 4.2
}
estudiante3 = {
    'cédula': '3',
    'nombre': 'Clara',
    'nota_fundamentos': 4.6
}
estudiante4 = {
    'cédula': '4',
    'nombre': 'Mafe',
    'nota_fundamentos': 4.1
}
estudiante5 = {
    'cédula': '5',
    'nombre': 'Juancha',
    'nota_fundamentos': 4.0
}
estudiante6 = {
    'cédula': '6',
    'nombre': 'Trosky',
    'nota_fundamentos': 4.6
}
estudiante7 = {
    'cédula': '7',
    'nombre': 'Diógenes',
    'nota_fundamentos': 4.2
}
grupillo = [estudiante1, estudiante2, estudiante3, estudiante4, estudiante5, estudiante6, estudiante7]

def calcular_promedio_y_cuadro_honor(grupo):
    team = grupo
    notas = []

    for i in team:
        notas.append(i['nota_fundamentos'])

    promedio = float(sum(notas)/len(notas))

    primero = 0
    segundo = 0
    tercero = 0
    aux = 0
    aux2 = 0
    aux3 = 0
    cuadro_honor = {}

    for i in team:
        if i['nota_fundamentos'] > primero:
            primero = i['nota_fundamentos']
            aux = [i['cédula']]
        elif i['nota_fundamentos'] == primero:
            aux = aux + [i['cédula']]

    cuadro_honor[1] = aux

    for i in team:
        if i['nota_fundamentos'] > segundo and i['nota_fundamentos'] != primero:
            segundo = i['nota_fundamentos']
            aux2 = [i['cédula']]
        elif i['nota_fundamentos'] == segundo:
            aux2 = aux2 [i['cédula']]

    cuadro_honor[2] = aux2

    for i in team:
        if i['nota_fundamentos'] > tercero and i['nota_fundamentos'] not in (primero, segundo):
            tercero = i['nota_fundamentos']
            aux3 = [i['cédula']]
        elif i['nota_fundamentos'] == tercero:
            aux3 = aux3 + [i['cédula']]

    cuadro_honor[3] = aux3

    print([promedio, cuadro_honor])
    
    return promedio, cuadro_honor

calcular_promedio_y_cuadro_honor(grupillo)
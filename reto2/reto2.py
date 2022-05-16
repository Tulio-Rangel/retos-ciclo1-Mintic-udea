estudiante1 = {
    'cédula': '1234564567',
    'nombre': 'Juancho',
    'nota_fundamentos': 4.5
}
estudiante2 = {
    'cédula': '1034464463',
    'nombre': 'Pedro',
    'nota_fundamentos': 4.2
}
estudiante3 = {
    'cédula': '1000564566',
    'nombre': 'Clara',
    'nota_fundamentos': 4.6
}
estudiante4 = {
    'cédula': '1300564367',
    'nombre': 'Mafe',
    'nota_fundamentos': 4.1
}
estudiante5 = {
    'cédula': '1030561507',
    'nombre': 'Juancha',
    'nota_fundamentos': 4.0
}
estudiante6 = {
    'cédula': '1204504462',
    'nombre': 'Trosky',
    'nota_fundamentos': 4.6
}
estudiante7 = {
    'cédula': '1054062533',
    'nombre': 'Diógenes',
    'nota_fundamentos': 4.2
}

grupo = [estudiante1, estudiante2, estudiante3, estudiante4, estudiante5, estudiante6, estudiante7]
notas = []

for i in grupo:
    notas.append(i['nota_fundamentos'])

promedio = float(sum(notas)/len(notas))

primero = 0
segundo = 0
tercero = 0
cuadro_honor = {}

for i in grupo:
    if i['nota_fundamentos'] > primero:
        primero = i['nota_fundamentos']
        aux = [i['cédula']]
    elif i['nota_fundamentos'] == primero:
        aux += [i['cédula']]

cuadro_honor[1] = aux

for i in grupo:
    if i['nota_fundamentos'] > segundo and i['nota_fundamentos'] != primero:
        segundo = i['nota_fundamentos']
        aux2 = [i['cédula']]
    elif i['nota_fundamentos'] == segundo:
        aux2 += [i['cédula']]

cuadro_honor[2] = aux2

for i in grupo:
    if i['nota_fundamentos'] > tercero and i['nota_fundamentos'] not in (primero, segundo):
        tercero = i['nota_fundamentos']
        aux3 = [i['cédula']]
    elif i['nota_fundamentos'] == tercero:
        aux3 += [i['cédula']]

cuadro_honor[3] = aux3

print(cuadro_honor)
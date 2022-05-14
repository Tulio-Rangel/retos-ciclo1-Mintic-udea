import operator

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
    'nota_fundamentos': 3.9
}
estudiante7 = {
    'cédula': '1054062533',
    'nombre': 'Diógenes',
    'nota_fundamentos': 3.8
}

grupo = [estudiante1, estudiante2, estudiante3, estudiante4, estudiante5, estudiante6, estudiante7]
notas = []

for i in grupo:
    notas.append(i['nota_fundamentos'])

promedio = float(sum(notas)/len(notas))

print(max(grupo, key=operator.itemgetter('nota_fundamentos'))['cédula'])

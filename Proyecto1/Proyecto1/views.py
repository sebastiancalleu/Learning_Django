from django.http import HttpResponse


def edad(request, ano, edad):
    periodo = ano -2019
    edadfutura = edad + periodo
    documento = """<html><body><h1>Esta sera tu edad en el año {}: {}</h1></body></html>""".format(ano, edadfutura)
    return HttpResponse(documento)
from django.http import HttpResponse
import datetime

def saludo(request):

    return HttpResponse("Hola mundo")

def damefecha(request):
    fecha_actual = datetime.datetime.now()

    documento = """ <html>
    <body>
    <h1> Fecha y hora actuales: {}</h1>
    </body>
    </html>
    """.format(fecha_actual)

    return HttpResponse(documento)


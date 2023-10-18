from django.http import HttpResponse
from django.template import Template, Context
import datetime

def saludo(request):
	return HttpResponse("Hola Django - Coder")

def segunda_vista(request):
    return HttpResponse("<br><hr>Ya entendimos esto, es muy simple :) ")

def diaDeHoy(request):
        dia = datetime.datetime.now()
        documentoDeTexto = f"Hoy es día: <br> {dia}"
        return HttpResponse(documentoDeTexto)
    
def miNombreEs(self, nombre):
    documentoDeTexto = f"Mi nombre es: <br><hr>  {nombre}"
    return HttpResponse(documentoDeTexto)


def probandoTemplate(self):
    miHtml = open("C:/Users/Admin/Desktop/tareas/My_repo1/SoyYO/templates/SoyYO/index.html")
    plantilla = Template(miHtml.read()) #Se carga en memoria nuestro documento, index   
    ##OJO importar template y contex, con: from django.template import Template, Context
    miHtml.close() #Cerramos el archivo
    miContexto = Context() #EN este caso no hay nada ya que no hay parametros, IGUAL hay que crearlo
    documento = plantilla.render(miContexto) #Aca renderizamos la plantilla en documento
    return HttpResponse(documento)

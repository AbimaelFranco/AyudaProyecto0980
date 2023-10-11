from django.shortcuts import render

from .models import perfiles

#Se carga la vista perfiles en la que se muestran todos los registros
def mostrar_perfiles(request):

    #Funciones de ORM
    
    perfiles_completos = perfiles.objects.all()    #Se obtienen todos los registros del modelo

    # per.delete()  #Permite eliminar todos los registros

    # perfiles.objects.create(nickname="usuario1", nombre="Nombre1", apellido="Apellido1", correo="usuario1@example.com")   #Permite crear un registro en una sola linea

    # perfil1 = perfiles(nickname="Alexander", nombre="Alexander", apellido="Franco", correo="correo1@example.com")    #Crea un objeto tipo perfiles que luego se guarda con save()
    # perfil1.save()  #Se salva el perfil1

    # perfil = Perfil.objects.get(nickname="usuario1")  #Filtrado de registros

    # perfiles = Perfil.objects.filter(nombre="Nombre1")    #Filtrado de registros

    # perfil = perfiles.objects.get(nickname="usuario1")    #Actualizacion de registros
    # perfil.nombre = "NuevoNombre"
    # perfil.save()

    #Debug para ver que todo este bien
    for perfili in perfiles_completos:
        print(f"ID: {perfili.id}")   #Obtiene el atributo id del perfil i-esimo
        print(f"Nickname: {perfili.nickname}")  #Obtiene el atributo nickname del perfil i-esimo
        print(f"Nombre: {perfili.nombre}")  #Obtiene el atributo nombre del perfil i-esimo
        print(f"Apellido: {perfili.apellido}") #Obtiene el atributo apellido del perfil i-esimo
        print(f"Correo: {perfili.correo}")  #Obtiene el atributo correo del perfil i-esimo
        print("-" * 20)  # Línea divisoria opcional para separar los registros

    return render(request, 'main/mostrar_perfiles.html', {'perfiles': perfiles_completos})
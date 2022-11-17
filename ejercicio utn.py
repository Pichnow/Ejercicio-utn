Python 3.10.0 (tags/v3.10.0:b494f59, Oct  4 2021, 19:00:18) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
respuesta = 's'
cant_estudios_primarios = 0
porcentaje_analfabeto = 0
mayor_cant_integrantes = 0
edad_promedio_domicilio = 0
edad_promedio_total = 0
acumulador_edad = 0
cant_no_posee = 0
cant_primario  = 0 
cant_secundario  = 0 
cant_terciario = 0 
cant_universitario  = 0
porcentaje_masc = 0
porcentaje_fem = 0
 
 
while (respuesta == 's'):
  Domicilio = input ("domicilio: ")
  tipo_vivienda = input("tipo de vivienda C(casa)/D(departamento): ")
  cantidad_hab = int(input("cantidad de habitantes: "))
  for h in range(1, cantidad_hab+1):
    nombre = input("nombre del habitante:")
    apellido = input("apellidos del habitante: ")
    edad= int(input("edad: "))
    acumulador_edad += edad
    sexo = input("sexo F/M: " )
    estudios = input("""
    estudios:
    N: no posee
    P: primario
    S: secundario
    T: terciario
    U: universitario""")
    if (estudios == 'P'):
      cant_primario +=1
    if (estudios == 'S'):
      cant_secundario +=1
    if (estudios == 'T'):
      cant_terciario +=1
    if (estudios == 'U'):
      cant_universitario +=1
    if (estudios == 'N'):
      cant_no_posee +=1
    estado_estudio = input("Estudios C(Completo)/I(Incompleto): ")
  respuesta = input("desea censar otro domicilio s/n: ")
  
 
 
 

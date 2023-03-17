def datos():
    print('\n')
    print("Franz Soria")
    print("Carrera:ingenieria de sistemas")
    print("Universidad:USFX")
    print("Facultad de Tecnologia")
    print("Ciudad de Sucre-Bolivia")
    print('\n')


accion = True
while accion:
    datos()
    print("1 imprimir  0 salir")
    seleccion = int(input("Seleccione:"))
    if seleccion == 0:
        accion = False
        print("Finalizado")

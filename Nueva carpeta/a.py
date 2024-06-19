import json,os

idB = 0
opcion = -1
opcionC= 0

def limpiar_pantalla():
    os.system('cls' if os.name == 'nt' else 'clear')

while opcion!=0:
    limpiar_pantalla()

    print("*********************************")
    print("*         Happy Store           *")
    print("*********************************")
    print("1 - Mantenedor de Servicios")
    print("2 - Tienda")
    print("3 - Reportes")
    print("0 - Salir")
    print("*********************************")

    try:
        opcion=int(input("Seleccione una opcion: "))

        if opcion==1:
            while opcionC!=5:
                limpiar_pantalla()

                print("*********************************")
                print("*         Happy Store           *")
                print("*********************************")
                print("1 - Mantenedor de Productos")
                print("2 - Mantenedor de Usuarios") 
                print("3 - Mantenedor de Vendedores")
                print("4 - Mantenedor de Boletas")
                print("5 - Regresar")
                print("*********************************")

                opcionC=int(input("Seleccione una opcion: "))

                if opcionC==1:
                    with open ("compras.json","r") as archivojsproduc:
                        leerproductos=json.load(archivojsproduc)
                        productos=[]
                        productos.append(leerproductos["productos"])

                    with open ("comprasProd.json","w") as archivojsproduc:
                        json.dump(productos,archivojsproduc,indent=4)

                elif opcionC==2:

                    with open ("comprasProd.json","r") as archivojsusuario:
                        leerusuarios=json.load(archivojsusuario)
                        usuarios=[]
                        usuarios.append(leerproductos["clientes"])

                    with open ("comprasUsu.json","w") as archivojsusuario:
                        json.dump(usuarios,archivojsusuario,indent=4)
                elif opcionC==3:

                    with open ("compras.json","r") as archivojsvendedores:
                        leervendedores=json.load(archivojsvendedores)
                        vendedores=[]
                        vendedores.append(leervendedores["vendedores"])

                    with open ("comprasVend.json","w") as archivojsvendedores:
                        json.dump(vendedores,archivojsvendedores,indent=4)

                elif opcionC==4:

                    print("Dame la id de la boleta")
                    idB=int(input(""))

                    with open("compras.json","r") as boletaid:

                        leerjson=json.load(boletaid)

                        for i in leerjson["detalle_boletas"]:
                            if i['id_boleta']== idB:
                                print(i)

                elif opcionC== 5:
                    input("Presione Enter para continuar...")
                    break

        if opcion == 2:




        if opcion == 0:
            break

    except ValueError:
        print("Entrada inválida. Por favor, ingrese un número.")
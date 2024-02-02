import os.path



resp = 0

while resp !=6:

    print("Menú, elixe unha opción: ")
    print("1) Crear un directorio")
    print ("2) Comprobar o contido do directorio")
    print ("3) Cambiar de directorio no que te atopas")
    print ("4) Abrir o editor de texto")
    print ("5) Borrar un directorio/arquivo")
    print ("6) Sair")
    
    
    resp = int(input(""))

    os.system('clear')

    match resp:
        case 1:
            print("Escribe o nome do directorio que queres crear:")
            dir1 = input()

            os.system('clear')

            os.mkdir(dir1)

            print("O directorio creouse satisfactoriamente")
            input("Preme enter para volver ao menu")

            os.system('clear')


        case 2:
            print("Contido deste directorio:")
            print(os.listdir())


        case 3:
            print("Escribe o nome do directorio ao que quere ingresar")
            print("Contido deste directorio:")
            print(os.listdir())
            ruta = input("(Tip: no caso de querer retroceder, introducir '..')")
            
            os.system('cd ' + ruta)


        case 2:
            print("po")


        case 6:
            print("")


## Notas: os.removedirs(name), os.remove(path, *, dir_fd=None)   

import os.path
import time



resp = 0

while resp !=6:

    print("Menú, elixe unha opción: ")
    print("1) Crear un directorio")
    print ("2) Comprobar o contido do directorio")
    print ("3) Calculadora")
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

            print("")
            print("")

            input("Preme enter para volver ao menu")
            os.system('clear')


        case 3:

            print("Que operacion queres realizar?")
            print("1) Suma")
            print("2) Resta")
            print("3) Multiplicación")
            print("4) División")
            
            calc=int(input(""))

            os.system('clear')

            if calc == 1:

                print("Introduce un número enteiro:")
                num1 = int(input())

                os.system('clear')

                print("Introduce outro número enteiro:")
                num2 = int(input())

                os.system('clear')

                num3 = num1 + num2

                print(f"{num1} + {num2} = {num3}")


            if calc == 2:

                print("Introduce un número enteiro:")
                num1 = int(input())

                os.system('clear')

                print("Introduce outro número enteiro:")
                num2 = int(input())

                os.system('clear')

                num3 = num1 - num2

                print(f"{num1} - {num2} = {num3}")


            if calc == 3:

                print("Introduce un número enteiro:")
                num1 = int(input())

                os.system('clear')

                print("Introduce outro número enteiro:")
                num2 = int(input())

                os.system('clear')

                num3 = num1 * num2

                print(f"{num1} * {num2} = {num3}")


            if calc == 4:

                print("Introduce un número enteiro:")
                num1 = int(input())

                os.system('clear')

                print("Introduce outro número enteiro:")
                num2 = int(input())

                os.system('clear')


                if num2 == 0:
                    
                    print("Non se pode dividir entre cero")

                else:
                   
                    num3 = num1 / num2

                    print(f"{num1} / {num2} = {num3}")


            print("")
            print("")

            input("Preme enter para volver ao menu")
            os.system('clear')


        case 4:

            print("Escribe o nome do arquivo que queres abrir/crear (con extensión):")
            file = input()

            os.system('nano ' + file)

            os.system('clear')


        case 5:

            print("Que tipo de arquivo queres eliminar? (escribe o número)")
            print("1) directorio")
            print("2) arquivo")
            print("3) cambiéi de opinión, quero volver ao menú")
            option=int(input(""))

            os.system('clear')

            if option == 1:

                print("Contido do directorio:")
                print(os.listdir())
                print("Escribe o nome do directorio que queres eliminar (comproba que esté baleiro):")
                dir2=input("")
                
                os.system('clear')

                os.system('rmdir ' + dir2)

                print("O directorio eliminouse correctamente")


            if option == 2:
            
                print("Contido do directorio:")
                print(os.listdir())
                print("Escribe o nome do arquivo que queres eliminar:")
                arq3=input("")
                
                os.system('clear')

                os.system('rm ' + arq3)

                print("O arquivo eliminouse correctamente")



            input("Preme enter para volver ao menu")
            os.system('clear')


        case 6:
            print("")


        case other:

            print("Non existe esa opción, elixe outra do menú")
            time.sleep(3)
            os.system('clear')


import texto_menus
import profesores




def menu_admin():
    while True:

        #menu principal admin
        opcion = texto_menus.opciones_principal()

        #salir del programa
        if opcion == "0":
            exit()

        #gestion profesores
        if opcion == "1":
            while True: 
                opcion = texto_menus.opciones_profesores()

                if opcion == "0":
                    break
                
                #añadir profesor
                elif opcion == "1":
                    profesores.añadir_profesor()

                #eliminar profesor
                elif opcion == "2":
                    profesores.eliminar_profesor()
                
                #modificar profesor
                elif opcion == "3":
                    profesores.modificar_profesor()
                
                #modificar materias profesor
                elif opcion == "4":
                    pass

                #lista profesores
                elif opcion == "5":
                    profesores.listar_profesores()

        elif opcion == "2":
            while True: 
                opcion = texto_menus.opciones_alumno()

                if opcion == "0":
                    break
                
                #añadir profesor
                elif opcion == "1":
                    profesores.añadir_profesor()

                #eliminar profesor
                elif opcion == "2":
                    profesores.eliminar_profesor()
                
                #modificar profesor
                elif opcion == "3":
                    profesores.modificar_profesor()
                
                #modificar materias profesor
                elif opcion == "4":
                    pass

                #lista profesores
                elif opcion == "5":
                    profesores.listar_profesores()



menu_admin()



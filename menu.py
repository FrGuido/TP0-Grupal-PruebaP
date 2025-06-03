import texto_menus





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

                elif opcion == "1":
                    pass

                elif opcion == "2":
                    pass

                elif opcion == "3":
                    pass

                elif opcion == "4":
                    pass






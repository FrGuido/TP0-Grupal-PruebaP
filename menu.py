import menu_texto
import profesores
import alumnos
import materias
import cursos




def menu_admin():
    while True:

        #menu principal admin
        opcion = menu_texto.opciones_principal()

        #salir del programa
        if opcion == "0":
            exit()

        #gestion profesores
        if opcion == "1":
            while True: 
                opcion = menu_texto.opciones_profesores()

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

                #lista profesores
                elif opcion == "4":
                    profesores.listar_profesores()

        #gestion alumnos
        elif opcion == "2":
            while True: 
                opcion = menu_texto.opciones_alumno()

                if opcion == "0":
                    break
                
                #añadir alumno
                elif opcion == "1":
                    alumnos.añadir_alumno()

                #eliminar alumnos
                elif opcion == "2":
                    alumnos.eliminar_alumno()
                
                #modificar alumnos
                elif opcion == "3":
                    alumnos.modificar_alumno()
                
                #modificar notas alumno
                elif opcion == "4":
                    pass

                #listar alumnos por curso
                elif opcion == "5":
                    pass
    
        #gestion cursos
        elif opcion == "3":
            cursos.modificar_curso()
        
        #gestion de materias
        elif opcion == '4':
            while True: 
                opcion = menu_texto.opciones_alumno()

                if opcion == "0":
                    break
                
                #añadir materia
                elif opcion == "1":
                    materias.crear_materia()

                #eliminar materia
                elif opcion == "2":
                    materias.elimiar_materia()

                #modificar materai
                elif opcion == "3":
                    materias.modificar_materia()
                



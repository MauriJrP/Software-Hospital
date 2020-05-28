#practica 14
#rodriguez perez mauricio de jesus
#kevin arturo fernandez roman
from colorama import *; import msvcrt; import os; from time import sleep; from datetime import datetime; import random;
#-------------------------------------------------------------------------------------------------------------------------------------------------------------
def alta_pacientes():
	x1 = 20; y1 = 10; x2 = 130; y2 = 40;
	imprime = False; numero = False; cont_lineas = 20; cont_lineas = 20; num_paciente = 10000000000;
	ventanas(x1,x2,y1,y2,0)
	print(Cursor.POS(66,10)+Fore.CYAN+"ALTA DE PACIENTE");
	print(Cursor.POS(40,15)+ Fore.GREEN + "¿Estuviste registrado anteriormente en el hospital? si(s)/no(n)")
	cha = msvcrt.getch();
	if cha == b'n' or cha == b'N':  #Crea un perfil desde 0
	    os.system('cls')
	    ventanas(x1,x2,y1,y2,0)
	    print(Cursor.POS(66,10)+Fore.CYAN+"ALTA DE PACIENTE");
	    archivo = open("d03-p14-rodriguez-fernandez-P.txt", mode= "r", encoding="utf-8")  #Abre el archivo para buscar el numero de paciente mas alto
	    leer = archivo.read()
	    num_paciente = str(num_paciente)
	    while True: #Busca el ultimo numero de paciente creado
	        if num_paciente in leer:
	            nss = int(num_paciente) + 1
	            num_paciente = str(nss)
	        else:
	            break
	    nss = int(num_paciente)
	    #Datos a ingresar
	    now = datetime.now()
	    fecha = now.date()
	    while True:
	        nombre = str(input(Cursor.POS(52,15)+"Ingresa tu nombre completo: "))
	        if nombre != '' and nombre != ' ':
	            break;
	        else:
	            print(Cursor.POS(52,16) + Fore.RED +  "Nombre invalido...");
	            sleep(1);
	            print(Cursor.POS(52,16) + Fore.RED +  "                   ");
	            print(Cursor.POS(52,15) + "                                                             ");
	    while True:
	        try:
	        	edad = int(input(Cursor.POS(52,17)+"Ingresa tu edad: "))
	        	if edad >= 0 and edad <= 120:
	        		break;
	        	else:
	        		print(Cursor.POS(52,18)+Fore.RED+"Ingresa unicamente numeros positivos...");
	        		sleep(1);
	        		print(Cursor.POS(52,18)+Fore.RED+"                                                 ")
	        		print(Cursor.POS(52,17)+"                                                                        ")	
	        except ValueError:
	        	print(Cursor.POS(52,18)+Fore.RED+"Ingresa unicamente numeros...")
	        	sleep(1);
	        	print(Cursor.POS(52,18)+Fore.RED+"                                                    ")
	        	print(Cursor.POS(52,17)+"                                                                        ")	
	    while True:
	    	servicio = str(input(Cursor.POS(52,19)+"Ingresa el servicio: "));
	    	if servicio != '' and servicio != ' ':
	    		break;
	    	else:
	    		print(Cursor.POS(52,20)+Fore.RED+"Ingresa un dato valido...")
	    		sleep(1);
	    		print(Cursor.POS(52,20)+"                          ")
	    		print(Cursor.POS(52,19)+"                                                              ")
	    while True:
	    	historial = str(input(Cursor.POS(52,21)+"¿Tienes algun antecedente medico que debamos saber?:"));
	    	if historial != '' and historial != ' ':
	    		break;
	    	else:
	    		print(Cursor.POS(52,22)+Fore.RED+"Ingresa un dato valido...")
	    		sleep(1);
	    		print(Cursor.POS(52,22)+"                          ")
	    		print(Cursor.POS(52,21)+"                                                                ")
	    archivo = open("d03-p14-rodriguez-fernandez-P.txt", mode="a", encoding="utf-8")   #Abre el archivo para guardar los datos ingresados al final
	    #Agrega que dato es
	    fecha = "Fecha de alta: " + str(fecha)
	    nombre = "Nombre: " + nombre
	    edad = "Edad: " + str(edad)
	    servicio = "Servicio: " + servicio
	    historial = "Historial medico: " + historial
	    medicos = 'Medicos: Sin medicos asignados'
	    #Agrega datos al archivo txt
	    archivo.write("\n");archivo.write(str(nss));archivo.write("\n");archivo.write("Estado: Activo\n");archivo.write(fecha);archivo.write("\n");
	    archivo.write(nombre);archivo.write("\n");archivo.write(str(edad));archivo.write("\n");archivo.write(servicio);archivo.write("\n");archivo.write(historial);
	    archivo.write("\n");archivo.write(medicos);archivo.write('\n');archivo.close();
	    print(Cursor.POS(55,30)+Fore.GREEN+"Te has dado de alta con exito")
	    print(Cursor.POS(55,32)+"Tu numero de paciente es:", Fore.GREEN + str(nss))
	    print(Cursor.POS(55,34)+Fore.LIGHTRED_EX+"Tiene 11 digitos")
	    print(Cursor.POS(55,36) + "Presione una tecla para continuar...")
	    ch= msvcrt.getch();
	elif cha == b's' or cha == b'S':  #Cambia a estado activo un perfil ya existente
	    os.system('cls')
	    ventanas(x1,x2,y1,y2,0); c = 0;
	    print(Cursor.POS(66,10)+Fore.CYAN+"ALTA DE PACIENTE");
	    while True:
	    	try:
	    		num_paciente = int(input(Cursor.POS(50,15)+"Ingresa tu numero de paciente: "))
	    		break;
	    	except ValueError:
	    		print(Cursor.POS(50,16)+Fore.RED+"Ingresa unicamente numeros...")
	    		sleep(1);
	    		print(Cursor.POS(50,16)+Fore.RED+"                             ")
	    		print(Cursor.POS(50,15)+"                                                                        ")
	    string = str(num_paciente)
	    archivo = open("d03-p14-rodriguez-fernandez-P.txt", mode="r", encoding="utf-8")
	    c = 0; r = 0; fe_aux = '';
	    while True:
	    	linea = archivo.readline();
	    	if not linea:
	    		break;
	    	if '\n' in linea:
	    		linea = linea.replace(linea,linea[:-1]);
	    	if string in linea:
	    		c+=1; r+=1;
	    	if "Fecha de alta: " in linea and c == 1 and r == 1:
	    		print("entro aqui"); sleep(1)
	    		fe_aux = linea[15:];
	    		c+=1;
	    		print(fe_aux);
	    archivo.close();
	    now = datetime.now(); fech = now.date(); fech = str(fech)
	    estad = string + "\nEstado: Inactivo" + "\nFecha de alta: "+ str(fe_aux); estadi = string + "\nEstado: Activo";fech = estadi + '\nFecha de alta: '+ str(fech); 
	    digitos = len(string)
	    if digitos == 11:
	        archivo = open("d03-p14-rodriguez-fernandez-P.txt", mode="r", encoding="utf-8")   #Abre el archivo para leer
	        archivo2 = open("d03-p14-rodriguez-fernandez-P.txt", mode="r+", encoding="utf-8")  #Abre el archivo para editar el estado
	        leer = archivo.read()
	        if estad in leer:  #Busca que se encuentre el numero de paciente ingresado y que este en estado activo
	            archivo2.write(leer.replace(estad,fech))  #Remplaza el estado activo por inactivo
	            print(Cursor.POS(50,20)+Fore.GREEN+"Te has dado de alta con exito...")
	            c+=1
	            sleep(1);
	        else:
	            print(Cursor.POS(50,20)+Fore.RED +"No se encontro tu numero de paciente...")
	            sleep(1)
	        archivo.close()
	        archivo2.close()
	    else:
	        print(Cursor.POS(50,20)+Fore.RED + "No se encontro tu numero de paciente...")
	        sleep(1)
	else:
	    print(Cursor.POS(55,20) + Fore.RED + "Ese dato no es valido...")
	    sleep(1)
	os.system('cls')
	pass;
#-------------------------------------------------------------------------------------------------------------------------------------------------------------
def editar_pacientes():
	os.system('cls')
	x1 = 20; y1 = 10; x2 = 130; y2 = 40;cont_lineas = 20
	ventanas(x1,x2,y1,y2,0)
	datos_modificar = False; datos_modi = "";lista = [];  
	print(Cursor.POS(69,10) +Fore.CYAN+ "EDITAR PERFIL");
	while True:
	    try:
	    	num_paciente = int(input(Cursor.POS(50,15)+"Ingresa tu numero de paciente: "))
	    	break;
	    except ValueError:
	    	print(Cursor.POS(50,16)+Fore.RED+"Ingresa unicamente numeros...")
	    	sleep(1);
	    	print(Cursor.POS(50,16)+Fore.RED+"                             ")
	    	print(Cursor.POS(50,15)+"                                                                        ")	
	archivo = open("d03-p14-rodriguez-fernandez-P.txt", mode="r", encoding="utf-8")
	leer1 = archivo.read()
	archivo.close()
	string = str(num_paciente)
	digitos = len(string)
	if digitos == 11:
	    if string in leer1:
	        os.system('cls')
	        ventanas(x1,x2,y1,y2,0)
	        print(Cursor.POS(69,10) +Fore.CYAN+ "EDITAR PERFIL");
	        print(Cursor.POS(50,14)+Fore.GREEN+"Datos modificables:")
	        print(Cursor.POS(50,15)+"1-. Nombre")
	        print(Cursor.POS(50,16)+"2-. Edad")
	        print(Cursor.POS(50,17)+"3-. Servicio")
	        print(Cursor.POS(50,18)+"4-. Antecedentes medicos")
	        while True:
	        	editar = str(input(Cursor.POS(50,20)+Fore.GREEN+"¿Que dato quieres modificar?: "+Fore.RESET));
	        	if editar == "1" or editar == "2" or editar == "3" or editar == "4":
	        		break;
	        	else:
	        		print(Cursor.POS(50,21)+Fore.RED+"Elige una opcion valida...")
	        		sleep(1)
	        		print(Cursor.POS(50,21)+"                             ")
	        		print(Cursor.POS(50,20)+"                                                                 ")
	        if editar == "1":
	            tipo_dato = "Nombre: "
	            while True:
	            	dato = str(input(Cursor.POS(50,22)+"Ingresa tu nombre: "));
	            	if dato != '' and dato != ' ':
	            		break;
	            	else:
	            		print(Cursor.POS(50,23)+Fore.RED+"Ingresa un dato valido...")
	            		sleep(1);
	            		print(Cursor.POS(50,23)+"                          ")
	            		print(Cursor.POS(50,22)+"                                                              ")
	            modificacion = tipo_dato + dato + "\n"
	        elif editar == "2":
	            tipo_dato = "Edad: "
	            while True:
	                try:
	                	dato = int(input(Cursor.POS(50,22)+"Ingresa tu edad: "))
	                	if dato >= 0 and dato <= 120:
	                		break;
	                	else:
	                		print(Cursor.POS(50,23)+Fore.RED+"Ingresa unicamente numeros positivos...");
	                		sleep(1);
	                		print(Cursor.POS(50,23)+Fore.RED+"                                                 ")
	                		print(Cursor.POS(50,22)+"                                                                        ")	
	                except ValueError:
	                	print(Cursor.POS(50,23)+Fore.RED+"Ingresa unicamente numeros...")
	                	sleep(1);
	                	print(Cursor.POS(50,23)+Fore.RED+"                                                    ")
	                	print(Cursor.POS(50,22)+"                                                                        ")	
	            string_edad = str(dato)
	            modificacion = tipo_dato + string_edad + "\n"
	        elif editar == "3":
	            tipo_dato = "Servicio: "
	            while True:
	            	dato = str(input(Cursor.POS(50,22)+"Ingresa el servicio: "));
	            	if dato != '' and dato != ' ':
	            		break;
	            	else:
	            		print(Cursor.POS(50,23)+Fore.RED+"Ingresa un dato valido...")
	            		sleep(1);
	            		print(Cursor.POS(50,23)+"                          ")
	            		print(Cursor.POS(50,22)+"                                                              ")
	            modificacion = tipo_dato + dato + "\n"
	        elif editar == "4":
	            tipo_dato = "Historial medico: "
	            while True:
	            	dato = str(input(Cursor.POS(50,22)+"Ingresa los antecendentes medicos: "));
	            	if dato != '' and dato != ' ':
	            		break;
	            	else:
	            		print(Cursor.POS(50,23)+Fore.RED+"Ingresa un dato valido...")
	            		sleep(1);
	            		print(Cursor.POS(50,23)+"                          ")
	            		print(Cursor.POS(50,22)+"                                                              ")
	            modificacion = tipo_dato + dato + "\n"
	        print(Cursor.POS(62,35) + Fore.GREEN + "Perfil actualizado correctamente")
	        archivo = open("d03-p14-rodriguez-fernandez-P.txt", mode="r", encoding="utf-8")
	        while True:
	            leer = archivo.readline()
	            if not leer:
	                break
	            if string in leer:
	                datos_modificar = True
	            if datos_modificar == True:
	                lista.append(leer)
	                datos_a_modi = "".join(lista)
	                if tipo_dato in leer:
	                    linea = leer
	                    dato_modi = linea.replace(leer, modificacion)
	            paciente_sig = num_paciente + 1
	            string_final = str(paciente_sig)
	            if string_final in leer:
	                datos_modificar = False
	        archivo.close()
	        archivo = open("d03-p14-rodriguez-fernandez-P.txt", mode="w", encoding="utf-8")
	        datos_modi = datos_a_modi.replace(linea, dato_modi)
	        modificacion_final = leer1.replace(datos_a_modi, datos_modi)
	        archivo.write(modificacion_final)
	    else:
	        print(Cursor.POS(57,20)+Fore.RED+"No se encontro tu numero de paciente...")
	else:
	    print(Cursor.POS(57,20)+Fore.RED+"No se encontro tu numero de paciente...")
	sleep(2)
	archivo.close()
	os.system('cls')
	pass;
#-------------------------------------------------------------------------------------------------------------------------------------------------------------
def historial_pacientes():	
	x1 = 20; y1 = 10; x2 = 130; y2 = 40;
	ventanas(x1,x2,y1,y2,0)
	print(Cursor.POS(64,10)+Fore.CYAN+"HISTORIAL DE PACIENTE")
	cont_lineas = 22; imprime = False;
	while True:
	    try:
	    	num_paciente = int(input(Cursor.POS(50,15)+"Ingresa tu numero de paciente: "))
	    	break;
	    except ValueError:
	    	print(Cursor.POS(50,16)+Fore.RED+"Ingresa unicamente numeros...")
	    	sleep(1);
	    	print(Cursor.POS(50,16)+Fore.RED+"                             ")
	    	print(Cursor.POS(50,15)+"                                                                        ")	
	paciente_sig = num_paciente + 1  #Sirve para saber hasta donde termina el perfil del paciente
	string = str(num_paciente)
	string_final = str(paciente_sig)
	lista_digitos = list(string)
	digitos = len(lista_digitos)
	datos_paciente = 0
	archivo = open("d03-p14-rodriguez-fernandez-P.txt", mode="r", encoding="utf-8")
	leer = archivo.read()
	archivo.close()
	archivo = open("d03-p14-rodriguez-fernandez-P.txt", mode="r", encoding="utf-8")
	print(Cursor.POS(71,19)+Fore.GREEN+"PERFIL")
	while (True):
	    leer1 = archivo.readline()
	    if string in leer1:
	        imprime = True
	    if not leer1:
	    	if imprime == False:
	    		print(Cursor.POS(50,18)+Fore.LIGHTRED_EX+"No se encontro ningun registro con ese numero...")
	    		print(Cursor.POS(71,19)+"           ")
	    	break;
	    if digitos == 11:
	        if imprime == True:
	            if string in leer:
	                if string_final in leer1:
	                    break
	                elif imprime == True:
	                    print(Cursor.POS(50,cont_lineas), leer1)
	                    cont_lineas += 1
	    else:
	        print(Cursor.POS(50,18)+Fore.LIGHTRED_EX+"No se encontro ningun registro con ese numero...")
	        print(Cursor.POS(71,19)+"           ")
	        break
	print(Cursor.POS(58,36) + "Presione una tecla para continuar...")
	ch = msvcrt.getch()
	archivo.close()
	os.system('cls')
#-------------------------------------------------------------------------------------------------------------------------------------------------------------
def eliminar_pacientes():
	x1 = 20; y1 = 10; x2 = 130; y2 = 40;
	ventanas(x1,x2,y1,y2,0)
	print(Cursor.POS(67,10)+Fore.CYAN+"ELIMINAR PACIENTE")
	while True:
	    try:
	    	num_paciente = int(input(Cursor.POS(50,17)+"Ingresa tu numero de paciente: "))
	    	break;
	    except ValueError:
	    	print(Cursor.POS(50,18)+Fore.RED+"Ingresa unicamente numeros...")
	    	sleep(1);
	    	print(Cursor.POS(50,18)+Fore.RED+"                             ")
	    	print(Cursor.POS(50,17)+"                                                                        ")	
	string = str(num_paciente)
	estad = string + "\nEstado: Activo"
	estadi = string + "\nEstado: Inactivo"
	digitos = len(string)
	if digitos == 11:
	    archivo = open("d03-p14-rodriguez-fernandez-P.txt", mode="r", encoding="utf-8")   #Abre el archivo para leer
	    archivo2 = open("d03-p14-rodriguez-fernandez-P.txt", mode="r+", encoding="utf-8")  #Abre el archivo para editar el estado
	    leer = archivo.read()
	    if estad in leer:  #Busca que se encuentre el numero de paciente ingresado y que este en estado activo
	        archivo2.write(leer.replace(estad,estadi))  #Remplaza el estado activo por inactivo
	        print(Cursor.POS(50,20)+Fore.GREEN+"Te has dado de baja con exito")
	    else:
	        print(Cursor.POS(50,20)+Fore.RED+"No se encontro tu numero de paciente")
	    archivo.close()
	    archivo2.close()
	else:
	    print(Cursor.POS(50,20)+Fore.RED+"No se encontro tu numero de paciente")
	sleep(1)
	os.system('cls')
#-------------------------------------------------------------------------------------------------------------------------------------------------------------
def pacientes(): #funcion principal pacientes
	t = 0;
	enter = False;
	men = 2; x1 = 50; y1 = 18; x2 = 100; y2 = 32;
	ventanas(x1, x2, y1, y2, men);
	while True:
		e0 = Cursor.POS(66,18)+Fore.CYAN+"ALTA DE PACIENTE";
		e1 = Cursor.POS(65,21)+"1.- Darte de alta";
		e2 = Cursor.POS(65,23)+"2.- Editar perfil";
		e3 = Cursor.POS(65,25)+"3.- Ver tu historial";
		e4 = Cursor.POS(65,27)+"4.- Darte de baja";
		e5 = Cursor.POS(65,29)+"5.- Regresar al menu";
		if enter == True:
			if t == 1:
				os.system("cls");
				alta_pacientes();
				ventanas(x1, x2, y1, y2, men);
			elif t == 2:
				os.system("cls");
				editar_pacientes();
				ventanas(x1, x2, y1, y2, men);
			elif t == 3:
				os.system("cls");
				historial_pacientes();
				ventanas(x1, x2, y1, y2, men);
			elif t == 4:
				os.system("cls");
				eliminar_pacientes();
				ventanas(x1, x2, y1, y2, men);
			elif t == 5:
				break;
		if t == 1 and enter == False:
			e1 = e1.replace(e1,Back.YELLOW + Fore.BLACK + e1 + Back.RESET + Fore.RESET);
			print(e0); print(e1); print(e2); print(e3); print(e4); print(e5);
		elif t == 2 and enter == False:
			e2 = e2.replace(e2,Back.YELLOW + Fore.BLACK + e2 + Back.RESET + Fore.RESET);
			print(e0); print(e1); print(e2); print(e3); print(e4);print(e5);
		elif t == 3 and enter == False:
			e3 = e3.replace(e3,Back.YELLOW + Fore.BLACK + e3 + Back.RESET + Fore.RESET);
			print(e0); print(e1); print(e2); print(e3); print(e4); print(e5);
		elif t == 4 and enter == False:
			e4 = e4.replace(e4,Back.YELLOW + Fore.BLACK + e4 + Back.RESET + Fore.RESET);
			print(e0); print(e1); print(e2); print(e3); print(e4); print(e5);
		elif t == 5 and enter == False:
			e5 = e5.replace(e5,Back.YELLOW + Fore.BLACK + e5 + Back.RESET + Fore.RESET);
			print(e0); print(e1); print(e2); print(e3); print(e4); print(e5);
		t,enter = teclas(t);
	os.system("cls");
#-------------------------------------------------------------------------------------------------------------------------------------------------------------
def diagnostico_medicos():
	LP = [100,200,300,500,600,1000,150,320,280,940,665,348,495,500]
	LM = ['325 mg de aspirina','500 mg de amoxicilina','250 mg de omeprazol','500 mg de paracetamol','325 mg de simvastatina']
	LD = ['se recuperara pronto, tome su medicacion...','no presenta sintomas severos, unicamente repose 5 dias...','muy probablemente requiera mas analisis...']
	ventanas(20,130,10,40,0);
	arch_med = open('d03-p14-rodriguez-fernandez-M.txt',mode = 'r', encoding = 'utf-8');
	print(Cursor.POS(64,10) + Fore.CYAN + "RESULTADOS ANALISIS");
	nombresL = []; cargosL = []; cedulasL = []; nombresLP = []; servicioLP = []; numeroLP = []; lineaE = ''; c = r = 0;
	while True:
		linea = arch_med.readline();
		if not linea:
			break;
		if '\n' in linea:
			linea = linea.replace(linea,linea[:-1]);
		if 'nombre:' in linea:
			nombresL.append(linea[7:]);
		if 'cargo:' in linea:
			cargosL.append(linea[6:]);
		if 'cedula:' in linea:
			cedulasL.append(linea[7:]);
	arch_med.close();
	arch_pac = open('d03-p14-rodriguez-fernandez-P.txt',mode = 'r', encoding = 'utf-8');
	while True:
		linea = arch_pac.readline();
		if not linea:
			break;
		if '\n' in linea:
			linea = linea.replace(linea,linea[:-1]);
		if 'Nombre: ' in linea:
			nombresLP.append(linea[8:]);
		if 'Servicio: ' in linea:
			servicioLP.append(linea[10:]);
		if '100' in linea:
			numeroLP.append(linea);
	arch_pac.close();
	if len(nombresL) == 0:
		print(Cursor.POS(21,11) + Fore.RED + "No hay medicos registrados...");
		sleep(2);
	elif len(nombresLP) == 0:
		print(Cursor.POS(21,11) + Fore.RED + "No hay pacientes registrados...");
		sleep(2);
	else:
		for i in range(len(nombresL)):
			print(Cursor.POS(21,11+i)+ Fore.GREEN + 'Nombre:',nombresL[i]);
		for i in range(len(cargosL)):	
			print(Cursor.POS(64,11+i)+ Fore.GREEN +'Cargo:',cargosL[i]);
		for i in range(len(cedulasL)):	
			print(Cursor.POS(94,11+i)+Fore.GREEN +'Cedula:',cedulasL[i]);
		print(Cursor.POS(21,11+len(cedulasL)) + Fore.LIGHTBLUE_EX + "-------------------------------------------------------------------------------------------------------------")
		esp = len(cedulasL) + 1;
		for i in range(len(nombresLP)):
			print(Cursor.POS(21,11+i+esp)+ Fore.GREEN + 'Nombre:',nombresLP[i]);
		for i in range(len(servicioLP)):	
			print(Cursor.POS(64,11+i+esp)+ Fore.GREEN +'Servicio:',servicioLP[i]);
		for i in range(len(numeroLP)):	
			print(Cursor.POS(94,11+i+esp)+Fore.GREEN +'# Paciente:',numeroLP[i]);
		esp = len(cedulasL)+len(numeroLP) - 2;
		print(Cursor.POS(21,15+esp) + f"Si desea salir pulse {Fore.GREEN + 'ESC' + Fore.RESET} de lo contrario cualquier tecla...");
		ch = msvcrt.getch();
		esp+=1;
		if ch != b'\x1b':
			while True:
				ced = input(Cursor.POS(21,15+esp) + "-. Ingrese la cedula del medico: ").upper();
				if ced in cedulasL:
					esp+=1;
					break;
				else:
					print(Cursor.POS(21,15+esp+1) + Fore.RED + "La cedula no existe...");
					sleep(2);
					print(Cursor.POS(21,15+esp+1) + Fore.RED + "                      ");
					print(Cursor.POS(21,15+esp) + "                                                                              ")
			while True:
				num = input(Cursor.POS(21,15+esp) + "-. Ingrese el numero del paciente: ").upper();
				if num in numeroLP:
					break;
				else:
					print(Cursor.POS(21,15+esp+1) + Fore.RED + "El numero no existe...");
					sleep(2);
					print(Cursor.POS(21,15+esp+1) + Fore.RED + "                      ");
					print(Cursor.POS(21,15+esp) + "                                                                                 ")
			aux_p = numeroLP.index(num);
			aux_m = cedulasL.index(ced);
			arch_med = open('d03-p14-rodriguez-fernandez-M.txt',mode = 'r', encoding = 'utf-8');
			lineaE = ''; r = c = 0;
			while True:
				linea = arch_med.readline();
				if not linea:
					break;
				if '\n' in linea:
					linea = linea.replace(linea,linea[:-1]);
				if 'cedula:' in linea and ced in linea:
					c+=1;
					r+=1;
				if 'pacientes:' in linea and c == 1 and r == 1:
					linea = linea.replace(linea,linea + num + ' ');
					c+=1;
				lineaE = lineaE + linea + '\n';
			arch_med.close();
			arch_med = open('d03-p14-rodriguez-fernandez-M.txt',mode = 'w+', encoding = 'utf-8');
			arch_med.write(lineaE);
			arch_med.close();
			#---------------------------------------------
			arch_pac = open('d03-p14-rodriguez-fernandez-P.txt',mode = 'r', encoding = 'utf-8');
			lineaE = ''; r = c = 0;
			while True:
				linea = arch_pac.readline();
				if not linea:
					break;
				if '\n' in linea:
					linea = linea.replace(linea,linea[:-1]);
				if num in linea:
					c+=1;
					r+=1;
				if 'Medicos: ' in linea and c == 1 and r == 1:
					if 'Sin medicos asignados' in linea:
						linea = 'Medicos: ';
					linea = linea.replace(linea,linea + ced + '|');
					c+=1;
				lineaE = lineaE + linea + '\n';
			arch_pac.close();
			arch_pac = open('d03-p14-rodriguez-fernandez-P.txt',mode = 'w+', encoding = 'utf-8');
			arch_pac.write(lineaE);
			arch_pac.close();
			os.system("cls");
			ventanas(20,130,10,40,0);
			print(Cursor.POS(69,10) + Fore.CYAN + "RESULTADOS");
			arch_hosp = open('d03-p14-rodriguez-fernandez-H.txt',mode = 'r', encoding = 'utf-8');
			n = ''; d = ''; now = datetime.now(); fecha = now.date();
			while True:
				linea = arch_hosp.readline();
				if not linea:
					break;
				if 'nombre:' in linea:
					n = linea[7:];
				if 'direccion:' in linea:
					d = linea[10:];
			arch_hosp.close();
			x = int(((150) - (len(n) + 9)) / 2);
			print(Cursor.POS(x,12) + Fore.GREEN + f"Hospital: {Fore.RESET + str(n)}");
			x = int(((150) - (len(d) + 10)) / 2);
			print(Cursor.POS(x,13) + Fore.GREEN + f"Direccion: {Fore.RESET + str(d)}");
			x = int(((150) - (len(str(fecha)) + 7)) / 2);
			print(Cursor.POS(x,14) + Fore.GREEN + f"Fecha: {Fore.RESET + str(fecha)}");
			print(Cursor.POS(21,17) + Fore.GREEN + f"Nombre del paciente: {Fore.RESET + str(nombresLP[aux_p]).upper()}");
			print(Cursor.POS(21,18) + Fore.GREEN + f"Numero de paciente: {Fore.RESET + str(numeroLP[aux_p])}");
			print(Cursor.POS(21,19) + Fore.GREEN + f"Servicio/Tipo de Analisis: {Fore.RESET + str(servicioLP[aux_p]).upper()}");
			print(Cursor.POS(21,21) + Fore.GREEN + f"Nombre del medico: {Fore.RESET + str(nombresL[aux_m]).upper()}");
			print(Cursor.POS(21,22) + Fore.GREEN + f"Cargo del medico: {Fore.RESET + str(cargosL[aux_m]).upper()}");
			print(Cursor.POS(21,23) + Fore.GREEN + f"Cedula del medico: {Fore.RESET + str(cedulasL[aux_m]).upper()}");
			print(Cursor.POS(21,26) + Fore.GREEN + f"Medicamentos: {Fore.RESET + random.choice(LM)}");
			print(Cursor.POS(21,28) + Fore.GREEN + f"Diagnostico: {Fore.RESET + random.choice(LD)}");
			precio = random.choice(LP); IVA = precio*0.16; preciofin = precio*1.16;
			print(Cursor.POS(110,35) + Fore.GREEN + f"Subtotal: {Fore.RESET + str(precio)} $");
			print(Cursor.POS(110,36) + Fore.GREEN + f"IVA: {Fore.RESET + str(round(IVA,2))} $");
			print(Cursor.POS(110,37) + Fore.GREEN + f"Total: {Fore.RESET + str(round(preciofin,2))} $");
			print(Cursor.POS(21,35) + "Presiona una tecla para continuar...");
			ch = msvcrt.getch();
	os.system("cls");
#-------------------------------------------------------------------------------------------------------------------------------------------------------------
def alta_medicos():
	ventanas(30,120,22,28,0);
	cedulasL = [];
	print(Cursor.POS(65,22) + Fore.CYAN + "AlTA DE MEDICO");
	arch_med = open('d03-p14-rodriguez-fernandez-M.txt',mode = 'r',encoding = 'utf-8');
	while True:
		linea = arch_med.readline();
		if not linea:
			break;
		if 'cedula:' in linea:
			if '\n' in linea:
				linea = linea.replace(linea,linea[:-1]);
			ced = linea[7:].upper();
			cedulasL.append(ced);
	arch_med.close();
	while True:
		nom = input(Cursor.POS(31,23) + "Ingrese el nombre completo del medico: ").upper();
		if nom != '' and nom != ' ':
			break;
		else:
			print(Cursor.POS(31,24) + Fore.RED +  "Nombre invalido...");
			sleep(1);
			print(Cursor.POS(31,24) + "                  ");
	while True:
		carg = input(Cursor.POS(31,24) + "Ingrese el cargo del medico: ").upper();
		if carg != '' and carg != ' ':
			break;
		else:
			print(Cursor.POS(31,25) + Fore.RED + "Cargo invalido...");
			sleep(1);
			print(Cursor.POS(31,25) + "                 ");
			print(Cursor.POS(31,24) + "                                                                       ");
	while True:
		ced = input(Cursor.POS(31,25) + "Ingrese la cedula del medico: ").upper();
		if ced not in cedulasL and ced != '' and ced != ' ':
			cedulasL.append(ced);
			break;
		elif ced not in cedulasL and ced == '' or ced == ' ':
			print(Cursor.POS(31,26) + Fore.RED + "La cedula es invalida...");
			sleep(1);	
			print(Cursor.POS(31,26) + "                          ")	
			print(Cursor.POS(31,25) + "                                                                       ")
		else:
			print(Cursor.POS(31,26) + Fore.RED + "La cedula ya existe...");
			sleep(1);	
			print(Cursor.POS(31,26) + "                      ")	
			print(Cursor.POS(31,25) + "                                                                       ")
	print(Cursor.POS(31,26) + Fore.GREEN + "Registrado con exito...");

	sleep(1);
	arch_med = open('d03-p14-rodriguez-fernandez-M.txt',mode = 'a',encoding = 'utf-8');
	nom = 'nombre:' + nom; carg = 'cargo:' + carg; ced = 'cedula:' + ced; pac = 'pacientes:'
	arch_med.write('\n'); arch_med.write(ced); arch_med.write('\n'); arch_med.write(nom); arch_med.write('\n'); arch_med.write(carg); arch_med.write('\n'); arch_med.write(pac);
	arch_med.close();
	os.system("cls");
#----------------------------------------------------------------------------------------------------------------------------------------------------------
def editar_medicos():
	ventanas(20,130,14,36,0);
	print(Cursor.POS(66,14) + Fore.CYAN + "VER/EDITAR MEDICO");
	arch_med = open('d03-p14-rodriguez-fernandez-M.txt',mode = 'r', encoding = 'utf-8');
	nombresL = []; cargosL = []; cedulasL = []; lineaE = ''; c = r = 0;
	while True:
		linea = arch_med.readline();
		if not linea:
			break;
		if '\n' in linea:
			linea = linea.replace(linea,linea[:-1]);
		if 'nombre:' in linea:
			nombresL.append(linea[7:]);
		if 'cargo:' in linea:
			cargosL.append(linea[6:]);
		if 'cedula:' in linea:
			cedulasL.append(linea[7:]);
	arch_med.close();
	for i in range(len(nombresL)):
		print(Cursor.POS(21,15+i)+ Fore.GREEN + 'Nombre:',nombresL[i]);
	for i in range(len(cargosL)):	
		print(Cursor.POS(67,15+i)+ Fore.GREEN +'Cargo:',cargosL[i]);
	for i in range(len(cedulasL)):	
		print(Cursor.POS(96,15+i)+Fore.GREEN +'Cedula:',cedulasL[i]);
	if len(nombresL) == 0:
		print(Cursor.POS(21,15) + Fore.RED + "No hay medicos registrados...");
		sleep(2);
	else:
		esp = len(cedulasL);
		print(Cursor.POS(21,15+esp) + f"Si desea salir pulse {Fore.GREEN + 'ESC' + Fore.RESET} de lo contrario cualquier tecla...");
		ch = msvcrt.getch();
		esp+=1;
		if ch != b'\x1b':
			while True:
				ced = input(Cursor.POS(21,15+esp) + "-. Ingrese la cedula del medico: ").upper();
				if ced in cedulasL:
					break;
				else:
					print(Cursor.POS(21,15+esp+1) + Fore.RED + "La cedula no existe...");
					sleep(2);
					print(Cursor.POS(21,15+esp+1) + Fore.RED + "                      ");
					print(Cursor.POS(21,15+esp) + "                                                ")
			print(Cursor.POS(21,15+esp+1) + "¿Que desea hacer?" + Fore.GREEN + " 1-Editar nombre | 2-Editar cargo | 3-Editar cedula | 4-Ver pacientes | O/T-Salir")
			chn = msvcrt.getch();
			esp+=1;
			if chn == b'1':
				while True:
					nom = input(Cursor.POS(21,15+esp+1) + "Ingresa el nuevo nombre: ").upper();
					if nom != ' ' and nom != '':
						break;
					else:
						print(Cursor.POS(21,15+esp+2) + Fore.RED + "El nombre es incorrecto...");
						sleep(2);
						print(Cursor.POS(21,15+esp+2) + Fore.RED + "                          ");
						print(Cursor.POS(21,15+esp+1) + "                                                ")
				arch_med = open('d03-p14-rodriguez-fernandez-M.txt',mode = 'r', encoding = 'utf-8');
				lineaE = ''; r = c = 0;
				while True:
					linea = arch_med.readline();
					if not linea:
						break;
					if '\n' in linea:
						linea = linea.replace(linea,linea[:-1]);
					if 'cedula:' in linea and ced in linea:
						c+=1;
						r+=1;
					if 'nombre:' in linea and c == 1 and r == 1:
						linea = linea.replace(linea,'nombre:' + nom);
						c+=1;
					lineaE = lineaE + linea + '\n';
				esp+=1;
				arch_med.close();
				arch_med = open('d03-p14-rodriguez-fernandez-M.txt',mode = 'w+', encoding = 'utf-8');
				arch_med.write(lineaE); arch_med.close();
				print(Cursor.POS(21,15+esp+1) + Fore.GREEN + "Nombre actualizado con exito...")
				sleep(2);
			elif chn == b'2':
				while True:
					carg = input(Cursor.POS(21,15+esp+1) + "Ingresa el nuevo cargo: ").upper();
					if carg != ' ' and carg != '':
						break;
					else:
						print(Cursor.POS(21,15+esp+2) + Fore.RED + "El cargo es incorrecto...");
						sleep(2);
						print(Cursor.POS(21,15+esp+2) + Fore.RED + "                          ");
						print(Cursor.POS(21,15+esp+1) +  "                           ");
				arch_med = open('d03-p14-rodriguez-fernandez-M.txt',mode = 'r', encoding = 'utf-8');
				lineaE = ''; r = c = 0;
				while True:
					linea = arch_med.readline();
					if not linea:
						break;
					if '\n' in linea:
						linea = linea.replace(linea,linea[:-1]);
					if 'cedula:' in linea and ced in linea:
						c+=1;
						r+=1;
					if 'cargo:' in linea and c == 1 and r == 1:
						linea = linea.replace(linea,'cargo:' + carg);
						c+=1;
					lineaE = lineaE + linea + '\n';
				esp+=1;
				arch_med.close();
				arch_med = open('d03-p14-rodriguez-fernandez-M.txt',mode = 'w+', encoding = 'utf-8');
				arch_med.write(lineaE); arch_med.close();
				print(Cursor.POS(21,15+esp+1) + Fore.GREEN + "Cargo actualizado con exito...")
				sleep(2);
			elif chn == b'3':
				ced_aux = ced;
				while True:
					ced = input(Cursor.POS(21,15+esp+1) + "Ingresa la nueva cedula: ").upper();
					if ced != ' ' and ced != '' and ced not in cedulasL:
						break;
					else:
						print(Cursor.POS(21,15+esp+2) + Fore.RED + "La cedula ya existe o es incorrecta...");
						sleep(2);
						print(Cursor.POS(21,15+esp+2) + Fore.RED + "                                      ");
						print(Cursor.POS(21,15+esp+1) +  "                          ");
				arch_med.close();
				arch_med = open('d03-p14-rodriguez-fernandez-M.txt',mode = 'r', encoding = 'utf-8');
				lineaE = ''; r = c = 0;
				while True:
					linea = arch_med.readline();
					if not linea:
						break;
					if '\n' in linea:
						linea = linea.replace(linea,linea[:-1]);
					if 'cedula:' in linea and ced_aux in linea:
						linea = linea.replace(linea,'cedula:' + ced);
					lineaE = lineaE + linea + '\n';
				esp+=1;
				arch_med.close();
				arch_med = open('d03-p14-rodriguez-fernandez-M.txt',mode = 'w+', encoding = 'utf-8');
				arch_med.write(lineaE); arch_med.close();
				print(Cursor.POS(21,15+esp+1) + Fore.GREEN + "Cedula actualizada con exito...")
				sleep(2);
			elif chn == b'4':
				os.system("cls");
				ventanas(20,130,14,36,0);
				print(Cursor.POS(67,14) + Fore.CYAN + "VER PACIENTES")
				arch_med = open('d03-p14-rodriguez-fernandez-M.txt',mode = 'r', encoding = 'utf-8');
				lineaE = ''; r = c = 0;
				while True:
					linea = arch_med.readline();
					if not linea:
						break;
					if '\n' in linea:
						linea = linea.replace(linea,linea[:-1]);
					if 'cedula:' in linea and ced in linea:
						c+=1;
						r+=1;
					if 'nombre:' in linea and c == 1 and r ==1:
						nom = linea[7:]
					if 'cargo:' in linea and c == 1 and r ==1:
						carg = linea[6:]
					if 'pacientes:' in linea and c == 1 and r == 1:
						lineaE = linea[10:]; lineaE = lineaE.split(); lineaE = set(lineaE); lineaE = list(lineaE);
						if '' in lineaE:
							lineaE.remove('')
						if len(lineaE) != 0:
							print(Cursor.POS(21,15) + Fore.GREEN + "Nombre del medico: "+ Fore.RESET + str(nom));
							print(Cursor.POS(21,16) + Fore.GREEN + "Cargo del medico: "+ Fore.RESET + str(carg));
							print(Cursor.POS(21,17) + Fore.GREEN + "Cedula del medico: "+ Fore.RESET + str(ced));
							for i in range(len(lineaE)):
								print(Cursor.POS(21,19+i) + Fore.GREEN +  "# Paciente: " + str(Fore.RESET + lineaE[i]));
							print(Cursor.POS(21,20+len(lineaE)) + "Presiona una tecla para continuar...");
							ch = msvcrt.getch();
						else:
							print(Cursor.POS(21,15) +Fore.RED + "El medico no posee pacientes activos...");
							sleep(2);
						c+=1;
				arch_med.close();
	os.system("cls");
#----------------------------------------------------------------------------------------------------------------------------------------------------------
def eliminar_medicos():
	ventanas(20,130,14,36,0);
	print(Cursor.POS(67,14) + Fore.CYAN + "ELIMINAR MEDICO");
	arch_med = open('d03-p14-rodriguez-fernandez-M.txt',mode = 'r', encoding = 'utf-8');
	nombresL = []; cargosL = []; cedulasL = []; lineaE = ''; c = r = 0;
	while True:
		linea = arch_med.readline();
		if not linea:
			break;
		if '\n' in linea:
			linea = linea.replace(linea,linea[:-1]);
		if 'nombre:' in linea:
			nombresL.append(linea[7:]);
		if 'cargo:' in linea:
			cargosL.append(linea[6:]);
		if 'cedula:' in linea:
			cedulasL.append(linea[7:]);
	arch_med.close();
	for i in range(len(nombresL)):
		print(Cursor.POS(21,15+i)+ Fore.GREEN + 'Nombre:',nombresL[i]);
	for i in range(len(cargosL)):	
		print(Cursor.POS(67,15+i)+ Fore.GREEN +'Cargo:',cargosL[i]);
	for i in range(len(cedulasL)):	
		print(Cursor.POS(96,15+i)+Fore.GREEN +'Cedula:',cedulasL[i]);
	if len(nombresL) == 0:
		print(Cursor.POS(21,15) + Fore.RED + "No hay medicos registrados...");
		sleep(2);
	else:
		esp = len(cedulasL);	
		while True:
			elim = input(Cursor.POS(21,15+esp) +"-. Ingrese la cedula del medico a eliminar: ").upper();
			if elim in cedulasL:
				arch_med = open('d03-p14-rodriguez-fernandez-M.txt',mode = 'r', encoding = 'utf-8');
				while True:
					linea = arch_med.readline();
					if not linea:
						break;
					if '\n' in linea:
						linea = linea.replace(linea,linea[:-1]);
					if 'cedula:' in linea and elim in linea:
						linea = linea.replace(linea,'');
						c+=1;
						r+=1;
					if 'nombre:' in linea and c == 1 and r == 1:
						linea = linea.replace(linea,'');
						c+=1;
					if 'cargo:' in linea and c == 2 and r == 1:
						linea = linea.replace(linea,'');
						c+=1;
					if 'pacientes:'in linea and c == 3 and r == 1: 
						linea = linea.replace(linea,'');
						c+=1;
					if linea != '':
						lineaE = lineaE + linea + '\n';
				arch_med.close();
				arch_med = open('d03-p14-rodriguez-fernandez-M.txt',mode = 'w+', encoding = 'utf-8');
				arch_med.write(lineaE);
				arch_med.close();
				print(Cursor.POS(21,15+esp+1) + Fore.GREEN + "Eliminado con exito...")
				sleep(1);
				break;
			else:
				print(Cursor.POS(21,15+esp+1) + Fore.RED + "La cedula no existe...");
				sleep(2);
				print(Cursor.POS(21,15+esp+1) + Fore.RED + "                      ");
				print(Cursor.POS(21,15+esp) +  "                                                                                         ");
	os.system("cls");
#----------------------------------------------------------------------------------------------------------------------------------------------------------
def medicos():
	t = 0;
	enter = False;
	men = 3; x1 = 50; y1 = 18; x2 = 100; y2 = 32;
	ventanas(x1, x2, y1, y2, men);
	while True:
		e0 = Cursor.POS(67,18)+Fore.CYAN+"ALTA DE MEDICOS";
		e1 = Cursor.POS(65,21)+"1.- Alta de medico";
		e2 = Cursor.POS(65,23)+"2.- Ver/Editar perfil de medico";
		e3 = Cursor.POS(65,25)+"3.- Resultados de Analisis";
		e4 = Cursor.POS(65,27)+"4.- Eliminar perfil de medico";
		e5 = Cursor.POS(65,29)+"5.- Regresar al menu";
		if enter == True:
			if t == 1:
				os.system("cls");
				alta_medicos();
				ventanas(x1, x2, y1, y2, men);
			elif t == 2:
				os.system("cls");
				editar_medicos();
				ventanas(x1, x2, y1, y2, men);
			elif t == 3:
				os.system("cls");
				diagnostico_medicos();
				ventanas(x1, x2, y1, y2, men);
			elif t == 4:
				os.system("cls");
				eliminar_medicos()
				#servicios_hospital();
				ventanas(x1, x2, y1, y2, men);
			elif t == 5:
				break;
		if t == 1 and enter == False:
			e1 = e1.replace(e1,Back.YELLOW + Fore.BLACK + e1 + Back.RESET + Fore.RESET);
			print(e0); print(e1); print(e2); print(e3); print(e4); print(e5);
		elif t == 2 and enter == False:
			e2 = e2.replace(e2,Back.YELLOW + Fore.BLACK + e2 + Back.RESET + Fore.RESET);
			print(e0); print(e1); print(e2); print(e3); print(e4);print(e5);
		elif t == 3 and enter == False:
			e3 = e3.replace(e3,Back.YELLOW + Fore.BLACK + e3 + Back.RESET + Fore.RESET);
			print(e0); print(e1); print(e2); print(e3); print(e4); print(e5);
		elif t == 4 and enter == False:
			e4 = e4.replace(e4,Back.YELLOW + Fore.BLACK + e4 + Back.RESET + Fore.RESET);
			print(e0); print(e1); print(e2); print(e3); print(e4); print(e5);
		elif t == 5 and enter == False:
			e5 = e5.replace(e5,Back.YELLOW + Fore.BLACK + e5 + Back.RESET + Fore.RESET);
			print(e0); print(e1); print(e2); print(e3); print(e4); print(e5);
		t,enter = teclas(t);
	os.system("cls");	
#----------------------------------------------------------------------------------------------------------------------------------------------------------
def nombre_hospital(): #en esta funcion se registra el nombre del hospital
	arch_hosp = open('d03-p14-rodriguez-fernandez-H.txt',mode = 'r',encoding = 'utf-8');
	ventanas(30,120,22,28,0);
	lineaE = '';
	while True:
		linea = arch_hosp.readline();
		if not linea:
			break;
		if 'nombre:' in linea:
			n_hosp = linea[7:];
	arch_hosp.close();
	print(Cursor.POS(65,22) + Fore.CYAN + "NOMBRE DE HOSPITAL");
	print(Cursor.POS(31,23) + "El nombre actual del hospital es: " + Fore.GREEN + str(n_hosp));
	print(Cursor.POS(31,24) +"¿Desea actualizar el nombre? si(s)/no(n)");
	ch = msvcrt.getch();
	if ch == b's' or ch == b'S':
		lineaE = '';
		while True:
			nombre = input(Cursor.POS(31,24) + "-.Ingresa el nuevo nombre del hospital: ");
			if nombre != '' and nombre != ' ':
				break;
			else:
				print(Cursor.POS(31,25) + Fore.RED + "El nombre introducido no es valida...");
				sleep(1);
				print(Cursor.POS(31,25) + Fore.RED + "                                        ");
				print(Cursor.POS(31,24) +  "                                                                            ");
		print(Cursor.POS(31,25) + Fore.GREEN + "Actualizado con exito...");
		arch_hosp = open('d03-p14-rodriguez-fernandez-H.txt',mode = 'r',encoding = 'utf-8');
		while True:
			linea = arch_hosp.readline();
			if '\n' in linea:
				linea = linea.replace(linea,linea[:-1]);
			if not linea:
				break;
			else:
				if 'nombre:' in linea:
					linea = linea.replace(linea,'nombre:' + nombre);
				lineaE = lineaE + linea + '\n';
		arch_hosp.close();
		arch_hosp = open('d03-p14-rodriguez-fernandez-H.txt',mode = 'w+',encoding = 'utf-8');
		arch_hosp.write(lineaE); arch_hosp.close();
		sleep(1.5);
	os.system("cls");
#----------------------------------------------------------------------------------------------------------------------------------------------------------
def direccion_hospital(): #se registra direccion del hospital
	arch_hosp = open('d03-p14-rodriguez-fernandez-H.txt',mode = 'r',encoding = 'utf-8');
	ventanas(30,120,22,28,0);
	lineaE = '';
	while True:
		linea = arch_hosp.readline();
		if not linea :
			break;
		if 'direccion:' in linea:
			d_hosp = linea[10:];
	arch_hosp.close();
	print(Cursor.POS(63,22) + Fore.CYAN + "DIRECCION DE HOSPITAL");
	print(Cursor.POS(31,23) + "La direccion actual del hospital es: " + Fore.GREEN + str(d_hosp));
	print(Cursor.POS(31,24) +"¿Desea actualizar la direccion? si(s)/no(n)");
	ch = msvcrt.getch();
	if ch == b's' or ch == b'S':
		while True:
			dire = input(Cursor.POS(31,24) + "-.Ingresa la nueva dirrecion del hospital: ");
			if dire != '' and dire != ' ':
				break;
			else:
				print(Cursor.POS(31,25) + Fore.RED + "La direccion introducida no es valida...");
				sleep(1);
				print(Cursor.POS(31,25) + Fore.RED + "                                        ");
				print(Cursor.POS(31,24) +  "                          ");
		print(Cursor.POS(31,25) + Fore.GREEN + "Actualizado con exito...");
		arch_hosp = open('d03-p14-rodriguez-fernandez-H.txt',mode = 'r',encoding = 'utf-8');
		while True:
			linea = arch_hosp.readline();
			if '\n' in linea:
				linea = linea.replace(linea,linea[:-1]);
			if not linea:		
				break;
			else:
				if 'direccion:' in linea:	
					linea = linea.replace(linea,'direccion:' + dire) ;
				lineaE = lineaE + linea + '\n' ;
		arch_hosp.close();
		arch_hosp = open('d03-p14-rodriguez-fernandez-H.txt',mode = 'w+',encoding = 'utf-8');
		arch_hosp.write(lineaE); arch_hosp.close();
		sleep(1.5);
	os.system("cls");
#----------------------------------------------------------------------------------------------------------------------------------------------------------
def servicios_hospital(): #se registran los servicios del hospital
	arch_hosp = open('d03-p14-rodriguez-fernandez-H.txt',mode = 'r',encoding = 'utf-8');
	ventanas(25,125,18,32,0);
	lineaE = ''; r = 0;
	#s_hosp = '';
	while True:
		linea = arch_hosp.readline();
		print(Cursor.POS(70,18) + Fore.CYAN + "SERVICIOS");
		if not linea:
			if ('' in s_hosp  or '\n' in s_hosp) and len(s_hosp) == 1:
				print(Cursor.POS(26,19) + Fore.RED + "No hay servicios registrados...");
				print(Cursor.POS(26,20) + "¿Desea agregar un servicio? si(s)/no(n)");
				ch = msvcrt.getch();
				if ch == b's' or ch == b'S':
					serv = input(Cursor.POS(26,21) + "Ingresa el nombre del servicio: ").lower();
					print(Cursor.POS(26,22) + Fore.GREEN +  "Servicio registrado con exito...");
					arch_hosp = open('d03-p14-rodriguez-fernandez-H.txt',mode = 'r',encoding = 'utf-8');
					while True:
						linea = arch_hosp.readline();
						if '\n' in linea:
							linea = linea.replace(linea,linea[:-1]);
						if not linea:
							break;
						else:
							if 'servicios:' in linea:
								linea = linea+serv+',';
							lineaE = lineaE + linea + '\n';
					arch_hosp.close();
					arch_hosp = open('d03-p14-rodriguez-fernandez-H.txt',mode = 'w+',encoding = 'utf-8');
					arch_hosp.write(lineaE);
					arch_hosp.close();
					sleep(1);
				elif ch == b'n' or ch == b'N':
					break;
				else:
					pass;
			break;
		if 'servicios:' in linea:
			s_hosp = linea[10:];
			s_hosp = s_hosp.split(",");
	if '\n' in s_hosp:
		s_hosp.remove('\n');
	if '' in s_hosp:
		s_hosp.remove('');
	arch_hosp.close();
	if len(s_hosp) != 0:
		s_hosp = set(s_hosp);
		s_hosp = list(s_hosp);
		print(Cursor.POS(26,19) + "-Los servicios que se ofrecen son: ");
		for i in range(len(s_hosp)):
			if i != '' and i != ' ' and i != '  ':
				r = 20 + i;
				print(Cursor.POS(26,r) + "-" + str(s_hosp[i]).upper());	
		print(Cursor.POS(26,r+2) +  "-¿Que desea hacer?" + Fore.GREEN + " 1-Agregar servicio | 2-Eliminar Servicio | O/T-Salir");
		ch = msvcrt.getch();
		if ch == b'1':
			lineaE = '';
			os.system("cls");
			ventanas(30,120,22,28,0);
			print(Cursor.POS(67,22) + Fore.CYAN + "AGREGAR SERVICIO");
			while True:
				serv = input(Cursor.POS(31,23) + "Ingrese el nombre del servicio: ").lower(); #corregir servicoo
				if serv != '' and serv != ' ':
					break;
				else:
					print(Cursor.POS(31,24) + Fore.RED +  "Ingrese un servicio valido...")
					sleep(2);
					print(Cursor.POS(31,24) + Fore.RED +  "                             ")
					print(Cursor.POS(31,23) +  "                                                    ");
			print(Cursor.POS(31,24) + Fore.GREEN +  "Servicio registrado con exito...");
			arch_hosp = open('d03-p14-rodriguez-fernandez-H.txt',mode = 'r',encoding = 'utf-8');
			while True:
				linea = arch_hosp.readline();
				if '\n' in linea:
					linea = linea.replace(linea,linea[:-1]);
				if not linea:
					
					break;
				else:
					if 'servicios:' in linea:
						linea = linea+serv+',';
					lineaE = lineaE + linea + '\n';
			arch_hosp.close();
			arch_hosp = open('d03-p14-rodriguez-fernandez-H.txt',mode = 'w+',encoding = 'utf-8');
			arch_hosp.write(lineaE);
			arch_hosp.close();
			sleep(1);
			os.system("cls");
		elif ch == b'2':
			lineaE = '';
			os.system("cls");
			ventanas(30,120,22,28,0);
			print(Cursor.POS(66,22) + Fore.CYAN + "ELIMINAR SERVICIO");
			while True:
				serv = input(Cursor.POS(31,23) + "Ingrese el nombre del servicio: ").lower(); #corregir servicoo
				if serv != '' and serv != ' ':
					break;
				else:
					print(Cursor.POS(31,24) + Fore.RED +  "Ingrese un servicio valido...")
					sleep(2);
					print(Cursor.POS(31,24) + Fore.RED +  "                             ")
					print(Cursor.POS(31,23) +  "                                     ");
			arch_hosp = open('d03-p14-rodriguez-fernandez-H.txt',mode = 'r',encoding = 'utf-8');
			while True:
				linea = arch_hosp.readline();
				if '\n' in linea:
					linea = linea.replace(linea,linea[:-1]);
				if not linea:
					 #agrandar ventanas y quitar ventana extra, solo pedir debajo de servicios la entrada deseada
					break;
				else:
					if serv in linea and 'servicios:' in linea and serv != '' and serv != ' ':
						linea = linea.replace(serv + ',','');
						print(Cursor.POS(31,24) + Fore.GREEN +  "Servicio eliminado con exito...");
					else:
						print(Cursor.POS(31,24) + Fore.RED + "El servicio no se encontro...")
				lineaE = lineaE + linea + '\n';
			arch_hosp.close();
			arch_hosp = open('d03-p14-rodriguez-fernandez-H.txt',mode = 'w+',encoding = 'utf-8');
			arch_hosp.write(lineaE);
			arch_hosp.close();
			sleep(1);
			os.system("cls");
		elif ch == b'3':
			os.system("cls");
		else:
			os.system("cls");
			pass;
	os.system("cls");
#----------------------------------------------------------------------------------------------------------------------------------------------------------
def hospital(): #funcio principal hospital
	t = 0;
	enter = False;
	men = 4; x1 = 50; y1 = 20; x2 = 100; y2 = 30;
	ventanas(x1, x2, y1, y2, men);
	while True:
		e0 = Cursor.POS(64,20)+Fore.CYAN+"ALTA DATOS DE HOSPITAL";
		e1 = Cursor.POS(65,22)+"1.- Nombre de hospital";
		e2 = Cursor.POS(65,24)+"2.- Direccion";
		e3 = Cursor.POS(65,26)+"3.- Servicios";
		e4 = Cursor.POS(65,28)+"4.- Regresar al menu";
		if t == 5:
			t = 4;
		if enter == True:
			if t == 1:
				os.system("cls");
				nombre_hospital();
				ventanas(x1, x2, y1, y2, men);
			elif t == 2:
				os.system("cls");
				direccion_hospital();
				ventanas(x1, x2, y1, y2, men);
			elif t == 3:
				os.system("cls");
				servicios_hospital();
				ventanas(x1, x2, y1, y2, men);
			elif t == 4:
				break;
		if t == 1 and enter == False:
			e1 = e1.replace(e1,Back.YELLOW + Fore.BLACK + e1 + Back.RESET + Fore.RESET);
			print(e0); print(e1); print(e2); print(e3); print(e4);
		elif t == 2 and enter == False:
			e2 = e2.replace(e2,Back.YELLOW + Fore.BLACK + e2 + Back.RESET + Fore.RESET);
			print(e0); print(e1); print(e2); print(e3); print(e4);
		elif t == 3 and enter == False:
			e3 = e3.replace(e3,Back.YELLOW + Fore.BLACK + e3 + Back.RESET + Fore.RESET);
			print(e0); print(e1); print(e2); print(e3); print(e4);
		elif t == 4 and enter == False:
			e4 = e4.replace(e4,Back.YELLOW + Fore.BLACK + e4 + Back.RESET + Fore.RESET);
			print(e0); print(e1); print(e2); print(e3); print(e4);
		t,enter = teclas(t);
	os.system("cls");
#----------------------------------------------------------------------------------------------------------------------------------------------------------
def ventanas(x1, x2, y1, y2, men):
    xi = x1;
    while x1 <= x2: #ejecucion del ciclo para generar ventanas emuladas
        print(Cursor.POS(x1,y1)+Back.CYAN+" ");
        print(Cursor.POS(x1,y2)+Back.CYAN+" ");
        x1 += 1;
    x1 = xi;
    yi = y1;
    while y1 <= y2: #ejecucion del ciclo para generar ventanas emuladas
        print(Cursor.POS(x1,y1)+Back.CYAN+" ");
        print(Cursor.POS(x2,y1)+Back.CYAN+" ");
        y1 += 1;
    y1 = yi;
    x_1 = x1+5; y_1 = y1 + 2;
    x_i = x_1
    while x_1 <= x2 + 1: #genera segunda ventana en x
        print(Cursor.POS(x_1,y2+1)+Back.BLUE+" ")
        x_1+=1;
    x_1 = x_i;
    while y_1 <= y2 + 1: #genera segunda ventana en y
        print(Cursor.POS(x2+1,y_1)+Back.BLUE+" ")
        print(Cursor.POS(x2+2,y_1)+Back.BLUE+" ")
        y_1+=1;
    if men == 1: #se valida una variable para determinar el ejercicio a ejecutar
    	print(Cursor.POS(60,5)+"-Rodriguez Perez Mauricio de Jesus");
    	print(Cursor.POS(62,6)+"-Fernandez Roman Kevin Arturo");
    	print(Cursor.POS(72,7)+"-Empresa N");
    	arch_hosp = open('d03-p14-rodriguez-fernandez-H.txt',mode = 'r',encoding = 'utf-8');
    	while True:
    		linea = arch_hosp.readline()
    		if 'nombre:' in linea:
    			nombre = linea[7:];		
    			break;
    	arch_hosp.close();
    	x = int(((150) - (len(nombre) + 6)) / 2);
    	print(Cursor.POS(x,15) + Fore.LIGHTBLUE_EX + "Hospital: " + str(nombre));
    	print(Cursor.POS(65,20)+"1.- Alta de pacientes");
    	print(Cursor.POS(65,25)+"2.- Alta de medicos");
    	print(Cursor.POS(65,30)+"3.- Alta de datos de hospital");
    	print(Cursor.POS(65,35)+"4.- Salir");
    elif men == 2: #se valida una variable para determinar el ejercicio a ejecutar
    	print(Cursor.POS(66,18)+Fore.CYAN+"ALTA DE PACIENTES");
    	print(Cursor.POS(65,21)+"1.- Darte de alta");
    	print(Cursor.POS(65,23)+"2.- Editar perfil");
    	print(Cursor.POS(65,25)+"3.- Ver tu historial");
    	print(Cursor.POS(65,27)+"4.- Darte de baja");
    	print(Cursor.POS(65,29)+"5.- Regresar al menu");   	
    elif men == 3: #se valida una variable para determinar el ejercicio a ejecutar
   		print(Cursor.POS(67,18)+Fore.CYAN+"ALTA DE MEDICOS");
   		print(Cursor.POS(65,21)+"1.- Alta de medico");
   		print(Cursor.POS(65,23)+"2.- Ver/Editar perfil de medico");
   		print(Cursor.POS(65,25)+"3.- Resultados de Analisis");
   		print(Cursor.POS(65,27)+"4.- Eliminar perfil de medico");
   		print(Cursor.POS(65,29)+"5.- Regresar al menu");
    elif men == 4: #se valida una variable para determinar el ejercicio a ejecutar
    	print(Cursor.POS(64,20)+Fore.CYAN+"ALTA DATOS DE HOSPITAL")
    	print(Cursor.POS(65,22)+"1.- Nombre de hospital");
    	print(Cursor.POS(65,24)+"2.- Direccion");
    	print(Cursor.POS(65,26)+"3.- Servicios");
    	print(Cursor.POS(65,28)+"4.- Regresar al menu");
    else:
        pass;
#----------------------------------------------------------------------------------------------------------------------------------------------------------
def teclas(n): #funcion para detectar las teclas o los numeros ingresador por el usuario
	enter = False; #detectar 5 teclas
	ch = msvcrt.getch();
	if ch == b'\xe0': #detecta las cuatro flechas
		ch = msvcrt.getch();
		if ch == b'H': #este es el diferenciador de la tecla hacia arriba
			n-=1;
			if n < 1:
				n = 1;
		elif ch == b'P': #este es el diferenciador de la tecla hacia abajo
			n+=1;
			if n > 5:
				n = 5;
	elif ch == b'1': #validar numero 1
		n = 1;
	elif ch == b'2': #validar numero 2
		n = 2;
	elif ch == b'3': #validar numero 3
		n = 3;
	elif ch == b'4': #validar numero 4
		n = 4;
	elif ch == b'5':
		n = 5;
	elif ch == b'\r': #enter
		enter = True;
	else:
		pass;
	return n,enter;
#----------------------------------------------------------------------------------------------------------------------------------------------------------
def menu():
	init(autoreset = True);
	cmd = 'mode 150,50'; #se ajusta el tamaño de la terminal
	os.system(cmd); #se pasa como parametro la variable
	os.system("cls"); #se hace una limpieza de pantalla para eliminar textos previos
	men = 1;
	ns = 0;
	enter = False;
	x1 = 20; y1 = 10; x2 = 130; y2 = 40;
	ventanas(x1, x2, y1, y2, men); #se llama a la funcion generadora de ventanas
	while True:
		e1 = Cursor.POS(65,20)+"1.- Alta de pacientes";
		e2 = Cursor.POS(65,25)+"2.- Alta de medicos";
		e3 = Cursor.POS(65,30)+"3.- Alta de datos de hospital";
		e4 = Cursor.POS(65,35)+"4.- Salir";
		if ns == 5:
			ns = 4;
		if enter == True: #si se retorna un valor True, entonces se ejecuta la opcion correspondiente
			if ns == 1: #se valida el valor del contador para ejecutar la funcion deseada
				os.system("cls");
				pacientes();
				ventanas(x1, x2, y1, y2, men);
			elif ns == 2: #se valida el valor del contador para ejecutar la funcion deseada
				os.system("cls");
				medicos();
				ventanas(x1, x2, y1, y2, men);
			elif ns == 3: #se valida el valor del contador para ejecutar la funcion deseada
				os.system("cls");
				hospital();
				ventanas(x1, x2, y1, y2, men);
			elif ns == 4: #se valida el valor del contador para ejecutar la funcion deseada
				os.system("cls")
				break;
		if ns == 1 and enter == False: #se reemplaza el color a uno distino
			e1 = e1.replace(e1,Back.YELLOW + Fore.BLACK + e1 + Back.RESET + Fore.RESET);
			print(e1); print(e2); print(e3); print(e4); #se imprimen las cadenas y la reemplazada
		elif ns == 2 and enter == False: #se reemplaza el color a uno distino
			e2 = e2.replace(e2,Back.YELLOW + Fore.BLACK + e2 +  Back.RESET + Fore.RESET);
			print(e1); print(e2); print(e3); print(e4); #se imprimen las cadenas y la reemplazada
		elif ns == 3 and enter == False: #se reemplaza el color a uno distino
			e3 = e3.replace(e3,Back.YELLOW + Fore.BLACK + e3 +  Back.RESET + Fore.RESET);
			print(e1); print(e2); print(e3); print(e4); #se imprimen las cadenas y la reemplazada
		elif ns == 4 and enter == False: #se reemplaza el color a uno distino
			e4 = e4.replace(e4,Back.YELLOW + Fore.BLACK + e4 + Back.RESET + Fore.RESET);
			print(e1); print(e2); print(e3); print(e4); #se imprimen las cadenas y la reemplazada
		ns,enter = teclas(ns); # se reciben dos parametros, uno para determinar la posicion de las opciones y el otro para determinar si se presiono enter
		#ventanas(x1, x2, y1, y2, men);
menu();
#----------------------------------------------------------------------------------------------------------------------------------------------------------



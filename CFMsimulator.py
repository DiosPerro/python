# Define la función cls() para limpiar la pantalla.
def cls():
	print("\033[H\033[2J", end="")

# Función para cuando el usuario ingrese una opción invalida. Termina el proceso.
def invalid():
	cls()
	print("Se ha ingresado una opción invalida.\n")

while True:
	print("Carreras disponibles: \n")
	print("1. Astronomía:\nHP: 80\nDMG: 110\nRES: 0\n")
	print("2. Física: \nHP: 80 \nDMG: 120 \nRES: 10\n")
	print("3. Estadística: \nHP: 60 \nDMG: 150 \nRES: 10\n")
	print("4. Geofísica \nHP: 80 \nDMG: 60 \nRES: 50\n")

	carrera = input("Selecciona tu carrera: ")
	if carrera in ["1","2","3","4"]:
		carrera = int(carrera)
		if carrera == 1:
			carrera_nombre = "Astronomía"
			playerHP = 80
			playerDMG = 110
			playerRES = 100
		elif carrera == 2:
			carrera_nombre = "Física"
			playerHP = 80
			playerDMG = 120
			playerRES = 90
		elif carrera == 3:
			carrera_nombre = "Estadística"
			playerHP = 60
			playerDMG = 150
			playerRES = 80
		else:
			carrera_nombre = "Geofísica"
			playerHP = 80
			playerDMG = 60
			playerRES = 50
		cls()
		while True:
			print("Has seleccionado la carrera de ",carrera_nombre,", y tus stats son: \nHP: ",playerHP,"\nDMG: ",playerDMG,"\nRES: ",100-playerRES,"\n\n¿Iniciamos?\n")
			iniciar = input("1. ¡Vamos!\n2. Pensándolo bien...\n\nTu decisión: ")
			if iniciar in ["1","2"]:
				iniciar = int(iniciar)
				break
			else:
				invalid()
		if iniciar == 1:
			break
		else:
			cls()
	else:
		invalid()

# Define variables de las stats default. Así, cuando el usuario se cure al máximo o resetee su HP, se reemplaza playerHP por defPlayerHP.
defPlayerHP = playerHP
defPlayerDMG = playerDMG
defPlayerRes = playerRES

# Funciones de turnos pelea. La RES es el porcentaje de daño recibido, lo que significa que un RES de 100 es una reducción del 0% del daño. Una RES de 80 es una reducción del 20% del daño, y así.
def dmgToE(a,b,c):			#a: playerDMG, b: eRES, c: nueva eHP.
	dmgDone = a*b/100
	print(dmgDone," de daño realizado.")
	global eHP
	eHP = c - dmgDone
	print("HP enemigo: ",eHP)
def dmgToM(a,b,c):			#a: eDMG, b: playerRES, c: nueva playerHP
	dmgReceived = a*b/100
	print(dmgReceived," de daño recibido.")
	global playerHP
	playerHP = c - dmgReceived

# Función que escribe las stats del jugador.
def playerStatus():
	print("        	STATS")
	print("HP: ",playerHP," | DMG: ",playerDMG," | RES: ",100-playerRES)

def pelea1skill():							# Función de pelea. 1 habilidad.
	while True:														# Pelea, inicia el jugador.
		global eHP
		global pHP
		global pRES
		if eHP <= 0 or pHP <= 0:
			break
		else:
			while True:
				turnoP = input("1. Atacar\n2. Huir\n\nTu decisión: ")
				if turnoP in ["1","2"]:
					turnoP = int(turnoP)
					break
				else:
					invalid()
					playerStatus()
					print("")
			if turnoP == 1:											# Ataque jugador a enemigo.
				cls()
				dmgToE(pDMG,eRES,eHP)
			else:										# Huir
				cls()
				break
			dmgToM(eDMG,pRES,pHP)
			print("")
			if pHP > 0 and eHP > 0:
				playerStatus()
				print("")
	if pHP <= 0:													# Fin del juego: Jugador sin HP.
		pHP = 0
		playerStatus()
		print("Te has quedado sin HP... Has perdido.\n")
	elif eHP <= 0:													# Fin de la pelea: Enemigo sin HP.
		playerStatus()
		print("¡El enemigo se ha quedado sin HP! Has ganado.\n")
	else:															# Fin del juego: Error.
		playerStatus()
		print("Por algún motivo, la pelea terminó.\n")


cls()
while True:
	print("Te encuentras, luego de largos meses de espera, en el Gran Concepción, bajo donde tus sueños inician, en el vano del Arco de Medicina. Con la precaución de nunca pisar el infame escudo en el centro de este, rodeas mirando el campanil en el fondo. Pero, escuchando los apresurados pasos de alguien corriendo, eres empujado por quien parece ser un estudiante apresurado y, en misma magnitud, confundido. Perdiendo el equilibrio, pisas el escudo, ¡y bien el mundo podría venirse abajo!\n")
	print("El estudiante desconocido abandonó la escena del crimen antes de que pudieras distinigir cualquier rasgo de este. Viendo tus pies sobre el escudo decides:\n")
	playerStatus()

	dec1 = input("\n1. Entrar en pánico.\n2. Mantener la calma.\n\n Tu elección: ")
	if dec1 in ["1","2"]:
		break
	else:
		invalid()	

dec1 = int(dec1)
if dec1 == 1:
	playerHP -= 1
	cls()
	print("\nEntras en pánico, algunas personas te miran mientras suprimes algo de tu desesperación en lo que te apartas del escudo. Sientes tu corazón presionarse en la presión del momento y pierdes 1 HP.\n")
	playerStatus()
elif dec1 == 2:
	playerDMG -= 1
	cls()
	print("\nMantienes la calma, la gente pretende ignorarte mientras caminas fuera del escudo, pese a que a pocos les importó y notaron, la verguenza te hace sentirte algo débil, perdiendo 1 DMG.\n")
	playerStatus()
else:
	invalid()

input("\nPresione Enter para continuar...")

#Stats del pastero.
eHP = 20
eDMG = 20
eRES = 100

cls()
while True:
	print("Evitando miradas, caminas y te adentras al campus. Te ves en una desorientación jamás prevista, pese a que ya habías estudiado el mapa del campus previamente, así que te las arreglas adentrándote pasado el Arco.\n")
	print("Camino al Campanil, te cruzas con un sospechoso sujeto de aspecto sombrío, sientes una gota de sudor recorrer tu frente cuando lo ves acercarse. Decides:\n")
	playerStatus()
	
	dec2 = input("\n1. Insultarlo\n2. Pegarle\n\nTu elección: ")
	if dec2 in ["1","2"]:
		dec2 = int(dec2)
		break
	else:
		invalid()	
		
if dec2 == 1:
	cls()
	dmgToM(eDMG,playerRES,playerHP)
	while True:
		print("El tipo, tremendamente ofendido, te pega con una velocidad imprevista. Aunque sí dolió, ciertamente dolió menos de lo que debería.\n")
		playerStatus()
		dec2_1 = input("\n1. PÉGALE\n2. CORRE\n\nTu decisión: ")
		if dec2_1 in ["1","2"]:
			dec2_1 = int(dec2_1)
			break
		else:
			invalid()
	if dec2_1 == 1:
		cls()
		print("")
		dmgToE(playerDMG,eRES,eHP)
		print("")
		playerStatus()
	else:
		cls()
		print("Te vas corriendo lejos del pastero lo más rápido que tus piernas permiten.\n")
		playerStatus()
else:
	cls()
	print("COMBO AL PASTERO\n")
	dmgToE(playerDMG,eRES,eHP)
	print("")
	playerStatus()
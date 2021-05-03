import pygame
import sys 
import random
from pygame.locals import *

#Display
pygame.init()
ventana = pygame.display.set_mode((650,448))
pygame.display.set_caption("Juego del Ahorcado")
icono = pygame.image.load('hangman_icon.png')
pygame.display.set_icon(icono
FPS = 60
clock = pygame.time.Clock()

#Colores
NEGRO = (0,0,0)
BLANCO = (255,255,255)

#Fuentes
label_font = pygame.font.SysFont("Courier New", 32)
word_font = pygame.font.SysFont("Calibri", 32)
win_font = pygame.font.SysFont("Calibri", 50)
input_font = pygame.font.SysFont("Arial", 20)

#Background
def background():
	fondo = pygame.image.load('background!.jpg')
	ventana.blit(fondo, [0,0])

#Label
def label():
	label = label_font.render("Juego del Ahorcado!",0,NEGRO)
	ventana.blit(label, (100,10))

#Carga de imágenes de la horca
imagenes = []
for i in range (7):
	imagen = pygame.image.load('hangman'+str(i)+'.png')
	imagenes.append(imagen)

#Variables
palabras = ["ADAPTACION","ANTIBIOTICO","ESTIMULACION","DISTROFIA","FISIOTERAPEUTA","CUADRIPLEJIA","DIAGNOSTICO","PROCEDIMIENTO","TEMPESTAD",
"ELECTROCARDIOGRAMA","IDIOSINCRASIA","VENTRILOCUO","CRONOMETRO","ASINTOMATICO","SISTEMATICO","PLATAFORMA","FOTOSINTESIS","INTERDISCIPLINARIO",
"COMPLEJIDAD","CALEIDOSCOPIO"]
palabra = random.choice(palabras)
letras = ["A","B","C","D","E","F","G","H","I","J","K","L","M","N","Ñ","O","P","Q","R","S","T","U","V","W","X","Y","Z"]
letras_usadas = []
error = 0
progreso = ""

#Palabra oculta
def display_word():
	pantalla = ""
	for ltr in palabra:
		if ltr in letras_usadas:
			pantalla += ltr + " "
		else:
			pantalla += "_ "
	texto = word_font.render(pantalla,1,NEGRO)
	ventana.blit(texto, (100,100))

#Cuadro letras usadas
def cuadro_ingresadas():
	pygame.draw.rect(ventana, BLANCO, (300,250,300,150),3)
	cuadro = input_font.render("Letras ingresadas:",0,NEGRO)
	ventana.blit(cuadro, (310,260))
	letras_usuario = " ".join(letras_usadas)
	ingreso =input_font.render(letras_usuario,0,NEGRO)
	ventana.blit(ingreso, (310,300))

#Horca
def hangman():
	if error == 0:
		ventana.blit(imagenes[0],(75,215))
	elif error == 1:
		ventana.blit(imagenes[1],(75,215))
	elif error == 2:
		ventana.blit(imagenes[2],(75,215))
	elif error == 3:
		ventana.blit(imagenes[3],(75,215))
	elif error == 4:
		ventana.blit(imagenes[4],(75,215))
	elif error == 5:
		ventana.blit(imagenes[5],(75,215))
	elif error == 6:
		ventana.blit(imagenes[6],(75,215))

#Mensaje - final de juego
def mensaje_w(mensaje):
	pygame.time.delay(1000)
	ventana.fill(BLANCO)
	texto = win_font.render(mensaje,1,NEGRO)
	ventana.blit(texto,(200,175))
	pygame.display.update()
	pygame.time.delay(2000)
	

def mensaje_l(mensaje):
	pygame.time.delay(1000)
	ventana.fill(NEGRO)
	texto = win_font.render(mensaje,1,BLANCO)
	ventana.blit(texto,(200,175))
	pygame.display.update()
	pygame.time.delay(2000)

#Game
def game():
	hangman()
	display_word()
	cuadro_ingresadas()
	pygame.display.update()

#Game Loop
run = True
while run:
	clock.tick(FPS)
	background()
	label()
	for event in pygame.event.get():
		if event.type == QUIT:
			pygame.quit()
			sys.exit()
		
		if event.type == pygame.KEYDOWN:
			for letra in letras:
				if letra == event.unicode.upper():
					letras_usadas.append(letra)
					if letra not in palabra:
						error += 1
					if letra in palabra:
						progreso += letra
	
	game()

	ganar = True
	for letter in palabra:
		if letter not in progreso:
			ganar = False

	if ganar:
		mensaje_w("GANASTE! ;)")
		break

	if error == 6:
		mensaje_l("PERDISTE! :(")
		break


from tkinter import *
import ply.lex as lex
import ply.yacc as yacc
import lexerRuby
import gramarRuby
# import ipdb
root=Tk()

miFrame=Frame(root,width=1200, height=600)
miFrame.pack()

# Labels
codeALabel=Label(miFrame,text="Code A:")
codeALabel.grid(row=1,column=1,sticky="w",padx=10,pady=5)

codeBLabel=Label(miFrame,text="Code B:")
codeBLabel.grid(row=3,column=1,sticky="w",padx=10,pady=5)

lexAString=StringVar()
lexBString=StringVar()
synctAString=StringVar()
synctBString=StringVar()
plagString=StringVar()

lexLabel=Label(miFrame,text="Lex:")
lexLabel.grid(row=1,column=3,sticky="w",padx=10,pady=5)

lexALabel=Label(miFrame,text="", textvariable=lexAString)
lexALabel.grid(row=2,column=3,sticky="w",padx=10,pady=5)

lexBLabel=Label(miFrame,text="", textvariable=lexBString)
lexBLabel.grid(row=4,column=3,sticky="w",padx=10,pady=5)

synctLabel=Label(miFrame,text="Synct:")
synctLabel.grid(row=1,column=4,sticky="w",padx=10,pady=5)

synctALabel=Label(miFrame,text="", textvariable=synctAString)
synctALabel.grid(row=2,column=4,sticky="w",padx=10,pady=5)

synctBLabel=Label(miFrame,text="", textvariable=synctBString)
synctBLabel.grid(row=4,column=4,sticky="w",padx=10,pady=5)

plagLabel=Label(miFrame,text="% plagiary:")
plagLabel.grid(row=1,column=5,sticky="w",padx=10,pady=5)

plagFinalLabel=Label(miFrame,text="", textvariable=plagString)
plagFinalLabel.grid(row=3,column=5,sticky="w",padx=10,pady=5)

# text areas
root.update()
width1 = int(miFrame.winfo_width() * 0.15)
height1 = int(miFrame.winfo_height() * 0.10)

codeA=Text(miFrame, width=width1, height=height1)
codeA.grid(row=2,column=1)

codeB=Text(miFrame, width=width1, height=height1)
codeB.grid(row=4,column=1)

# Creamos scrollbar
scrollVertA=Scrollbar(miFrame,command=codeA.yview)
# Colocamos el scrollbar en la ventana en la columna siguiente
scrollVertA.grid(row=2,column=2)
# El Scrollbar se adapta al tamano del textArea
scrollVertA.grid(row=2,column=2,sticky="nsew")
# la barra de Scroll se ubique con el texto
codeA.config(yscrollcommand=scrollVertA.set)

# Creamos scrollbar
scrollVertB=Scrollbar(miFrame,command=codeB.yview)
# Colocamos el scrollbar en la ventana en la columna siguiente
scrollVertB.grid(row=4,column=2)
# El Scrollbar se adapta al tamano del textArea
scrollVertB.grid(row=4,column=2,sticky="nsew")
# la barra de Scroll se ubique con el texto
codeB.config(yscrollcommand=scrollVertB.set)

# Codigo para el boton
def get_textA():
	return codeA.get("1.0",'end-1c')
#Metodos para realizar el analisis lexico
def codigoBotonLexico():
	textA = get_textA()
	textB = get_textB()
	listaA,listaB=separadorPalabaras(textA,textB)
	if len(listaA) > 0 and len(listaB) > 0:
		lexAString.set('Correcto')
		lexBString.set('Correcto')
	if len(listaA) > 0 and len(listaB) == 0:
		lexAString.set('Correcto')
		lexBString.set('Incorrecto')
	if len(listaA) == 0 and len(listaB) > 0:
		lexAString.set('Incorrecto')
		lexBString.set('Correcto')
	if len(listaA) == 0 and len(listaB) == 0:
		lexAString.set('Incorrecto')
		lexBString.set('Incorrecto')

	print("\n\n************** LISTA 1 ******************")
	print(listaA)
	print("\n\n************** LISTA 2 ******************")
	print(listaB)
	print("\n\n")


def separadorPalabaras(stringA,stringB):
	listaTokenA=separadorLista(stringA.split('\n'))
	listaTokenB=separadorLista(stringB.split('\n'))
	return listaTokenA,listaTokenB

def separadorLista(lista):
	retorno=[]
	vacio=[]
	for iterador in lista:
		listatemp=iterador.split(' ')
		temp=[]
		for palabra in listatemp:
			token=generarToken(palabra)
			if token == '':
				return vacio
			temp.append(token)
		retorno.append(temp)
	return retorno

def generarToken(palabra):
	lex.input(palabra)
	token=lex.token()
	if token is not None:
		return token.type
	return ''
#-----------------------------------------------------------------------------------------------
#Metodos para realizar el analisis sintactico
def get_textB():
	return codeB.get("1.0",'end-1c')

def codigoBotonSintactico():
	synctAString.set('Correcto')
	synctBString.set('Incorrecto')
	textA = get_textA()
	textB = get_textB()
	listaA=validarSintaxis(textA.split('\n'))
	listaB=validarSintaxis(textB.split('\n'))
	if len(listaA) > 0 and len(listaB) > 0:
		synctAString.set('Correcto')
		synctBString.set('Correcto')
	elif len(listaA) > 0 and len(listaB) == 0:
		synctAString.set('Correcto')
		synctBString.set('Incorrecto')
	elif len(listaA) == 0 and len(listaB) > 0:
		synctAString.set('Incorrecto')
		synctBString.set('Correcto')
	elif len(listaA) == 0 and len(listaB) == 0:
		synctAString.set('Incorrecto')
		synctBString.set('Incorrecto')
	print("\n\n************** LISTA ARB 1 ******************")
	print(listaA)
	print("\n\n************** LISTA ARB 2 ******************")
	print(listaB)
	print("\n\n")

def validarSintaxis(lista):
	listRetorno=[]
	vacia=[]
	for linea in lista:
		resultado=analizadorSintactico(linea)
		if resultado == '':
			return vacia
		listRetorno.append(resultado)
	return listRetorno

def analizadorSintactico(linea):
	analizador=gramarRuby.parser
	# ipdb.set_trace()
	arbol=analizador.parse(linea)
	if arbol is not None:
		return arbol
	return ''

#----------------------------------------------------------------------------------------------
def codigoBotonPlagio():
    textA = get_textA()
    textB = get_textB()
    listaA=generarTokenlista(textA.replace('\n',' ').split(' '))
    listaB=generarTokenlista(textB.replace('\n',' ').split(' '))
    listaCom=comparar(listaA,listaB)
    if len(listaA) == len(listaCom):
        plagString.set('100%')
    else:
        plagio=calcularPlagio(len(listaA),len(listaCom))
        print(plagio)
        plagString.set(str(plagio)+'%')

    print(listaA)
    print(listaB)
    print(listaCom)
def comparar(lista1,lista2):
    comparacion = [item for item in lista1 if item in lista2]
    return comparacion
def calcularPlagio(numeroToken,numeroConicidencias):
    plagio=(numeroConicidencias*100)//numeroToken
    return plagio
def generarTokenlista(lista):
    listaretorno=[]
    for item in lista:
        token=generarToken(item)
        listaretorno.append(token)
    return listaretorno
# Crear botones
botonLex=Button(root, text="Lexical analysis", command=codigoBotonLexico)
botonLex.config(cursor='hand2')
botonLex.pack()

botonSynct=Button(root, text="Syntactic analysis", command=codigoBotonSintactico)
botonSynct.config(cursor='hand2')
botonSynct.pack()

botonComp=Button(root, text="% plagiary", command=codigoBotonPlagio)
botonComp.config(cursor='hand2')
botonComp.pack()

# Codigo para el boton
# def codigoBoton2():
# 	print(minombre.get())

###################################################################################

root.mainloop()


"""
CODE

i = 10
if i == 10
	puts "yes"
else
	puts "no"
end


"""

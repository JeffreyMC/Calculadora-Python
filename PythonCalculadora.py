# calculadora simple

from tkinter import *

import parser

ventanaPrincipal = Tk()

ventanaPrincipal.title('Calculadora')

# ESPACIO EN EL QUE SE MOSTRARÁN LAS OPERACIONES
display = Entry(ventanaPrincipal)
display.grid(row=1, columnspan=6, sticky=W+E)

# FUNCIONES
# función que obtiene números
indice = 0


def obtenerNumeros(n):
    global indice
    display.insert(indice, n)
    indice += 1


def obtenerOperacion(operacion):
    global indice
    longitud = len(operacion)
    display.insert(indice, operacion)
    indice += longitud


# limpiar pantalla
def limpiarPantalla():
    display.delete(0, END)


# eliminar un digito
def eliminaDigito():
    estadoPantalla = display.get()
    if len(estadoPantalla):
        nuevoEstadoPantalla = estadoPantalla[:-1]
        limpiarPantalla()
        display.insert(0, nuevoEstadoPantalla)
    else:
        limpiarPantalla()


# realizar operaciones
def calcular():
    estadoPantalla = display.get()
    try:
        expresion = parser.expr(estadoPantalla).compile()
        resultado = eval(expresion)
        limpiarPantalla()
        display.insert(0, resultado)
    except expression as identifier:
        limpiarPantalla()
        display.insert(0, 'ERROR')


# botones números
Button(ventanaPrincipal, text='1', command=lambda: obtenerNumeros(1)).grid(
    row=2, column=0, sticky=W+E)
Button(ventanaPrincipal, text='2', command=lambda: obtenerNumeros(2)).grid(
    row=2, column=1, sticky=W+E)
Button(ventanaPrincipal, text='3', command=lambda: obtenerNumeros(1)).grid(
    row=2, column=2, sticky=W+E)
Button(ventanaPrincipal, text='4', command=lambda: obtenerNumeros(3)).grid(
    row=3, column=0, sticky=W+E)
Button(ventanaPrincipal, text='5', command=lambda: obtenerNumeros(4)).grid(
    row=3, column=1, sticky=W+E)
Button(ventanaPrincipal, text='6', command=lambda: obtenerNumeros(5)).grid(
    row=3, column=2, sticky=W+E)
Button(ventanaPrincipal, text='7', command=lambda: obtenerNumeros(6)).grid(
    row=4, column=0, sticky=W+E)
Button(ventanaPrincipal, text='8', command=lambda: obtenerNumeros(7)).grid(
    row=4, column=1, sticky=W+E)
Button(ventanaPrincipal, text='9', command=lambda: obtenerNumeros(8)).grid(
    row=4, column=2, sticky=W+E)

# botones operaciones
Button(ventanaPrincipal, text='AC', command=lambda: limpiarPantalla()).grid(
    row=5, column=0, sticky=W+E)
Button(ventanaPrincipal, text='0', command=lambda: obtenerNumeros(0)).grid(
    row=5, column=1, sticky=W+E)
Button(ventanaPrincipal, text='.', command=lambda: obtenerNumeros(
    '.')).grid(row=5, column=2, sticky=W+E)

Button(ventanaPrincipal, text='+', command=lambda: obtenerOperacion('+')
       ).grid(row=2, column=3, sticky=W+E)
Button(ventanaPrincipal, text='-', command=lambda: obtenerOperacion('-')
       ).grid(row=3, column=3, sticky=W+E)
Button(ventanaPrincipal, text='*', command=lambda: obtenerOperacion('*')
       ).grid(row=4, column=3, sticky=W+E)
Button(ventanaPrincipal, text='/', command=lambda: obtenerOperacion('/')
       ).grid(row=5, column=3, sticky=W+E)

Button(ventanaPrincipal, text='🡄', command=lambda: eliminaDigito()).grid(
    row=2, column=4, sticky=W+E, columnspan=2)
Button(ventanaPrincipal, text='exp', command=lambda: obtenerOperacion(
    '**')).grid(row=3, column=4, sticky=W+E)
Button(ventanaPrincipal, text='^2', command=lambda: obtenerOperacion(
    '**2')).grid(row=3, column=5, sticky=W+E)
Button(ventanaPrincipal, text='(', command=lambda: obtenerOperacion(
    '(')).grid(row=4, column=4, sticky=W+E)
Button(ventanaPrincipal, text=')', command=lambda: obtenerOperacion(
    ')')).grid(row=4, column=5, sticky=W+E)
Button(ventanaPrincipal, text='=', command=lambda: calcular()).grid(
    row=5, column=4, sticky=W+E, columnspan=2)

# trata de hacer resposive los botones
filas = 5
columnas = 5
for i in range(filas):
    ventanaPrincipal.grid_rowconfigure(i,  weight=1)
for i in range(columnas):
    ventanaPrincipal.grid_columnconfigure(i,  weight=1)

# inicia la aplicación
ventanaPrincipal.mainloop()

import sys
import tkinter as tk
from tkinter import *


# posiciones N(arriba), E(derecha), S(abajo), W(izquierda)
class Aplicacion:
    def __init__(self):
        self.ventana = tk.Tk()
        # para obtener medidas de la pantalla para la ventana
        self.altoPantalla = self.ventana.winfo_screenheight()
        self.anchoPantalla = self.ventana.winfo_screenwidth()
        self.alto = int(self.altoPantalla-300)
        self.ancho = int(self.anchoPantalla-300)

        # formatos para la ventana de la app
        self.ventana.geometry(f'{self.ancho}x{self.alto}')
        self.ventana.title('OLC2-PROYECTO1')
        self.ventana['bg'] = '#49A'

        # llamado al menu principal
        self.crearMenu()

        # configuracion del area de trabajo
        self.ventana.rowconfigure(0, minsize=self.alto, weight=1)
        self.ventana.columnconfigure(1, weight=1)
        self.ventana.columnconfigure(2, minsize=30)
        self.ventana.columnconfigure(3, weight=1)

        # creacon y agregacion de los componentes
        self.crearComponentes()

        # corra la applicacion
        self.ventana.mainloop()


    # funcionalidad para salir
    def salir(self):
        self.ventana.quit()
        self.ventana.destroy()
        sys.exit()

    # ------------------------------
    # funcionalidad para reportes
    def reporteErrores(self):
        print('Reporte de error')

    def reporteSemantico(self):
        print('Reporte de erores Semanticos')

    def tablaSimbolo(self):
        print('Reporte de tabla de simbolos')

    def tablaBD(self):
        print('Reporte de taba de BD')

    # ---------------------------------


    # menu principal
    def crearMenu(self):
        menuPrincipal = Menu(self.ventana)
        menuPrincipal['bg'] = '#49A'

        # subMenu para manejo de archivos
        subMenuArchivo = Menu(menuPrincipal, tearoff=False)
        subMenuArchivo.add_command(label='Abrir')
        subMenuArchivo.add_separator()
        subMenuArchivo.add_command(label='Salir',command=self.salir)
        
        # subMenu para menjo de reportes
        subMenuReportes = Menu(menuPrincipal, tearoff=False)
        subMenuReportes.add_command(label='Tabla Simbolos', command=self.tablaSimbolo)
        subMenuReportes.add_command(label='Tabla de Errores', command=self.reporteErrores)
        subMenuReportes.add_command(label='Tabla BD', command=self.tablaBD)
        subMenuReportes.add_command(label='Errores Semanticos', command=self.reporteSemantico)

        menuPrincipal.add_cascade(menu=subMenuArchivo, label='Archivo')
        menuPrincipal.add_cascade(menu=subMenuReportes, label='Reportes')
        self.ventana.config(menu=menuPrincipal)


    #  creacion de componentes
    def crearComponentes(self):
        frameBotones = Frame(relief=RAISED, bd=2)
        frameBotones['bg'] = '#49A'
        botonAbrir = Button(frameBotones, text='Abrir')
        botonCompilar = Button(frameBotones, text='Compilar')
        # expasion de los botones de forma horizontal (stiky)
        botonAbrir.grid(row=0, column=0, sticky='WE', padx=5, pady= 5)
        botonCompilar.grid(row=1, column=0, sticky='WE', padx=5, pady=5)
        frameBotones.grid(row=0, column=0, sticky='NS')


        frameEntrada = Frame(relief=RAISED, bd=1)
        frameEntrada.rowconfigure(0, minsize=self.alto, weight=1)
        frameEntrada.columnconfigure(0, weight=1)

        self.textAreaEntrada = Text(frameEntrada, wrap=WORD)
        self.textAreaEntrada.grid(row=0, column=0, sticky='nswe')

        scrollbar = Scrollbar(frameEntrada, orient='vertical', command=self.textAreaEntrada.yview)
        scrollbar.grid(row=0, column=1, sticky='ns')
        self.textAreaEntrada['yscrollcommand'] = scrollbar.set

        frameEntrada.grid(row=0, column=1, sticky='nswe')

        separador = Frame(relief=RAISED, bd=1)
        separador.grid(row=0, column=2, sticky='ns')

        self.textAreaSalida = Text(wrap=WORD)
        self.textAreaSalida.grid(row=0, column=3, sticky='nswe')


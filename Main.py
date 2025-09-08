from Cola import Cola
from Paciente import Paciente
import tkinter as tk
from tkinter import ttk

#cola de pacientes
cola_pacientes = Cola()

#tiempos de cada consulta
tiempos_especialidad = {
    "Medicina General": 10,
    "Pediatría": 15,
    "Ginecología": 20,
    "Dermatología": 25
}

#Ventana principal
ventana = tk.Tk()
ventana.title("Ventana de prueba")
ventana.geometry("900x500")

# Configurar grid para que sea responsive
ventana.grid_rowconfigure(3, weight=1)
ventana.grid_columnconfigure(0, weight=1)
ventana.grid_columnconfigure(1, weight=1)
ventana.grid_columnconfigure(2, weight=1)
ventana.grid_columnconfigure(3, weight=1)

#paciente
etiqueta_nombre = tk.Label(ventana, text="Nombre del paciente")
etiqueta_nombre.grid(row=0, column=0, padx=5, pady=5, sticky="w")

nombre_paciente = tk.Entry(ventana, width=40)
nombre_paciente.grid(row=0, column=1, padx=5, pady=5, sticky="w")

etiqueta_edad = tk.Label(ventana, text="Edad del paciente")
etiqueta_edad.grid(row=1, column=0, padx=5, pady=5, sticky="w")

edad_paciente = tk.Entry(ventana, width=5)
edad_paciente.grid(row=1, column=1, padx=5, pady=5, sticky="w")

#especialidad
etiqueta_especialidad = tk.Label(ventana, text="Especialidad")
etiqueta_especialidad.grid(row=2, column=0, padx=5, pady=5, sticky="w")

especilidad_seleccionada = tk.StringVar(ventana)
especilidad_seleccionada.set("Seleccione una especialidad")

opciones_especialidad = [
    "Medicina General",
    "Pediatría",
    "Ginecología",
    "Dermatología"
]

menu_especialidad = tk.OptionMenu(ventana, especilidad_seleccionada, *opciones_especialidad)
menu_especialidad.grid(row=2, column=1, padx=5, pady=5, sticky="w")

#Funciones para agregar pacientes a treeview
def agregar_paciente():
    nombre = nombre_paciente.get().strip()
    edad = edad_paciente.get().strip()
    especialidad = especilidad_seleccionada.get()
    tiempo_consulta = tiempos_especialidad[especialidad]

    paciente = Paciente(nombre, int(edad), especialidad, tiempo_consulta)
    cola_pacientes.encolar(paciente)

    actualizar_tabla()

    nombre_paciente.delete(0, tk.END)
    edad_paciente.delete(0, tk.END)
    especilidad_seleccionada.set("Seleccione una especialidad")


def actualizar_tabla():
    for item in tabla_pacientes.get_children():
        tabla_pacientes.delete(item)

    for i, paciente in enumerate(cola_pacientes.obtener_todos(), 1):
        tabla_pacientes.insert("", "end", values=(
            i,
            paciente.nombre,
            paciente.edad,
            paciente.especialidad,
            f"{paciente.tiempo_consulta} min"
        ))

#boton para crear turno en cola
boton_agregar = tk.Button(ventana, text="Crear turno", command= agregar_paciente)
boton_agregar.grid(row=3, column=0, padx=5, pady=5, sticky="n")

#Tabla de pacientes en cola
tabla_pacientes = ttk.Treeview(ventana, columns=("#", "Nombre", "Edad", "Especialidad", "Tiempo en cola"), show="headings")
tabla_pacientes.grid(row=3, column=1, sticky="nsew", padx=10, pady=10)

#Columnas de la tabla
tabla_pacientes.heading("#", text="#")
tabla_pacientes.heading("Nombre", text="Nombre")
tabla_pacientes.heading("Edad", text="Edad")
tabla_pacientes.heading("Especialidad", text="Especialidad")
tabla_pacientes.heading("Tiempo en cola", text="Tiempo")

tabla_pacientes.column("#", width=40, anchor="center")
tabla_pacientes.column("Nombre", width=150, anchor="center")
tabla_pacientes.column("Edad", width=50, anchor="center")
tabla_pacientes.column("Especialidad", width=150, anchor="center")
tabla_pacientes.column("Tiempo en cola", width=100, anchor="center")


if __name__=="__main__":
    ventana.mainloop()
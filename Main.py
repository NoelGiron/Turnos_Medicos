import tkinter as tk

#Ventana principal
ventana = tk.Tk()
ventana.title("Ventana de prueba")
ventana.geometry("800x600")

#paciente
etiqueta_nombre = tk.Label(ventana, text="Nombre del paciente")
etiqueta_nombre.grid(row=0, column=0, padx=5, pady=5, sticky="e")

nombre_paciente = tk.Entry(ventana, width=30)
nombre_paciente.grid(row=0, column=1, padx=5, pady=5, sticky="w")

#especialidad
etiqueta_especialidad = tk.Label(ventana, text="Especialidad")
etiqueta_especialidad.grid(row=1, column=0, padx=5, pady=5, sticky="e")

especilidad_seleccionada = tk.StringVar(ventana)
especilidad_seleccionada.set("Seleccione una especialidad")

opciones_especialidad = [
    "Medicina General",
    "Pediatría",
    "Ginecología",
    "Dermatología"
]

menu_especialidad = tk.OptionMenu(ventana, especilidad_seleccionada, *opciones_especialidad)
menu_especialidad.grid(row=1, column=1, padx=5, pady=5, sticky="w")



if __name__=="__main__":
    ventana.mainloop()
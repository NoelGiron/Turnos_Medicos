import tkinter as tk

#Ventana principal
ventana = tk.Tk()
ventana.title("Ventana de prueba")
ventana.geometry("800x600")

#paciente
etiqueta_nombre = tk.Label(ventana, text="Nombre del paciente")
etiqueta_nombre.pack(pady=5)
nombre_paciente = tk.Entry(ventana)
nombre_paciente.pack(pady=5)

etiqueta_especialidad = tk.Label(ventana, text="Especialidad")
etiqueta_especialidad.pack(pady=5)
lista_especialidad = tk.Listbox(ventana, height=4)
lista_especialidad.pack(pady=5)
lista_especialidad.insert(1, "Medicina General")
lista_especialidad.insert(2, "Pediatría")
lista_especialidad.insert(3, "Ginecología")
lista_especialidad.insert(4, "Dermatología")



if __name__=="__main__":
    ventana.mainloop()
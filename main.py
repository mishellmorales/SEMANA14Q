import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from tkcalendar import Calendar

class AgendaApp:
    def _init_(self, master):
        self.master = master
        master.title("Agenda Personal")

        # Contenedor para la lista de eventos
        self.eventos_frame = ttk.Frame(master)
        self.eventos_frame.pack(pady=10)

        self.lista_eventos = ttk.Treeview(self.eventos_frame, columns=("Fecha", "Hora", "Descripción"), selectmode="extended")
        self.lista_eventos.heading("#0", text="ID")
        self.lista_eventos.heading("Fecha", text="Fecha")
        self.lista_eventos.heading("Hora", text="Hora")
        self.lista_eventos.heading("Descripción", text="Descripción")
        self.lista_eventos.pack()

        # Contenedor para la entrada de datos
        self.entrada_frame = ttk.Frame(master)
        self.entrada_frame.pack(pady=10)

        ttk.Label(self.entrada_frame, text="Fecha:").grid(row=0, column=0, padx=5, pady=5)
        self.calendario = Calendar(self.entrada_frame, selectmode="day", date_pattern="yyyy-mm-dd")
        self.calendario.grid(row=0, column=1, padx=5, pady=5)

        ttk.Label(self.entrada_frame, text="Hora:").grid(row=1, column=0, padx=5, pady=5)
        self.entry_hora = ttk.Entry(self.entrada_frame)
        self.entry_hora.grid(row=1, column=1, padx=5, pady=5)

        ttk.Label(self.entrada_frame, text="Descripción:").grid(row=2, column=0, padx=5, pady=5)
        self.entry_descripcion = ttk.Entry(self.entrada_frame)
        self.entry_descripcion.grid(row=2, column=1, padx=5, pady=5)

        # Contenedor para los botones
        self.botones_frame = ttk.Frame(master)
        self.botones_frame.pack(pady=10)

        self.btn_agregar = ttk.Button(self.botones_frame, text="Agregar Evento", command=self.agregar_evento)
        self.btn_agregar.grid(row=0, column=0, padx=5, pady=5)

        self.btn_eliminar = ttk.Button(self.botones_frame, text="Eliminar Evento Seleccionado", command=self.eliminar_evento)
        self.btn_eliminar.grid(row=0, column=1, padx=5, pady=5)

        self.btn_salir = ttk.Button(self.botones_frame, text="Salir", command=master.quit)
        self.btn_salir.grid(row=0, column=2, padx=5, pady=5)

    def agregar_evento(self):
        fecha = self.calendario.get_date()
        hora = self.entry_hora.get()
        descripcion = self.entry_descripcion.get()

        if fecha and hora and descripcion:
            self.lista_eventos.insert("", "end", values=(fecha, hora, descripcion))
            self.calendario.set_date("")  # Limpiar el calendario después de agregar evento
            self.entry_hora.delete(0, 'end')
            self.entry_descripcion.delete(0, 'end')
        else:
            messagebox.showwarning("Datos faltantes", "Por favor ingrese todos los datos.")

    def eliminar_evento(self):
        seleccionados = self.lista_eventos.selection()
        if seleccionados:
            confirmacion = messagebox.askyesno("Confirmar eliminación", "¿Está seguro de que desea eliminar el evento seleccionado?")
            if confirmacion:
                for item in seleccionados:
                    self.lista_eventos.delete(item)
        else:
            messagebox.showinfo("Sin selección", "Por favor seleccione un evento para eliminar.")

def main():
    root = tk.Tk()
    app = AgendaApp(root)
    root.mainloop()

if _name_ == "_main_":
    main()
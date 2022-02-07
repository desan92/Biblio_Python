import bbdd_library
from tkinter import *
from tkinter import ttk
from tkinter import messagebox

class App(Tk):
    def __init__(self, *args, **kwargs):
        Tk.__init__(self, *args, **kwargs)

        container = Frame(self)
        container.pack(side="top", fill="both", expand=True)

        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.frames = {}

        for F in (PaginaInicial, PaginaUsuaris, PaginaLlibres):
            frame = F(container, self)

            self.frames[F] = frame

            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame(PaginaInicial)

    def show_frame(self, cont):
        frame = self.frames[cont]
        frame.tkraise()


class PaginaInicial(Frame):
    def __init__(self, parent, controller):
        Frame.__init__(self, parent)

        # create all of the main containers
        self.top_frame = Frame(self, bg='#7B5A08', width=1200, height=100, pady=3)
        self.main_frame = Frame(self, bg='#ffffc4', width=1200, height=500, padx=3, pady=3)

        # layout all of the main containers
        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure(1, weight=1)

        self.top_frame.grid(row=0, sticky="ew")
        self.main_frame.grid(row=1, sticky="nsew")

        self.Title()

        # create the center widgets
        self.main_frame.grid_rowconfigure(0, weight=1)
        self.main_frame.grid_columnconfigure(1, weight=1)

        self.ctr_mid = Frame(self.main_frame, bg='#ffffc4', width=250, height=190, padx=3, pady=3)
        self.ctr_mid.grid(row=0, column=1, sticky="nsew")

        self.btn_users = Button(self.ctr_mid, fg="white", bg="#7B5A08", font="HELVETICA 10 bold", text="Search Users",
                           relief="flat", cursor="hand1", width=30, height=5, command=lambda: controller.show_frame(PaginaUsuaris))
        self.btn_users.place(relx=0.35, rely=0.5, anchor=CENTER)
        self.btn_books = Button(self.ctr_mid, fg="white", bg="#7B5A08", font="HELVETICA 10 bold", text="Search Books",
                           relief="flat", cursor="hand1", width=30, height=5, command=lambda: controller.show_frame(PaginaLlibres))
        self.btn_books.place(relx=0.65, rely=0.5, anchor=CENTER)

    def Title(self):
        # create the widgets for the top frame
        self.model_label = Label(self.top_frame, text='London Library', fg="white", bg="#7B5A08", font="HELVETICA 30 bold")

        # layout the widgets in the top frame
        self.model_label.place(relx=0.5, rely=0.5, anchor=CENTER)

class PaginaUsuaris(Frame):
    def __init__(self, parent, controller):
        Frame.__init__(self, parent)

        # create all of the main containers
        self.top_frame = Frame(self, bg='#7B5A08', width=1200, height=100, pady=3)
        self.main_frame = Frame(self, bg='#ffffc4', width=1200, height=500, padx=3, pady=3)

        # layout all of the main containers
        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure(1, weight=1)

        self.top_frame.grid(row=0, sticky="ew")
        self.main_frame.grid(row=1, sticky="nsew")

        # create the center widgets
        self.main_frame.grid_rowconfigure(0, weight=1)
        self.main_frame.grid_columnconfigure(1, weight=1)

        self.ctr_left = Frame(self.main_frame, bg='#ffffc4', width=350, height=190)
        self.ctr_right = Frame(self.main_frame, bg='#ffffc4', width=550, height=190, padx=3, pady=3)

        self.ctr_left.grid(row=0, column=0, sticky="ns")
        self.ctr_right.grid(row=0, column=1, sticky="nsew")

        self.Title()
        self.BuscadorId()
        self.InsertUsuari()
        self.DibuixarLlista(id="")

        self.btn_tornar = Button(self.ctr_right, text="Pagina Inicial", relief="flat", background="#7B5A08", cursor="hand1",
                            foreground="white", command=lambda: controller.show_frame(PaginaInicial)).place(relx=0.9, rely=0.9, anchor=CENTER, width=90)

    def Title(self):
        # create the widgets for the top frame
        self.model_label = Label(self.top_frame, text='London Library', fg="white", bg="#7B5A08", font="HELVETICA 30 bold")

        # layout the widgets in the top frame
        self.model_label.place(relx=0.5, rely=0.5, anchor=CENTER)

    def BuscadorId(self):
        ref = ""
        self.id = StringVar()

        # BUSCADOR PER ID.
        self.model_label = Label(self.ctr_left, text='Search Users', fg="#7B5A08", bg="#ffffc4", font="HELVETICA 14 bold")
        self.model_label.place(relx=0.5, rely=0.1, anchor=CENTER)
        self.txt_id = Entry(self.ctr_left, font=("Arial", 12), textvariable=self.id).place(relx=0.5, rely=0.18, anchor=CENTER)
        self.btn_search = Button(self.ctr_left, text="Buscar", relief="flat", background="#7B5A08", cursor="hand1",
                            foreground="white", command=lambda: self.buscarUsuari(self.id.get())).place(relx=0.35, rely=0.26, anchor=CENTER, width=90)
        self.btn_reset = Button(self.ctr_left, text="Restablir", relief="flat", background="#7B5A08", cursor="hand1",
                           foreground="white", command=lambda: self.buscarUsuari(ref)).place(relx=0.65, rely=0.26, anchor=CENTER, width=90)

    def InsertUsuari(self):
        self.nom = StringVar()
        self.cognom = StringVar()
        self.telefon = StringVar()
        self.email = StringVar()

        # INSERT USUARIS
        self.model_label = Label(self.ctr_left, text='Insert Users', fg="#7B5A08", bg="#ffffc4",
                                 font="HELVETICA 14 bold")
        self.model_label.place(relx=0.5, rely=0.4, anchor=CENTER)
        self.label_nom = Label(self.ctr_left, foreground="#7B5A08", background="#ffffc4", text="Nom:",
                               font="HELVETICA 8 bold").place(
            relx=0.15, rely=0.5, anchor=CENTER)
        self.txt_nom = Entry(self.ctr_left, font=("Arial", 12), textvariable=self.nom).place(relx=0.5, rely=0.5, anchor=CENTER)
        self.label_cognom = Label(self.ctr_left, foreground="#7B5A08", background="#ffffc4", text="Cognom:",
                                  font="HELVETICA 8 bold").place(
            relx=0.15, rely=0.6, anchor=CENTER)
        self.txt_cognom = Entry(self.ctr_left, font=("Arial", 12), textvariable=self.cognom).place(relx=0.5, rely=0.6, anchor=CENTER)
        self.label_tlf = Label(self.ctr_left, foreground="#7B5A08", background="#ffffc4", text="Telefon:",
                               font="HELVETICA 8 bold").place(
            relx=0.15, rely=0.7, anchor=CENTER)
        self.txt_tlf = Entry(self.ctr_left, font=("Arial", 12), textvariable=self.telefon).place(relx=0.5, rely=0.7, anchor=CENTER)
        self.label_email = Label(self.ctr_left, foreground="#7B5A08", background="#ffffc4", text="Email:",
                                 font="HELVETICA 8 bold").place(
            relx=0.15, rely=0.8, anchor=CENTER)
        self.txt_email = Entry(self.ctr_left, font=("Arial", 12), textvariable=self.email).place(relx=0.5, rely=0.8, anchor=CENTER)
        self.btn_insert = Button(self.ctr_left, text="Insertar", relief="flat", background="#7B5A08", cursor="hand1",
                                 foreground="white", command=self.GuardarUsuari).place(relx=0.5, rely=0.9, anchor=CENTER, width=90)

    def DibuixarLlista(self, id):
        self.llista = ttk.Treeview(self.ctr_right, columns=(1, 2, 3, 4, 5), show="headings", height="15")
        self.estil = ttk.Style()
        self.estil.theme_use("clam")

        # aixo es el que es vol canviar.
        self.estil.configure("Treeview.Heading", background="#7B5A08", relief="flat", foreground="white")
        self.llista.heading(1, text="Id")
        self.llista.heading(2, text="Nom")
        self.llista.heading(3, text="Cognom")
        self.llista.heading(4, text="Telefon")
        self.llista.heading(5, text="Email")
        self.llista.column(1, anchor=CENTER, width=80)  # modifica alguna caracteristica de la columna
        self.llista.column(2, anchor=CENTER)
        self.llista.column(3, anchor=CENTER)
        self.llista.column(4, anchor=CENTER, width=120)
        self.llista.column(5, anchor=CENTER)
        self.llista.place(relx=0.5, rely=0.4, anchor=CENTER)

        self.llista.bind("<Double 1>", self.obtenirFila)
        if id == "":
            d = bbdd_library.bbdd_biblioteca()
            elements = d.SelectAllUsers()

            for i in elements:
                self.llista.insert('', 'end', value=i)

        else:
            d = bbdd_library.bbdd_biblioteca()
            elements = d.SelectUser(id)

            for i in elements:
                self.llista.insert('', 'end', value=i)

        print(elements)

    def NetejarLlista(self):
        self.llista.delete(*self.llista.get_children())

    def buscarUsuari(self, id):
        self.NetejarLlista()
        self.DibuixarLlista(id)

    def GuardarUsuari(self):
        id = ""
        element = [self.nom.get(), self.cognom.get(), self.telefon.get(), self.email.get()]
        d = bbdd_library.bbdd_biblioteca()  # es crida a la classe de la bbdd
        d.InsertUser(element)  # crida a la funcio de la bbdd insert

        # es posa el nom, edat i carrera en blanc
        self.nom.set("")
        self.cognom.set("")
        self.telefon.set("")
        self.email.set("")

        # es neteja la llista i es torna a posar.
        self.NetejarLlista()
        self.DibuixarLlista(id)

    def obtenirFila(self, event):
        self.name = StringVar()
        self.surname = StringVar()
        self.phone = StringVar()
        self.mail = StringVar()

        #no fa res, aparentment.
        #NomFila = self.llista.identify_row(event.y)

        element = self.llista.item(self.llista.focus())
        print(element)
        i = element['values'][0]
        n = element['values'][1]
        s = element['values'][2]
        p = element['values'][3]
        m = element['values'][4]

        #El método set() asigna un valor a una variable de control. Se utiliza para modificar el valor o estado de un widget
        self.name.set(n)
        self.surname.set(s)
        self.phone.set(p)
        self.mail.set(m)

        pop = Toplevel(self.main_frame, background="#ffffc4")
        pop.geometry("400x300")
        label_n = Label(pop, foreground="#7B5A08", background="#ffffc4", text="Nom:",
                                 font="HELVETICA 8 bold").place(relx=0.15, rely=0.2, anchor=CENTER)
        txt_n = Entry(pop, textvariable=self.name).place(relx=0.45, rely=0.2, anchor=CENTER)
        label_s = Label(pop, foreground="#7B5A08", background="#ffffc4", text="Cognom:",
                        font="HELVETICA 8 bold").place(relx=0.15, rely=0.3, anchor=CENTER)
        txt_s = Entry(pop, textvariable=self.surname).place(relx=0.45, rely=0.3, anchor=CENTER)
        label_p = Label(pop, foreground="#7B5A08", background="#ffffc4", text="Telefon:",
                        font="HELVETICA 8 bold").place(relx=0.15, rely=0.4, anchor=CENTER)
        txt_p = Entry(pop, textvariable=self.phone).place(relx=0.45, rely=0.4, anchor=CENTER)
        label_p = Label(pop, foreground="#7B5A08", background="#ffffc4", text="Email:",
                        font="HELVETICA 8 bold").place(relx=0.15, rely=0.5, anchor=CENTER)
        txt_m = Entry(pop, textvariable=self.mail).place(relx=0.45, rely=0.5, anchor=CENTER)
        btn_canviar = Button(pop, text="Canviar", relief="flat", background="#7B5A08", cursor="hand1",
                                  foreground="white", command=lambda: self.editar(i, self.name.get(), self.surname.get(), self.phone.get(), self.mail.get())).place(relx=0.4, rely=0.7, anchor=CENTER, width=90)
        btn_eliminar = Button(pop, text="Eliminar", relief="flat", background="#7B5A08", cursor="hand1",
                             foreground="white", command=lambda: self.eliminar(i)).place(relx=0.7, rely=0.7, anchor=CENTER, width=90)

    def editar(self, id, name, surname, phone, mail):
        ar = [name, surname, phone, mail]
        cadena = ""

        d = bbdd_library.bbdd_biblioteca()
        d.UpdateUser(ar, id)
        messagebox.showinfo(title="Actualitzacio", message="S'ha actualitzat correctament!")
        self.NetejarLlista()
        self.DibuixarLlista(cadena)


    def eliminar(self, id):
        cadena = ""
        d = bbdd_library.bbdd_biblioteca()
        d.DeleteUser(id)
        messagebox.showinfo(title="Eliminat", message="S'ha actualitzat correctament!")
        self.NetejarLlista()
        self.DibuixarLlista(cadena)


class PaginaLlibres(Frame):
    def __init__(self, parent, controller):
        Frame.__init__(self, parent)

        ref1 = ""
        ref2 = ""

        # create all of the main containers
        self.top_frame = Frame(self, bg='#7B5A08', width=1200, height=100, pady=3)
        self.main_frame = Frame(self, bg='#ffffc4', width=1200, height=500, padx=3, pady=3)

        # layout all of the main containers
        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure(1, weight=1)

        self.top_frame.grid(row=0, sticky="ew")
        self.main_frame.grid(row=1, sticky="nsew")

        # create the center widgets
        self.main_frame.grid_rowconfigure(0, weight=1)
        self.main_frame.grid_columnconfigure(1, weight=1)

        self.ctr_left = Frame(self.main_frame, bg='#ffffc4', width=350, height=190)
        self.ctr_right = Frame(self.main_frame, bg='#ffffc4', width=550, height=190, padx=3, pady=3)

        self.ctr_left.grid(row=0, column=0, sticky="ns")
        self.ctr_right.grid(row=0, column=1, sticky="nsew")

        self.Title()
        self.BuscardorLLibre()
        self.InsertLLibre()
        self.DibuixarLlista(ref1, ref2)

        self.btn_tornar = Button(self.ctr_right, text="Pagina Inicial", relief="flat", background="#7B5A08", cursor="hand1",
                            foreground="white", command=lambda: controller.show_frame(PaginaInicial)).place(relx=0.9, rely=0.9, anchor=CENTER, width=90)

    def Title(self):
        # create the widgets for the top frame
        self.model_label = Label(self.top_frame, text='London Library', fg="white", bg="#7B5A08", font="HELVETICA 30 bold")

        # layout the widgets in the top frame
        self.model_label.place(relx=0.5, rely=0.5, anchor=CENTER)

    def BuscardorLLibre(self):
        ref1 = ""
        ref2 = ""
        self.nom_llibre = StringVar()
        self.autor_llibre = StringVar()

        # BUSCADOR PER ID.
        self.model_label = Label(self.ctr_left, text='Search Books', fg="#7B5A08", bg="#ffffc4",
                                 font="HELVETICA 14 bold")
        self.model_label.place(relx=0.5, rely=0.1, anchor=CENTER)
        self.label_nom_llibre = Label(self.ctr_left, foreground="#7B5A08", background="#ffffc4", text="Nom:",
                               font="HELVETICA 8 bold").place(
            relx=0.15, rely=0.18, anchor=CENTER)
        self.txt_nom_llibre = Entry(self.ctr_left, font=("Arial", 12), textvariable=self.nom_llibre).place(relx=0.5, rely=0.18, anchor=CENTER)
        self.label_nom_autor = Label(self.ctr_left, foreground="#7B5A08", background="#ffffc4", text="Autor:",
                                      font="HELVETICA 8 bold").place(
            relx=0.15, rely=0.26, anchor=CENTER)
        self.txt_nom_autor = Entry(self.ctr_left, font=("Arial", 12), textvariable=self.autor_llibre).place(relx=0.5, rely=0.26, anchor=CENTER)
        self.btn_search = Button(self.ctr_left, text="Buscar", relief="flat", background="#7B5A08", cursor="hand1",
                                 foreground="white", command=lambda: self.buscarLLibre(self.nom_llibre.get(), self.autor_llibre.get())).place(relx=0.35, rely=0.34, anchor=CENTER, width=90)
        self.btn_reset = Button(self.ctr_left, text="Restablir", relief="flat", background="#7B5A08", cursor="hand1",
                                foreground="white", command=lambda: self.buscarLLibre(ref1, ref2)).place(relx=0.65, rely=0.34, anchor=CENTER, width=90)

    def InsertLLibre(self):
        self.nom = StringVar()
        self.llibre = StringVar()
        self.editorial = StringVar()

        # INSERT LLibres
        self.model_label = Label(self.ctr_left, text='Insert Books', fg="#7B5A08", bg="#ffffc4", font="HELVETICA 14 bold")
        self.model_label.place(relx=0.5, rely=0.5, anchor=CENTER)
        self.label_nom = Label(self.ctr_left, foreground="#7B5A08", background="#ffffc4", text="Nom:",
                          font="HELVETICA 8 bold").place(
            relx=0.15, rely=0.6, anchor=CENTER)
        self.txt_nom = Entry(self.ctr_left, font=("Arial", 12), textvariable=self.nom).place(relx=0.5, rely=0.6, anchor=CENTER)
        self.label_autor = Label(self.ctr_left, foreground="#7B5A08", background="#ffffc4", text="Autor:",
                            font="HELVETICA 8 bold").place(
            relx=0.15, rely=0.7, anchor=CENTER)
        self.txt_autor = Entry(self.ctr_left, font=("Arial", 12), textvariable=self.llibre).place(relx=0.5, rely=0.7, anchor=CENTER)
        self.label_editorial = Label(self.ctr_left, foreground="#7B5A08", background="#ffffc4", text="Editorial:",
                                font="HELVETICA 8 bold").place(
            relx=0.15, rely=0.8, anchor=CENTER)
        self.txt_editorial = Entry(self.ctr_left, font=("Arial", 12), textvariable=self.editorial).place(relx=0.5, rely=0.8, anchor=CENTER)
        self.btn_insert = Button(self.ctr_left, text="Insertar", relief="flat", background="#7B5A08", cursor="hand1",
                            foreground="white", command=self.GuardarLLibre).place(relx=0.5, rely=0.9, anchor=CENTER, width=90)

    def DibuixarLlista(self, ref1, ref2):
        self.llista = ttk.Treeview(self.ctr_right, columns=(1, 2, 3, 4, 5), show="headings", height="15")
        self.estil = ttk.Style()
        self.estil.theme_use("clam")

        # aixo es el que es vol canviar.
        self.estil.configure("Treeview.Heading", background="#7B5A08", relief="flat", foreground="white")
        self.llista.heading(1, text="Id")
        self.llista.heading(2, text="Nom llibre")
        self.llista.heading(3, text="Autor")
        self.llista.heading(4, text="Editorial")
        self.llista.heading(5, text="Disponible")
        self.llista.column(1, anchor=CENTER, width=80)  # modifica alguna caracteristica de la columna
        self.llista.column(2, anchor=CENTER)
        self.llista.column(3, anchor=CENTER)
        self.llista.column(4, anchor=CENTER)
        self.llista.column(5, anchor=CENTER, width=120)
        self.llista.place(relx=0.5, rely=0.4, anchor=CENTER)

        self.llista.bind("<Double 1>", self.obtenirFila)
        if ref1 == "" and ref2 == "":
            d = bbdd_library.bbdd_biblioteca()
            elements = d.SelectAllBooks()

            for i in elements:
                self.llista.insert('', 'end', value=i)

        else:
            d = bbdd_library.bbdd_biblioteca()
            elements = d.SelectBooks(ref1, ref2)

            for i in elements:
                self.llista.insert('', 'end', value=i)

    def NetejarLlista(self):
        self.llista.delete(*self.llista.get_children())

    def buscarLLibre(self, ref1, ref2):
        self.NetejarLlista()
        self.DibuixarLlista(ref1, ref2)

    def GuardarLLibre(self):
        ref1 = ""
        ref2 = ""
        element = [self.nom.get(), self.llibre.get(), self.editorial.get()]
        d = bbdd_library.bbdd_biblioteca()  # es crida a la classe de la bbdd
        d.InsertBook(element)  # crida a la funcio de la bbdd insert

        # es posa el nom, edat i carrera en blanc
        self.nom.set("")
        self.llibre.set("")
        self.editorial.set("")

        # es neteja la llista i es torna a posar.
        self.NetejarLlista()
        self.DibuixarLlista(ref1, ref2)

    def obtenirFila(self, event):
        self.name_book = StringVar()
        self.name_author = StringVar()
        self.name_editorial = StringVar()

        #no fa res, aparentment.
        #NomFila = self.llista.identify_row(event.y)

        element = self.llista.item(self.llista.focus())
        print(element)
        i = element['values'][0]
        nb = element['values'][1]
        na = element['values'][2]
        ne = element['values'][3]
        disponible = element['values'][4]

        #El método set() asigna un valor a una variable de control. Se utiliza para modificar el valor o estado de un widget
        self.name_book.set(nb)
        self.name_author.set(na)
        self.name_editorial.set(ne)

        pop = Toplevel(self.main_frame, background="#ffffc4")
        pop.geometry("400x300")

        label_nb = Label(pop, foreground="#7B5A08", background="#ffffc4", text="Llibre:",
                                 font="HELVETICA 8 bold").place(relx=0.15, rely=0.2, anchor=CENTER)
        txt_nb = Entry(pop, textvariable=self.name_book).place(relx=0.45, rely=0.2, anchor=CENTER)
        label_na = Label(pop, foreground="#7B5A08", background="#ffffc4", text="Autor:",
                        font="HELVETICA 8 bold").place(relx=0.15, rely=0.3, anchor=CENTER)
        txt_na = Entry(pop, textvariable=self.name_author).place(relx=0.45, rely=0.3, anchor=CENTER)
        label_ne = Label(pop, foreground="#7B5A08", background="#ffffc4", text="Editorial:",
                        font="HELVETICA 8 bold").place(relx=0.15, rely=0.4, anchor=CENTER)
        txt_ne = Entry(pop, textvariable=self.name_editorial).place(relx=0.45, rely=0.4, anchor=CENTER)
        btn_arrendar = Button(pop, text="Moviment", relief="flat", background="#7B5A08", cursor="hand1",
                                   foreground="white", command=lambda: self.openArrendar(i, disponible)).place(relx=0.7, rely=0.55, anchor=CENTER, width=90)
        btn_canviar = Button(pop, text="Canviar", relief="flat", background="#7B5A08", cursor="hand1",
                                  foreground="white", command=lambda: self.editar(i, self.name_book.get(), self.name_author.get(), self.name_editorial.get())).place(relx=0.4, rely=0.7, anchor=CENTER, width=90)
        btn_eliminar = Button(pop, text="Eliminar", relief="flat", background="#7B5A08", cursor="hand1",
                             foreground="white", command=lambda: self.eliminar(i)).place(relx=0.7, rely=0.7, anchor=CENTER, width=90)

    def openArrendar(self, id, disponible):
        self.id_autor = StringVar()

        pop_arrendar = Toplevel(self.main_frame, background="#ffffc4")
        pop_arrendar.geometry("300x200")
        label_id_llibre = Label(pop_arrendar, foreground="#7B5A08", background="#ffffc4", text="id_Llibre:",
                         font="HELVETICA 8 bold").place(relx=0.15, rely=0.2, anchor=CENTER)
        label_id = Label(pop_arrendar, foreground="#7B5A08", background="#ffffc4", text=id,
                         font="HELVETICA 8 bold").place(relx=0.3, rely=0.2, anchor=CENTER)


        #PER CONTROLAR QUE SI ESTA ARRENDAT NO EL PUGI LLOGAR.
        if disponible:
            label_id_autor = Label(pop_arrendar, foreground="#7B5A08", background="#ffffc4", text="id_Autor:",
                                   font="HELVETICA 8 bold").place(relx=0.15, rely=0.3, anchor=CENTER)
            txt_idu = Entry(pop_arrendar, textvariable=self.id_autor).place(relx=0.5, rely=0.3, anchor=CENTER)
            btn_insertar = Button(pop_arrendar, text="Guardar", relief="flat", background="#7B5A08", cursor="hand1",
                              foreground="white", command=lambda: self.GuardarLloguer(id, self.id_autor.get())).place(relx=0.7, rely=0.7,
                                                                                          anchor=CENTER, width=90)

        else:

            label_nom = Label(pop_arrendar, foreground="#7B5A08", background="#ffffc4", text=self.name_book.get(),
                             font="HELVETICA 8 bold").place(relx=0.5, rely=0.3, anchor=CENTER)
            btn_tornar = Button(pop_arrendar, text="Tornar", relief="flat", background="#7B5A08", cursor="hand1",
                                  foreground="white",
                                  command=lambda: self.tornar(id)).place(relx=0.7,
                                                                                                      rely=0.7,
                                                                                                      anchor=CENTER,
                                                                                                      width=90)


    def editar(self, id, name_book, name_author, name_editorial):
        ar = [name_book, name_author, name_editorial]
        ref1 = ""
        ref2 = ""

        d = bbdd_library.bbdd_biblioteca()
        d.UpdateBook(ar, id)
        messagebox.showinfo(title="Actualitzacio", message="S'ha actualitzat correctament!")
        self.NetejarLlista()
        self.DibuixarLlista(ref1, ref2)

    def eliminar(self, id):
        ref1 = ""
        ref2 = ""

        d = bbdd_library.bbdd_biblioteca()
        d.DeleteBook(id)
        messagebox.showinfo(title="Eliminat", message="S'ha actualitzat correctament!")
        self.NetejarLlista()
        self.DibuixarLlista(ref1, ref2)

    def GuardarLloguer(self, idb, idu):
        ref1 = ""
        ref2 = ""
        d = bbdd_library.bbdd_biblioteca()
        d.InsertLlogar(idu, idb)
        messagebox.showinfo(title="Actualitzacio", message="S'ha actualitzat correctament!")
        self.NetejarLlista()
        self.DibuixarLlista(ref1, ref2)

    def tornar(self, id):
        ref1 = ""
        ref2 = ""
        d = bbdd_library.bbdd_biblioteca()
        element = d.SelectIdArrendat(id)
        id_llogat = element[0][0]

        lloguer = d.UpdateArrendat(id_llogat)
        messagebox.showinfo(title="Actualitzacio", message="S'ha actualitzat correctament!")
        self.NetejarLlista()
        self.DibuixarLlista(ref1, ref2)

root = App()
root.title("LIBRARY")
root.geometry("1200x600")

root.mainloop()

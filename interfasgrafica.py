"""
-------------------------------
Compnentes de tkinter
-------------------------------
Tk- Es el conteneor de todos los elementos (widgets) que tendra interfaz 
    ademas es el que llamaremos Raiz o Root. su tamaño puede definirse o modificarse

Frame- El Frame o Marco es por si mismo un widget aunque no nos permita interactuar con el  programa
       el marco sera el contenedor de los widgets que utilicemos
 
Label- Es un widget  en el que podemos mostrar textos estaticos

Entry- Cuadro de texto para ingresar textos costro (Una sola linea)

Text- Este widget nos permite ingresar textos largos (multilinea)

Button- Es un boton en el texto

Radiobutton- Es un circuito el cual  podemos hacerle clic y seleccionar una opcion

Checkbutton- Es un cuadrado que nos permite  seleccionar opciones

Menu- Sonlos tipicos botones que vemos en la  ventanas en la parte superior que despliegan opciones

Diallogs- Ventanas emergentes que muestran informacion al usuario. Como lo pueden ser alertas 
          o ventanas para  elegir archivos, etc...
"""
#Importacion de la biblioteca tkinter
from cgitb import text
from itertools import tee
import tkinter as tk
import tkinter
from tkinter import*
from tkinter import ttk
from tkinter import messagebox
from tkinter import font
from uuid import getnode
import pymongo
import pymongo

"""Se creae la raiz o root de la interfaz
Importa de la libreria tkinter y la nombra tk, esto facilita lo  de estar 
importando cada clase
"""
class Usuario:
    """
    Esta clase es usada para determminar los atributos los cuales serviran para que el 
    usuario pueda determinar sus datos y poder incribirse de forma correcto en el seguro
    °Leon Dorado°
    -----------------
    Atributos:
    -----------------
    Prinombre : str
        Ingreso del primer nombre del usuario
    Segnombre : str
        Ingreso del segundo nombre del usuario
    Priapellido : str
        Ingreso del primer apellido del usuario
    Segapellido : str
        Ingreso del segundo apellido del usuario
    edad : int
        Edad del usuario
    cedula: str
        Cedula de identidad del usuario
    Usuario : str
        Usuario del cleinte para inicio de secion
    Contra : str
        Contraseña del cliente
    Provincia : str  
        Provincia del usuario
    -----------------
    Metodo:
    -----------------
    def __init__(self,Prinombre,Segnombre,Priapellido,Segapellido,edad,cedula,Usuario,Contra,provincia):
        Metodo constructor de la clase Usuario esta almacenara los datos del usuario o cliente
    """
    def __init__(self,Prinombre,Segnombre,Priapellido,Segapellido,edad,cedula,Usuario,Contra,provincia):
        """
        Metodo constructor de la clase Usuario esta almacenara los datos del usuario o cliente
        -----------------
        Atributos:    
        -----------------
        Prinombre : str
            Ingreso del primer nombre del usuario
        Segnombre : str
            Ingreso del segundo nombre del usuario
        Priapellido : str
            Ingreso del primer apellido del usuario
        Segapellido : str
            Ingreso del segundo apellido del usuario
        edad : int
            Edad del usuario
        cedula: str
            Cedula de identidad del usuario
        Usuario : str
            Usuario del cleinte para inicio de secion
        Contra : str
            Contraseña del cliente 
        Provincia : str  
            Provincia del usuario
        """
        self.Prinombre=Prinombre
        self.Segnombre=Segnombre
        self.Priapellido=Priapellido
        self.Segapellido=Segapellido
        self.edad=edad
        self.cedula=cedula
        self.usuario=Usuario
        self.Contra=Contra
        self.provincia=provincia
        
    
def PrimerInterfas():
    """
    Creacion de la vetana o interfas la  cual alamacenara la informacion del 
    cliente, para esto se le asigna un nombre a la interfas, asi mismo medidas
    """
    Dorado = Tk()
    """Nombre de la vneta de la interfas """
    Dorado.title("Seguro Leon Dorado")
    """Medidasde la interfas o ventana"""
    Dorado.geometry("300x600")
    tabla=ttk.Treeview(Dorado, columns=4)
    tabla.grid(row=4, column=0, columnspan=4)
    tabla.heading("#0", text="ID")
    tabla.heading("#1", text="nombre")
    Dorado.mainloop()

def CrearBloques():
    """
    Funcion usada para registrar los datos del cliente en la plataforma 
    de la aseguradora
    """
    Dorado = Tk()
    """Medidasde la interfas o ventana"""
    Dorado.geometry("300x600")
    """Texto para podre guiar el cliente al momento de registrarse """
    labelPrincipal=Label(Dorado, text="Proceda a completar los campos del regsitro ")
    labelPrincipal.pack()
    
    """Entrada del primer nombre del cliente"""    
    Bloque1= Label(Dorado,text="Ingrese su primer nombres", bg="light blue")
    texto1 =  Entry(Dorado, bg="blue")
    Bloque1.pack(pady=5)
    texto1.pack(pady=7)    
    """Entrada del segundo nombre del cliente"""
    Bloque2= Label(Dorado,text="Ingrese su segundo nombre", bg="light blue")
    texto2 =  Entry(Dorado, bg="blue")
    Bloque2.pack(pady=5)
    texto2.pack(pady=7) 
    
    """Ingreso del primer apellido del cliente"""
    Bloque3= Label(Dorado,text="Ingrese su primer apellido", bg="light blue")
    texto3 =  Entry(Dorado, bg="blue")
    Bloque3.pack(pady=5)
    texto3.pack(pady=7)    
    
    """Ingreso del segundo apellido del cliente"""
    Bloque4= Label(Dorado,text="Ingrese su segundo apellido", bg="light blue")
    texto4 =  Entry(Dorado, bg="blue")
    Bloque4.pack(pady=5)
    texto4.pack(pady=7)   
    
    """Ingreso de la edad del cliente"""
    Bloque5= Label(Dorado,text="Ingrese su edad", bg="light blue")
    texto5 =  Entry(Dorado, bg="blue")
    Bloque5.pack(pady=5)
    texto5.pack(pady=7) 
    
    """Ingreso del numero de cedula o pasporte del cliente"""
    Bloque6= Label(Dorado,text="Ingrese su numero de cedula o pasaporte", bg="light blue")
    texto6 =  Entry(Dorado, bg="blue")
    Bloque6.pack(pady=5)
    texto6.pack(pady=7)    
    
    """Ingreso del usuario del cliente para el inicio de secion """
    Bloque8 = Label  (Dorado,text="Ingrese un usuario ",bg="light blue")
    texto8 = Entry(Dorado,bg="blue")
    Bloque8.pack(pady=5)
    texto8.pack(pady=7)
    
    """Ingres su contraseña para el inicio de secion"""
    Bloque9 = Label(Dorado,text="Ingrese un contraseña",bg="light blue")
    texto9 = Entry(Dorado,bg="blue")
    Bloque9.pack(pady=5)
    texto9.pack(pady=7)
        
    """Ingreso de la provincia en la que reside el cliente"""
    Bloque7 = Label(Dorado,text="Ingres la provincia en la que recide actualmente",bg = "light blue")
    texto7 = Entry(Dorado,bg="blue") 
    Bloque7.pack(pady=5)
    texto7.pack(pady=7)
    
    quit = Button(Dorado, text="QUIT", fg="red",command=Dorado.bloque.destroy)
    quit.pack(side="bottom")
        
    def Datosenget():
        """
        Funacion usada para obtener las cadenas de los datos ingresados por el cliente
        Se crea un diccionario con los datos ingresados
        """     
        DatosCliente={"Primer nonmbre": texto1.get(),"Segundo nombre": texto2.get(),"Primer apellido": texto3.get(),"Segundo apellido":texto4.get(),"Edad":texto5.get(),"Numero de cedula registrado":texto6.get()
                      ,"Usuario del cliente":texto8.get(),"Contraseña del cliente": texto9.get(),"Provencia ":texto7.get()}
        """Se le agrega nuevos datos al diccionario"""
        Registrarse=coleccion.insert_one(DatosCliente)
    """Boton asignado a que registre los datos en la base de datos o MongoDB"""
    registro = Button(Dorado, text="Registrarse ", command=Datosenget)
    registro.pack()
    """bucle o funcion  del repite el codigo las veces requeridas"""
    Dorado.mainloop()

def InicioSecion():
    """Inicio de secion del cliente en la cual se valida si el posee un usuario o contraseña"""
    segundo = Tk()
    segundo.title("Inicio de secion")    
    """Medidas de la interfaz o ventana"""
    segundo.geometry("500x500")
    segundo.resizable(width="False", height="False")
    entradaUsuario=Entry(segundo, font=font.Font(family="Arial", size = "10"),textvar="", width=32, relief="flat")
    entradaUsuario.place(x=150, y=292)
    entradaContra=Entry(segundo, font=font.Font(family="Arial", size = "10"),textvar="", width=32, relief="flat")
    entradaContra.place(x=150, y=292)
    mostrarUsuario=Label(segundo, text = "Ingrese su usuario")
    mostrarUsuario.config(bg= "white", font=font.Font(family="Arial", size = "10"))
    mostrarUsuario.place(x=190, y=253)
    mostrarContra=Label(segundo, text = "Ingrese su contraseña")
    mostrarContra.config(bg= "white", font=font.Font(family="Arial", size = "10"))
    mostrarContra.place(x=190, y=253)
    validarInfo=Button(segundo, text= "heart", cursor="hand2", bg= "#0a509f",fg= "white",  width=2, height=1, relief="flat", command = lambda: validarUsua(entradaUsuario.get()) ) 
    validarInfo.place(x=433, y=290)
    ValidarContra=Button(segundo, text= "heart", cursor="hand2", bg= "#0a509f",fg= "white",  width=2, height=1, relief="flat", command = lambda: validarContra(mostrarContra.get()) ) 
    ValidarContra.place(x=433, y=290)
    segundo.mainloop()

def SegundaInterfas():
    """Se crea la nueva interfas o ventana"""
    SegInterfas = Toplevel()
    SegInterfas.title("Cuenta de seguros")
    """Medidas de la interfaz o ventana"""
    SegInterfas.geometry("500x500") 
    Datos=tk.Label(SegInterfas, text = "Datos del Usuario")
    Datos.config(bg= "white", fg="#4779b2",font=("Arial", 11, "bold"))
    Datos.place(x=1, y=100)
    Usuario.usuario="2300284342"
    query={"cedula": Usuario.usuario}
    find1 = coleccion.find
    specificFind = coleccion.find(query)
    Usuario.Contra="2300284342"
    query={"cedula": Usuario.Contra}
    find2 = coleccion.find
    specificFind = coleccion.find(query)
    for find in specificFind:
        """Nombres del cliente"""
        Nombre=Label(SegInterfas, text = "Nombres: ")
        Nombre.config(bg= "white",font=("Arial", 12, "bold"))
        Nombre.place(x=1, y=120)  
              
        Datonombres=tk.Label(SegInterfas, text = (find["nombre"], find["nombre2"]))
        Datonombres.config(bg= "white",font=("Arial", 12))
        Datonombres.place(x=70, y=120)
        
        """Apellidos del cliente"""
        apellido=tk.Label(SegInterfas, text = "Apellidos: ")
        apellido.config(bg= "white",font=("Arial", 12, "bold"))
        apellido.place(x=1, y=140)   
             
        Datoapellidos=tk.Label(SegInterfas, text = (find["apellido"], find["apellido2"]))
        Datoapellidos.config(bg= "white",font=("Arial", 12))
        Datoapellidos.place(x=70, y=140)
        
        """Provincia en la que se registro el cliente"""
        provinciaLabel=tk.Label(SegInterfas, text = "Provincia & Ciudad: ")
        provinciaLabel.config(bg= "white", font=("Arial", 12, "bold"))
        provinciaLabel.place(x=1, y=160)  
              
        provincia=tk.Label(SegInterfas, text = (find["provincia"]))
        provincia.config(bg= "white", font=("Arial", 12))
        provincia.place(x=132, y=160)
        
        """Edad ingresada por el cliente"""
        edadlabel=tk.Label(SegInterfas, text = "Edad: ")
        edadlabel.config(bg= "white", font=("Arial", 12, "bold"))
        edadlabel.place(x=300, y=140)   
             
        edad=tk.Label(SegInterfas, text = (find["edad"]))
        edad.config(bg= "white", font=("Arial", 12))
        edad.place(x=340, y=140)
        
        
    
    
    SegInterfas.mainloop()
       
def queryCedulas():
    coleccionTotal=coleccion.find()
    coleccion=[]
    for i in coleccionTotal:
        coleccion.append(i['cedula'])
    return coleccion

def validarUsua(usuario):
    UsuariosTotal=queryCedulas()
    if usuario in UsuariosTotal:
        usuario.usuario=usuario
        SegundaInterfas()
    else:
        messagebox.showwarning("Datos mal ingresados vuelva a intentar")    

def validarContra(Contra):
    ContraTotal=queryCedulas()
    if Contra in ContraTotal:
        Contra.usuario=Contra
        SegundaInterfas()
    else:
        messagebox.showwarning("Datos mal ingresados vuelva a intentar")    

if __name__ =="__main__":
    
    RegistroClientesNuevos =  pymongo.MongoClient("mongodb://localhost:27017/")
    MONGO_BASED="BaseClientes"
    COLECCION = "ClienteNuevos"
    baseDatos=RegistroClientesNuevos[MONGO_BASED]
    coleccion = baseDatos [COLECCION]
    
    """Ingreso de los datos en mongo"""
    clientes=Usuario("","","", "", "", "", "", "")
    clientes.InicioSecion()

 
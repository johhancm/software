import tkinter as tk

ventana = tk.Tk()
#ventana.title("Tienda X ()")
ventana.geometry("700x500")
ventana.configure(bg = "white")



#variables

cliente = tk.StringVar()
ruc = tk.StringVar()
producto1 = tk.StringVar()
producto2 = tk.StringVar()
producto3 = tk.StringVar()
producto4 = tk.StringVar()
producto5 = tk.StringVar()
producto6 = tk.StringVar()

cantidad1 = tk.StringVar()
cantidad2 = tk.StringVar()
cantidad3 = tk.StringVar()
cantidad4 = tk.StringVar()
cantidad5 = tk.StringVar()
cantidad6 = tk.StringVar()

precio1 = tk.StringVar()
precio2 = tk.StringVar()
precio3 = tk.StringVar()
precio4 = tk.StringVar()
precio5 = tk.StringVar()
precio6 = tk.StringVar()

resultado1 = tk.StringVar()
resultado2 = tk.StringVar()
resultado3 = tk.StringVar()
resultado4 = tk.StringVar()
resultado5 = tk.StringVar()
resultado6 = tk.StringVar()
resultadoT = tk.StringVar()
resultadoTIVA = tk.StringVar()
iva = tk.StringVar()
lista = [producto1,producto2,producto3,producto4,producto5,producto6,precio1,precio2,precio3,precio4,precio5,precio6,cantidad1,cantidad2,cantidad3,cantidad4,cantidad5,cantidad6]
compro = False

#funciones

def digit ():
    global compro
    for i in lista:
        if i.get().isdigit() == True:
            compro = True
def calcular():
    digit ()
    print(compro)
    if compro == True:
        
        resultado1.set(float(cantidad1.get())*float(precio1.get()))
        resultado2.set(float(cantidad2.get())*float(precio2.get()))
        resultado3.set(float(cantidad3.get())*float(precio3.get()))
        resultado4.set(float(cantidad4.get())*float(precio4.get()))
        resultado5.set(float(cantidad5.get())*float(precio5.get()))
        resultado6.set(float(cantidad6.get())*float(precio6.get()))
        resultadoT.set("Subtotal: "+ str(float(resultado1.get())+float(resultado2.get())+float(resultado3.get())+float(resultado4.get())+float(resultado5.get())+float(resultado6.get())))
        iva.set("Iva: " + str(0.12*(float(resultado1.get())+float(resultado2.get())+float(resultado3.get())+float(resultado4.get())+float(resultado5.get())+float(resultado6.get()))))
        resultadoTIVA.set("Total: " + str(1.12*(float(resultado1.get())+float(resultado2.get())+float(resultado3.get())+float(resultado4.get())+float(resultado5.get())+float(resultado6.get()))))

def limpiar():
    cliente.set("")
    ruc.set("")
    producto1.set("")
    producto2.set("")
    producto3.set("")
    producto4.set("")
    producto5.set("")
    producto6.set("")

    cantidad1.set("")
    cantidad2.set("")
    cantidad3.set("")
    cantidad4.set("")
    cantidad5.set("")
    cantidad6.set("")

    precio1.set("")
    precio2.set("")
    precio3.set("")
    precio4.set("")
    precio5.set("")
    precio6.set("")

    resultado1.set("")
    resultado2.set("")
    resultado3.set("")
    resultado4.set("")
    resultado5.set("")
    resultado6.set("")
    resultadoT.set("")
    resultadoTIVA .set("")
    iva.set("")

tk.Label(text="FACTURA", bg= "white").place(x=275,y=10)

tk.Label(text="Cliente: ", bg= "white").place(x=10,y=40)
tk.Label(text="RUC: ", bg= "white").place(x=10,y=70)



tk.Entry(textvariable = cliente,bd=1,width=45,justify="left").place(x=100,y=40)
tk.Entry(textvariable = ruc,bd=1,width=45,justify="left").place(x=100,y=70)

tk.Button(text="limpiar",width=10,height=1, bg= "Orange", command= limpiar).place(x=570,y=40)
tk.Button(text="calcular",width=10,height=1,bg= "Orange", command= calcular).place(x=570,y=70)

tk.Label(text="PRODUCTO ", bg= "white").place(x=100,y=100)
tk.Label(text="CANTIDAD ", bg= "white").place(x=220,y=100)
tk.Label(text="PRECIO U. ", bg= "white").place(x=320,y=100)
tk.Label(text="PRECIO T.", bg= "white").place(x=420,y=100)

#tk.Label(text="Jefes:  ", bg= "white").place(x=10,y=460)


tk.Entry(textvariable = producto1,bd=1,width=12,justify="left").place(x=90,y=130)


tk.Entry(textvariable = producto2,bd=1,width=12,justify="left").place(x=90,y=160)


tk.Entry(textvariable = producto3,bd=1,width=12,justify="left").place(x=90,y=190)


tk.Entry(textvariable = producto4,bd=1,width=12,justify="left").place(x=90,y=220)


tk.Entry(textvariable = producto5,bd=1,width=12,justify="left").place(x=90,y=250)


tk.Entry(textvariable = producto6,bd=1,width=12,justify="left").place(x=90,y=280)



tk.Entry(textvariable = cantidad1,bd=1,width=5,justify="left").place(x=230,y=130)


tk.Entry(textvariable = cantidad2,bd=1,width=5,justify="left").place(x=230,y=160)


tk.Entry(textvariable = cantidad3,bd=1,width=5,justify="left").place(x=230,y=190)


tk.Entry(textvariable = cantidad4,bd=1,width=5,justify="left").place(x=230,y=220)


tk.Entry(textvariable = cantidad5,bd=1,width=5,justify="left").place(x=230,y=250)


tk.Entry(textvariable = cantidad6,bd=1,width=5,justify="left").place(x=230,y=280)



tk.Entry(textvariable = precio1,bd=1,width=8,justify="left").place(x=315,y=130)


tk.Entry(textvariable = precio2,bd=1,width=8,justify="left").place(x=315,y=160)


tk.Entry(textvariable = precio3,bd=1,width=8,justify="left").place(x=315,y=190)


tk.Entry(textvariable = precio4,bd=1,width=8,justify="left").place(x=315,y=220)


tk.Entry(textvariable = precio5,bd=1,width=8,justify="left").place(x=315,y=250)


tk.Entry(textvariable = precio6,bd=1,width=8,justify="left").place(x=315,y=280)



tk.Label(textvariable = resultado1, bg="white", bd=1,width=8,justify="left").place(x=420,y=130)


tk.Label(textvariable = resultado2, bg="white", bd=1,width=8,justify="left").place(x=420,y=160)


tk.Label(textvariable = resultado3, bg="white", bd=1,width=8,justify="left").place(x=420,y=190)


tk.Label(textvariable = resultado4, bg="white", bd=1,width=8,justify="left").place(x=420,y=220)


tk.Label(textvariable = resultado5, bg="white", bd=1,width=8,justify="left").place(x=420,y=250)


tk.Label(textvariable = resultado6, bg="white", bd=1,width=8,justify="left").place(x=420,y=280)

tk.Label(textvariable = resultadoT,justify="left").place(x=370,y=350)
tk.Label(textvariable = iva,justify="left").place(x=370,y=380)
tk.Label(textvariable = resultadoTIVA ,justify="left").place(x=480,y=10)

ventana.mainloop()

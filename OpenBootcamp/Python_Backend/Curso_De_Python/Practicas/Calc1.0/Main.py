from Modules.User_Interface import Interfaz
import tkinter

def main():
    ventana_principal = tkinter.Tk()
    Interfaz(ventana_principal)
    ventana_principal.mainloop()

if __name__ == "__main__":
    main()

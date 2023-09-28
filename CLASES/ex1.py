'''
Braian Catriel Gatto
--------
Ejercicio 01
Nos encargan el desarrollo de una aplicación que le permita a sus usuarios operar
en la bolsa de valores:
A) Para ello se cargarán los siguientes datos hasta que el usuario lo decida:
* Nombre
* Monto en pesos de la operación (no menor a $10000)
* Cantidad de instrumentos
* Tipo (CEDEAR, BONOS, MEP)
B) Luego del ingreso mostrar en pantalla todos los datos.
C) Realizar los siguientes informes:
1. Tipo de instrumento que más se operó.
2. Cantidad de usuarios que compraron entre 150 y 200 BONOS y que invirtieron
más de $50000.
3. Nombre y cantidad de instrumentos del usuario que compró BONOS o MEP,
que menos dinero invirtió. Puede ser más de uno.
4. Nombre de los usuarios que invirtieron en CEDEAR, cuya inversión supere el
monto promedio
5. Porcentaje de usuarios que no invirtieron en MEP, siempre y cuando el monto
no supere los $50000.
'''
import tkinter
from tkinter.messagebox import showinfo as alert
from tkinter.messagebox import askyesno as question
from tkinter.simpledialog import askstring as prompt
import customtkinter


class App(customtkinter.CTk):

    def __init__(self):
        super().__init__()

        # configure window
        self.title("UTN Fra")

        self.btn_cargar = customtkinter.CTkButton(master=self, text="Cargar datos", command=self.btn_cargar)
        self.btn_cargar.grid(row=2, pady=10, columnspan=2, sticky="nsew")

        self.btn_mostrar = customtkinter.CTkButton(master=self, text="Mostrar datos", command=self.btn_mostrar)
        self.btn_mostrar.grid(row=3, pady=10, columnspan=2, sticky="nsew")

        self.name_list = ["a", "b", "c", "d", "e"]
        self.mount_list = [10000, 20000, 10000, 15000, 25000]
        self.instruments_list = [1, 5, 2, 1, 5]
        self.instrument_type_list = ["CEDEAR", "CEDEAR", "BONOS", "MEP", "CEDEAR"]

        self.total_spent_list = []

    def btn_cargar(self):
        while True:
            name = prompt(title="", prompt="Ingrese el nombre: ")
            while name == "" or name == False or name.isdigit() == True:
                alert(title="", message="Datos inválidos.")
                name = prompt(title="", prompt="Ingrese el nombre: ")
            self.name_list.append(name)

            mount = prompt(title="", prompt="Ingrese un monto (no menor a $10000)")
            while mount == "" or mount == False or mount.isdigit() == False or int(mount) < 10000:
                alert(title="", message="Datos inválidos.")
                mount = prompt(title="", prompt="Ingrese un monto (no menor a $10000)")
            mount_int = int(mount)
            self.mount_list.append(mount_int)
            
            instruments = prompt(title="", prompt="Ingrese la cantidad de instrumentos: ")
            while instruments == "" or instruments == False or instruments.isdigit() == False:
                alert(title="", message="Datos inválidos.")
                instruments = prompt(title="", prompt="Ingrese la cantidad de instrumentos: ")
            instruments_int = int(instruments)
            self.instruments_list.append(instruments_int)
            
            instrument_type = prompt(title="", prompt="Ingrese el tipo de instrumento (CEDEAR, BONOS, MEP) :")
            while instrument_type not in ["CEDEAR", "BONOS", "MEP"]:
                alert(title="", message="Datos inválidos.")
                instrument_type = prompt(title="", prompt="Ingrese el tipo de instrumento (CEDEAR, BONOS, MEP) :")
            self.instrument_type_list.append(instrument_type)

            cancel = input("¿CONTINUAR? si/no ").lower()

            if cancel != "si":
                print(self.name_list, self.mount_list, self.instruments_list, self.instrument_type_list)
                break

    def btn_mostrar(self):
        quantity = len(self.name_list)

        cedear_count = 0
        bonos_count = 0
        mep_count = 0

        user_quantity_150_250_mount_and_more_5000_money = 0

        for i in quantity:
            match self.instrument_type_list[i]:
                case "CEDEAR":
                    cedear_count += 1
                case "BONOS":
                    bonos_count += 1
                case "MEP":
                    mep_count += 1

            total_spent_mount = self.instruments_list[i] * self.mount_list[i]
            self.total_spent_list.append(total_spent_mount)
            
            if self.instruments_list[i] > 150 and self.instruments_list[i] < 200 and self.total_spent_list[i] > 50000:
                user_quantity_150_250_mount_and_more_5000_money += 1

        if cedear_count > bonos_count and cedear_count > mep_count:
            most_chosen_type = "El más elegido es CEDEAR"
        elif bonos_count > mep_count:
            most_chosen_type = "El más elegido es BONOS"
        else:
            most_chosen_type = "El más elegido es MEP"

        info = f"{most_chosen_type}, {user_quantity_150_250_mount_and_more_5000_money}"
        
        alert(title="", message= info)

            

if __name__ == "__main__":
    app = App()
    app.geometry("300x300")
    app.mainloop()

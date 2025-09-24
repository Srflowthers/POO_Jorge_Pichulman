import os, time, datetime

# -------------------- MODELOS --------------------
class Mascota:
    def __init__(self, nombre, fecha_nacimiento=None, hambre=50, sueno=30, suciedad=30, felicidad=50):
        self.nombre = nombre
        self.fecha_nacimiento = fecha_nacimiento if fecha_nacimiento else datetime.datetime.now().strftime("%d/%m/%y")
        self.estado_hambre = hambre
        self.estado_sueno = sueno
        self.estado_suciedad = suciedad
        self.estado_felicidad = felicidad

    def get_fecha(self):
        return f"Fecha de nacimiento de {self.nombre}: {self.fecha_nacimiento}"

    def alimentar(self):
        if self.estado_hambre >= 100:
            print(f"{self.nombre} ya esta lleno xd")
        else:
            self.estado_hambre += 20
            self.estado_felicidad += 5
            if self.estado_hambre > 100:
                self.estado_hambre = 100
            print(f"Has alimentado a {self.nombre}. Hambre ahora: {self.estado_hambre}/100")

    def estado(self):
        print(f"""
        --- Estado de {self.nombre} ---
        Hambre: {self.estado_hambre}/100
        Sueno: {self.estado_sueno}/100
        Suciedad: {self.estado_suciedad}/100
        Felicidad: {self.estado_felicidad}/100
        """)

    def accion(self):
        return "Hace algo..."

class Ave(Mascota):
    def __init__(self, nombre, fecha_nacimiento=None):
        super().__init__(nombre, fecha_nacimiento)
        self.estado_felicidad = 100
        self.estado_sueno = 100
    def accion(self): return f"{self.nombre} esta volando xd"

class Reptil(Mascota):
    def accion(self): return f"{self.nombre} se arrastra lentamente"

class Pez(Mascota):
    def accion(self): return f"{self.nombre} nada felizmente"

class Anfibio(Mascota):
    def accion(self): return f"{self.nombre} nada y salta"

class Mamifero(Mascota):
    def accion(self): return f"{self.nombre} corre rapido"

# -------------------- CONTROLADOR --------------------
RUTA_TXT = "tamagochi.txt"

def limpiar_consola():
    os.system("cls" if os.name == "nt" else "clear")

def guardar_mascota(mascota):
    with open(RUTA_TXT, "w") as f:
        f.write(f"{mascota.nombre},{mascota.fecha_nacimiento},{mascota.estado_hambre},{mascota.estado_sueno},{mascota.estado_suciedad},{mascota.estado_felicidad}")
    print("Mascota guardada xd")

def cargar_mascota():
    if not os.path.exists(RUTA_TXT): return None
    with open(RUTA_TXT, "r") as f:
        data = f.read().strip().split(",")
        if len(data) == 6:
            nombre, fecha, hambre, sueno, suciedad, felicidad = data
            return Mascota(nombre, fecha, int(hambre), int(sueno), int(suciedad), int(felicidad))
    return None

def crear_mascota():
    limpiar_consola()
    print("""
    === TIPOS DE MASCOTA ===
    1. Ave
    2. Reptil
    3. Pez
    4. Anfibio
    5. Mamifero
    """)
    tipo = input("Elige el tipo de mascota: ")
    nombre = input("Ingresa el nombre de tu mascota: ")
    if not tipo.isdigit() or not (1 <= int(tipo) <= 5):
        print("Error: opcion debe ser numero entre 1 y 5 xd")
        return None
    if not nombre.isalpha():
        print("Error: el nombre solo puede tener letras")
        return None
    tipo = int(tipo)
    if tipo == 1: mascota = Ave(nombre)
    elif tipo == 2: mascota = Reptil(nombre)
    elif tipo == 3: mascota = Pez(nombre)
    elif tipo == 4: mascota = Anfibio(nombre)
    else: mascota = Mamifero(nombre)
    guardar_mascota(mascota)
    return mascota

def degradar_estado(mascota):
    mascota.estado_hambre -= 5
    mascota.estado_sueno -= 5
    if mascota.estado_hambre < 0: mascota.estado_hambre = 0
    if mascota.estado_sueno < 0: mascota.estado_sueno = 0
    guardar_mascota(mascota)

# -------------------- VISTA --------------------
def menu_mascota(mascota):
    tiempo_ultimo = time.time()
    while True:
        print("""
        === MENU DE MASCOTA ===
        1. Ver estado
        2. Alimentar
        3. Ver fecha de nacimiento
        4. Accion especial
        5. Salir
        """)
        opcion = input("Elige una opcion: ")
        if opcion == "1":
            mascota.estado()
        elif opcion == "2":
            mascota.alimentar()
        elif opcion == "3":
            print(mascota.get_fecha())
        elif opcion == "4":
            print(mascota.accion())
        elif opcion == "5":
            guardar_mascota(mascota)
            print("Juego guardado y saliendo xd")
            break
        else:
            print("Opcion no valida")
        if time.time() - tiempo_ultimo >= 20:
            degradar_estado(mascota)
            tiempo_ultimo = time.time()

# -------------------- MAIN --------------------
def main():
    mascota = cargar_mascota()
    if mascota: print(f"Se cargo la mascota {mascota.nombre} xd")
    else: mascota = crear_mascota()
    if mascota: menu_mascota(mascota)
    else: print("No se pudo crear mascota")

if __name__ == "__main__":
    main()

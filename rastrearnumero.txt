import time
import webbrowser
import os  # Para ejecutar el archivo menu.py

def rastrear_numero():
    while True:
        print(""" 
============================================ 
          📍 MÓDULO 1: RASTREAR NÚMERO 📍 
============================================ 
1️⃣  Generar link de rastreo (YouTube/Grabify/IPLogger) 
2️⃣  Usar Seeker para ubicación en tiempo real 
3️⃣  Consultar bases de datos (Truecaller/GEOfinder) 
0️⃣  Volver 
99️⃣ Ejecutar menu.py (Volver al menú principal) 
============================================ 
""")
        opcion = input("Selecciona una opción: ")
        
        if opcion == "1":
            generar_link_rastreo()
        elif opcion == "2":
            usar_seeker()
        elif opcion == "3":
            consultar_bases_datos()
        elif opcion == "0":
            return
        elif opcion == "99":
            ejecutar_menu_principal()
        else:
            print("❌ Opción no válida. Inténtalo de nuevo.")
            time.sleep(2)

def generar_link_rastreo():
    print("""
============================================
      🔗 Generar Link de Rastreo
============================================
1️⃣  Usar Grabify
2️⃣  Usar IPLogger
3️⃣  Usar RastrearNúmero.com
0️⃣  Volver
99️⃣ Ejecutar menu.py (Volver al menú principal)
============================================
""")
    opcion = input("Selecciona una opción: ")
    
    if opcion == "1":
        webbrowser.open("https://grabify.link/")
    elif opcion == "2":
        webbrowser.open("https://iplogger.org/")
    elif opcion == "3":
        webbrowser.open("https://rastrearnumero.com/herramientas/link/crearlink.php")
    elif opcion == "0":
        return
    elif opcion == "99":
        ejecutar_menu_principal()
    else:
        print("❌ Opción no válida.")
    input("Presiona Enter para volver...")
    rastrear_numero()

def usar_seeker():
    print("""
============================================
      📡 Usar Seeker para Ubicación
============================================
Pasos:
1️⃣  Instalar Seeker con:
      git clone https://github.com/thewhiteh4t/seeker.git
2️⃣  Ingresar en la carpeta:
      cd seeker
3️⃣  Ejecutar Seeker:
      python3 seeker.py
============================================
99️⃣ Ejecutar menu.py (Volver al menú principal)
""")
    opcion = input("Selecciona una opción: ")
    
    if opcion == "99":
        ejecutar_menu_principal()
    input("Presiona Enter para volver...")
    rastrear_numero()

def consultar_bases_datos():
    print("""
============================================
      🔍 Consultar Bases de Datos
============================================
1️⃣  Usar Truecaller
2️⃣  Usar GEOfinder
0️⃣  Volver
99️⃣ Ejecutar menu.py (Volver al menú principal)
============================================
""")
    opcion = input("Selecciona una opción: ")
    
    if opcion == "1":
        webbrowser.open("https://www.truecaller.com/")
    elif opcion == "2":
        webbrowser.open("https://geofinder.mobi/")
    elif opcion == "0":
        return rastrear_numero()
    elif opcion == "99":
        ejecutar_menu_principal()
    else:
        print("❌ Opción no válida.")
    input("Presiona Enter para volver...")
    rastrear_numero()

def ejecutar_menu_principal():
    # Ejecuta el archivo menu.py
    os.system("python menu.py")

if __name__ == "__main__":
    rastrear_numero()

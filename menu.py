import os
import time

def menu():
    while True:
        os.system("cls" if os.name == "nt" else "clear")
        print("====================================")
        print("            MENÚ PRINCIPAL          ")
        print("====================================")
        print("1️⃣  Rastrear Número")
        print("2️⃣  Obtener Cuenta")
        print("3️⃣  OSINT")
        print("4️⃣  Hacking")
        print("5️⃣  SPY (Monitoreo)")
        print("6️⃣  Recuperación de Datos (Forense)")
        print("7️⃣  Metadatos")
        print("8️⃣  WiFi Hack")
        print("9️⃣  Historial (Sábana de Llamadas)")
        print("🔟  Tutoriales")
        print("0️⃣  Salir")
        print("====================================")

        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            print("\nHas seleccionado 'Rastrear Número'.")
            os.system("python rastrearnumero.py")  # Ejecuta el script cuando se elige la opción 1
        elif opcion == "2":
            print("\nHas seleccionado 'Obtener Cuenta'.")
        elif opcion == "3":
            print("\nHas seleccionado 'OSINT'.")
        elif opcion == "4":
            print("\nHas seleccionado 'Hacking'.")
        elif opcion == "5":
            print("\nHas seleccionado 'SPY (Monitoreo)'.")
        elif opcion == "6":
            print("\nHas seleccionado 'Recuperación de Datos (Forense)'.")
        elif opcion == "7":
            print("\nHas seleccionado 'Metadatos'.")
        elif opcion == "8":
            print("\nHas seleccionado 'WiFi Hack'.")
        elif opcion == "9":
            print("\nHas seleccionado 'Historial (Sábana de Llamadas)'.")
        elif opcion == "10":
            print("\nHas seleccionado 'Tutoriales'.")
        elif opcion == "0":
            print("\nGracias por usar el menú. Saliendo...")
            time.sleep(2)
            break
        else:
            print("\n❌ Opción no válida. Inténtalo de nuevo.")

        input("\nPresiona Enter para continuar...")

if __name__ == "__main__":
    menu()

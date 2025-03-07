import os

def mostrar_presentacion():
    print("""
====================================
 ███████╗██╗  ██╗ █████╗ ███╗   ██╗
 ██╔════╝██║  ██║██╔══██╗████╗  ██║
 ███████╗███████║███████║██╔██╗ ██║
 ╚════██║██╔══██║██╔══██║██║╚██╗██║
 ███████║██║  ██║██║  ██║██║ ╚████║
 ╚══════╝╚═╝  ╚═╝╚═╝  ╚═╝╚═╝  ╚═══╝
====================================
       Bienvenido a SHANEKE
====================================
""")

def pedir_contraseña():
    while True:
        contraseña = input("Ingresa la contraseña para continuar: ")
        if contraseña == "sh2025":
            print("Acceso concedido.")
            break
        else:
            print("Contraseña incorrecta. Intenta de nuevo.")

def confirmar_continuar():
    while True:
        respuesta = input("¿Deseas continuar? (S/N): ").strip().lower()
        if respuesta in ["s", "yes", "y"]:
            return True
        elif respuesta in ["n", "no"]:
            print("Operación cancelada.")
            return False
        else:
            print("Opción inválida. Responde con S o N.")

def ejecutar_menu():
    print("Cargando el menú...")
    os.system("menu.py")  # Ejecuta menu.py
    input("\nPresiona Enter para volver al inicio...")


if __name__ == "__main__":
    while True:
        mostrar_presentacion()
        pedir_contraseña()
        if confirmar_continuar():
            ejecutar_menu()

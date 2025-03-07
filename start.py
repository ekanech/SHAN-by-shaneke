import subprocess

# Usuario de GitHub proporcionado
usuario_github = "Shaneke (ekanech) | Logicm368 · she/her"

# Mostrar el usuario de GitHub
print(f"Mi usuario de GitHub es: {usuario_github}")

# Ejecutar el script presentacion.py
try:
    subprocess.run(["python", "presentacion.py"], check=True)
except subprocess.CalledProcessError as e:
    print(f"Error al ejecutar presentacion.py: {e}")
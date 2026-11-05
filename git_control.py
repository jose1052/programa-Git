import os
from git import Repo

# 1. Definir la ruta de tu repositorio local en el Escritorio
repo_path = os.path.expanduser("~/Desktop/programa-git")

try:
    # 2. Inicializar el acceso al repositorio
    repo = Repo(repo_path)
    print(f"Conectado con éxito al repositorio: {repo.working_tree_dir}")

    # 3. Hacer checkout del archivo a la versión específica que deseas (0d3ceeb)
    # Esto equivale a: git checkout 0d3ceeb -- klotin.txt
    repo.git.checkout("0d3ceeb", "--", "klotin.txt")
    print("✓ Archivo 'klotin.txt' restaurado a su versión original.")

    # 4. Hacer el 'git add' del archivo restaurado
    repo.index.add(["klotin.txt"])
    print("✓ Archivo agregado al área de preparación (Staging area).")

    # 5. Hacer el 'git commit'
    commit_message = "volver al principio desde script de Python"
    nuevo_commit = repo.index.commit(commit_message)
    print(f"✓ Commit creado con éxito: '{commit_message}' (ID: {nuevo_commit.hexsha[:7]})")

    # 6. Hacer el 'git push' a tu remoto asignado 'github' en la rama 'master'
    print("Subiendo cambios a GitHub, por favor espera...")
    origen_remoto = repo.remote(name="github")
    origen_remoto.push(refspec="master")
    print("🚀 ¡Todo listo! Los cambios se subieron correctamente a GitHub.")

except Exception as e:
    print(f"❌ Ocurrió un error durante la ejecución: {e}")


edad = int(input("ingrese su edad: "))
if edad < 17:
    print("No puedes votar")
elif edad >= 18 and edad <= 65:
    print("Puedes votar")
else:
    print("Puedes votar")
    
    
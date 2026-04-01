import os
import sys
import subprocess
import tkinter as tk    
from tkinter import filedialog
import openpyxl

# --- 1. CONFIGURACIÓN INICIAL ---
root = tk.Tk()
root.withdraw() 
directory = filedialog.askdirectory(title="Selecciona la carpeta raíz del Proyecto")

if not directory:
    exit()

project_name = os.path.basename(directory).lower().replace(" ", "-")


# --- 2. CREACIÓN DE ESTRUCTURA COMPLETA ---
main_folders = ['docs-tecnica', 'recursos-media', 'negocio-legal', 'development']
for folder in main_folders:
    os.makedirs(os.path.join(directory, folder), exist_ok=True)

dev_path = os.path.join(directory, 'development')
folders = ['privadas', 'publicas']

for sub in folders:
    path= os.path.join(dev_path, sub)
    os.makedirs(path, exist_ok=True)

dev_private = os.path.join(dev_path, 'privadas')
dev_public = os.path.join(dev_path, 'publicas')

privadas = ['backend-fastapi', 'mobile-react-native', 'unity-sim-csharp', 'hardware-vhdl', 'firmware-micros']
publicas = ['frontend-react'] 

for sub in (privadas):
    path = os.path.join(dev_private, sub)
    os.makedirs(path, exist_ok=True)
    
    # LÓGICA EXCLUSIVA PARA EL BACKEND (.env y .venv)
    if sub == 'backend-fastapi':
        # Archivo .env solo en backend
        with open(os.path.join(path, ".env"), "w") as f:
            f.write("# Configuración del Backend\nSECRET_KEY=tu_token_aqui\nDEBUG=True\n")
        
        # Entorno virtual solo en backend
        print(f"📦 Creando venv exclusivo en {sub}...")
        subprocess.run([sys.executable, "-m", "venv", os.path.join(path, ".venv")], check=True)

###Ceración e carpeta públicas
for sub in (publicas):
    path = os.path.join(dev_public, sub)
    os.makedirs(path, exist_ok=True)


# --- 3. ARCHIVOS DE APOYO ADICIONALES ---
with open(os.path.join(directory, 'README.md'), 'w', encoding='utf-8') as f:
    f.write(f"# {project_name.upper()}\nProyecto creado...")

wb = openpyxl.Workbook()
wb.save(os.path.join(directory, 'Master_Engineering_Schedule.xlsx'))

"""

# --- 4. FUNCIÓN DE GESTIÓN DE REPOS ---
def configurar_y_subir_repo(folder_path, repo_suffix, is_private):
    if not os.path.exists(folder_path): return
    os.chdir(folder_path)
    repo_name = f"{project_name}-{repo_suffix}"
    
    subprocess.run(["git", "init"], capture_output=True)
    with open(".gitignore", "w") as f:
        f.write("**/.venv/\n**/node_modules/\n**/__pycache__/\n.env\nbuild/\n*.xlsx\n")
    
    privacy = "--private" if is_private else "--public"
    try:
        subprocess.run(["gh", "repo", "create", repo_name, privacy, "--source=.", "--remote=origin"], check=True)
        
        subprocess.run(["git", "add", "."], capture_output=True)
        subprocess.run(["git", "commit", "-m", "Initial commit: Ecosistema con venv solo en backend"], capture_output=True)
        subprocess.run(["git", "branch", "-M", "main"], capture_output=True)
        subprocess.run(["git", "push", "-u", "origin", "main"], capture_output=True)
        
        print(f"✅ Repo '{repo_name}' configurado y subido.")
    except:
        print(f"⚠️ El repo '{repo_name}' ya existe o hubo un error.")

# A. REPO PRIVADO (Todo el proyecto)
configurar_y_subir_repo(directory, "core-private", True)

# B. REPO PÚBLICO (Solo Frontend)
frontend_path = os.path.join(dev_path, 'frontend-react')
configurar_y_subir_repo(frontend_path, "frontend-public", False)

print(f"\n🚀 PROYECTO LISTO: Entorno virtual y .env creados ÚNICAMENTE en 'backend-fastapi'.")
"""
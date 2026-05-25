import os

# CONFIGURACION SEGURA
MOD_PATH = os.path.abspath(os.path.join(os.getcwd(), "mod", "Conosur"))
DIRS_TO_PURIFY = [
    os.path.join(MOD_PATH, "history", "countries"),
    os.path.join(MOD_PATH, "common", "countries"),
    os.path.join(MOD_PATH, "history", "pops", "1836.1.1"),
    os.path.join(MOD_PATH, "history", "pops", "1861.4.14")
]

# LISTAS DE CONSERVACION (Whitelists)
KEEP_TAGS = ["CHL", "ARG", "URU", "PRG", "PAT", "GYA", "CUB", "USA", "CSU", "MAP", "DIA", "VNZ"]
KEEP_FILES_EXACT = [
    "Chile.txt", "Argentina.txt", "Uruguay.txt", "Paraguay.txt", 
    "Patagonia.txt", "Guayana.txt", "Cuba.txt", "USA.txt", "United States.txt",
    "Mapuche.txt", "Diaguita.txt", "Conosur.txt", "Venezuela.txt", "Madagascar.txt"
]

def is_safe_to_modify(target_path):
    """Garantiza que no escapemos del directorio del mod."""
    return MOD_PATH in os.path.abspath(target_path)

def should_keep(filename):
    """Verifica si el archivo coincide con nuestra whitelist."""
    if filename in KEEP_FILES_EXACT:
        return True
    for tag in KEEP_TAGS:
        if tag in filename:
            return True
    return False

def purify_directory(directory):
    if not os.path.exists(directory):
        print(f"[-] Directorio no encontrado, omitiendo: {directory}")
        return

    print(f"[*] Purificando: {directory}")
    for filename in os.listdir(directory):
        file_path = os.path.join(directory, filename)
        
        if not os.path.isfile(file_path):
            continue

        if not should_keep(filename):
            if is_safe_to_modify(file_path):
                try:
                    os.remove(file_path)
                    print(f"    [+] Removido: {filename}")
                except Exception as e:
                    print(f"    [!] Error removiendo {filename}: {e}")
            else:
                print(f"    [!] ALERTA DE SEGURIDAD: Intento de borrar fuera del mod -> {file_path}")

if __name__ == "__main__":
    print("Iniciando Purificación Segura de Conosur...")
    for d in DIRS_TO_PURIFY:
        purify_directory(d)
    print("Purificación completada.")

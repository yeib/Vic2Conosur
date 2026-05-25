import os
import shutil
import re

MOD_DIR = os.path.abspath(os.path.join(os.getcwd(), "mod", "Conosur"))
BASE_GAME_DIR = os.getcwd()

def copy_pop_file(filename):
    base_file = os.path.join(BASE_GAME_DIR, "history", "pops", "1836.1.1", filename)
    mod_file = os.path.join(MOD_DIR, "history", "pops", "1836.1.1", filename)
    if not os.path.exists(mod_file) and os.path.exists(base_file):
        os.makedirs(os.path.dirname(mod_file), exist_ok=True)
        shutil.copy2(base_file, mod_file)
    return mod_file

def inject_pop(file_path, prov_id, pop_text, check_string):
    if not os.path.exists(file_path): return
    with open(file_path, 'r', encoding='ISO-8859-1') as f:
        content = f.read()
    
    if check_string in content:
        print(f"[-] Saltando {os.path.basename(file_path)}, ya contiene los datos.")
        return

    pattern = rf"({prov_id}\s*=\s*{{)"
    if not re.search(pattern, content):
        content += f"\n{prov_id} = {{\n{pop_text}\n}}\n"
    else:
        content = re.sub(pattern, rf"\1\n{pop_text}\n", content, count=1)
    
    with open(file_path, 'w', encoding='ISO-8859-1') as f:
        f.write(content)
    print(f"[+] Inyectado en {os.path.basename(file_path)} (Provincia {prov_id})")

def main():
    files_needed = {
        "United Kingdom.txt": (300, "\tartisans = { culture = chilean religion = catholic size = 500 }", "size = 500", "chilean"),
        "France.txt": (425, "\tartisans = { culture = chilean religion = catholic size = 500 }", "size = 500", "chilean"),
        "Spain.txt": (487, "\tartisans = { culture = chilean religion = catholic size = 500 }", "size = 500", "chilean"),
        "United States.txt": (220, "\tartisans = { culture = chilean religion = catholic size = 500 }", "size = 500", "chilean"),
        "Peru.txt": (2295, "\tartisans = { culture = chilean religion = catholic size = 500 }", "size = 500", "chilean"),
        "Bolivia.txt": (2311, "\tartisans = { culture = chilean religion = catholic size = 500 }", "size = 500", "chilean"),
        "Egypt.txt": (1745, "\tfarmers = { culture = malagasy religion = animist size = 80000 }\n\tartisans = { culture = malagasy religion = animist size = 5000 }", "malagasy", "malagasy")
    }
    
    print("--- INICIANDO DIÁSPORA Y TRASLADO MALGACHE ---")
    for filename, (prov_id, pop_text, _, check_string) in files_needed.items():
        mod_file = copy_pop_file(filename)
        inject_pop(mod_file, prov_id, pop_text, check_string)
    print("--- COMPLETADO ---")

if __name__ == "__main__":
    main()

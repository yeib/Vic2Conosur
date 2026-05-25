import os
import re
import shutil

MOD_DIR = os.path.abspath(os.path.join(os.getcwd(), "mod", "Conosur"))
BASE_GAME_DIR = os.getcwd()

def set_treasury(file_path, amount):
    if not os.path.exists(file_path):
        print(f"[-] Archivo no encontrado para tesoro: {file_path}")
        return
    with open(file_path, 'r', encoding='ISO-8859-1') as f:
        content = f.read()

    # Reemplazar o añadir cash y treasury al principio
    content = re.sub(r"^cash\s*=\s*\d+", "", content, flags=re.MULTILINE)
    content = re.sub(r"^treasury\s*=\s*\d+", "", content, flags=re.MULTILINE)
    
    new_header = f"cash = {amount}\ntreasury = {amount}\n"
    content = new_header + content.lstrip()

    with open(file_path, 'w', encoding='ISO-8859-1') as f:
        f.write(content)
    print(f"[+] Tesoro configurado a {amount} en: {os.path.basename(file_path)}")

def configure_cuba():
    cuba_path = os.path.join(MOD_DIR, "history", "countries", "CUB - Cuba.txt")
    if not os.path.exists(cuba_path): return
    with open(cuba_path, 'r', encoding='ISO-8859-1') as f:
        content = f.read()
    
    content = re.sub(r"government\s*=\s*\w+", "government = absolute_monarchy", content)
    with open(cuba_path, 'w', encoding='ISO-8859-1') as f:
        f.write(content)
    print("[+] Cuba configurada como Monarquía Absoluta.")

def create_patagonia_file():
    pat_path = os.path.join(MOD_DIR, "history", "countries", "PAT - Patagonia.txt")
    content = """cash = 1000000
treasury = 1000000
capital = 2396
primary_culture = patagonian
religion = catholic
government = absolute_monarchy
plurality = 0.0
nationalvalue = nv_order
literacy = 0.1
non_state_culture_literacy = 0.05
civilized = yes

upper_house = {
	conservative = 100
}

ruling_party = PAT_conservative

1836.1.1 = {
	treasury = 1000000
}
"""
    with open(pat_path, 'w', encoding='ISO-8859-1') as f:
        f.write(content)
    print("[+] Creado archivo base para Patagonia.")

def register_countries():
    countries_file = os.path.join(MOD_DIR, "common", "countries.txt")
    if not os.path.exists(countries_file): return
    with open(countries_file, 'r', encoding='ISO-8859-1') as f:
        content = f.read()
    
    tags_to_add = [
        ('PAT', 'Patagonia.txt'),
        ('CSU', 'Conosur.txt'),
        ('MAP', 'Mapuche.txt'),
        ('DIA', 'Diaguita.txt'),
        ('GYA', 'Guayana.txt')
    ]
    
    for tag, filename in tags_to_add:
        if f"{tag}\t" not in content and f"{tag} " not in content:
            content += f"\n{tag}\t\t= \"countries/{filename}\""
            
    with open(countries_file, 'w', encoding='ISO-8859-1') as f:
        f.write(content)
    print("[+] Países personalizados registrados en countries.txt.")

def modify_province(prov_id, owner=None, rgo_size=None, rgo_output=None, trade_goods=None):
    # Buscar en el juego base
    base_prov_dir = os.path.join(BASE_GAME_DIR, "history", "provinces")
    prov_file_path = None
    relative_path = None
    
    for root, _, files in os.walk(base_prov_dir):
        for file in files:
            if file.startswith(f"{prov_id} -"):
                prov_file_path = os.path.join(root, file)
                relative_path = os.path.relpath(prov_file_path, BASE_GAME_DIR)
                break
        if prov_file_path: break

    if not prov_file_path:
        print(f"[-] Provincia {prov_id} no encontrada en el juego base.")
        return

    # Copiar al mod si no existe
    mod_prov_path = os.path.join(MOD_DIR, relative_path)
    os.makedirs(os.path.dirname(mod_prov_path), exist_ok=True)
    if not os.path.exists(mod_prov_path):
        shutil.copy2(prov_file_path, mod_prov_path)

    with open(mod_prov_path, 'r', encoding='ISO-8859-1') as f:
        content = f.read()

    modified = False
    if owner:
        content = re.sub(r"owner\s*=\s*\w+", f"owner = {owner}", content)
        content = re.sub(r"controller\s*=\s*\w+", f"controller = {owner}", content)
        if f"add_core = {owner}" not in content:
            content += f"\nadd_core = {owner}"
        modified = True
    
    if trade_goods:
        content = re.sub(r"trade_goods\s*=\s*\w+", f"trade_goods = {trade_goods}", content)
        modified = True

    if rgo_size:
        if "rgo_size" not in content:
            content += f"\nrgo_size = {rgo_size}"
        else:
            content = re.sub(r"rgo_size\s*=\s*[\d.]+", f"rgo_size = {rgo_size}", content)
        modified = True

    if rgo_output:
        if "rgo_output" not in content:
            content += f"\nrgo_output = {rgo_output}"
        else:
            content = re.sub(r"rgo_output\s*=\s*[\d.]+", f"rgo_output = {rgo_output}", content)
        modified = True

    if modified:
        with open(mod_prov_path, 'w', encoding='ISO-8859-1') as f:
            f.write(content)

def apply_super_rgos_and_sovereignty():
    print("[*] Aplicando Super RGOs y Soberanía...")
    # CHILE (Hierro, Azufre, Carbón, Metales Preciosos) - 8 / 3.0
    chile_provinces = {
        "2324": "iron", "2325": "sulphur", "2326": "coal", "2327": "precious_metals",
        "2328": "iron", "2329": "sulphur", "2330": "coal", "2331": "precious_metals", "2332": "iron"
    }
    for pid, good in chile_provinces.items():
        modify_province(pid, rgo_size=8, rgo_output=3.0, trade_goods=good)

    # PATAGONIA (Dueño PAT, Petróleo y Caucho) - 8 / 3.0
    patagonia_provinces = {
        "2333": "oil", "2334": "rubber", "2335": "oil", "2391": "rubber", 
        "2392": "oil", "2393": "rubber", "2394": "oil", "2395": "rubber", 
        "2396": "oil", "2397": "rubber", "2398": "oil", "2399": "rubber", "2400": "oil"
    }
    for pid, good in patagonia_provinces.items():
        modify_province(pid, owner="PAT", rgo_size=8, rgo_output=3.0, trade_goods=good)

    # CUBA (Dueño CUB Caribe) - 4.5
    caribbean_ids = [
        "2209", "2210", "2211", "2212", # Cuba
        "2213", "2215", # Haiti
        "2214", "2216", # Dominicana
        "2217", "2219", "2222", "203" # Jamaica, Bahamas, PR, Bermuda
    ]
    for pid in caribbean_ids:
        modify_province(pid, owner="CUB", rgo_size=4.5)

    # PARAGUAY (Algodón) - 8 / 3.0
    prg_ids = ["2339", "2340", "2341", "2342", "2343"]
    for pid in prg_ids:
        modify_province(pid, rgo_size=8, rgo_output=3.0, trade_goods="cotton")

    # URUGUAY (Seda y Tintes) - 8 / 3.0
    uru_provinces = {"2344": "silk", "2345": "dye", "2346": "silk", "2347": "dye"}
    for pid, good in uru_provinces.items():
        modify_province(pid, rgo_size=8, rgo_output=3.0, trade_goods=good)

    # USA NORTE (Recursos) - 8 / 3.0
    usa_ids = ["232", "223", "220", "163", "173", "243"] # NY, Philly, DC, Chicago, Detroit, Boston
    for pid in usa_ids:
         modify_province(pid, rgo_size=8, rgo_output=3.0)

if __name__ == "__main__":
    print("--- INICIANDO PLAN MAESTRO: ECONOMÍA Y SOBERANÍA ---")
    set_treasury(os.path.join(MOD_DIR, "history", "countries", "CHL - Chile.txt"), 5000000)
    set_treasury(os.path.join(MOD_DIR, "history", "countries", "USA - USA.txt"), 1000000)
    create_patagonia_file()
    configure_cuba()
    register_countries()
    apply_super_rgos_and_sovereignty()
    print("--- PLAN MAESTRO COMPLETADO ---")

import os
import re

POPS_1836_DIR = os.path.abspath(os.path.join(os.getcwd(), "mod", "Conosur", "history", "pops", "1836.1.1"))

def process_file(filename, process_function):
    """Función envoltura para leer, procesar y escribir de forma segura."""
    file_path = os.path.join(POPS_1836_DIR, filename)
    if not os.path.exists(file_path):
        return

    # Victoria 2 usa codificación ANSI/Latin-1
    with open(file_path, 'r', encoding='ISO-8859-1') as f:
        original_content = f.read()

    new_content = process_function(original_content)

    # Idempotencia: Solo escribir si hay cambios reales
    if new_content != original_content:
        with open(file_path, 'w', encoding='ISO-8859-1') as f:
            f.write(new_content)
        print(f"[+] Actualizado: {filename}")

def chilenize(content):
    """Cambia cultura a chilean y religión a catholic."""
    c = re.sub(r"culture\s*=\s*\w+", "culture = chilean", content)
    c = re.sub(r"religion\s*=\s*\w+", "religion = catholic", c)
    return c

def catholicize_platenses(content):
    """Asigna catolicismo a todas las poblaciones."""
    # Como es Sudamérica (excepto nativos puros), generalizamos la religión base
    return re.sub(r"religion\s*=\s*\w+", "religion = catholic", content)

def remove_afro(content):
    """Busca bloques de pops afro y los elimina."""
    # Encuentra bloques completos como: farmers = { culture = african_minor ... }
    # y los elimina para hacer la 'limpieza' requerida.
    pattern = re.compile(r"\w+\s*=\s*\{[^{}]*culture\s*=\s*(african_minor|afro_caribeno|ashanti|yoruba|beafada|bakongo)[^{}]*\}", re.IGNORECASE)
    return pattern.sub("", content)

def madagascar_swap(content):
    """Reemplaza la población nativa por Jewish."""
    # Limpiamos el contenido actual y creamos uno nuevo predefinido
    jewish_pops = """
2115 = {
	aristocrats = { culture = jewish religion = jewish size = 1000 }
	clergymen = { culture = jewish religion = jewish size = 1000 }
	artisans = { culture = jewish religion = jewish size = 5000 }
	soldiers = { culture = jewish religion = jewish size = 2000 }
	farmers = { culture = jewish religion = jewish size = 50000 }
}
2116 = { farmers = { culture = jewish religion = jewish size = 30000 } }
2117 = { farmers = { culture = jewish religion = jewish size = 30000 } }
2118 = { farmers = { culture = jewish religion = jewish size = 30000 } }
2119 = { farmers = { culture = jewish religion = jewish size = 30000 } }
2120 = { farmers = { culture = jewish religion = jewish size = 30000 } }
2121 = { farmers = { culture = jewish religion = jewish size = 30000 } }
2122 = { farmers = { culture = jewish religion = jewish size = 30000 } }
"""
    return jewish_pops

if __name__ == "__main__":
    print("Ejecutando Plan Maestro Demográfico...")
    
    process_file("Chile.txt", chilenize)
    
    for platense in ["Argentina.txt", "Uruguay.txt", "Paraguay.txt"]:
        process_file(platense, catholicize_platenses)
        process_file(platense, remove_afro)
    process_file("Chile.txt", remove_afro)
    
    process_file("Madagascar.txt", madagascar_swap)
    
    print("Rebalanceo demográfico completado.")

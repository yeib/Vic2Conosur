import os
import shutil
import re

MOD_DIR = os.path.abspath(os.path.join(os.getcwd(), "mod", "Conosur"))
BASE_GAME_DIR = os.getcwd()

def main():
    filename = "Great Britain.txt"
    base_file = os.path.join(BASE_GAME_DIR, "history", "pops", "1836.1.1", filename)
    mod_file = os.path.join(MOD_DIR, "history", "pops", "1836.1.1", filename)
    
    if not os.path.exists(mod_file) and os.path.exists(base_file):
        os.makedirs(os.path.dirname(mod_file), exist_ok=True)
        shutil.copy2(base_file, mod_file)
    
    with open(mod_file, 'r', encoding='ISO-8859-1') as f:
        content = f.read()
        
    pop_text = "\tartisans = { culture = chilean religion = catholic size = 500 }"
    if "chilean" not in content:
        pattern = r"(300\s*=\s*\{)"
        content = re.sub(pattern, rf"\1\n{pop_text}\n", content, count=1)
        with open(mod_file, 'w', encoding='ISO-8859-1') as f:
            f.write(content)
        print("Inyectado en Gran Bretaña (Londres)")

if __name__ == "__main__":
    main()

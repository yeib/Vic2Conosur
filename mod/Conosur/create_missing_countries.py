import os

MOD_COUNTRIES_DIR = r"mod/Conosur/common/countries"
os.makedirs(MOD_COUNTRIES_DIR, exist_ok=True)

patagonia_content = """color = { 100 150 200 }
graphical_culture = SouthAmericanGC
party = {
	name = "PAT_conservative"
	start_date = 1836.1.1
	end_date = 2000.1.1
	ideology = conservative
	economic_policy = interventionism
	trade_policy = protectionism
	religious_policy = moralism
	citizenship_policy = residency
	war_policy = jingoism
}
"""

conosur_content = """color = { 163 138 72 }
graphical_culture = SouthAmericanGC
party = {
	name = "CSU_conservative"
	start_date = 1836.1.1
	end_date = 2000.1.1
	ideology = conservative
	economic_policy = interventionism
	trade_policy = protectionism
	religious_policy = moralism
	citizenship_policy = residency
	war_policy = jingoism
}
"""

mapuche_content = """color = { 38 131 72 }
graphical_culture = SouthAmericanGC
party = {
	name = "MAP_conservative"
	start_date = 1836.1.1
	end_date = 2000.1.1
	ideology = conservative
	economic_policy = interventionism
	trade_policy = protectionism
	religious_policy = moralism
	citizenship_policy = residency
	war_policy = jingoism
}
"""

diaguita_content = """color = { 181 72 38 }
graphical_culture = SouthAmericanGC
party = {
	name = "DIA_conservative"
	start_date = 1836.1.1
	end_date = 2000.1.1
	ideology = conservative
	economic_policy = interventionism
	trade_policy = protectionism
	religious_policy = moralism
	citizenship_policy = residency
	war_policy = jingoism
}
"""

guayana_content = """color = { 200 180 50 }
graphical_culture = SouthAmericanGC
party = {
	name = "GYA_conservative"
	start_date = 1836.1.1
	end_date = 2000.1.1
	ideology = conservative
	economic_policy = interventionism
	trade_policy = protectionism
	religious_policy = moralism
	citizenship_policy = residency
	war_policy = jingoism
}
"""

files = {
    "Patagonia.txt": patagonia_content,
    "Conosur.txt": conosur_content,
    "Mapuche.txt": mapuche_content,
    "Diaguita.txt": diaguita_content,
    "Guayana.txt": guayana_content
}

for filename, content in files.items():
    filepath = os.path.join(MOD_COUNTRIES_DIR, filename)
    with open(filepath, "w", encoding="utf-8") as f:
        f.write(content)
    print(f"Creado: {filepath}")

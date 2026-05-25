# Victoria 2: Conosur Mod - Development Roadmap & State

## Overall Goal
Develop the 'Conosur' mod for Victoria 2 by implementing a complete "Day 1" (1836) global overhaul. This involves creating powerful, ahistorical unified states and redistributing territories to create a balanced, multipolar world.

## Current State: Phase 1 Completed, Phase 2 Started

### ✅ Phase 1: Stable Borders & Geopolitics (COMPLETED)
- **Global Territorial Realignment:** All major unifiers and mega-empires have achieved their designated borders for the 1836 start.
  - **Notable Expansions:** 
    - **Russia:** Full control of Siberia (Ob, Yeniseysk, Yakutsk, Chukotka).
    - **Sokoto:** Hegemony over Central/West Africa (Bornu, Hausaland, Cameroon, etc.).
    - **South Africa:** Domination of Southern Africa, including Hereroland, Botswana, and Walvis Bay.
    - **Brazil:** Expansion into the Andes and Amazon (Acre, La Paz, Cochabamba, Eastern Bolivia).
    - **USA:** Consolidated the Northwest and Maritime Canada (New Brunswick, Nova Scotia).
    - **Germany:** Secured Alsace-Lorraine and Wielkopolskie.
    - **Scandinavia:** Acquired Karelia.
    - **Arabia & Portugal:** Arabia controls the Somali coast; Portugal expanded in West and East Africa.
    - **Guayana & Gran Colombia:** Secured vital coastal and Amazonian provinces.
  - **Capital Adjustments:** Bolivia's capital successfully relocated to Potosi (2314).
- **Standardized Orders of Battle (OOB):** 
  - To prevent day-1 crashes and ensure fairness, all 133 countries have been standardized.
  - Each nation starts with exactly **1 army** (5 brigades: 3 infantry, 1 cavalry, 1 artillery) in their capital.
  - Coastal nations start with a maximum of **2 ships** (1 frigate, 1 transport) at their primary naval base.

### 🔄 Phase 2: Cultural & Demographic Overhaul (IN PROGRESS)
- **New Cultures Injected:** 
  - Latin American group: `chilean`, `patagon`.
  - Native American group: `mapuche`, `diaguita`.
- **National Identities:** 
  - **Chile (CHL):** Primary culture `chilean`, accepted `south_andean`. POPs in Chilean territory converted to 100% Catholic Chileans.
  - **Patagonia (PAT):** Primary culture `patagon`, accepted `south_andean`. POPs in Patagonian territory converted to 100% Catholic Patagons.
  - **Native Nations:** Mapuche (MAP) and Diaguita (DIA) configured to be releasable/rebel-spawnable with their respective primary cultures.
- **Next Steps:** Review and inject accurate demographics and cultural distributions for the remaining mega-empires and unifiers.

## Technical Mandates
- All modifications MUST occur within the `mod/Conosur/` directory. Base game files must remain untouched.
- Text files must use ANSI (`ISO-8859-1`) encoding.
- Ownership, control, and cores in province history files must be defined at the top level, outside any date blocks.

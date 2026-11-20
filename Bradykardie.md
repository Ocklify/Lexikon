---
stand: 2026-11-02
aliases:
  - Bradyarrhythmie
  - bradykarde Herzrhythmusstörung
  - AV-Block
  - Schrittmacher
tags:
  - Bradykardie
  - Notfallmedizin
  - Reanimation
  - Intensivmedizin
  - AV-Block
  - Katecholamine
  - Perfusor
---

# Bradykardie
*(Stand: 02.11.2026)*

---
## 💬 KURZ
- meist als HF < 60/min definiert  
- bei Sportlern ist Bradykardie meist normal  
    - **Behandle den Patienten, nicht die Zahl** 😉  
- entscheidend ist, ob der Patient *symptomatisch* ist:  
    - Schock, Synkope, Angina Pectoris, Herzinsuffizienz  
- Notfalltherapie:  
    - Atropin, Adrenalin, [Isoprenalin](docs/Isoprenalin.md), Pacing  

---
## 🚨 CAVE / MERKE 💡

> [!warning] Vor jeder Therapie: Hypoxie ausschließen
> O₂, SpO₂ und [cABCDE](docs/cABCDE.md)-Schema · Therapiemanagement nach Algorithmus (s. u.)

> [!danger] KEIN Atropin bei:
> - **Mobitz II / AV-Block III / breiter Kammerersatzrhythmus**
> 	→ Atropin wirkt (fast) nicht, kann den Block verschlechtern → **Pacing**
> - **Herztransplantierte / Querschnittsgelähmte**
> 	→ denerviertes Herz, paradoxer AV-Block möglich
> 	→ **Aminophyllin** (100–200 mg i.v. langsam) oder direkt Pacing

> [!info] Ursache immer mitbedenken
> - **[Hyperkaliämie](docs/Kalium.md)** als Ursache immer bedenken  
> - Digitoxin / β-Blocker / Calciumantagonisten als Ursache?  
> 	→ [Antidota](docs/Antidota.md) (s. u.)

---

## ❓ URSACHEN

| Kategorie | Beispiele |
| --- | --- |
| Vagal/reflektorisch | Intubation, Absaugen, okulokardialer Reflex, Karotissinus, Peritoneum/Viszera |
| Medikamenten-überdosierung | [Betablocker](docs/Betablocker.md), Ca-Antagonisten, Clonidin, Digoxin, Amiodaron, Suxamethonium, Neostigmin, Opioide |
| Ischämie | Inferiorer MI (AV-Knoten) → AV-Block<br>anteriorer MI → breiter QRS |
| Metabolisch | [Hyperkaliämie](docs/Kalium.md) ❗️, Hypothyreose, Hypothermie |
| Neurologisch | ↑ ICP (Cushing-Reflex: Hypertonie + Bradykardie + Atemstörung) |
| Sonstiges | Sinusknotendysfunktion (SSS), nach Kardioversion, Schlafapnoe, Sportlerherz (asymptomatisch!) |

---

## 📈 EKG-LOKALISATION

| Block | Lokalisation | Atropin? |
| --- | --- | --- |
| Sinusbradykardie | Sinusknoten | ja ✅ |
| AV-Block I (PQ > 200 ms) | AV-Knoten | ja ✅ |
| AV-Block II – Typ Mobitz I (= Wenckebach) | suprahisär (AV-Knoten) | ja ✅ |
| AV-Block II – Typ Mobitz II | infrahisär | NEIN ❌ → Pacing |
| AV-Block III, **schmaler QRS**<br>(QRS < 120 ms, HF 40–60/min) | junktional/suprahisär | NEIN ❌ → Pacing |
| AV-Block III, **breiter QRS**<br>(QRS > 120 ms, HF 20–40/min) | infrahisär | NEIN ❌ → Pacing |

> [!tip] Faustregel
> - **AV- Block I / Mobitz I (suprahisär) = Atropin wirkt meist**
> - **Mobitz II / AV-Block III (hochgradig) = Atropin unzuverlässig bis schädlich → Pacing**

---

## 🏥 MANAGEMENT (ERC 2025)
1. **Bedrohliche Symptome?**
    - RR↓ (syst. < 90), Synkope, AP, Herzinsuffizienz  
    - Nein → beobachten, Monitoring, weitere Diagnostik  
    - Ja → **Atropin 0,5 mg i.v.**, alle 3–5 min wiederholen bis **max. 3 mg** 💡
2. **Atropin wirksam? Patient stabil?**  
    - Ja → beobachten, Monitoring, weitere Diagnostik  
    - Nein → Second-line Medikamente oder Pacing  
3. Second-line Medikamente:  
    - **Isoprenalin 1–5 µg/min** 
    - **Adrenalin 2–10 µg/min**  
    - Isoprenalin + Adrenalin vermeiden (Arrhythmiegefahr)  
4. Transkutanes Pacing (TCP) als Überbrückung:
    - Rate 60–80/min, Demand-Modus
    - Output ab ~30 mA hochtitrieren bis Capture (QRS im EKG + palpabler Puls, alternativ Sonographie)
    - Pacing ist schmerzhaft → Analgosedierung 💡
5. Transvenöser SM (temporär) → **Permanenter Schrittmacher = definitive Therapie**

--- 

## 💉 SPEZIALSITUATIONEN
- **β-Blocker/Ca-Antagonisten-Intoxikation:**
    - **Früh & parallel eskalieren** – nicht sequentiell jeden Schritt abwarten ❗️
    - **Pacing oft ineffektiv**
    - **1. Basistherapie:** Volumen + Atropin-Versuch (wirkt oft kaum → nicht aufhalten lassen)
    - **2. Calcium** (v. a. bei Ca-Antagonisten, aber auch bei Betablockern sinnvoll):
        - Calciumgluconat 10 % **10–30 ml i.v.** (Wdh. nach 5–10 min möglich)
        - effektiver: **Calciumchlorid 10 % 10 ml** (3-fache Ca²⁺-Menge) → bevorzugt über ZVK 💡
    - **3. High-Dose-Insulin (HIET) frühzeitig** – nicht erst wenn „refraktär“ ❗️:
        - **Insulin 1 IE/kg i.v.-Bolus** → dann **1–2(–10) IE/kg/h** titriert
        - **Glucose 10 % 0,25 g/kg/h** parallel · **BZ initial alle 15–30 min** (Ziel: Euglykämie)  
        - **K⁺ überwachen/substituieren** – Insulin shiftet K⁺ nach intrazellulär 🚨
    - **4. Katecholamine:**
        - frühzeitig starten  
        - Isoprenalin, Adrenalin, Noradrenalin  
    - **5. Glucagon – nur noch nachrangig:**
        - **50 µg/kg i.v.-Bolus** über 1–2 min  
            → ca. 3–5(–10) mg  
            → dann **1–15 mg/h** titriert  
        - bei β-Blockern; bei Ca-Antagonisten Wirkung fraglich
        - CAVE: 1. häufig Übelkeit/Erbrechen, 2. Tachyphylaxie, 3. wirkt nur 10–15 min 💡
    - **6. Refraktär:**
        - **Lipid-Emulsion**:
            - 1,5 ml/kg 20 % Bolus  
            - dann 0,25 ml/kg/min  
        - **Methylenblau** bei refraktärer Vasoplegie: 1–2 mg/kg i.v.
        - an **ECMO** denken  
    - **Giftnotruf einbeziehen** ☎️ 
        - München: +49 89 - 19240
        - Berlin: +49 30 - 19240
- **[Hyperkaliämie](docs/Kalium.md):** 
    - Calciumgluconat, Glukose+Insulin, etc. als Überbrückung  
    - dann K⁺ definitiv senken (Furosemid, ggf. Dialyse)  
    - Bradykardie ist hier Spätsymptom und Alarmzeichen🚨
- **Herztransplantierte und Querschnittsgelähmte:**
    - kein Atropin  
    - **Aminophyllin** (100–200 mg i.v. langsam) 
    - oder direkt Pacing

---
## 📊 VERGLEICH

| Maßnahme | Dosis | Angriffspunkt | CAVE |
| --- | --- | --- | --- |
| Atropin | 0,5 mg i.v., max. 3 mg | M2-Blockade (vagal) | wirkt nicht infrahisär |
| [Isoprenalin](docs/Isoprenalin.md) | 1–5 µg/min | β1/β2 | Vasodilatation, KHK ⚠️ |
| Adrenalin | 2–10 µg/min | α + β | Ischämie, Arrhythmie |
| Dopamin | 5–20 µg/kg/min | DA/β1/α | Tachykardie, NW Vielfalt |
| Glucagon | 50 µg/kg, dann 1–15 mg/h | cAMP direkt (receptorunabhängig) | nur BB/CBB, Tachyphylaxie |
| Pacing | Rate 60–80/min, bis Capture | elektrisch | Schmerz! nur Überbrückung |
| Transvenöser SM | Rate 60–80/min, bis Capture | elektrisch | nur Überbrückung |
| Permanenter SM | individuell angepasst | elektrisch | **Ziel** |

> ERC: Atropin in 0,5-mg-Schritten · AHA: 1-mg-Schritte (jeweils max. 3 mg)

---
<details>
<summary>🔤 Abkürzungen</summary>
<table>
<tr><td>AP</td><td>Angina pectoris</td></tr>
<tr><td>BB</td><td>Betablocker</td></tr>
<tr><td>BZ</td><td>Blutzucker</td></tr>
<tr><td>CCB</td><td>Calciumkanalblocker</td></tr>
<tr><td>HF</td><td>Herzfrequenz</td></tr>
<tr><td>HIET</td><td>High-Dose Insulin Euglycemic Therapy</td></tr>
<tr><td>ICP</td><td>intrakranieller Druck</td></tr>
<tr><td>MI</td><td>Myokardinfarkt</td></tr>
<tr><td>QS</td><td>Querschnitt</td></tr>
<tr><td>SM</td><td>Schrittmacher</td></tr>
<tr><td>SSS</td><td>Sick-Sinus-Syndrom (Sinusknotendysfunktion)</td></tr>
<tr><td>TCP</td><td>transkutanes Pacing</td></tr>
<tr><td>ZVK</td><td>zentraler Venenkatheter</td></tr>
</table>
</details>

<details>
<summary>📚 Quellen</summary>
<ul>
<li>ERC Guidelines 2025: Adult Advanced Life Support (Soar et al., Resuscitation 2025;215(Suppl 1)) – Bradykardie-Algorithmus, Atropin 500 µg, Isoprenalin, Adrenalin 2–10 µg/min, Aminophyllin bei Transplantat/QS, kein Atropin bei hochgradigem AV-Block + breitem QRS</li>
<li>ERC Guidelines 2021: Adult ALS (Soar et al., Resuscitation 2021) – Vorgängerversion</li>
<li>Resuscitation Council UK, Adult ALS Guideline 2021 &amp; 2025</li>
<li>AHA Guidelines 2025, Part 9: Adult Advanced Life Support (Circulation 2025;152(Suppl 2)) – Atropin 1 mg, Dopamin 5–20 µg/kg/min, Adrenalin 2–10 µg/min, TCP</li>
<li>ACC/AHA/HRS 2018: Guideline on Bradycardia and Cardiac Conduction Delay (Circulation 2019;140:e382–e482)</li>
<li>Expertenkonsensus Ca-Antagonisten-Intoxikation (Stellpflug et al., Crit Care Med 2017) – Calcium, HIET, Katecholamine als First-line</li>
<li>ANZCOR Guideline 11.9 – Managing Acute Dysrhythmias (Atropin, Glucagon/HIET, Transplantat-Warnung)</li>
<li>StatPearls: Transcutaneous Pacing (NCBI Bookshelf)</li>
<li>WikEM: Beta-blocker toxicity; Maryland Poison Center: Glucagon Antidote Facts (50 µg/kg, 1–15 mg/h)</li>
<li>Amboss-SOP: Bradykarde Herzrhythmusstörungen (Atropin 0,5–1 mg, Isoprenalin/Adrenalin nicht simultan)</li>
<li>Fachinformation Isoprenalin Macure (Carinopharm) – Titrationsschema, Verdünnung 4 µg/ml</li>
</ul>
</details>
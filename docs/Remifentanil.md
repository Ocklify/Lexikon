# Remifentanil 
= Ultiva ®

### 🚨 CAVE / MERKE 💡
- selektiver Vollagonist am µ-Opioidrezeptor
	→ ca. 200x stärker als Morphin
- kurzer WE (1 min), kurze WD (<5 min)
- keine [Kumulation](Kumulation.md) 
	→ ideal für präzise Steuerung
- keine postoperative Analgesie 
	→ frühzeitig Umstellung nötig (z.B. Piritramid)
- kein DANI / DALI    

---

### 💊 DOSIERUNG
- initialer Bolus: 0,5–1  μg/kg über ≥30 s (optional)
	→ 40–80 μg bei 80 kg 😉
- Perfusor (OP): 0,1–0,3 μg/kg/min
	→ siehe auch Perfusorschema 😉
- TCI-Zielwert: ca. 6 ng/ml 
- Geriatrie: 
	→ reduzierte Dosis empfohlen 
	→ ½ Bolus, ⅓ Laufrate
- am OP-Ende i.d.R. Piritramid
	→ 4,5–7,5 mg i.v.

---

<h3>📌 INTERAKTIVER RECHNER</h3>

<label for="kg">Körpergewicht (kg):</label><br>
<input type="number" id="kg" value="70" min="30" max="150" step="1"><br><br>

<label for="konz">Konzentration (μg/ml):</label><br>
<select id="konz">
  <option value="20">20 μg/ml (1 mg/50 ml)</option>
  <option value="40" selected>40 μg/ml (2 mg/50 ml)</option>
  <option value="100">100 μg/ml (5 mg/50 ml)</option>
</select><br><br>

<label for="dosis">Dosierung (μg/kg/min):</label><br>
<select id="dosis">
  <option value="0.1">0.1</option>
  <option value="0.2">0.2</option>
  <option value="0.25" selected>0.25</option>
  <option value="0.3">0.3</option>
  <option value="0.4">0.4</option>
  <option value="0.5">0.5</option>
</select><br><br>

<p><strong>Infusionsrate:</strong> <span id="output">–</span> ml/h</p>

<script>
function calculate() {
  const kg = parseFloat(document.getElementById("kg").value);
  const konz = parseFloat(document.getElementById("konz").value);
  const dosis = parseFloat(document.getElementById("dosis").value);
  const mlh = (kg * dosis / konz * 60).toFixed(1);
  document.getElementById("output").textContent = isNaN(mlh) ? "–" : mlh;
}
document.querySelectorAll("input, select").forEach(el => el.addEventListener("input", calculate));
calculate();
</script>

---

### 📌 PERFUSORLISTEN

##### 💧 Ultiva® 1 mg / 50 ml NaCl (20 μg/ml) 
##### 🕖 Eingriffe bis zu 1 Stunde  

| Dosierung (μg/kg/min) | 50 kg | 60 kg | 70 kg | 80 kg | 90 kg | 100 kg |
|------------------------|:-----:|:-----:|:-----:|:-----:|:-----:|:------:|
| 0,5                   | 75,0  | 90,0  | 105,0 | 120,0 | 135,0 | 150,0  |
| 0,4                   | 60,0  | 72,0  | 84,0  | 96,0  | 108,0 | 120,0  |
| 0,3                   | 45,0  | 54,0  | 63,0  | 72,0  | 81,0  | 90,0   |
| 0,25                  | 37,5  | 45,0  | 52,5  | 60,0  | 67,5  | 75,0   |
| 0,2                   | 30,0  | 36,0  | 42,0  | 48,0  | 54,0  | 60,0   |
| 0,1                   | 15,0  | 18,0  | 21,0  | 24,0  | 27,0  | 30,0   |

---

##### 💧 Ultiva® 2 mg / 50 ml NaCl (40 μg/ml)
##### 🕖 Eingriffe von 1 bis 2 Stunden  

| Dosierung (μg/kg/min) | 50 kg | 60 kg | 70 kg | 80 kg | 90 kg | 100 kg |
|------------------------|:-----:|:-----:|:-----:|:-----:|:-----:|:------:|
| 0,5                   | 37,5  | 45,0  | 52,5  | 60,0  | 67,5  | 75,0   |
| 0,4                   | 30,0  | 36,0  | 42,0  | 48,0  | 54,0  | 60,0   |
| 0,3                   | 22,5  | 27,0  | 31,5  | 36,0  | 40,5  | 45,0   |
| 0,25                  | 18,8  | 22,5  | 26,3  | 30,0  | 33,8  | 37,5   |
| 0,2                   | 15,0  | 18,0  | 21,0  | 24,0  | 27,0  | 30,0   |
| 0,1                   | 7,5   | 9,0   | 10,5  | 12,0  | 13,5  | 15,0   |

---

##### 💧 Ultiva® 5 mg / 50 ml NaCl (100 μg/ml)
##### 🕖 längere Eingriffe    

| Dosierung (μg/kg/min) | 50 kg | 60 kg | 70 kg | 80 kg | 90 kg | 100 kg |
|------------------------|:-----:|:-----:|:-----:|:-----:|:-----:|:------:|
| 0,5                   | 15,0  | 18,0  | 21,0  | 24,0  | 27,0  | 30,0   |
| 0,4                   | 12,0  | 14,4  | 16,8  | 19,2  | 21,6  | 24,0   |
| 0,3                   | 9,0   | 10,8  | 12,6  | 14,4  | 16,2  | 18,0   |
| 0,25                  | 7,5   | 9,0   | 10,5  | 12,0  | 13,5  | 15,0   |
| 0,2                   | 6,0   | 7,2   | 8,4   | 9,6   | 10,8  | 12,0   |
| 0,1                   | 3,0   | 3,6   | 4,2   | 4,8   | 5,4   | 6,0    |

---

### ⚗️ PHARMAKOLOGIE

| Parameter                   | Wert                                      |
| --------------------------- | ----------------------------------------- |
| Wirkungseintritt            | ca. 1 Minute                              |
| Wirkdauer                   | < 5 Minuten                               |
| Metabolismus                | unspezifische Esterasen (nicht hepatisch) |
| [Kumulation](Kumulation.md) | keine                                     |

---

### 🚦 INDIKATIONEN
- intraoperative Analgesie (v.a. bei TIVA)  
- Analgesie bei beatmeten Intensivpatienten ≥18 J
- neurochirurgische Eingriffe mit engmaschiger Steuerung

---

### ❌ KONTRAINDIKATIONEN
- bekannte Überempfindlichkeit  
- nicht zur postoperativen Schmerztherapie geeignet

---

### 🔄 WECHSELWIRKUNGEN
- Wirkungsverstärkung durch Hypnotika, Benzodiazepine, Inhalationsanästhetika (z. B. [Propofol](Propofol.md), Isofluran)  
- Dosisreduktion dieser Substanzen möglich

---

### 🌀 NEBENWIRKUNGEN
- Atemdepression  
- Bradykardie, Hypotonie  
- Muskelrigidität bei Bolusgabe ⚠️
- Übelkeit, Erbrechen

---

### 🔤 Abkürzungen

| Kürzel | Bedeutung                             |
| ------ | ------------------------------------- |
| DALI   | Dosisanpassung bei Leberinsuffizienz  |
| DANI   | Dosisanpassung bei Niereninsuffizienz |
| TCI    | Target Controlled Infusion            |
| TIVA   | Total Intravenöse Anästhesie          |
| WE     | Wirkungseintritt                      |
| WD     | Wirkdauer                             |

---

### 📚 Quellen
- Stanski et al. (1995): Pharmacokinetics and pharmacodynamics of remifentanil. *Anesthesiology*, 82(4), 899–915. [PubMed](https://pubmed.ncbi.nlm.nih.gov/7703930/)  
- Egan et al. (2004): Remifentanil vs. fentanyl: pharmacokinetics and clinical implications. *Drugs*, 64(8), 865–886. [SpringerLink](https://link.springer.com/article/10.2165/00003495-200464080-00003)  
- „Pharmakotherapie in der Anästhesie und Intensivmedizin", 2011
- ﻿﻿Der Anästhesist, 08/18
- ﻿﻿„Analgesie bei Traumapatienten in der Notfallmedizin", N+R, 06/19
- Fachinfo Remifentanil, abgerufen am 14.10.2025: https://www.fachinfo.de/fi/pdf/013638

---
### 🏷️ Tags
#Narkose  #Opioid  #Schmerztherapie  #TIVA #Anästhesie  #Intensivmedizin  #Pharmakologie #Perfusorschema  #Dosierung  #Wirkung  #Nebenwirkungen  
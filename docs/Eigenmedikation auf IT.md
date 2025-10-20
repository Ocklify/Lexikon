# Eigenmedikation auf IT


<!DOCTYPE html>
<html lang="de">
<head>
<meta charset="UTF-8">
<title>Eigenmedikation ITS – Interaktive Suche</title>
<style>
  body {
    font-family: system-ui, -apple-system, Segoe UI, Roboto, Helvetica, Arial;
    background: #f5f7fa;
    padding: 20px;
    color: #333;
  }
  h2 { margin-bottom: 10px; }
  .search-box {
    position: relative;
    max-width: 400px;
  }
  input[type="text"] {
    width: 100%;
    padding: 10px;
    font-size: 15px;
    border-radius: 6px;
    border: 1px solid #ccc;
  }
  .suggestions {
    position: absolute;
    top: 100%;
    left: 0;
    right: 0;
    background: #fff;
    border: 1px solid #ccc;
    border-top: none;
    max-height: 200px;
    overflow-y: auto;
    z-index: 10;
  }
  .suggestions div {
    padding: 8px;
    cursor: pointer;
  }
  .suggestions div:hover {
    background: #f0f0f0;
  }
  .output {
    border-radius: 10px;
    padding: 16px;
    max-width: 600px;
    box-shadow: 0 3px 8px rgba(0,0,0,0.1);
    display: none;
    margin-top: 20px;
  }
  .green { background: #e6f9ec; border-left: 6px solid #2e8b57; }
  .red   { background: #fdeaea; border-left: 6px solid #b22222; }
  .yellow{ background: #fff9e6; border-left: 6px solid #b38f00; }
  .title { font-weight: 600; margin-bottom: 6px; font-size: 16px; }
</style>
</head>
<body>

<h2>🩺 Interaktive Medikamentensuche: Eigenmedikation auf ITS</h2>
<p>Gib einen Medikamentennamen ein:</p>

<div class="search-box">
  <input type="text" id="drugInput" placeholder="z.B. Levodopa, Bisoprolol, Ramipril...">
  <div id="suggestions" class="suggestions"></div>
</div>

<div id="output" class="output"></div>

<script>
// Datenbank: Medikament -> Kategorie + Text
const data = {
  "Levodopa": {color:"green", text:"Essenzielle Weitergabe. Abruptes Absetzen → akinetische Krise. Transdermale Systeme erhalten. CYP2C19-Interaktionen gering."},
  "Rotigotin": {color:"green", text:"Essenzielle Weitergabe. Abruptes Absetzen → akinetische Krise. Transdermale Systeme erhalten. CYP2C19-Interaktionen gering."},
  "Levetiracetam": {color:"green", text:"Weitergabe essenziell. TDM empfohlen."},
  "Valproat": {color:"green", text:"Weitergabe essenziell. TDM empfohlen. Bei Leberinsuffizienz kritisch. CYP2C9 relevant."},
  "L-Thyroxin": {color:"green", text:"Weitergabe enteral möglich. Keine relevante Interaktion. Monitoring bei Hypothermie."},
  "Bisoprolol": {color:"green", text:"Weitergabe bei KHK, Tachyarrhythmie. Pause bei Sepsis oder Bradykardie erwägen. CYP2D6 relevant."},
  "Metoprolol": {color:"green", text:"Weitergabe bei KHK, Tachyarrhythmie. Pause bei Sepsis oder Bradykardie erwägen. CYP2D6 relevant."},
  "Sertralin": {color:"green", text:"Weitergabe bei psychiatrischer Indikation. QT-Zeit beachten. CYP2C19/CYP3A4 relevant."},
  "Escitalopram": {color:"green", text:"Weitergabe bei psychiatrischer Indikation. QT-Zeit beachten. CYP2C19/CYP3A4 relevant."},
  "Quetiapin": {color:"green", text:"Weitergabe bei psychiatrischer Indikation. Sedierung und Delirrisiko beachten. CYP1A2/CYP3A4 relevant."},
  "Olanzapin": {color:"green", text:"Weitergabe bei psychiatrischer Indikation. Sedierung und Delirrisiko beachten. CYP1A2/CYP3A4 relevant."},
  "Amlodipin": {color:"green", text:"Weitergabe bei stabiler Hämodynamik. CYP3A4 relevant."},
  "Valsartan": {color:"green", text:"Weitergabe bei stabiler Hämodynamik. AT1-Blocker besser steuerbar als ACE-Hemmer. CYP3A4 relevant."},
  "Pantoprazol": {color:"green", text:"Weitergabe bei Ulkusprophylaxe oder Antikoagulation. Übertherapie häufig. CYP2C19 relevant."},

  "Metformin": {color:"red", text:"Absetzen: Risiko für Laktatazidose. Nur Insulin auf ITS."},
  "Empagliflozin": {color:"red", text:"Absetzen: Risiko für Ketoazidose, Volumenverlust. Nur Insulin auf ITS."},
  "Torasemid": {color:"red", text:"Substitution durch Furosemid: +kürzere WD, +flexible Titration, –mehr Hypokaliämie. CYP2C9 relevant."},
  "Ibuprofen": {color:"red", text:"Kontraindiziert: nephrotoxisch, gastrotoxisch, gerinnungshemmend. Paracetamol bevorzugt. CYP2C9 relevant."},
  "Diclofenac": {color:"red", text:"Kontraindiziert: nephrotoxisch, gastrotoxisch, gerinnungshemmend. Paracetamol bevorzugt. CYP2C9 relevant."},
  "Oxycodon retard": {color:"red", text:"Substitution durch kurzwirksame Alternativen. Retardierung bei Sondengabe problematisch. CYP3A4 relevant."},
  "Apixaban": {color:"red", text:"Umstellung auf Heparin: +steuerbar, +antagonisierbar, –HIT-Risiko beachten. CYP3A4 relevant."},
  "Rivaroxaban": {color:"red", text:"Umstellung auf Heparin: +steuerbar, +antagonisierbar, –HIT-Risiko beachten. CYP3A4 relevant."},
  "Marcumar": {color:"red", text:"Umstellung auf Heparin: +steuerbar, +antagonisierbar, –HIT-Risiko beachten."},
  "Simvastatin": {color:"red", text:"Pause bei Leberwertanstieg oder Rhabdomyolyse-Risiko. Re-Evaluation postoperativ. CYP3A4 relevant."},
  "Allopurinol": {color:"red", text:"Absetzen bei akuter Erkrankung. Interaktionen mit Azathioprin. Xanthinoxidase relevant."},
  "Finasterid": {color:"red", text:"Nicht relevant auf ITS. Keine Fortführung nötig."},

  "Ramipril": {color:"yellow", text:"Weitergabe bei Herzinsuffizienz. Pause bei Hypertonie als alleiniger Indikation oder Hypotonie."},
  "Enalapril": {color:"yellow", text:"Weitergabe bei Herzinsuffizienz. Pause bei Hypertonie als alleiniger Indikation oder Hypotonie."},
  "Haloperidol": {color:"yellow", text:"Weitergabe bei Psychose. Pause bei Delir oder QT-Verlängerung. CYP2D6/CYP3A4 relevant."},
  "Risperidon": {color:"yellow", text:"Weitergabe bei Psychose. Pause bei Delir oder QT-Verlängerung. CYP2D6/CYP3A4 relevant."},
  "Donepezil": {color:"yellow", text:"Weitergabe bei stabiler enteraler Gabe. Delirrisiko vs. kognitive Stabilität abwägen. CYP3A4 relevant."},
  "Rivastigmin": {color:"yellow", text:"Weitergabe bei stabiler enteraler Gabe. Delirrisiko vs. kognitive Stabil


<!DOCTYPE html>
<html lang="de">
<head>
<meta charset="UTF-8">
<title>Eigenmedikation ITS – Interaktives Menü</title>
<style>
  body {
    font-family: system-ui, -apple-system, Segoe UI, Roboto, Helvetica, Arial;
    background: #f5f7fa;
    padding: 20px;
    color: #333;
  }
  h2 { margin-bottom: 10px; }
  select {
    padding: 10px;
    font-size: 15px;
    border-radius: 6px;
    border: 1px solid #ccc;
    width: 100%;
    max-width: 400px;
    margin-bottom: 20px;
  }
  .output {
    border-radius: 10px;
    padding: 16px;
    max-width: 600px;
    box-shadow: 0 3px 8px rgba(0,0,0,0.1);
    display: none;
    animation: fadeIn 0.3s ease-in-out;
  }
  .green { background: #e6f9ec; border-left: 6px solid #2e8b57; }
  .red   { background: #fdeaea; border-left: 6px solid #b22222; }
  .yellow{ background: #fff9e6; border-left: 6px solid #b38f00; }
  @keyframes fadeIn {
    from {opacity:0; transform: translateY(5px);}
    to {opacity:1; transform: translateY(0);}
  }
  .title { font-weight: 600; margin-bottom: 6px; }
</style>
</head>
<body>

<h2>🩺 Interaktives Auswahlmenü: Eigenmedikation auf ITS</h2>
<p>Wähle ein Medikament aus der Liste, um Details zu sehen:</p>

<select id="drugSelect">
  <option value="">-- Medikament auswählen --</option>
  <optgroup label="✅ Weitergabe empfohlen">
    <option value="Parkinsonmedikation">Parkinsonmedikation</option>
    <option value="Antiepileptika">Antiepileptika</option>
    <option value="Schilddrüsenmedikation">Schilddrüsenmedikation</option>
    <option value="Beta-Blocker">Beta-Blocker</option>
    <option value="SSRI">SSRI</option>
    <option value="Antipsychotika">Antipsychotika</option>
    <option value="Antihypertensiva">Antihypertensiva</option>
    <option value="PPI">PPI</option>
  </optgroup>
  <optgroup label="❌ Kontraindiziert / Substitution">
    <option value="Antidiabetika">Orale Antidiabetika</option>
    <option value="Torasemid">Torasemid</option>
    <option value="NSAR">NSAR</option>
    <option value="Retardpraeparate">Retardpräparate</option>
    <option value="DOAK">DOAK / Marcumar</option>
    <option value="Statine">Statine</option>
    <option value="Allopurinol">Allopurinol</option>
    <option value="Finasterid">Finasterid</option>
  </optgroup>
  <optgroup label="⚖️ Situativ abwägen">
    <option value="ACE">ACE-Hemmer</option>
    <option value="Neuroleptika">Neuroleptika</option>
    <option value="Antidementiva">Antidementiva</option>
    <option value="Antihistaminika">Antihistaminika</option>
    <option value="Spironolacton">Spironolacton</option>
    <option value="Clonidin">Clonidin</option>
    <option value="ASS">ASS / TAH</option>
  </optgroup>
</select>

<div id="output" class="output"></div>

<script>
const data = {
  "Parkinsonmedikation": {color:"green", text:"Nie absetzen → akinetische Krise. Transdermale Systeme erhalten."},
  "Antiepileptika": {color:"green", text:"Essentiell; TDM bei Valproat. Leberfunktion beachten."},
  "Schilddrüsenmedikation": {color:"green", text:"Enteral weitergeben. Monitoring bei Hypothermie."},
  "Beta-Blocker": {color:"green", text:"Bei KHK/Arrhythmie weiter; Pause bei Sepsis/Bradykardie erwägen."},
  "SSRI": {color:"green", text:"Weitergabe; QT-Zeit beachten."},
  "Antipsychotika": {color:"green", text:"Weitergabe; Sedierung/Delirrisiko beachten."},
  "Antihypertensiva": {color:"green", text:"Bei stabiler Hämodynamik weitergeben."},
  "PPI": {color:"green", text:"Bei Ulkusprophylaxe/Antikoagulation."},

  "Antidiabetika": {color:"red", text:"Absetzen → nur Insulin (Risiko: Laktatazidose, Ketoazidose, Volumenverlust)."},
  "Torasemid": {color:"red", text:"Substitution durch Furosemid (kürzere WD, besser titrierbar)."},
  "NSAR": {color:"red", text:"Kontraindiziert → Paracetamol bevorzugen."},
  "Retardpraeparate": {color:"red", text:"Umstellung auf kurzwirksame Alternativen (Sondengabe problematisch)."},
  "DOAK": {color:"red", text:"Umstellung auf Heparin (steuerbar, antagonisierbar; HIT beachten)."},
  "Statine": {color:"red", text:"Pause bei Leberwert↑/Rhabdomyolyse-Risiko; postop reevaluieren."},
  "Allopurinol": {color:"red", text:"Absetzen bei akuter Erkrankung; Interaktion mit Azathioprin."},
  "Finasterid": {color:"red", text:"Nicht relevant auf ITS; Fortführung nicht nötig."},

  "ACE": {color:"yellow", text:"Bei Herzinsuffizienz weiter; Pause bei Hypotonie/alleiniger Hypertonie."},
  "Neuroleptika": {color:"yellow", text:"Bei Psychose weiter; Pause bei Delir oder QT-Verlängerung."},
  "Antidementiva": {color:"yellow", text:"Kognitive Stabilität vs. Delirrisiko abwägen."},
  "Antihistaminika": {color:"yellow", text:"Bei Allergie weiter; Sedierung beachten."},
  "Spironolacton": {color:"yellow", text:"Bei Herzinsuffizienz weiter; Hyperkaliämie beachten."},
  "Clonidin": {color:"yellow", text:"Bei Entzugssyndromen/Krise; Sedierung beachten."},
  "ASS": {color:"yellow", text:"Thromboseprophylaxe vs. Blutungsrisiko individuell entscheiden."}
};

document.getElementById("drugSelect").addEventListener("change", function() {
  const val = this.value;
  const out = document.getElementById("output");
  if (val && data[val]) {
    out.className = "output " + data[val].color;
    out.innerHTML = `<div class="title">${val}</div><div>${data[val].text}</div>`;
    out.style.display = "block";
  } else {
    out.style.display = "none";
  }
});
</script>

</body>
</html>





<!-- Moderner Pocket-Guide: Eigenmedikation auf ITS -->

<style>
  .card {
    border-radius: 10px;
    padding: 12px 16px;
    margin: 10px 0;
    font-family: system-ui, -apple-system, Segoe UI, Roboto, Helvetica, Arial;
    font-size: 14px;
    box-shadow: 0 2px 6px rgba(0,0,0,0.1);
  }
  .green { background: #e6f9ec; border-left: 6px solid #2e8b57; }
  .red   { background: #fdeaea; border-left: 6px solid #b22222; }
  .yellow{ background: #fff9e6; border-left: 6px solid #b38f00; }
  .card h3 {
    margin-top: 0;
    font-size: 15px;
    font-weight: 600;
  }
  .card ul {
    margin: 6px 0 0 16px;
    padding: 0;
  }
  .card ul li {
    margin: 4px 0;
  }
</style>

<div class="card green">
  <h3>✅ Weitergabe empfohlen</h3>
  <ul>
    <li><strong>Parkinsonmedikation:</strong> Nie absetzen → akinetische Krise</li>
    <li><strong>Antiepileptika:</strong> Essentiell; TDM bei Valproat</li>
    <li><strong>Schilddrüsenmedikation:</strong> Enteral weitergeben</li>
    <li><strong>Beta‑Blocker:</strong> Bei KHK/Arrhythmie; Pause bei Sepsis/Brady</li>
    <li><strong>SSRI:</strong> Weitergabe; QT‑Zeit beachten</li>
    <li><strong>Antipsychotika:</strong> Weitergabe; Delir-/Sedierungsrisiko</li>
    <li><strong>Antihypertensiva (Amlodipin/AT1):</strong> Bei stabiler Hämodynamik</li>
    <li><strong>PPI:</strong> Bei Ulkusprophylaxe/Antikoagulation</li>
  </ul>
</div>

<div class="card red">
  <h3>❌ Kontraindiziert / Substitution</h3>
  <ul>
    <li><strong>Orale Antidiabetika:</strong> Absetzen → nur Insulin</li>
    <li><strong>Torasemid:</strong> Substitution durch Furosemid</li>
    <li><strong>NSAR:</strong> Kontraindiziert → Paracetamol</li>
    <li><strong>Retardpräparate:</strong> → kurzwirksame Alternativen</li>
    <li><strong>DOAK/Marcumar:</strong> → Heparin (steuerbar, antagonisierbar)</li>
    <li><strong>Statine:</strong> Pause bei Leberwert↑/Rhabdomyolyse‑Risiko</li>
    <li><strong>Allopurinol:</strong> Absetzen bei akuter Erkrankung</li>
    <li><strong>Finasterid:</strong> Nicht relevant auf ITS</li>
  </ul>
</div>

<div class="card yellow">
  <h3>⚖️ Situativ abwägen</h3>
  <ul>
    <li><strong>ACE‑Hemmer:</strong> Bei HI weiter; Pause bei Hypotonie</li>
    <li><strong>Neuroleptika:</strong> Bei Psychose weiter; Pause bei Delir/QT↑</li>
    <li><strong>Antidementiva:</strong> Nutzen vs. Delirrisiko</li>
    <li><strong>Antihistaminika:</strong> Bei Allergie; Sedierung beachten</li>
    <li><strong>Spironolacton:</strong> Bei HI weiter; Hyperkaliämie beachten</li>
    <li><strong>Clonidin:</strong> Bei Entzug/Krise; Sedierung beachten</li>
    <li><strong>ASS/TAH:</strong> Nutzen (Thrombose) vs. Blutungsrisiko</li>
  </ul>
</div>


---

✅ Weitergabe empfohlen

Kategorie	Empfehlung	
Parkinsonmedikation (Levodopa, Rotigotin)	Essenzielle Weitergabe. Abruptes Absetzen → akinetische Krise. Transdermale Systeme erhalten. CYP2C19-Interaktionen gering.	
Antiepileptika (Levetiracetam, Valproat)	Weitergabe essenziell. TDM empfohlen. Valproat bei Leberinsuffizienz kritisch. CYP2C9 relevant.	
Schilddrüsenmedikation (L-Thyroxin)	Weitergabe enteral möglich. Keine relevante Interaktion. Monitoring bei Hypothermie.	
Beta-Blocker (Bisoprolol, Metoprolol)	Weitergabe bei KHK, Tachyarrhythmie. Pause bei Sepsis oder Bradykardie erwägen. CYP2D6 relevant.	
Antidepressiva (SSRI: Sertralin, Escitalopram)	Weitergabe bei psychiatrischer Indikation. QT-Zeit beachten. CYP2C19/CYP3A4 relevant.	
Antipsychotika (Quetiapin, Olanzapin)	Weitergabe bei psychiatrischer Indikation. Sedierung und Delirrisiko beachten. CYP1A2/CYP3A4 relevant.	
Antihypertensiva (Amlodipin, AT1-Blocker)	Weitergabe bei stabiler Hämodynamik. AT1-Blocker besser steuerbar als ACE-Hemmer. CYP3A4 relevant.	
PPIs (Pantoprazol)	Weitergabe bei Ulkusprophylaxe oder Antikoagulation. Übertherapie häufig. CYP2C19 relevant.	


---

❌ Kontraindiziert / Substitution empfohlen

Kategorie	Empfehlung	
Orale Antidiabetika (Metformin, Empagliflozin)	Absetzen: Risiko für Laktatazidose, Ketoazidose, Volumenverlust. Nur Insulin auf ITS.	
Schleifendiuretika (Torasemid)	Substitution durch Furosemid: +kürzere WD, +flexible Titration, –mehr Hypokaliämie. CYP2C9 relevant.	
NSAR (Ibuprofen, Diclofenac)	Kontraindiziert: nephrotoxisch, gastrotoxisch, gerinnungshemmend. Paracetamol bevorzugt. CYP2C9 relevant.	
Retardpräparate (z.B. Oxycodon retard)	Substitution durch kurzwirksame Alternativen. Retardierung bei Sondengabe problematisch. CYP3A4 relevant.	
Orale Antikoagulanzien (DOAK, Marcumar)	Umstellung auf Heparin: +steuerbar, +antagonisierbar, –HIT-Risiko beachten. CYP3A4 relevant bei DOAK.	
Statine (Simvastatin)	Pause bei Leberwertanstieg oder Rhabdomyolyse-Risiko. Re-Evaluation postoperativ. CYP3A4 relevant.	
Allopurinol	Absetzen bei akuter Erkrankung. Interaktionen mit Azathioprin. CYP-unabhängig, aber Xanthinoxidase relevant.	
Finasterid	Nicht relevant auf ITS. CYP3A4 relevant. Keine Fortführung nötig.	


---

⚖️ Situativ abwägen

Kategorie	Empfehlung	
ACE-Hemmer (Ramipril, Enalapril)	Weitergabe bei Herzinsuffizienz. Pause bei Hypertonie als alleiniger Indikation oder Hypotonie. CYP-unabhängig.	
Neuroleptika (Haloperidol, Risperidon)	Weitergabe bei Psychose. Pause bei Delir oder QT-Verlängerung. CYP2D6/CYP3A4 relevant.	
Antidementiva (Donepezil, Rivastigmin)	Weitergabe bei stabiler enteraler Gabe. Delirrisiko vs. kognitive Stabilität abwägen. CYP3A4 relevant.	
Antihistaminika (Cetirizin, Loratadin)	Weitergabe bei Allergieanamnese. Sedierung beachten. CYP3A4 relevant.	
Spironolacton	Weitergabe bei Herzinsuffizienz. Hyperkaliämie-Risiko beachten. CYP3A4 relevant.	
Clonidin	Weitergabe bei Entzugssyndromen oder hypertensiver Krise. Sedierung beachten. CYP-unabhängig.	
ASS 100 / TAH (Clopidogrel, Ticagrelor)	Weitergabe bei kardiovaskulärer Indikation. Blutungsrisiko vs. Thromboseprophylaxe. CYP2C19/CYP3A4 relevant.	


---

🔤 Abkürzungen

Kürzel	Bedeutung	
ACE	Angiotensin-Converting-Enzyme	
AT1	Angiotensin-II-Rezeptor Typ 1	
CYP	Cytochrom-P450-Enzymfamilie	
DOAK	Direkte orale Antikoagulanzien	
ITS	Intensivstation	
NSAR	Nichtsteroidale Antirheumatika	
PPI	Protonenpumpenhemmer	
QT	Zeitintervall im EKG	
SSRI	Selektive Serotonin-Wiederaufnahmehemmer	
TDM	Therapeutisches Drug Monitoring	
TAH	Thrombozytenaggregationshemmer	
WD	Wirkdauer	


---

📚 Quellen

• KBV: Top 30 Arzneimittel in Deutschland KBV Gesundhe...
• Health-Rise: Häufigste Medikamente in Deutschland Mein Gesundh...
• Gelbe Liste: CYP-450-Interaktionen Gelbe Liste
• Thieme: Arzneimittelinteraktionen in der Intensivmedizin thieme-conne...


---

🏷️ Tags

Intensivmedizin, Anästhesie, Eigenmedikation, Medikationsanamnese, Hausmedikation, Pharmakologie, Medikamentensicherheit, Interaktionen, CYP, Delir, Organdysfunktion, TDM, Substitution, Monitoring, Polypharmazie, operative ITS, perioperative Medizin, mobile-ready, klinische Entscheidungsfindung

---


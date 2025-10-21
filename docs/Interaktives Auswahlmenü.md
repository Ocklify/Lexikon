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






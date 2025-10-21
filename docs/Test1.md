

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
  .search-box { position: relative; max-width: 400px; }
  input[type="text"] {
    width: 100%; padding: 10px; font-size: 15px;
    border-radius: 6px; border: 1px solid #ccc;
  }
  .suggestions {
    position: absolute; top: 100%; left: 0; right: 0;
    background: #fff; border: 1px solid #ccc; border-top: none;
    max-height: 200px; overflow-y: auto; z-index: 10;
  }
  .suggestions div { padding: 8px; cursor: pointer; }
  .suggestions div:hover { background: #f0f0f0; }
  .output {
    border-radius: 10px; padding: 16px; max-width: 600px;
    box-shadow: 0 3px 8px rgba(0,0,0,0.1);
    display: none; margin-top: 20px;
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
// Datenbank: nur 3 Beispiele pro Kategorie
const data = {
  // ✅ Weitergabe empfohlen
  "Levodopa": {color:"green", text:"Essenzielle Weitergabe. Abruptes Absetzen → akinetische Krise. Transdermale Systeme erhalten. CYP2C19-Interaktionen gering."},
  "Valproat": {color:"green", text:"Weitergabe essenziell. TDM empfohlen. Bei Leberinsuffizienz kritisch. CYP2C9 relevant."},
  "Bisoprolol": {color:"green", text:"Weitergabe bei KHK, Tachyarrhythmie. Pause bei Sepsis oder Bradykardie erwägen. CYP2D6 relevant."},

  // ❌ Kontraindiziert
  "Metformin": {color:"red", text:"Absetzen: Risiko für Laktatazidose. Nur Insulin auf ITS."},
  "Ibuprofen": {color:"red", text:"Kontraindiziert: nephrotoxisch, gastrotoxisch, gerinnungshemmend. Paracetamol bevorzugt. CYP2C9 relevant."},
  "Simvastatin": {color:"red", text:"Pause bei Leberwertanstieg oder Rhabdomyolyse-Risiko. Re-Evaluation postoperativ. CYP3A4 relevant."},

  // ⚖️ Situativ
  "Ramipril": {color:"yellow", text:"Weitergabe bei Herzinsuffizienz. Pause bei Hypertonie als alleiniger Indikation oder Hypotonie."},
  "Haloperidol": {color:"yellow", text:"Weitergabe bei Psychose. Pause bei Delir oder QT-Verlängerung. CYP2D6/CYP3A4 relevant."},
  "Spironolacton": {color:"yellow", text:"Weitergabe bei Herzinsuffizienz. Hyperkaliämie-Risiko beachten. CYP3A4 relevant."}
};

// Autocomplete Logik
const input = document.getElementById("drugInput");
const suggestions = document.getElementById("suggestions");
const output = document.getElementById("output");

input.addEventListener("input", function() {
  const val = this.value.toLowerCase();
  suggestions.innerHTML = "";
  if (!val) return;
  Object.keys(data).forEach(drug => {
    if (drug.toLowerCase().includes(val)) {
      const div = document.createElement("div");
      div.textContent = drug;
      div.addEventListener("click", () => selectDrug(drug));
      suggestions.appendChild(div);
    }
  });
});

function selectDrug(drug) {
  input.value = drug;
  suggestions.innerHTML = "";
  const info = data[drug];
  output.className = "output " + info.color;
  output.innerHTML = `<div class="title">${drug}</div><div>${info.text}</div>`;
  output.style.display = "block";
}
</script>

</body>
</html>





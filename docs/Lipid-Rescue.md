# Lipid Rescue

---
## 💬 KURZ
- intravenöse Gabe einer fettemulgierten Lösung (z. B. Intralipid® 20 %)
- Therapie der systemischen [Lokalanaesthetika](Lokalanaesthetika.md)-Intoxikation ([LAST](LAST.md))
- bindet lipophile LA im Plasma („lipid sink“) und kann kardiotoxische Effekte abschwächen

---
## 💊 DOSIERUNG (nach DGAI-Leitlinie)

<details>
<summary>💉 Lipid Rescue Rechner (interaktiv)</summary>

<div style="border:1px solid #ccc; border-radius:8px; padding:1em; margin-top:1em; background:#f9f9f9; font-family:sans-serif; max-width:400px">
  <label for="kgInput">Körpergewicht (kg):</label><br>
  <input type="number" id="kgInput" value="80" style="width:100%; margin:0.5em 0; padding:0.3em"><br>

  <button onclick="calculateLipidRescue()" style="padding:0.5em; width:100%; background:#0078D4; color:white; border:none; border-radius:4px">Berechnen</button>

  <div id="lipidResult" style="margin-top:1em; font-size:0.9em; color:#333"></div>
</div>

<script>
function calculateLipidRescue() {
  const kg = parseFloat(document.getElementById("kgInput").value);
  if (isNaN(kg) || kg <= 0) return;

  const bolus = Math.round(1.5 * kg);
  const perfusor = Math.round(0.25 * kg * 30);
  const total = bolus + perfusor;

  document.getElementById("lipidResult").innerHTML = `
    <strong>Dosierung für ${kg} kg:</strong><br>
    • Initialbolus: <strong>${bolus} ml</strong><br>
    • Perfusor (30 min): <strong>${perfusor} ml</strong><br>
    • Gesamtmenge: <strong>${total} ml</strong>
  `;
}
</script>

</details>

- **Initialbolus:**  
  1,5 ml/kg *Intralipid*® 20 % i.v. über 1 min  
  → bei 80 kg: **120 ml Bolus**

- dann **Perfusor:**  
  0,25 ml/kg/min über 30–60 min  
  → bei 80 kg: **20 ml/min**<br>→ max. **400–500 ml gesamt**

- **Rebolus:**  
  bei persistierender Instabilität:  
  → bis zu **2 weitere Bolusgaben** möglich

---
## 🧭 HINWEISE
- Anwendung bei **kardialer oder refraktärer ZNS-Toxizität**  
- **Frühzeitig** beginnen – nicht als Ultima Ratio  
- **Reanimationsmaßnahmen** parallel fortführen  
- **Nicht mit Ringerlösungen mischen** ⚠️<br>→ Inkompatibilität!

---
<details>
<summary>🔤 Abkürzungen</summary>

| Kürzel | Bedeutung |
|--------|-----------|
| LA     | Lokalanästhetikum |
| LAST   | Local Anesthetic Systemic Toxicity |
| i.v.   | intravenös |
| ml/kg  | Milliliter pro Kilogramm Körpergewicht |

</details>

<details>
<summary>📚 Quellen</summary>

- [S1-Leitlinie: Prävention & Therapie der systemischen Lokalanästhetika-Intoxikation (DGAI, 2020)](https://www.ai-online.info/archiv/2020/06-2020/s1-leitlinie-praevention-therapie-der-systemischen-lokalanaesthetika-intoxikation-last-aktualisierte-handlungsempfehlungen-der-dgai.html)  
- [DocCheck Flexikon – Lokalanästhetika-Intoxikation](https://flexikon.doccheck.com/de/Lokalan%C3%A4sthetika-Intoxikation)  
- [UKGM SOP LA-Intoxikation (2016/17)](https://www.ukgm.de/ugm_2/deu/umr_ana/PDF/sop_la_intox_2016_17.pdf)  

</details>

<details>
<summary>🏷️ Tags</summary>

`#LipidRescue` `#LAST` `#Lokalanästhetika` `#Toxizität` `#Notfall` `#Intralipid` `#Dosierung` `#Kardiotoxizität` `#ZNS` `#Anästhesie`  

</details>

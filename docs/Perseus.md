# Perseus - Narkosegerät
*(Stand: 25.03.2026)*

---
## 🫁 GASE

### O₂ (Sauerstoff)
- **Normwerte:**
	→ FiO₂: Raumluft 0,21; klinisch meist 0,3–0,5 unter Narkose
	→ EtO₂: ca. 0,16–0,18 bei FiO₂ 0,21
- Differenz FiO₂–EtO₂:
	→ normal ≈ 0,03–0,05 = normale alveoläre Aufnahme
	→ wenn Unterschied kleiner (<0,02) → Shunt/Diffusionsstörung
	→ wenn Unterschied größer (>0,06) → hohe O₂-Aufnahme, z. B. bei Hypermetabolismus

> [!Beispiel]
> **Shunt-Schätzung:**
> FiO₂ 0,5 – EtO₂ 0,45 = 0,05 → normale Oxygenierung.
> FiO₂ 0,5 – EtO₂ 0,48 = 0,02 → Hinweis auf relevanten Shunt.

### CO₂ (Kohlendioxid)

| Parameter       | Normwert                     | Pathologie (Hinweis)                     |
|-----------------|-----------------------------|------------------------------------------|
| **EtCO₂**       | 35–45 mmHg (4,6–6,0 kPa)    | **>50 mmHg**: Hypoventilation/COPD       |
| **FiCO₂**       | ~0 mmHg                     | **>5 mmHg**: **Rebreathing** (Kalk wechseln!) |
| **EtCO₂-Abfall**| –                           | **>10 mmHg**: Kreislaufstillstand!       |

> [!warning]
> **Plötzlicher EtCO₂-Abfall?**
> 1. **Kreislauf prüfen** (Puls, RR).
> 2. **Beatmung kontrollieren** (Tubuslage, Leckage).
> 3. **Herzdruckmassage** vorbereiten.

### Narkosegase & MAC

| Narkosegas                  | MAC (40 Jahre, 1 atm) | MAC (70 Jahre)   |
| --------------------------- | --------------------- | ---------------- |
| [Sevofluran](Sevofluran.md) | 2,0 Vol%              | ~1,4 Vol% (–30%) |
| Desfluran                   | 6,0 Vol%              | ~4,2 Vol% (–30%) |
| Isofluran                   | 1,15 Vol%             | ~0,8 Vol% (–30%) |

> [!info]
> **Faustregel:**
> MAC sinkt um **~6% pro Dekade** nach dem 40. Lebensjahr.
> **Beispiel:**
> 70-jähriger Patient → MAC(Sevo) ≈ 2,0 × 0,7 = **1,4 Vol%**.

---
## 📈 KURVEN & VOLUMINA

### CO₂-Kurve (Kapnographie)
**Kurvenformen & Interpretation**

| Kurvenform             | Beschreibung                                     | Ursache                                                      |
| ---------------------- | ------------------------------------------------ | ------------------------------------------------------------ |
| **Normal**             | Flaches Plateau, schnelle Rückkehr zur Baseline. | Gesunde Lunge.                                               |
| **Haifischflosse**     | Langsamer Anstieg, verzögerter Abfall.           | **Bronchospasmus** (z. B. [Asthma](Asthma-Bronchiale.md)). |
| **Plötzlicher Abfall** | Abrupter Abfall auf 0.                           | ⚠️**Kreislaufstillstand** oder Tubusdislokation.             |

> [!tip]
> **Haifischflosse**
> **Maßnahmen:**
> 1. **Bronchodilatator** (z. B. Salbutamol) geben.
> 2. **Exspiration verlängern**

### Druckkurve
- Ppeak: <30 cmH₂O
- Pplat: <25 cmH₂O
- PEEP: 5–8 cmH₂O üblich
- Differenz Ppeak–Pplat = Resistance (indirekt)

### Flowkurve
- Exspiration vollständig → Flow kehrt zur Null-Linie zurück
- Restflow → Auto-PEEP
- Spontanatmung → unregelmäßige Flowmuster

### VT & MV
- VT: 6–8 ml/kg KG (ideales KG)
- MV: 5–8 l/min bei Erwachsenen
- Schwankungen → Spontanatmung oder Leckagen

> [!info]
> **Auto-PEEP**
> **Gefahr:**
> Auto-PEEP erhöht die **Nachlast des rechten Herzens**!
> **Lösung:**
> - **Exspirationszeit verlängern** (z. B. I:E = 1:3).
> - **PEEP reduzieren** (aber nicht unter 5 cmH₂O).

---
## 🧮 ERWEITERE PARAMETER

### Cdyn (dynamische Compliance)

**Formel:**
$$
C_{dyn} = \frac{V_T}{P_{peak} - PEEP}
$$

| Cdyn-Wert       | Interpretation                     | Beispiel (70 kg)                     |
|-----------------|-------------------------------------|--------------------------------------|
| **50–100 ml/cmH₂O** | Normal.                          | VT 500 ml, Ppeak 20 cmH₂O → Cdyn = 500/(20–5) = **33 ml/cmH₂O** (grenzwertig). |
| **<30 ml/cmH₂O**  | **Restriktive Pathologie** (ARDS, Ödem). | VT 400 ml, Ppeak 25 cmH₂O → Cdyn = 400/(25–5) = **20 ml/cmH₂O** (kritisch!). |

> [!tip]
> **Lagerungseffekt**
> **Bauchlagerung bei ARDS** (vor allem auf IT)
> - **Vorher**: Cdyn = 25 ml/cmH₂O.
> - **Nachher**: Cdyn = 45 ml/cmH₂O → **Bessere Oxygenierung!**

### MV × CO₂ (Ventilationseffizienz)

| Situation                          | MV × CO₂ (ml/min) | Interpretation                                                                    |
| ---------------------------------- | ----------------- | --------------------------------------------------------------------------------- |
| **Akute Lungenembolie**            | <150              | ⚠️ **Stark erniedrigt!** Perfusionsstörung → CO₂-Elimination ↓.                   |
| **schwere [COPD](COPD.md)**        | 100–200           | **Erniedrigt!** Hohe Totraumventilation → ineffiziente CO₂-Elimination.           |
| **in Ruhe (wach)**                 | 200–250           | Basale CO₂-Produktion ohne Stress.                                                |
| **Leichte Narkose**                | 250–300           | Leichte Stoffwechselsteigerung durch Anästhetika.                                 |
| **OP-Stress (Standard)**           | **300–400**       | **Normal unter Narkose!** Chirurgischer Stimulus → Sympathikusaktivierung → CO₂↑. |
| **Schwere [Sepsis](Sepsis.md)/MH** | >400 (bis >500)   | ⚠️ **Pathologisch!** Hypermetabolismus, Fieber, Schmerzen.                        |

### O₂-Uptake (VO₂)
**Sauerstoffverbrauch unter Narkose & OP-Stress**

**Formel:**
$$
VO_2 = (FiO_2 - EtO_2) \times MV
$$

| VO₂-Wert (70 kg)   | Interpretation                                                               | OP-Beispiel (MV = 6–8 l/min)                                                                           |
| ------------------ | ---------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------ |
| **<200 ml/min**    | **Erniedrigt** (tiefe Narkose, Hypothermie, Kreislaufdepression).            | Patient unter tiefer [Propofol](Propofol.md)-Narkose + Hypothermie (35°C): VO₂ = 180 ml/min.           |
| **250–300 ml/min** | **Normal in Ruhe** (wach, keine Belastung).                                  | Präoperativ                                                                                            |
| **300–400 ml/min** | **Normal unter Narkose!** Chirurgische Stimulation → Sympathikusaktivierung. | 65-jähriger Patient bei Laparotomie: VO₂ = 350 ml/min (FiO₂ 0,45 – EtO₂ 0,40 = 0,05 → 0,05 × 7 l/min). |
| **400–500 ml/min** | **Moderate Steigerung** (OP-Stress + leichte Hypothermie).                   | Patient in Ausleitungsphase mit Shivering: VO₂ = 450 ml/min.                                           |
| **>500 ml/min**    | **Pathologisch!** [Sepsis](Sepsis.md), MH, schwere Entzündungsreaktion.      | Sepsis-Patient mit Fieber 39°C: VO₂ = 550 ml/min (FiO₂ 0,5 – EtO₂ 0,35 = 0,15 → 0,15 × 8 l/min).       |

> [!tip] OP-Praxis
> - **300–400 ml/min sind unter Narkose normal!**
> - ⚠️ **Werte > 500 ml/min** (ohne Erklärung) sind **pathologisch**:
>   - **[Sepsis](Sepsis.md)?** → Laktat, CRP, Blutkultur.
>   - **[Maligne-Hyperthermie](Maligne-Hyperthermie.md)?** → Temperatur, CK, Kalium.
>   - **Übermäßige Stimulation?** → Narkosetiefe prüfen (BIS, klinische Zeichen).

### ΔVT (Delta Tidalvolumen)
**Atemvariabilität & Narkosetiefe**

| ΔVT-Wert        | Interpretation                     | Klinische Relevanz                     |
|-----------------|-------------------------------------|----------------------------------------|
| **10–20%**      | Normale Spontanatmung.              | –                                      |
| **<5%**         | **Tiefe Sedierung/Relaxation**.     | Extubation erst bei ΔVT >15%!          |
| **>30%**        | **Aktiver Atemantrieb** (Schmerz, zu flache Narkose). | **Narkose vertiefen** oder Analgesie geben. |

> [!info]
> **Ausleitung**
> **ΔVT steigt von 5% auf 20%?**
> → **Spontanatmung kehrt zurück**
> → Extubation vorbereiten

---

<details>
  <summary>🩺 Praxisbeispiele</summary>
  <div>
    <h4>1. COPD-Patient (GOLD III) unter Narkose</h4>
    <ul>
      <li><strong>Szenario:</strong> 68-jähriger Mann, Leistenhernien-OP, GOLD III, BMI 28</li>
      <li><strong>Monitoring:</strong>
        <ul>
          <li>EtCO₂: 52 mmHg (↑) → <strong>CO₂-Retention</strong> durch Obstruktion</li>
          <li>MV × CO₂: 180 ml/min (↓) → <strong>Totraumventilation ~75%</strong></li>
          <li>ΔVT: 35% → <strong>unregelmäßige Spontanatmung</strong> gegen Beatmung</li>
          <li>Flowkurve: Restflow → <strong>Auto-PEEP (5 cmH₂O)</strong></li>
        </ul>
      </li>
      <li><strong>Maßnahmen:</strong>
        <ul>
          <li>VT reduzieren (von 8 auf 6 ml/kg)</li>
          <li>PEEP auf 8 cmH₂O (über Auto-PEEP)</li>
          <li>Exspirationszeit verlängern (I:E = 1:3)</li>
          <li>Bronchodilatator (Salbutamol 2 Hübe über Tubus)</li>
        </ul>
      </li>
    </ul>

    <h4>2. Narkoseausleitung nach Laparoskopie</h4>
    <ul>
      <li><strong>Szenario:</strong> 45-jährige Frau, postop. Ausleitung</li>
      <li><strong>Verlauf:</strong>
        <table>
          <tr><th>Zeit</th><th>EtO₂</th><th>ΔVT</th><th>EtCO₂</th><th>Interpretation</th></tr>
          <tr><td>0 min</td><td>0,30</td><td>5%</td><td>42 mmHg</td><td>Tiefe Narkose</td></tr>
          <tr><td>3 min</td><td>0,36</td><td>12%</td><td>40 mmHg</td><td><strong>Wash-out der Narkosegase</strong></td></tr>
          <tr><td>7 min</td><td>0,42</td><td>22%</td><td>36 mmHg</td><td><strong>Spontanatmung kehrt zurück</strong> → Extubation vorbereiten</td></tr>
        </table>
      </li>
      <li><strong>Achtung:</strong>
        <ul>
          <li>Plötzlicher EtCO₂-Abfall → <strong>Laryngospasmus-Risiko!</strong></li>
          <li>ΔVT > 25% + regelmäßige Atemzüge → <strong>Extubationskriterien erfüllt</strong></li>
        </ul>
      </li>
    </ul>

    <h4>3. Lagerungseffekte: Bauchlagerung bei ARDS</h4>
    <ul>
      <li><strong>Szenario:</strong> 55-jähriger Mann, ARDS (PaO₂/FiO₂ 150), Bauchlagerung</li>
      <li><strong>Vorher/Nachher:</strong>
        <table>
          <tr><th>Parameter</th><th>Vorher</th><th>Nachher</th><th>Interpretation</th></tr>
          <tr><td>Cdyn</td><td>28 ml/cmH₂O</td><td>42 ml/cmH₂O</td><td><strong>Bessere Compliance</strong></td></tr>
          <tr><td>FiO₂–EtO₂</td><td>0,12</td><td>0,07</td><td><strong>Reduzierter Shunt</strong></td></tr>
          <tr><td>O₂-Uptake</td><td>220 ml/min</td><td>280 ml/min</td><td><strong>Verbesserte Oxygenierung</strong></td></tr>
        </table>
      </li>
      <li><strong>Klinische Konsequenz:</strong>
        <ul>
          <li>PEEP beibehalten (10 cmH₂O)</li>
          <li>FiO₂ reduzieren (von 0,8 auf 0,6 möglich)</li>
        </ul>
      </li>
    </ul>

    <h4>4. Herzinsuffizienz (NYHA III) mit Lungenödem</h4>
    <ul>
      <li><strong>Szenario:</strong> 72-jähriger Mann, dekompensierte Herzinsuffizienz, Lungenödem</li>
      <li><strong>Monitoring:</strong>
        <table>
          <tr><th>Parameter</th><th>Wert</th><th>Interpretation</th><th>Maßnahme</th></tr>
          <tr><td>Cdyn</td><td>22 ml/cmH₂O</td><td><strong>Lungenstauung</strong> (Compliance ↓)</td><td><strong>Diurese</strong> (Furosemid 40 mg i.v.)</td></tr>
          <tr><td>FiO₂–EtO₂</td><td>0,09</td><td><strong>Shunt durch Ödem</strong></td><td><strong>PEEP auf 10 cmH₂O</strong></td></tr>
          <tr><td>EtCO₂</td><td>32 mmHg</td><td><strong>Hyperventilation</strong> (Dyspnoe)</td><td><strong>VT auf 6 ml/kg</strong> reduzieren</td></tr>
          <tr><td>Pplat</td><td>28 cmH₂O</td><td><strong>Grenzwertig</strong> (Barotrauma-Risiko)</td><td><strong>Drücke <30 cmH₂O</strong> halten</td></tr>
        </table>
      </li>
      <li><strong>Warnung:</strong>
        <ul>
          <li>Hoher PEEP kann <strong>Vorlast des rechten Herzens</strong> erhöhen!</li>
          <li><strong>Lösung:</strong> PEEP schrittweise auf 8–10 cmH₂O titrieren + <strong>Dobutamin</strong> bei Hypotonie.</li>
        </ul>
      </li>
    </ul>

    <h4>5. Sepsis-Patient mit Hypermetabolismus</h4>
    <ul>
      <li><strong>Szenario:</strong> 58-jähriger Mann, Sepsis (Laktat 3,2 mmol/l), Fieber 39,2°C</li>
      <li><strong>Monitoring:</strong>
        <table>
          <tr><th>Parameter</th><th>Wert</th><th>Interpretation</th></tr>
          <tr><td>VO₂</td><td>520 ml/min</td><td><strong>Hypermetabolismus</strong> (Sepsis)</td></tr>
          <tr><td>MV × CO₂</td><td>480 ml/min</td><td><strong>Erhöhte CO₂-Produktion</strong></td></tr>
          <tr><td>Cdyn</td><td>30 ml/cmH₂O</td><td><strong>Lunge steif</strong> (beginnendes ARDS?)</td></tr>
        </table>
      </li>
      <li><strong>Maßnahmen:</strong>
        <ol>
          <li>MV auf 10 l/min erhöhen (aber <strong>Ppeak <30 cmH₂O</strong>!)</li>
          <li>Sedierung vertiefen (Propofol + Fentanyl)</li>
          <li>Kühlung (Zieltemperatur 36,5°C)</li>
          <li>Antibiotika (nach Blutkultur)</li>
          <li>Volumenmanagement (ZVD-Ziel: 8–12 mmHg)</li>
        </ol>
      </li>
    </ul>
  </div>
</details>

---
<details>
<summary>🔤 Abkürzungen</summary>
<div>
  <table>
    <thead>
      <tr>
        <th style="width: 120px;">Abkürzung</th>
        <th>Bedeutung</th>
      </tr>
    </thead>
    <tbody>
      <tr><td>ARDS</td><td>Acute Respiratory Distress Syndrome</td></tr>
      <tr><td>BGA</td><td>Blutgasanalyse</td></tr>
      <tr><td>BIS</td><td>Bispektraler Index (Narkosetiefe)</td></tr>
      <tr><td>Cdyn</td><td>Dynamische Compliance</td></tr>
      <tr><td>CK</td><td>Kreatinkinase (MH-Marker)</td></tr>
      <tr><td>COPD</td><td>Chronic Obstructive Pulmonary Disease</td></tr>
      <tr><td>CRP</td><td>C-reaktives Protein</td></tr>
      <tr><td>ΔVT</td><td>Delta Tidalvolumen (Variabilität)</td></tr>
      <tr><td>EtCO₂</td><td>Endexspiratorisches CO₂</td></tr>
      <tr><td>EtO₂</td><td>Exspiratorische Sauerstofffraktion</td></tr>
      <tr><td>FiCO₂</td><td>Inspiratorisches Kohlendioxid</td></tr>
      <tr><td>FiO₂</td><td>Inspiratorische Sauerstofffraktion</td></tr>
      <tr><td>GOLD</td><td>Global Initiative for Chronic Obstructive Lung Disease (COPD-Klassifikation)</td></tr>
      <tr><td>I:E</td><td>Inspirations-Exspirations-Verhältnis</td></tr>
      <tr><td>IT</td><td>Intensivstation</td></tr>
      <tr><td>MAC</td><td>Minimale alveoläre Konzentration</td></tr>
      <tr><td>MH</td><td>Maligne Hyperthermie</td></tr>
      <tr><td>MV</td><td>Atemminutenvolumen</td></tr>
      <tr><td>MV × CO₂</td><td>Ventilationseffizienz (CO₂-Elimination)</td></tr>
      <tr><td>NYHA</td><td>New York Heart Association (Herzinsuffizienz-Klassifikation)</td></tr>
      <tr><td>O₂-Uptake</td><td>Sauerstoffaufnahme (VO₂)</td></tr>
      <tr><td>OP</td><td>Operation / Operationssaal</td></tr>
      <tr><td>PAOP</td><td>Pulmonalarterienokklusionsdruck</td></tr>
      <tr><td>PEEP</td><td>Positive Endexpiratory Pressure</td></tr>
      <tr><td>Pplat</td><td>Plateaudruck</td></tr>
      <tr><td>Ppeak</td><td>Spitzendruck</td></tr>
      <tr><td>ScvO₂</td><td>Zentrale Venensättigung</td></tr>
      <tr><td>ZVD</td><td>Zentraler Venendruck</td></tr>
    </tbody>
  </table>
  <style>
    details table {
      width: 100%;
      border-collapse: collapse;
      margin: 1em 0;
    }
    details th, details td {
      border: 1px solid #ddd;
      padding: 8px;
      text-align: left;
    }
    details th {
      background-color: #f2f2f2;
    }
    details tr:nth-child(even) {
      background-color: #f9f9f9;
    }
  </style>
</div>
</details>

<details>
<summary>📚 Quellen</summary>
<div>
  <ul>
    <li><strong>Dräger Perseus A500</strong> – <em>Technical Manual & Clinical Guide</em> (2023)
      <ul><li>Praktische Beatmungsstrategien unter Narkose</li></ul>
    </li>
    <li><strong>Gattinoni L, Marini JJ</strong> – <em>ARDS: Mechanics and Gas Exchange</em>, <em>Intensive Care Med</em> (2020)
      <ul><li>Lagerungstherapie & Compliance-Optimierung</li></ul>
    </li>
    <li><strong>Miller RD</strong> – <em>Miller’s Anesthesia</em>, 9th Edition (2020)
      <ul><li>Standardwerk für Narkoseführung & Beatmungsmanagement</li></ul>
    </li>
    <li><strong>Nunn JF</strong> – <em>Applied Respiratory Physiology</em>, 8th Edition (2022)
      <ul><li>Grundlagen der Atemphysiologie</li></ul>
    </li>
    <li><strong>West JB</strong> – <em>Respiratory Physiology: The Essentials</em>, 10th Edition (2021)
      <ul><li>O₂/CO₂-Austausch & Shunt-Physiologie</li></ul>
    </li>
    <li><strong>Eger EI et al.</strong> – <em>MAC and Anesthetic Potency</em>, <em>Anesth Analg</em> (2019)
      <ul><li>Altersabhängige MAC-Werte</li></ul>
    </li>
  </ul>
</div>
</details>

<details>
<summary>🏷️ Tags</summary>
<div>
  <ul>
    <li>Anästhesie</li>
    <li>Narkosegerät</li>
    <li>Beatmung</li>
    <li>Dräger Perseus</li>
    <li>Monitoring</li>
    <li>Physiologie</li>
    <li>Intensivmedizin</li>
    <li>Operation</li>
    <li>Atemmechanik</li>
    <li>ARDS</li>
    <li>COPD</li>
    <li>Sepsis</li>
    <li>Herzinsuffizienz</li>
    <li>Lungenödem</li>
  </ul>
</div>
</details>
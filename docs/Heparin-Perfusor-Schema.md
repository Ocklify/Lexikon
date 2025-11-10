<!DOCTYPE html>
<html lang="de">
<head>
  <meta charset="UTF-8">
  <title>Perfusor-Schema</title>
</head>
<body>
  <label for="targetRange"><strong>Zielbereich wählen:</strong></label>
  <select id="targetRange">
    <option value="">– bitte wählen –</option>
    <option value="range1">40–60 s</option>
    <option value="range2">50–70 s</option>
    <option value="range3">60–80 s</option>
  </select>

  <!-- Tabellen -->
  <div id="range1" class="schema" style="display:none">
    <h3>🩺 Zielbereich: 40–60 s</h3>
    <table border="1">
      <thead><tr><th>aPTT (s)</th><th>Maßnahme</th><th>Kontrolle</th></tr></thead>
      <tbody>
        <tr><td>&lt;40</td><td>+20 % Dosis</td><td>6 h</td></tr>
        <tr><td>40–60</td><td>keine Änderung</td><td>12 h</td></tr>
        <tr><td>61–75</td><td>–10 % Dosis</td><td>6 h</td></tr>
        <tr><td>76–90</td><td>Infusion 1 h pausieren, dann –20 %</td><td>6 h</td></tr>
        <tr><td>&gt;90</td><td>Infusion 2 h pausieren, dann –30 %</td><td>6 h</td></tr>
      </tbody>
    </table>
  </div>

  <div id="range2" class="schema" style="display:none">
    <h3>🩺 Zielbereich: 50–70 s</h3>
    <table border="1">
      <thead><tr><th>aPTT (s)</th><th>Maßnahme</th><th>Kontrolle</th></tr></thead>
      <tbody>
        <tr><td>&lt;45</td><td>+20 % Dosis</td><td>6 h</td></tr>
        <tr><td>45–50</td><td>+10 % Dosis</td><td>6 h</td></tr>
        <tr><td>51–70</td><td>keine Änderung</td><td>12 h</td></tr>
        <tr><td>71–85</td><td>–10 % Dosis</td><td>6 h</td></tr>
        <tr><td>86–100</td><td>Infusion 1 h pausieren, dann –20 %</td><td>6 h</td></tr>
        <tr><td>&gt;100</td><td>Infusion 2 h pausieren, dann –30 %</td><td>6 h</td></tr>
      </tbody>
    </table>
  </div>

  <div id="range3" class="schema" style="display:none">
    <h3>🩺 Zielbereich: 60–80 s</h3>
    <table border="1">
      <thead><tr><th>aPTT (s)</th><th>Maßnahme</th><th>Kontrolle</th></tr></thead>
      <tbody>
        <tr><td>&lt;50</td><td>+20 % Dosis</td><td>6 h</td></tr>
        <tr><td>50–59</td><td>+10 % Dosis</td><td>6 h</td></tr>
        <tr><td>60–80</td><td>keine Änderung</td><td>12 h</td></tr>
        <tr><td>81–95</td><td>–10 % Dosis</td><td>6 h</td></tr>
        <tr><td>96–110</td><td>Infusion 1 h pausieren, dann –20 %</td><td>6 h</td></tr>
        <tr><td>&gt;110</td><td>Infusion 2 h pausieren, dann –30 %</td><td>6 h</td></tr>
      </tbody>
    </table>
  </div>

  <script>
  function updateSchema() {
    const value = document.getElementById("targetRange").value;
    document.querySelectorAll(".schema").forEach(el => el.style.display = "none");
    if (value) {
      document.getElementById(value).style.display = "block";
    }
  }
  document.getElementById("targetRange").addEventListener("change", updateSchema);
  updateSchema(); // initialer Aufruf
  </script>

  <hr>

  <!-- Zusatzinfos -->
  <details>
    <summary>🔤 Abkürzungen</summary>
    <table>
      <thead>
        <tr><th>Abkürzung</th><th>Bedeutung</th></tr>
      </thead>
      <tbody>
        <tr><td>aPTT</td><td>aktivierte partielle Thromboplastinzeit</td></tr>
        <tr><td>IE</td><td>Internationale Einheiten</td></tr>
        <tr><td>UFH</td><td>unfraktioniertes Heparin</td></tr>
      </tbody>
    </table>
  </details>

  <details>
    <summary>📚 Quellen</summary>
    <ul>
      <li><a href="https://www2.medizin.uni-greifswald.de/transfus/fileadmin/user_upload/Gerinnung/Dokumente_Gerinnung/41dosierschema_heparin.pdf" target="_blank">Greifswald-Schema – Universitätsmedizin Greifswald (PDF)</a></li>
      <li>Hirsh J, Raschke R. <em>Heparin and low-molecular-weight heparin: mechanisms of action, pharmacokinetics, dosing, monitoring, efficacy, and safety.</em> Chest. 2004;126(3):188S–203S.</li>
      <li>AWMF S2k-Leitlinie: „Antikoagulation bei internistischen Erkrankungen“ (2021)</li>
      <li><a href="https://www.notfallguru.de/leitsymptome/perfusoren/heparinperfusor" target="_blank">Notfallguru – Heparin-Perfusor Schema</a></li>
      <li><a href="https://high-dose.net/pages/heparin.html" target="_blank">High-Dose.net – Schockraum-Checkliste</a></li>
      <li><a href="https://anae-doc.de/heparin-antikoagulation-auf-intensivstation/" target="_blank">Anae-doc.de – Heparin auf Intensivstation</a></li>
    </ul>
  </details>

  <details>
    <summary>🏷️ Tags</summary>
    <p>#Heparin #Antikoagulation #aPTT #Notfallmedizin #Intensivmedizin #Pharmakotherapie #UFH #Perfusor #ITS</p>
  </details>

</body>
</html>

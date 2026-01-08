from pathlib import Path
import mkdocs_gen_files

def format_title(filename):
    raw = Path(filename).stem.replace("-", " ").replace("_", " ")
    if raw.isupper():
        return raw
    return " ".join(word.capitalize() for word in raw.split())

# Alle Markdown-Dateien unter docs/ sammeln
files = sorted(Path("docs").rglob("*.md"))

entries = []
for path in files:
    if path.name in ["index.md", "index_all.md"]:
        continue
    if path.is_file() and path.suffix == ".md":
        rel_path = path.relative_to("docs")
        title = format_title(path.name)
        entries.append((title, rel_path.as_posix()))

# Alphabetisch sortieren
entries = sorted(entries, key=lambda x: x[0].lower())

# In drei Spalten blockweise aufteilen
total = len(entries)
chunk_size = (total + 2) // 3
columns = [
    entries[0:chunk_size],
    entries[chunk_size:2*chunk_size],
    entries[2*chunk_size:]
]

# HTML-Grid erzeugen mit Markdown-Unterstützung
with mkdocs_gen_files.open("index_all.md", "w") as f:
    f.write("# Lexikon-Index\n\n")
    f.write('<div class="grid-3" markdown="1">\n\n')
    for col in columns:
        f.write('<div markdown="1">\n')
        for title, link in col:
            f.write(f"- [{title}]({link})\n")
        f.write("</div>\n\n")
    f.write("</div>\n")

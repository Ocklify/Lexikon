from pathlib import Path
import mkdocs_gen_files

# Alle Markdown-Dateien im docs/-Ordner sammeln
files = sorted(Path("docs").rglob("*.md"))

with mkdocs_gen_files.open("index_all.md", "w") as f:
    f.write("# Automatischer Index\n\n")
    for path in files:
        if path.name in ["index.md", "index_all.md"]:
            continue
        title = path.stem
        rel_path = path.relative_to("docs")
        f.write(f"- [{title}]({rel_path.as_posix()})\n")

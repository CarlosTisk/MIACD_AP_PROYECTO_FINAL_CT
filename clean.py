import json
from copy import deepcopy

in_path = "MIACD_AP_PROYECTO_FINAL.ipynb"
out_path = "MIACD_AP_PROYECTO_FINAL_clean.ipynb"

with open(in_path, "r", encoding="utf-8") as f:
    nb = json.load(f)

nb_clean = deepcopy(nb)

# Quitar metadata de widgets a nivel notebook
nb_clean.setdefault("metadata", {})
nb_clean["metadata"].pop("widgets", None)

# Limpiar outputs y posibles restos de widgets por celda
for cell in nb_clean.get("cells", []):
    if cell.get("cell_type") == "code":
        cell["outputs"] = []
        cell["execution_count"] = None
        if "metadata" in cell:
            cell["metadata"].pop("widgets", None)
            if "jupyter" in cell["metadata"]:
                cell["metadata"]["jupyter"].pop("outputs_hidden", None)
                cell["metadata"]["jupyter"].pop("source_hidden", None)

# Asegurar nbformat consistente
nb_clean["nbformat"] = nb.get("nbformat", 4)
nb_clean["nbformat_minor"] = max(nb.get("nbformat_minor", 0), 5)

with open(out_path, "w", encoding="utf-8") as f:
    json.dump(nb_clean, f, ensure_ascii=False, indent=1)

print("Listo:", out_path)

"""Build the game: inline the sprites into one self-contained HTML file.
Outputs:
  dist/wizard-grove.html  page body only (for publishing as a Claude artifact)
  index.html              full standalone page (open in any phone browser)
"""
import base64, pathlib
root = pathlib.Path(__file__).parent
def uri(name):
    return "data:image/png;base64," + base64.b64encode((root / "assets" / name).read_bytes()).decode()
src = (root / "src" / "game.html").read_text()
body = src.replace("__WIZARD__", uri("wizard.png")).replace("__GRASS__", uri("grass.png")).replace("__WIZARD_FIST__", uri("wizard_nostaff.png"))
(root / "dist").mkdir(exist_ok=True)
(root / "dist" / "wizard-grove.html").write_text(body)
head = '<!doctype html>\n<html lang="en">\n<head>\n<meta charset="utf-8">\n<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover, user-scalable=no">\n<meta name="apple-mobile-web-app-capable" content="yes">\n'
(root / "index.html").write_text(head + body.replace("<canvas", "</head>\n<body>\n<canvas", 1) + "\n</body>\n</html>\n")
print("built")

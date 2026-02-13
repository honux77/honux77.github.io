"""Build script: renders Jinja2 templates with YAML data into _site/."""

import shutil
import sys
from pathlib import Path

import yaml
from jinja2 import Environment, FileSystemLoader

ROOT = Path(__file__).resolve().parent
SITE_DIR = ROOT / "_site"
DATA_FILE = ROOT / "data" / "site.yaml"
TEMPLATE_DIR = ROOT / "templates"


def main():
    print("🚀 Starting build...")

    if not DATA_FILE.exists():
        print(f"❌ Error: {DATA_FILE} not found")
        sys.exit(1)

    if not TEMPLATE_DIR.exists():
        print(f"❌ Error: {TEMPLATE_DIR} not found")
        sys.exit(1)

    print(f"📄 Loading data from {DATA_FILE.name}")
    with open(DATA_FILE, encoding="utf-8") as f:
        data = yaml.safe_load(f)

    sections = ["site", "hero", "nav", "profile", "projects", "blogs", "support", "footer"]
    for section in sections:
        status = "✅" if section in data else "⚠️"
        print(f"  {status} {section}")

    print(f"🎨 Rendering template")
    env = Environment(
        loader=FileSystemLoader(TEMPLATE_DIR),
        autoescape=True,
    )
    template = env.get_template("index.html")
    html = template.render(**data)

    print(f"📁 Preparing {SITE_DIR.name}/")
    if SITE_DIR.exists():
        shutil.rmtree(SITE_DIR)
    SITE_DIR.mkdir()

    print(f"💾 Writing index.html ({len(html)} bytes)")
    (SITE_DIR / "index.html").write_text(html, encoding="utf-8")

    print(f"📦 Copying static assets")
    for asset_dir in ("css", "js"):
        src = ROOT / asset_dir
        if src.exists():
            shutil.copytree(src, SITE_DIR / asset_dir)
            file_count = sum(1 for _ in (SITE_DIR / asset_dir).rglob("*") if _.is_file())
            print(f"  ✅ {asset_dir}/ ({file_count} files)")
        else:
            print(f"  ⚠️  {asset_dir}/ (not found)")

    (SITE_DIR / ".nojekyll").write_text("")
    print(f"  ✅ .nojekyll")

    print(f"✨ Build complete → {SITE_DIR}")


if __name__ == "__main__":
    main()

"""Build script: renders Jinja2 templates with YAML data into _site/."""

import shutil
from pathlib import Path

import yaml
from jinja2 import Environment, FileSystemLoader

ROOT = Path(__file__).resolve().parent
SITE_DIR = ROOT / "_site"


def main():
    # Load data
    with open(ROOT / "data" / "site.yaml", encoding="utf-8") as f:
        data = yaml.safe_load(f)

    # Render template
    env = Environment(
        loader=FileSystemLoader(ROOT / "templates"),
        autoescape=True,
    )
    template = env.get_template("index.html")
    html = template.render(**data)

    # Prepare _site
    if SITE_DIR.exists():
        shutil.rmtree(SITE_DIR)
    SITE_DIR.mkdir()

    # Write rendered HTML
    (SITE_DIR / "index.html").write_text(html, encoding="utf-8")

    # Copy static assets
    for asset_dir in ("css", "js"):
        src = ROOT / asset_dir
        if src.exists():
            shutil.copytree(src, SITE_DIR / asset_dir)

    # .nojekyll for GitHub Pages
    (SITE_DIR / ".nojekyll").write_text("")

    print(f"Build complete → {SITE_DIR}")


if __name__ == "__main__":
    main()

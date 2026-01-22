import argparse
import re
from pathlib import Path

IMAGE_EXTS = {".jpg", ".jpeg", ".png", ".gif", ".webp"}
KEY_ORDER = ("src", "size", "alt")


def strip_quotes(value):
    if len(value) >= 2 and value[0] == value[-1] and value[0] in ("\"", "'"):
        return value[1:-1]
    return value


def yaml_value(value):
    if value == "":
        return "\"\""
    needs_quotes = bool(
        re.search(r"[\n\r\t:#]", value)
        or value.startswith((" ", "-", "?", ":", "@", "&", "*", "!", "|", ">", "'", "\""))
        or value.endswith(" ")
    )
    if not needs_quotes:
        return value
    escaped = value.replace("\"", "\\\"")
    return f"\"{escaped}\""


def parse_gallery_yaml(text):
    items = []
    current = None
    for raw_line in text.splitlines():
        line = raw_line.strip()
        if not line or line.startswith("#"):
            continue
        if line.startswith("- "):
            match = re.match(r"-\s*src:\s*(.+)", line)
            if match:
                if current:
                    items.append(current)
                src = strip_quotes(match.group(1).strip())
                current = {"src": src}
            else:
                current = None
            continue
        if current and ":" in line:
            key, value = line.split(":", 1)
            key = key.strip()
            value = strip_quotes(value.strip())
            if value != "":
                current[key] = value
    if current:
        items.append(current)
    return items


def parse_gallery_page(text):
    items = []
    pattern = re.compile(
        r"<figure class=\"([^\"]*gallery-tile[^\"]*)\"[^>]*>\\s*"
        r"<a class=\"gallery-link\" href=\"([^\"]+)\"",
        re.IGNORECASE,
    )
    for classes, href in pattern.findall(text):
        item = {"src": href}
        if "gallery-tile--hero" in classes:
            item["size"] = "hero"
        elif "gallery-tile--wide" in classes:
            item["size"] = "wide"
        items.append(item)
    return items


def load_existing_items(data_path, page_path):
    if data_path.exists():
        return parse_gallery_yaml(data_path.read_text(encoding="utf-8"))
    if page_path.exists():
        return parse_gallery_page(page_path.read_text(encoding="utf-8"))
    return []


def gather_gallery_images(root, gallery_dir):
    if not gallery_dir.exists():
        gallery_dir.mkdir(parents=True, exist_ok=True)
        return []
    files = []
    for path in gallery_dir.rglob("*"):
        if path.is_file() and path.suffix.lower() in IMAGE_EXTS:
            files.append(path)
    return ["/" + path.relative_to(root).as_posix() for path in sorted(files)]


def normalize_src(src):
    return src.casefold()


def merge_items(existing_items, new_srcs, prepend=False):
    managed_prefix = "/wp-content/uploads/gallery/"
    new_srcs_lookup = {normalize_src(src): src for src in new_srcs}
    kept_items = []
    existing_srcs = set()
    for item in existing_items:
        src = item.get("src")
        if not src:
            continue
        src_key = normalize_src(src)
        if src.startswith(managed_prefix):
            if src_key in new_srcs_lookup:
                kept_items.append(item)
                existing_srcs.add(src_key)
            continue
        kept_items.append(item)
        existing_srcs.add(src_key)
    additions = [
        {"src": new_srcs_lookup[normalize_src(src)]}
        for src in new_srcs
        if normalize_src(src) not in existing_srcs
    ]
    if not additions:
        return kept_items
    if prepend:
        return additions + kept_items
    return kept_items + additions


def dump_yaml(items):
    lines = []
    for item in items:
        src = item.get("src")
        if not src:
            continue
        lines.append(f"- src: {yaml_value(src)}")
        for key in KEY_ORDER[1:]:
            if key in item:
                lines.append(f"  {key}: {yaml_value(item[key])}")
        extra_keys = [key for key in item.keys() if key not in KEY_ORDER]
        for key in sorted(extra_keys):
            lines.append(f"  {key}: {yaml_value(item[key])}")
    lines.append("")
    return "\n".join(lines)


def main():
    parser = argparse.ArgumentParser(
        description="Update the gallery data file using images from wp-content/uploads/gallery."
    )
    parser.add_argument("--prepend", action="store_true", help="Add new images to the top.")
    parser.add_argument("--data-file", default="_data/gallery.yml")
    parser.add_argument("--page-file", default="pages/gallery.md")
    parser.add_argument("--gallery-dir", default="wp-content/uploads/gallery")
    args = parser.parse_args()

    root = Path(__file__).resolve().parents[1]
    data_path = root / args.data_file
    page_path = root / args.page_file
    gallery_dir = root / args.gallery_dir

    existing_items = load_existing_items(data_path, page_path)
    new_srcs = gather_gallery_images(root, gallery_dir)
    merged_items = merge_items(existing_items, new_srcs, prepend=args.prepend)

    data_path.parent.mkdir(parents=True, exist_ok=True)
    data_path.write_text(dump_yaml(merged_items), encoding="utf-8")


if __name__ == "__main__":
    raise SystemExit(main())

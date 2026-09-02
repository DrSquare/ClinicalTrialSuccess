"""Convert the local clinical trial success PDF to page-traced Markdown."""

from __future__ import annotations

import re
from pathlib import Path

from pypdf import PdfReader


PDF_PATH = Path("Dynamic Clinical Trial Success Rates for Drugs in the 21st Century.pdf")
MARKDOWN_PATH = Path("Dynamic Clinical Trial Success Rates for Drugs in the 21st Century.md")


def clean_text(text: str) -> str:
    replacements = {
        "\ufb01": "fi",
        "\ufb02": "fl",
        "\u2013": "-",
        "\u2014": "-",
        "\u2212": "-",
        "\u00a0": " ",
    }
    for source, target in replacements.items():
        text = text.replace(source, target)
    text = text.replace("\r", "")
    text = re.sub(r" +", " ", text)
    text = re.sub(r"\n{3,}", "\n\n", text)
    return text.strip()


def main() -> None:
    reader = PdfReader(str(PDF_PATH))
    metadata = dict(reader.metadata or {})
    title = str(metadata.get("/Title") or PDF_PATH.stem)
    author = metadata.get("/Author")

    lines: list[str] = [
        "---",
        f'title: "{title.replace(chr(34), chr(39))}"',
        f'source_pdf: "{PDF_PATH.name}"',
        'doi: "10.1038/s41467-025-64552-2"',
        'article_url: "https://doi.org/10.1038/s41467-025-64552-2"',
        f"pages: {len(reader.pages)}",
    ]
    if author:
        lines.append(f'authors: "{str(author).replace(chr(34), chr(39))}"')
    lines.extend(
        [
            "generated_from_local_pdf: true",
            "---",
            "",
            f"# {title}",
            "",
            "> Text extracted from the local PDF in this repository. Page breaks are preserved as second-level headings for traceability.",
        ]
    )

    for page_number, page in enumerate(reader.pages, start=1):
        lines.extend(
            [
                "",
                f"## Page {page_number}",
                "",
                clean_text(page.extract_text() or ""),
            ]
        )

    MARKDOWN_PATH.write_text("\n".join(lines).rstrip() + "\n", encoding="utf-8")
    print(MARKDOWN_PATH.resolve())
    print(f"pages={len(reader.pages)} bytes={MARKDOWN_PATH.stat().st_size}")


if __name__ == "__main__":
    main()

from pathlib import Path

from pypdf import PdfReader, PdfWriter


COVER_LETTER = Path("public/daniel-morgan-cover-letter-fe-fundinfo.pdf")
CV = Path("public/daniel-morgan-cv-fe-fundinfo.pdf")
OUTPUT = Path("public/daniel-morgan-application-fe-fundinfo.pdf")


def main() -> None:
    writer = PdfWriter()

    for source in (COVER_LETTER, CV):
        reader = PdfReader(source)
        for page in reader.pages:
            writer.add_page(page)

    writer.add_metadata(
        {
            "/Title": "Daniel Morgan - Application for AI Product Builder",
            "/Author": "Daniel Morgan",
            "/Subject": "Cover letter and CV for FE fundinfo",
        }
    )

    with OUTPUT.open("wb") as output_file:
        writer.write(output_file)

    print(OUTPUT)


if __name__ == "__main__":
    main()

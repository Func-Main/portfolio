from pathlib import Path

from reportlab.lib.colors import HexColor
from reportlab.lib.enums import TA_LEFT
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import ParagraphStyle
from reportlab.lib.units import mm
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.pdfbase import pdfmetrics
from reportlab.platypus import Paragraph, SimpleDocTemplate, Spacer


OUTPUT = Path("public/daniel-morgan-cover-letter-luma.pdf")
INK = HexColor("#151515")
MUTED = HexColor("#555555")
LINK = HexColor("#2456A6")


def main() -> None:
    pdf = SimpleDocTemplate(
        str(OUTPUT),
        pagesize=A4,
        rightMargin=27 * mm,
        leftMargin=27 * mm,
        topMargin=24 * mm,
        bottomMargin=24 * mm,
        title="Daniel Morgan - Cover Letter for Luma",
        author="Daniel Morgan",
        subject="Application for Creative Technologist at Luma",
    )

    body = ParagraphStyle(
        "Body",
        fontName="Helvetica",
        fontSize=10.5,
        leading=16,
        textColor=INK,
        alignment=TA_LEFT,
        spaceAfter=11,
    )
    name = ParagraphStyle(
        "Name",
        parent=body,
        fontName="Helvetica-Bold",
        fontSize=22,
        leading=26,
        spaceAfter=3,
    )
    contact = ParagraphStyle(
        "Contact",
        parent=body,
        fontSize=9,
        leading=12,
        textColor=MUTED,
        spaceAfter=24,
    )
    greeting = ParagraphStyle(
        "Greeting",
        parent=body,
        fontName="Helvetica-Bold",
        spaceAfter=14,
    )
    signoff = ParagraphStyle(
        "Signoff",
        parent=body,
        spaceAfter=2,
    )

    story = [
        Paragraph("Daniel Morgan", name),
        Paragraph(
            f'<link href="mailto:danmorgz@googlemail.com" color="{LINK.hexval()}">danmorgz@googlemail.com</link>'
            " &nbsp; | &nbsp; "
            f'<link href="https://danmorgan.vercel.app" color="{LINK.hexval()}">danmorgan.vercel.app</link>',
            contact,
        ),
        Paragraph("Dear Luma Hiring Team,", greeting),
        Paragraph(
            "I began my career directing music videos before moving into product design and software engineering. Since then, I've built a career that combines creative thinking with hands-on technical skills - taking ideas from an early concept through to something people can see, use, and experience.",
            body,
        ),
        Paragraph(
            "Alongside products inspired by my other love, sport, my apps have often had a strong creative thread: developing the content and visual identity for "
            f'<link href="https://apps.apple.com/gb/app/looselips/id1578749536" color="{LINK.hexval()}"><u>Looselips</u></link>'
            ", creating audio-guided workouts for "
            f'<link href="https://www.happyfloorapp.com" color="{LINK.hexval()}"><u>Happy Floor</u></link>'
            ", and building AI image-generation workflows and content pipelines for "
            f'<link href="https://apps.apple.com/gb/app/blablaaha-learn-spanish/id6755297500" color="{LINK.hexval()}"><u>BlaBlaAHA!</u></link>.' ,
            body,
        ),
        Paragraph(
            "For the past five years, I've had a slightly unhealthy obsession with 3D scanning, particularly photogrammetry and Gaussian splatting. My project "
            f'<link href="https://www.instagram.com/reel/DZNFhtSxp8O/?igsh=Ym1zYzhhOHBnbG1v" color="{LINK.hexval()}"><u>Queer Encounters</u></link>'
            " explores its potential as a documentary medium by pairing captured spaces and people with audio interviews. I've also built my own React and Remotion pipelines for generating audiograms and image slideshows for the project.",
            body,
        ),
        Paragraph(
            "More recently, I won Gold at an ElevenLabs hackathon. The brief was to &quot;remix&quot; its website, so I transformed it into an interactive film using ComfyUI, Seedance, AI music, Logic, and React. "
            f'<link href="https://lostintheweights.vercel.app" color="{LINK.hexval()}"><u>You can watch the project here</u></link> (just press play).' ,
            body,
        ),
        Paragraph(
            "This feels like a genuinely good fit for me. I'd love to talk.",
            body,
        ),
        Spacer(1, 7),
        Paragraph("Best,", signoff),
        Paragraph("Daniel Morgan", greeting),
    ]

    pdf.build(story)
    print(OUTPUT)


if __name__ == "__main__":
    main()

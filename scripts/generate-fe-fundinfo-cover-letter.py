from pathlib import Path

from reportlab.lib.colors import HexColor
from reportlab.lib.enums import TA_LEFT
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import ParagraphStyle
from reportlab.lib.units import mm
from reportlab.platypus import Paragraph, SimpleDocTemplate, Spacer


OUTPUT = Path("public/daniel-morgan-cover-letter-fe-fundinfo.pdf")
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
        title="Daniel Morgan - Cover Letter for FE fundinfo",
        author="Daniel Morgan",
        subject="Application for AI Product Builder at FE fundinfo",
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
        fontSize=8.1,
        leading=12,
        textColor=INK,
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
            f'<link href="mailto:danmorgz@googlemail.com" color="{INK.hexval()}">danmorgz@googlemail.com</link>'
            " &nbsp; | &nbsp; "
            f'<link href="https://danmorgan.vercel.app" color="{INK.hexval()}">danmorgan.vercel.app</link>'
            " &nbsp; | &nbsp; UK passport holder, currently relocating to London",
            contact,
        ),
        Paragraph("Dear FE fundinfo Hiring Team,", greeting),
        Paragraph(
            "I've spent more than 15 years building software and taking loosely formed ideas through to useful products. I've done that as a founder, product designer, and hands-on engineer: working out what the first version should be, building it, and putting it in front of people. I am comfortable moving between customer conversations, product decisions, and software development.",
            body,
        ),
        Paragraph(
            "I'm genuinely excited by the prospect of working somewhere I have the autonomy to choose the right tools and turn ideas into professional-looking prototypes in days. Keeping up with new AI tools has become an important part of how I work. Although I've been coding for more than 15 years, what I enjoy is the process of creating products, not writing code.",
            body,
        ),
        Paragraph(
            "At Func Main, I design and build my own products alongside selected client work. Recently that has included "
            f'<link href="https://apps.apple.com/gb/app/blablaaha-learn-spanish/id6755297500" color="{LINK.hexval()}"><u>BlaBlaAHA!</u></link>'
            ", an AI-native language app with custom content-production workflows; an agent that turns a photograph of a festival poster into a playlist; and a code-driven video editor built with Next.js and Remotion. I also competed in three one-week ElevenLabs hackathons, winning Gold for an "
            f'<link href="https://lostintheweights.vercel.app" color="{LINK.hexval()}"><u>interactive film/website</u></link>'
            " built with ComfyUI, Seedance, AI music, Logic, and React.",
            body,
        ),
        Paragraph(
            "Earlier, I founded Active in Time and grew it from a one-person business to a team of five. We worked directly with UK leisure operators, built a profitable SaaS platform, and turned our consumer swimming app into a four-year global partnership with Speedo. At Pentland Brands, I worked inside the Innovation Team building prototypes for brands including Lacoste, Speedo, and Berghaus.",
            body,
        ),
        Paragraph(
            "I hope you agree that I'd be a good fit for this role, and I'd love the chance to sell myself face to face.",
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

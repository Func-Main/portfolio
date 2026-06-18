from pathlib import Path
from typing import Optional, Union
import re
import textwrap

PAGE_W, PAGE_H = 595, 842
MARGIN = 44
BOTTOM = 38

PUBLIC_CONTACT = [
    ("danmorgz@googlemail.com", "mailto:danmorgz@googlemail.com"),
    ("danmorgan.vercel.app", "https://danmorgan.vercel.app"),
    ("Malaga, Spain (Spanish resident, UK passport)", None),
]
PRIVATE_CONTACT = [
    ("danmorgz@googlemail.com", "mailto:danmorgz@googlemail.com"),
    ("+447894998333", "tel:+447894998333"),
    ("danmorgan.vercel.app", "https://danmorgan.vercel.app"),
    ("Malaga, Spain (Spanish resident, UK passport)", None),
]
SPORTS_CONTACT = [
    ("danmorgz@googlemail.com", "mailto:danmorgz@googlemail.com"),
    ("danmorgan.vercel.app", "https://danmorgan.vercel.app"),
    ("Malaga, Spain (Spanish resident, UK passport; open to relocation)", None),
]
OPENAI_CONTACT = [
    ("danmorgz@googlemail.com", "mailto:danmorgz@googlemail.com"),
    ("danmorgan.vercel.app", "https://danmorgan.vercel.app"),
    ("Malaga, Spain (Spanish resident, UK passport; open to Madrid)", None),
]
GENIE_CONTACT = [
    ("danmorgz@googlemail.com", "mailto:danmorgz@googlemail.com"),
    ("danmorgan.vercel.app", "https://danmorgan.vercel.app"),
    ("Malaga, Spain (Spanish resident, UK passport; remote-ready)", None),
]
ATTIO_CONTACT = [
    ("danmorgz@googlemail.com", "mailto:danmorgz@googlemail.com"),
    ("danmorgan.vercel.app", "https://danmorgan.vercel.app"),
    ("Currently relocating to London (Spanish resident, UK passport)", None),
]
ACCENTURE_CONTACT = [
    ("danmorgz@googlemail.com", "mailto:danmorgz@googlemail.com"),
    ("danmorgan.vercel.app", "https://danmorgan.vercel.app"),
    (
        "Currently relocating to London (Spanish resident, UK passport; willing to travel within the UK)",
        None,
    ),
]

SECTIONS = [
    (
        "SUMMARY",
        [
            (
                "p",
                "Product designer, founder, and engineer with 15+ years building apps, creative technology, and full-stack software. Recently focused on AI-native and audio-first products, and on using AI to make better work faster. I am a scrappy mix of product, engineering, and design, optimistic and easy to work with.",
            ),
        ],
    ),
    (
        "SKILLS",
        [
            (
                "p",
                "Product design, AI-native product design, audio-first product design, rapid prototyping, iOS app development, Elixir and Phoenix full-stack development, creative technology, video production and visual asset creation.",
            ),
        ],
    ),
    (
        "EXPERIENCE",
        [
            ("job", "Func Main, Founder, Tech & Product - June 2016 - Present"),
            (
                "p",
                "Independent product studio where I've launched, grown, and sold my own apps, alongside selected client work.",
            ),
            (
                "bullet",
                "BlaBlaAHA! - AI-native, audio-first language app built around short listening sessions and conversational confidence.",
            ),
            (
                "bullet",
                "Happy Floor - Pelvic health app with audio-guided exercises, video tutorials, daily goals, and progression plans.",
            ),
            (
                "bullet",
                "Looselips - Conversation app with 1000+ prompts for dating, relationships, friends, and family.",
            ),
            (
                "bullet",
                "Bend.com - AI, social, and backend feature work for one of the world's most popular stretching apps.",
            ),
            (
                "bullet",
                "ElevenLabs Hacks - Competed in 3 ElevenLabs Hacks and won Gold in the Vercel challenge.",
            ),
            (
                "job",
                "Active in Time Ltd, Founder & Product - July 2012 - Present",
            ),
            (
                "p",
                "Founded a health and leisure technology company that grew from a one-person shop to five full-time employees. Splashpath became Apple's No. 1 Health & Fitness app in the UK, then relaunched globally as Speedo Fit through an exclusive four-year partnership with Speedo. The company continues to operate profitably, though I am no longer involved day to day.",
            ),
            (
                "bullet",
                "Active in Time - Profitable SaaS platform helping UK leisure operators manage pool timetables and programme changes.",
            ),
            (
                "bullet",
                "Speedo Fit - Global swim training and tracking app created through an exclusive partnership with Speedo.",
            ),
            (
                "job",
                "Wilde, Chief Executive Officer - September 2019 - December 2020",
            ),
            (
                "p",
                "Secured investment from Founders Factory and assembled the team to launch a new queer travel product, until COVID rained on our parade.",
            ),
            (
                "job",
                "Pentland Brands, Creative Technologist - March 2018 - September 2019",
            ),
            (
                "p",
                "Rapidly designed and built web/mobile prototypes for global brands including Lacoste, Speedo, and Berghaus.",
            ),
            (
                "job",
                "Beeline, Mobile Product Design & Development - May 2016 - January 2017",
            ),
            (
                "p",
                "Worked with the founders to plan, design, and build the first version of the Beeline app after a successful Kickstarter campaign.",
            ),
            ("job", "Pulse Films, Video Director - 2006 - 2012"),
            (
                "p",
                "Directed over 15 music videos and commercials, including a viral marketing campaign I conceived and directed that won a Cannes Lions Gold Lion.",
            ),
        ],
    ),
    (
        "EDUCATION",
        [
            (
                "p",
                "Bournemouth University - Bachelor's Degree, TV Production, 2003 - 2006. Grade: 1st.",
            ),
        ],
    ),
    (
        "INTERESTS",
        [
            (
                "p",
                "Padel, water polo, Spanish, music, podcasting, photography, and queer community projects.",
            ),
        ],
    ),
]

SPORTS_SECTIONS = [
    (
        "SUMMARY",
        [
            (
                "p",
                "Product designer, founder, and engineer with 15+ years building apps across sports, health, fitness, and creative technology. My first sports app, Splashpath, grew to 500k users, became Apple's No. 1 Health & Fitness app in the UK, and led to a four-year global partnership with Speedo. Recently I've been using AI workflows to improve the speed and quality of my product design and engineering work. I am a scrappy mix of product, engineering, and design, optimistic and easy to work with.",
            ),
        ],
    ),
    (
        "SKILLS",
        [
            (
                "p",
                "Sports product design, iOS app development, Elixir and Phoenix full-stack development, rapid prototyping, AI-assisted product development, audio-guided training products, SaaS/CMS platforms, creative technology, video production and visual asset creation.",
            ),
        ],
    ),
    (
        "EXPERIENCE",
        [
            (
                "job",
                "Active in Time Ltd, Founder & Product - July 2012 - Present",
            ),
            (
                "p",
                "Founded a health and leisure technology company that grew from a one-person shop to five full-time employees. Splashpath grew to 500k users and became Apple's No. 1 Health & Fitness app in the UK, then relaunched globally as Speedo Fit through an exclusive four-year partnership with Speedo. The company continues to operate profitably, though I am no longer involved day to day.",
            ),
            (
                "bullet",
                "Speedo Fit - Global swim training and tracking app created through an exclusive partnership with Speedo.",
            ),
            (
                "bullet",
                "Active in Time - Profitable SaaS platform helping UK leisure operators manage pool timetables and programme changes.",
            ),
            ("job", "Func Main, Founder, Tech & Product - June 2016 - Present"),
            (
                "p",
                "Independent product studio where I've launched, grown, and sold my own apps, alongside selected client work.",
            ),
            (
                "bullet",
                "Bend.com - AI, social, and backend feature work for one of the world's most popular stretching apps.",
            ),
            (
                "bullet",
                "Happy Floor - Pelvic health app with audio-guided exercises, video tutorials, daily goals, and progression plans.",
            ),
            (
                "bullet",
                "Padel Robot Trainer - AI-assisted training companion for a padel ball machine, with structured practice for bandejas, viboras, volleys, and audio-guided workouts.",
            ),
            (
                "job",
                "Pentland Brands, Creative Technologist - March 2018 - September 2019",
            ),
            (
                "p",
                "Rapidly designed and built web/mobile prototypes for global brands including Lacoste, Speedo, and Berghaus.",
            ),
            (
                "job",
                "Beeline, Mobile Product Design & Development - May 2016 - January 2017",
            ),
            (
                "p",
                "Worked with the founders of a bicycle-tech startup to plan, design, and build the first version of the Beeline app after a successful Kickstarter campaign.",
            ),
            ("job", "Pulse Films, Video Director - 2006 - 2012"),
            (
                "p",
                "Directed over 15 music videos and commercials, including a viral marketing campaign I conceived and directed that won a Cannes Lions Gold Lion.",
            ),
        ],
    ),
    (
        "EDUCATION",
        [
            (
                "p",
                "Bournemouth University - Bachelor's Degree, TV Production, 2003 - 2006. Grade: 1st.",
            ),
        ],
    ),
    (
        "INTERESTS",
        [
            (
                "p",
                "Padel, water polo, swimming, Spanish, music, podcasting, photography, and queer community projects. Currently training to compete in padel at the Valencia Gay Games.",
            ),
        ],
    ),
]

OPENAI_SECTIONS = [
    (
        "SUMMARY",
        [
            (
                "p",
                "Founder and engineer with 15+ years turning early ideas into products people actually use. I like working close to customers, understanding what they are trying to do, and then making the first useful version quickly enough that everyone can learn from it. Recently I have been focused on AI and audio-first products, rapid prototyping, and helping new technology feel practical, clear, and useful.",
            ),
        ],
    ),
    (
        "SKILLS",
        [
            (
                "p",
                "AI product deployment, solution discovery, rapid prototyping, full-stack product engineering, iOS app development, Elixir and Phoenix, JavaScript/TypeScript, customer-facing technical leadership, product strategy, technical documentation, creative technology, video and audio product workflows.",
            ),
        ],
    ),
    (
        "EXPERIENCE",
        [
            ("job", "Func Main, Founder, Tech & Product - June 2016 - Present"),
            (
                "p",
                "Independent product studio where I design, build, and ship my own products, alongside selected client work. My role spans customer discovery, technical architecture, product strategy, hands-on implementation, launch, and iteration.",
            ),
            (
                "bullet",
                "BlaBlaAHA! - AI-native, audio-first language app built around short listening sessions, conversational confidence, and fast content iteration.",
            ),
            (
                "bullet",
                "Bend.com - AI, social, and backend feature work for one of the world's most popular stretching apps.",
            ),
            (
                "bullet",
                "Happy Floor - Pelvic health app with audio-guided exercises, video tutorials, daily goals, and progression plans.",
            ),
            (
                "bullet",
                "ElevenLabs Hacks - Competed in 3 ElevenLabs Hacks, building rapid voice and agentic media prototypes, and won Gold in the Vercel challenge.",
            ),
            (
                "bullet",
                "Remotion Video Creator - Next.js and Remotion editor for prompting, composing, and rendering videos directly from code.",
            ),
            (
                "job",
                "Active in Time Ltd, Founder & Product - July 2012 - Present",
            ),
            (
                "p",
                "Founded a health and leisure technology company that grew from a one-person shop to five full-time employees. Built and operated a profitable SaaS platform for UK leisure operators, and led the product partnership that relaunched Splashpath globally as Speedo Fit through an exclusive four-year partnership with Speedo.",
            ),
            (
                "job",
                "Wilde, Chief Executive Officer - September 2019 - December 2020",
            ),
            (
                "p",
                "Secured investment from Founders Factory and assembled the team to launch a new queer travel product, leading product, hiring, partnerships, and investor communication until COVID stopped travel.",
            ),
            (
                "job",
                "Pentland Brands, Creative Technologist - March 2018 - September 2019",
            ),
            (
                "p",
                "Worked inside the Innovation Team to rapidly design and build web and mobile prototypes for global brands including Lacoste, Speedo, and Berghaus, translating early strategic opportunities into tangible product experiments.",
            ),
            (
                "job",
                "Beeline, Mobile Product Design & Development - May 2016 - January 2017",
            ),
            (
                "p",
                "Worked directly with the founders to plan, design, and build the first version of the Beeline app after a successful Kickstarter campaign.",
            ),
        ],
    ),
    (
        "EDUCATION",
        [
            (
                "p",
                "Bournemouth University - Bachelor's Degree, TV Production, 2003 - 2006. Grade: 1st.",
            ),
        ],
    ),
    (
        "INTERESTS",
        [
            (
                "p",
                "Spanish, padel, water polo, music, podcasting, photography, and queer community projects.",
            ),
        ],
    ),
]

GENIE_SECTIONS = [
    (
        "SUMMARY",
        [
            (
                "p",
                "Founder and engineer with 15+ years turning early ideas into products people actually use. For the last 18 months I have used AI-assisted development every day to build and launch my own applications, and I have become very interested in how agentic systems change the way small teams design, build, and ship. I like working from outcomes, creating clarity where there is not yet a spec, and moving quickly from idea to working product.",
            ),
        ],
    ),
    (
        "SKILLS",
        [
            (
                "p",
                "AI-assisted development, agentic workflows, rapid prototyping, full-stack product engineering, JavaScript/TypeScript, Node.js and Next.js product engineering, Elixir and Phoenix, iOS app development, systems thinking, product strategy, technical design, customer discovery, founder-led delivery.",
            ),
        ],
    ),
    (
        "EXPERIENCE",
        [
            ("job", "Func Main, Founder, Tech & Product - June 2016 - Present"),
            (
                "p",
                "Independent product studio where I design, build, and ship my own products, alongside selected client work. My role spans product discovery, technical architecture, hands-on implementation, launch, iteration, and using AI tools to increase the speed and quality of the work.",
            ),
            (
                "bullet",
                "BlaBlaAHA! - AI-native, audio-first language app built around short listening sessions, conversational confidence, and fast content iteration.",
            ),
            (
                "bullet",
                "Bend.com - AI, social, and backend feature work for one of the world's most popular stretching apps.",
            ),
            (
                "bullet",
                "Happy Floor - Pelvic health app with audio-guided exercises, video tutorials, daily goals, and progression plans.",
            ),
            (
                "bullet",
                "ElevenLabs Hacks - Competed in 3 ElevenLabs Hacks, building rapid voice and agentic media prototypes, and won Gold in the Vercel challenge.",
            ),
            (
                "bullet",
                "Remotion Video Creator - Next.js and Remotion editor for prompting, composing, and rendering videos directly from code.",
            ),
            (
                "job",
                "Active in Time Ltd, Founder & Product - July 2012 - Present",
            ),
            (
                "p",
                "Founded a health and leisure technology company that grew from a one-person shop to five full-time employees. Built and operated a profitable SaaS platform for UK leisure operators, and led the product partnership that relaunched Splashpath globally as Speedo Fit through an exclusive four-year partnership with Speedo.",
            ),
            (
                "job",
                "Wilde, Chief Executive Officer - September 2019 - December 2020",
            ),
            (
                "p",
                "Secured investment from Founders Factory and assembled the team to launch a new queer travel product, leading product, hiring, partnerships, and investor communication until COVID stopped travel.",
            ),
            (
                "job",
                "Pentland Brands, Creative Technologist - March 2018 - September 2019",
            ),
            (
                "p",
                "Worked inside the Innovation Team to rapidly design and build web and mobile prototypes for global brands including Lacoste, Speedo, and Berghaus, translating early strategic opportunities into tangible product experiments.",
            ),
            (
                "job",
                "Beeline, Mobile Product Design & Development - May 2016 - January 2017",
            ),
            (
                "p",
                "Worked directly with the founders to plan, design, and build the first version of the Beeline app after a successful Kickstarter campaign.",
            ),
        ],
    ),
    (
        "EDUCATION",
        [
            (
                "p",
                "Bournemouth University - Bachelor's Degree, TV Production, 2003 - 2006. Grade: 1st.",
            ),
        ],
    ),
    (
        "INTERESTS",
        [
            (
                "p",
                "Spanish, padel, water polo, music, podcasting, photography, and queer community projects.",
            ),
        ],
    ),
]

ATTIO_SECTIONS = [
    (
        "SUMMARY",
        [
            (
                "p",
                "Founder and product engineer with 15+ years turning ambiguous ideas into products people actually use.",
            ),
        ],
    ),
    (
        "SKILLS",
        [
            (
                "p",
                "Elixir and Phoenix, iOS app development, full-stack development, APIs, databases, product design, customer research, rapid prototyping, and AI-assisted development. Fairly new to React, TypeScript, and Node.js, but comfortable picking up languages and frameworks after 15+ years of programming.",
            ),
        ],
    ),
    (
        "EXPERIENCE",
        [
            ("job", "Func Main, Founder, Tech & Product - June 2016 - Present"),
            (
                "p",
                "Independent product studio where I design, build, and ship my own products, alongside selected client work. My role spans customer discovery, technical architecture, hands-on implementation, launch, iteration, and using AI tools to increase the speed and quality of the work.",
            ),
            (
                "bullet",
                "BlaBlaAHA! - AI-native, audio-first language app built around short listening sessions, conversational confidence, and fast content iteration.",
            ),
            (
                "bullet",
                "Bend.com - AI, social, and backend feature work for one of the world's most popular stretching apps.",
            ),
            (
                "bullet",
                "Happy Floor - Pelvic health app with audio-guided exercises, video tutorials, daily goals, and progression plans.",
            ),
            (
                "bullet",
                "ElevenLabs Hacks - Competed in 3 ElevenLabs Hacks, building rapid voice and agentic media prototypes, and won Gold in the Vercel challenge.",
            ),
            (
                "bullet",
                "Remotion Video Creator - Next.js and Remotion editor for prompting, composing, and rendering videos directly from code.",
            ),
            (
                "job",
                "Active in Time Ltd, Founder & Product - July 2012 - Present",
            ),
            (
                "p",
                "Founded a health and leisure technology company that grew from a one-person shop to five full-time employees. Built and operated a profitable SaaS platform for UK leisure operators, and led the product partnership that relaunched Splashpath globally as Speedo Fit through an exclusive four-year partnership with Speedo.",
            ),
            (
                "job",
                "Wilde, Chief Executive Officer - September 2019 - December 2020",
            ),
            (
                "p",
                "Secured investment from Founders Factory and assembled the team to launch a new queer travel product, leading product, hiring, partnerships, and investor communication until COVID stopped travel.",
            ),
            (
                "job",
                "Pentland Brands, Creative Technologist - March 2018 - September 2019",
            ),
            (
                "p",
                "Worked inside the Innovation Team to rapidly design and build web and mobile prototypes for global brands including Lacoste, Speedo, and Berghaus, translating early strategic opportunities into tangible product experiments.",
            ),
            (
                "job",
                "Beeline, Mobile Product Design & Development - May 2016 - January 2017",
            ),
            (
                "p",
                "Worked directly with the founders of a bicycle-tech startup to plan, design, and build the first version of the Beeline app after a successful Kickstarter campaign.",
            ),
        ],
    ),
    (
        "EDUCATION",
        [
            (
                "p",
                "Bournemouth University - Bachelor's Degree, TV Production, 2003 - 2006. Grade: 1st.",
            ),
        ],
    ),
    (
        "INTERESTS",
        [
            (
                "p",
                "Spanish, padel, water polo, music, podcasting, photography, and queer community projects.",
            ),
        ],
    ),
]

ACCENTURE_SECTIONS = [
    (
        "SUMMARY",
        [
            (
                "p",
                "Founder and product engineer with 15+ years building products from ambiguous early ideas through to real users. Recently focused on AI-native apps, agentic prototypes, and using AI-assisted development to move quickly from product idea to working system.",
            ),
        ],
    ),
    (
        "SKILLS",
        [
            (
                "p",
                "Elixir and Phoenix, iOS app development, full-stack development, APIs, databases, product design, customer research, client workshops, rapid prototyping, AI-assisted development, agentic product prototypes, OpenAI and ElevenLabs workflows. Comfortable picking up new languages, frameworks, and AI tooling after 15+ years of programming.",
            ),
        ],
    ),
    (
        "EXPERIENCE",
        [
            ("job", "Func Main, Founder, Tech & Product - June 2016 - Present"),
            (
                "p",
                "Independent product studio where I design, build, and ship my own products, alongside selected client work. My role spans customer discovery, technical architecture, hands-on implementation, launch, iteration, and using AI tools to increase the speed and quality of the work.",
            ),
            (
                "bullet",
                "BlaBlaAHA! - AI-native, audio-first language app built around short listening sessions, conversational confidence, and fast content iteration.",
            ),
            (
                "bullet",
                "ElevenLabs Hacks - Competed in 3 ElevenLabs Hacks, building rapid voice and agentic media prototypes, and won Gold in the Vercel challenge.",
            ),
            (
                "bullet",
                "Remotion Video Creator - Next.js and Remotion editor for prompting, composing, and rendering videos directly from code.",
            ),
            (
                "bullet",
                "Bend.com - AI, social, and backend feature work for one of the world's most popular stretching apps.",
            ),
            (
                "bullet",
                "Happy Floor - Pelvic health app with audio-guided exercises, video tutorials, daily goals, and progression plans.",
            ),
            (
                "job",
                "Active in Time Ltd, Founder & Product - July 2012 - Present",
            ),
            (
                "p",
                "Founded a health and leisure technology company that grew from a one-person shop to five full-time employees. Built and operated a profitable SaaS platform for UK leisure operators, and led the product partnership that relaunched Splashpath globally as Speedo Fit through an exclusive four-year partnership with Speedo.",
            ),
            (
                "job",
                "Wilde, Chief Executive Officer - September 2019 - December 2020",
            ),
            (
                "p",
                "Secured investment from Founders Factory and assembled the team to launch a new queer travel product, leading product, hiring, partnerships, and investor communication until COVID stopped travel.",
            ),
            (
                "job",
                "Pentland Brands, Creative Technologist - March 2018 - September 2019",
            ),
            (
                "p",
                "Worked inside the Innovation Team to rapidly design and build web and mobile prototypes for global brands including Lacoste, Speedo, and Berghaus, translating early strategic opportunities into tangible product experiments.",
            ),
            (
                "job",
                "Beeline, Mobile Product Design & Development - May 2016 - January 2017",
            ),
            (
                "p",
                "Worked directly with the founders of a bicycle-tech startup to plan, design, and build the first version of the Beeline app after a successful Kickstarter campaign.",
            ),
        ],
    ),
    (
        "EDUCATION",
        [
            (
                "p",
                "Bournemouth University - Bachelor's Degree, TV Production, 2003 - 2006. Grade: 1st.",
            ),
        ],
    ),
    (
        "INTERESTS",
        [
            (
                "p",
                "Spanish, padel, water polo, music, podcasting, photography, and queer community projects.",
            ),
        ],
    ),
]

SECTION_GAPS = {
    "SUMMARY": 17,
    "SKILLS": 17,
    "EXPERIENCE": 18,
    "EDUCATION": 16,
    "INTERESTS": 0,
}


def esc(value: str) -> str:
    return value.replace("\\", "\\\\").replace("(", "\\(").replace(")", "\\)")


def text_width(value: str, size: float) -> float:
    return len(value) * size * 0.49


def render_page(
    contact: list[tuple[str, Optional[str]]],
    sections: list[tuple[str, list[tuple[str, str]]]] = SECTIONS,
) -> tuple[str, list[dict[str, object]]]:
    ops: list[str] = []
    links: list[dict[str, object]] = []
    y = PAGE_H - MARGIN

    def ensure(space: float) -> None:
        if y - space < BOTTOM:
            raise ValueError("CV content no longer fits on one page")

    def text(x: float, line: str, size: float = 9, font: str = "F1", leading: float = 11) -> None:
        nonlocal y
        ensure(leading)
        ops.append(f"BT /{font} {size} Tf {x} {y:.2f} Td ({esc(line)}) Tj ET")
        y -= leading

    def contact_line(x: float, parts: list[tuple[str, Optional[str]]], size: float = 8.1, leading: float = 12) -> None:
        nonlocal y
        ensure(leading)
        labels = [label for label, _ in parts]
        line = " | ".join(labels)
        ops.append(f"BT /F1 {size} Tf {x} {y:.2f} Td ({esc(line)}) Tj ET")

        cursor_x = x
        separator_width = text_width(" | ", size)
        for label, uri in parts:
            label_width = text_width(label, size)
            if uri:
                links.append(
                    {
                        "uri": uri,
                        "rect": [
                            cursor_x,
                            y - 2,
                            cursor_x + label_width,
                            y + size + 2,
                        ],
                    }
                )
            cursor_x += label_width + separator_width

        y -= leading

    def gap(amount: float) -> None:
        nonlocal y
        ensure(amount)
        y -= amount

    def wrap_lines(value: str, width: int) -> list[str]:
        return textwrap.wrap(
            value,
            width=width,
            break_long_words=False,
            replace_whitespace=False,
        )

    def paragraph(value: str, width: int = 100, size: float = 8.9, leading: float = 11.2) -> None:
        for line in wrap_lines(value, width):
            text(MARGIN, line, size=size, leading=leading)
        gap(3.5)

    def bullet(value: str) -> None:
        for index, line in enumerate(wrap_lines(value, 94)):
            prefix = "- " if index == 0 else "  "
            text(MARGIN + 10, prefix + line, size=8.45, leading=10.35)
        gap(1.2)

    text(MARGIN, "Daniel Morgan", size=23, font="F2", leading=25)
    contact_line(MARGIN, contact)
    gap(13)

    for title, items in sections:
        ensure(28)
        text(MARGIN, title, size=8.9, font="F2", leading=10.5)
        gap(3)
        for kind, value in items:
            if kind == "job":
                gap(5)
                for line in wrap_lines(value, 82):
                    text(MARGIN, line, size=10.0, font="F2", leading=12.2)
                gap(2)
            elif kind == "bullet":
                bullet(value)
            else:
                paragraph(value)
        gap(SECTION_GAPS[title])

    return "\n".join(ops), links


def build_pdf(content: str, links: list[dict[str, object]]) -> bytes:
    objects: list[bytes] = []

    def add_obj(data: Union[bytes, str]) -> int:
        if isinstance(data, str):
            data = data.encode("latin-1")
        objects.append(data)
        return len(objects)

    add_obj("<< /Type /Catalog /Pages 2 0 R >>")
    objects.append(b"")
    add_obj("<< /Type /Font /Subtype /Type1 /BaseFont /Helvetica >>")
    add_obj("<< /Type /Font /Subtype /Type1 /BaseFont /Helvetica-Bold >>")

    stream = content.encode("latin-1")
    content_ref = add_obj(
        f"<< /Length {len(stream)} >>\nstream\n".encode("latin-1")
        + stream
        + b"\nendstream"
    )

    annotation_refs = []
    for link in links:
        x1, y1, x2, y2 = link["rect"]
        uri = esc(str(link["uri"]))
        annotation_refs.append(
            add_obj(
                f"<< /Type /Annot /Subtype /Link /Rect [{x1:.2f} {y1:.2f} {x2:.2f} {y2:.2f}] /Border [0 0 0] /A << /S /URI /URI ({uri}) >> >>"
            )
        )
    annotations = ""
    if annotation_refs:
        annotations = " /Annots [" + " ".join(f"{ref} 0 R" for ref in annotation_refs) + "]"

    page_ref = add_obj(
        f"<< /Type /Page /Parent 2 0 R /MediaBox [0 0 {PAGE_W} {PAGE_H}] /Resources << /Font << /F1 3 0 R /F2 4 0 R >> >> /Contents {content_ref} 0 R{annotations} >>"
    )
    objects[1] = (
        f"<< /Type /Pages /Kids [{page_ref} 0 R] /Count 1 >>".encode("latin-1")
    )

    pdf = bytearray(b"%PDF-1.4\n%\xe2\xe3\xcf\xd3\n")
    offsets = [0]
    for index, obj in enumerate(objects, 1):
        offsets.append(len(pdf))
        pdf.extend(f"{index} 0 obj\n".encode("latin-1"))
        pdf.extend(obj)
        pdf.extend(b"\nendobj\n")

    xref = len(pdf)
    pdf.extend(f"xref\n0 {len(objects) + 1}\n".encode("latin-1"))
    pdf.extend(b"0000000000 65535 f \n")
    for offset in offsets[1:]:
        pdf.extend(f"{offset:010d} 00000 n \n".encode("latin-1"))
    pdf.extend(
        f"trailer\n<< /Size {len(objects) + 1} /Root 1 0 R >>\nstartxref\n{xref}\n%%EOF\n".encode(
            "latin-1"
        )
    )
    return bytes(pdf)


def assert_contains(path: Path, expected: str, absent: Optional[str] = None) -> None:
    text = path.read_bytes().decode("latin-1", errors="ignore")
    if expected not in text:
        raise AssertionError(f"{path} does not contain {expected!r}")
    if absent and absent in text:
        raise AssertionError(f"{path} unexpectedly contains {absent!r}")


def main() -> None:
    outputs = [
        (Path("public/daniel-morgan-cv.pdf"), PUBLIC_CONTACT, SECTIONS),
        (Path("public/daniel-morgan-cv-sports.pdf"), SPORTS_CONTACT, SPORTS_SECTIONS),
        (Path("public/daniel-morgan-cv-openai.pdf"), OPENAI_CONTACT, OPENAI_SECTIONS),
        (Path("public/daniel-morgan-cv-genie.pdf"), GENIE_CONTACT, GENIE_SECTIONS),
        (Path("public/daniel-morgan-cv-attio.pdf"), ATTIO_CONTACT, ATTIO_SECTIONS),
        (Path("public/daniel-morgan-cv-accenture.pdf"), ACCENTURE_CONTACT, ACCENTURE_SECTIONS),
        (Path("daniel-morgan-cv-private.pdf"), PRIVATE_CONTACT, SECTIONS),
    ]
    for path, contact, sections in outputs:
        content, links = render_page(contact, sections)
        path.write_bytes(build_pdf(content, links))

    assert_contains(
        Path("public/daniel-morgan-cv.pdf"),
        "mailto:danmorgz@googlemail.com",
        "+447894998333",
    )
    assert_contains(
        Path("public/daniel-morgan-cv.pdf"),
        "https://danmorgan.vercel.app",
    )
    assert_contains(
        Path("daniel-morgan-cv-private.pdf"),
        "tel:+447894998333",
    )
    assert_contains(
        Path("public/daniel-morgan-cv-sports.pdf"),
        "Speedo Fit",
        "+447894998333",
    )
    assert_contains(
        Path("public/daniel-morgan-cv-openai.pdf"),
        "AI product deployment",
        "+447894998333",
    )
    assert_contains(
        Path("public/daniel-morgan-cv-genie.pdf"),
        "agentic workflows",
        "+447894998333",
    )
    assert_contains(
        Path("public/daniel-morgan-cv-attio.pdf"),
        "Founder and product engineer",
        "+447894998333",
    )
    assert_contains(
        Path("public/daniel-morgan-cv-accenture.pdf"),
        "ElevenLabs workflows",
        "+447894998333",
    )

    for path, _, _ in outputs:
        print(path)


if __name__ == "__main__":
    main()

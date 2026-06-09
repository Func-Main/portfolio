import { ExternalLink, FileText, Instagram, Linkedin, Mail } from "lucide-react";
import type { Metadata } from "next";
import Link from "next/link";
import { Badge } from "@/components/ui/badge";
import { buttonVariants } from "@/components/ui/button";

export const metadata: Metadata = {
  title: "CV - Daniel Morgan",
  description:
    "CV for Daniel Morgan, a product designer, founder, and engineer building apps, AI-native products, and creative technology.",
};

const contactLinks = [
  {
    label: "Email",
    href: "mailto:danmorgz@googlemail.com",
  },
  {
    label: "Portfolio",
    href: "https://danmorgan.vercel.app",
  },
  {
    label: "PDF",
    href: "/daniel-morgan-cv.pdf",
  },
];

const skills = [
  "Product design",
  "AI-native product design",
  "Audio-first product design",
  "Rapid prototyping",
  "iOS app development",
  "Elixir and Phoenix full-stack development",
  "Creative technology",
  "Video production and visual asset creation",
];

const experience = [
  {
    role: "Founder, Tech & Product",
    company: "Func Main",
    dates: "June 2016 - Present",
    body: [
      "Independent product studio where I've launched, grown, and sold my own apps, alongside selected client work.",
    ],
    selectedWork: [
      {
        title: "BlaBlaAHA!",
        href: "https://apps.apple.com/gb/app/blablaaha-learn-spanish/id6755297500",
        description:
          "AI-native, audio-first language app built around short listening sessions and conversational confidence.",
      },
      {
        title: "Happy Floor",
        href: "https://www.happyfloorapp.com",
        description:
          "Pelvic health app with audio-guided exercises, video tutorials, daily goals, and progression plans.",
      },
      {
        title: "Looselips",
        href: "https://apps.apple.com/gb/app/looselips/id1578749536",
        description:
          "Conversation app with 1000+ prompts for dating, relationships, friends, and family.",
      },
      {
        title: "Bend.com",
        href: "https://www.bend.com",
        description:
          "AI, social, and backend feature work for one of the world's most popular stretching apps.",
      },
      {
        title: "ElevenLabs Hacks",
        href: "https://www.instagram.com/reel/DYBAKTMIMBD/?igsh=MWozM3o3bXY0NGtmeg==",
        description:
          "Competed in 3 ElevenLabs Hacks and won Gold in the Vercel challenge.",
      },
    ],
  },
  {
    role: "Founder & Product",
    company: "Active in Time Ltd",
    dates: "July 2012 - Present",
    body: [
      "Founded a health and leisure technology company that grew from a one-person shop to five full-time employees. Splashpath became Apple's No. 1 Health & Fitness app in the UK, then relaunched globally as Speedo Fit through an exclusive four-year partnership with Speedo. The company continues to operate profitably, though I am no longer involved day to day.",
    ],
    selectedWork: [
      {
        title: "Active in Time",
        description:
          "Profitable SaaS platform helping UK leisure operators manage pool timetables and programme changes.",
      },
      {
        title: "Speedo Fit",
        description:
          "Global swim training and tracking app created through an exclusive partnership with Speedo.",
      },
    ],
  },
  {
    role: "Chief Executive Officer",
    company: "Wilde",
    dates: "September 2019 - December 2020",
    body: [
      "Secured investment from Founders Factory and assembled the team to launch a new queer travel product, until COVID rained on our parade.",
    ],
  },
  {
    role: "Creative Technologist",
    company: "Pentland Brands",
    dates: "March 2018 - September 2019",
    body: [
      "Rapidly designed and built web/mobile prototypes for global brands including Lacoste, Speedo, and Berghaus.",
    ],
  },
  {
    role: "Mobile Product Design & Development",
    company: "Beeline",
    dates: "May 2016 - January 2017",
    body: [
      "Worked with the founders to plan, design, and build the first version of the Beeline app after a successful Kickstarter campaign.",
    ],
  },
  {
    role: "Video Director",
    company: "Pulse Films",
    dates: "2006 - 2012",
    body: [
      "Directed over 15 music videos and commercials, including a viral marketing campaign I conceived and directed that won a Cannes Lions Gold Lion.",
    ],
  },
];

function Section({
  children,
  eyebrow,
}: {
  children: React.ReactNode;
  eyebrow: string;
}) {
  return (
    <section className="border-t py-10" style={{ borderColor: "var(--subtle-divider)" }}>
      <div className="grid gap-5 md:grid-cols-[11rem_1fr]">
        <h2 className="font-mono text-xs uppercase text-muted-foreground">
          {eyebrow}
        </h2>
        <div>{children}</div>
      </div>
    </section>
  );
}

function WorkLink({
  description,
  href,
  title,
}: {
  description: string;
  href?: string;
  title: string;
}) {
  const titleContent = href ? (
    <a
      className="inline-flex items-center gap-1 font-normal text-foreground underline decoration-foreground/25 underline-offset-4 transition hover:decoration-foreground"
      href={href}
      rel="noreferrer"
      target="_blank"
    >
      {title}
      <ExternalLink aria-hidden="true" className="size-3" />
    </a>
  ) : (
    <span className="font-normal text-foreground">{title}</span>
  );

  return (
    <li>
      {titleContent}
      <span className="text-muted-foreground"> - {description}</span>
    </li>
  );
}

export default function CVPage() {
  return (
    <main className="min-h-screen pb-20">
      <header className="mx-auto flex h-16 max-w-6xl items-center justify-between px-5">
        <Link className="font-mono text-sm font-normal uppercase" href="/">
          Daniel Morgan
        </Link>
        <div className="flex items-center gap-2">
          <a
            className={buttonVariants({ variant: "outline", size: "sm" })}
            href="/CV"
            rel="noreferrer"
            target="_blank"
          >
            CV
          </a>
        </div>
      </header>

      <section className="mx-auto max-w-6xl px-5 py-12 md:py-16">
        <div className="grid gap-8 md:grid-cols-[1fr_18rem] md:items-end">
          <div>
            <p className="font-mono text-xs uppercase text-muted-foreground">
              CV
            </p>
            <h1 className="mt-4 max-w-3xl font-title text-5xl font-normal leading-tight tracking-normal text-balance md:text-7xl">
              Daniel Morgan
            </h1>
            <p className="mt-5 max-w-3xl text-lg leading-8 text-muted-foreground">
              Product designer, founder, and engineer with 15+ years building
              apps, creative technology, and full-stack software. Recently
              focused on AI-native and audio-first products, and on using AI to
              make better work faster. I am a scrappy mix of product,
              engineering, and design, optimistic and easy to work with.
            </p>
          </div>

          <aside
            className="rounded-lg border bg-card p-5"
            style={{ borderColor: "var(--subtle-border)" }}
          >
            <div className="mb-4 flex items-center gap-2">
              <FileText aria-hidden="true" className="size-4 text-muted-foreground" />
              <p className="font-mono text-xs uppercase text-muted-foreground">
                Contact
              </p>
            </div>
            <div className="space-y-2 text-sm">
              {contactLinks.map((link) => (
                <a
                  className="block text-foreground underline decoration-foreground/25 underline-offset-4 transition hover:decoration-foreground"
                  href={link.href}
                  key={link.href}
                  rel={link.href.startsWith("http") ? "noreferrer" : undefined}
                  target={link.href.startsWith("http") ? "_blank" : undefined}
                >
                  {link.label}
                </a>
              ))}
              <p className="pt-2 text-muted-foreground">
                Malaga, Spain (Spanish resident, UK passport)
              </p>
            </div>
          </aside>
        </div>
      </section>

      <div className="mx-auto max-w-6xl px-5">
        <Section eyebrow="Skills">
          <div className="flex flex-wrap gap-2">
            {skills.map((skill) => (
              <Badge key={skill} variant="outline">
                {skill}
              </Badge>
            ))}
          </div>
        </Section>

        <Section eyebrow="Experience">
          <div className="space-y-10">
            {experience.map((item) => (
              <article key={`${item.company}-${item.role}`}>
                <div className="grid gap-1 md:grid-cols-[1fr_auto] md:items-baseline">
                  <h3 className="text-xl font-normal leading-tight">
                    {item.company}, {item.role}
                  </h3>
                  <p className="font-mono text-xs uppercase text-muted-foreground">
                    {item.dates}
                  </p>
                </div>
                <div className="mt-4 space-y-4 text-base leading-7 text-muted-foreground">
                  {item.body.map((paragraph) => (
                    <p key={paragraph}>{paragraph}</p>
                  ))}
                  {item.selectedWork ? (
                    <div>
                      <p className="font-mono text-xs uppercase text-muted-foreground">
                        Selected work
                      </p>
                      <ul className="mt-3 list-disc space-y-2 pl-5">
                        {item.selectedWork.map((work) => (
                          <WorkLink key={work.title} {...work} />
                        ))}
                      </ul>
                    </div>
                  ) : null}
                </div>
              </article>
            ))}
          </div>
        </Section>

        <Section eyebrow="Education">
          <div>
            <div className="grid gap-1 md:grid-cols-[1fr_auto] md:items-baseline">
              <h3 className="text-xl font-normal leading-tight">
                Bournemouth University, Bachelor&apos;s Degree, TV Production
              </h3>
              <p className="font-mono text-xs uppercase text-muted-foreground">
                2003 - 2006
              </p>
            </div>
            <p className="mt-3 text-muted-foreground">Grade: 1st.</p>
          </div>
        </Section>

        <Section eyebrow="Interests">
          <p className="text-base leading-7 text-muted-foreground">
            Padel, water polo, Spanish, music, podcasting, photography, and
            queer community projects.
          </p>
        </Section>
      </div>

      <footer
        className="mt-8 border-t text-foreground"
        style={{ borderColor: "var(--subtle-divider)" }}
      >
        <div className="mx-auto flex max-w-6xl justify-end px-5 py-8">
          <div className="flex gap-2">
            <a
              className={buttonVariants({ variant: "secondary", size: "sm" })}
              href="/CV"
              rel="noreferrer"
              target="_blank"
            >
              CV
            </a>
            <a
              className={buttonVariants({ variant: "secondary", size: "icon" })}
              href="mailto:danmorgz@googlemail.com"
              aria-label="Email"
            >
              <Mail aria-hidden="true" />
            </a>
            <a
              aria-label="LinkedIn"
              className={buttonVariants({ variant: "secondary", size: "icon" })}
              href="https://www.linkedin.com/in/daniel-morgan-london"
              rel="noreferrer"
              target="_blank"
            >
              <Linkedin aria-hidden="true" />
            </a>
            <a
              aria-label="Instagram"
              className={buttonVariants({ variant: "secondary", size: "icon" })}
              href="https://www.instagram.com/danoflondon?igsh=MXB3bWpydG8xYjFkYQ%3D%3D&utm_source=qr"
              rel="noreferrer"
              target="_blank"
            >
              <Instagram aria-hidden="true" />
            </a>
          </div>
        </div>
      </footer>
    </main>
  );
}

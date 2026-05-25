/*

 Text boxes from < https://www.infyways.com/tools/text-box-generator/ >

 ╔══════════════════════════════════ Section ═══════════════════════════════════╗
 ║                                                                              ║
 ║                                                                              ║
 ║                                Document Setup                                ║
 ║                                                                              ║
 ║                                                                              ║
 ╚══════════════════════════════════════════════════════════════════════════════╝
*/

#let appendix_numbering = (..numbers) => {
  let numbers = numbers.pos().rev()

  let _ = numbers.pop()
  let alpha = numbers.pop()

  let base = str.to-unicode("A")
  let alpha = str.from-unicode(base + alpha - 1)

  let rest = numbers.rev().map(str)

  if rest.len() == 0 {
    alpha
  } else {
    alpha + "." + rest.join(".")
  }
}
#let prototype = (
  name: "Mentalorium",
  url: link("https://lptimey.github.io/Mentalorium/"),
  pictures: (),
)
#let date = datetime.today()
// #let date = datetime(day: 27, month: 2, year: 2026) // Manuelles Datum
#let studiengang = ("User Experience Design", "UXD", "UXD_B")
#let semester = "SoSe26"
#let school = ("Technische Hochschule Ingolstadt", "THI")

#set document(
  author: ("Tim Ruland", "Marc Obst", "Nicolas Weber"),
  date: date,
  title: [
    The long-term effect of indicating AI fallibility on automation bias in mental health application users.
  ],
  description: "//TODO: Description",
  keywords: (..school, ..studiengang, semester, date.display("[year]-[month]-[day]")),
)

#set page(
  paper: "a4",
  margin: (x: 1.8cm, y: 1.5cm),
  numbering: "1",
  header: [
    #set text(8pt)
    #grid(
      columns: (1fr, 1fr, 1fr),
      inset: 0.25cm,
      align: (left, center, right),

      school.at(0), [STUD Study - Long Term AI Automation Bias], context document.author.join(", "),
    )
  ],
  footer: [
    #set text(8pt)
    #grid(
      columns: (1fr, 1fr, 1fr),
      inset: 0.25cm,
      align: (left, center, right),

      semester, context here().page(), date.display("[day].[month].[year]"),
    )
  ],
)

// text settings
#set text(
  font: "libertinus serif",
  size: 11pt,
  lang: "en",
  region: "GB",
  number-width: "tabular",
  overhang: true,
  slashed-zero: true,
)
#set par(justify: true)
// Add line numbers
#set par.line(numbering: line => text(fill: red, size: 8pt)[#line])

// set Code font
#show raw: it => text(font: "JetBrainsMono NF")[#it]

// Color Links
#show link: it => {
  if type(it.dest) == str {
    text(
      underline([#it], stroke: stroke(
        thickness: 0.05em,
        dash: "solid",
        paint: blue.darken(75%),
      )),
      fill: blue.darken(75%),
    )
  } else if type(it.dest) == label {
    text(
      underline([#it], stroke: stroke(
        thickness: 0.05em,
        dash: "dashed",
        paint: black.transparentize(50%),
      )),
      fill: black,
    )
  } else if type(it.dest) == location {
    text(
      underline([#it], stroke: stroke(
        thickness: 0.05em,
        dash: "solid",
        paint: black,
      )),
      fill: black,
    )
  } else {
    it
    // [#it (unknown dest type = #type(it.dest))]
  }
}

// Number equations and list them as figures
#show figure.where(kind: "equation"): it => block[
  #grid(
    columns: (1fr, auto),
    align: center,

    it.body,
    align(right)[
      (#context counter(figure.where(kind: "equation")).display())
    ],
  )

  #it.caption
]
#show math.equation.where(block: true): it => figure(kind: "equation", supplement: "Equation", it)

// set heading numbering-scheme
#set heading(numbering: "1.1.a.I")

/*
 ╔══════════════════════════════════ Section ═══════════════════════════════════╗
 ║                                                                              ║
 ║                                                                              ║
 ║                              Glossary Definition                             ║
 ║                                                                              ║
 ║                                                                              ║
 ╚══════════════════════════════════════════════════════════════════════════════╝
*/
/// from https://typst.app/universe/package/glossarium/
#import "./vendor/glossarium-0.5.9/glossarium.typ": (
  agls, gls, gls-description, gls-long, gls-longplural, gls-plural, gls-short, glspl, make-glossary, print-glossary,
  register-glossary,
)
#show: make-glossary
#let entry-list = (
  (
    key: "web-component",
    short: "Web Component",
    long: "Web Komponente",
    plural: "Web Components",
    longplural: "Web Komponenten",
    description: [
      Ein Webstandard zur Erstellung wiederverwendbarer, gekapselter HTML-Elemente mit eigener Struktur, Logik und Styling.
      Web Components basieren auf Technologien wie Custom Elements, Shadow DOM und HTML Templates und ermöglichen die Definition eigener Tags zur Laufzeit im Browser.
      Sie erlauben eine modulare Entwicklung von Benutzeroberflächen ohne Abhängigkeit von externen Frameworks und sind nativ im Browser unterstützt.
    ],
  ),
)
#register-glossary(entry-list, use-key-as-short: false)

/*
 ╔══════════════════════════════════ Section ═══════════════════════════════════╗
 ║                                                                              ║
 ║                                                                              ║
 ║                                Document Start                                ║
 ║                                                                              ║
 ║                                                                              ║
 ╚══════════════════════════════════════════════════════════════════════════════╝
*/

#align((center), pad(bottom: 0.75cm, top: 0.75cm)[
  #title()
])

*Authors*\
#context {
  grid(
    columns: (1fr, 1fr, 1fr),
    align: center,
    ..document.author.map(name => name + "*")
  )
}
\*: equal contribution

#heading(numbering: none)[Abstract] <Abstract>
#lorem(100)

#heading(numbering: none)[Keywords] <Keywords>
#context document.keywords.join("; ")

#outline(title: "Table of Contents")

#heading(numbering: none)[Glossary] <Glossary>
#print-glossary(
  entry-list,
  // show-all: true, // Zeigt auch nicht-verwendete Glossar-Einträge an
)

#set page(columns: 2)

= Introduction <Intro>
#lorem(500)

= Methods <Methods>
#lorem(215)
#figure(image("assets/imgs/design/Result.jpg", width: 50%))
$ x = 1 $
$ x = 1 $
$x = 1$
#lorem(215)

= Results <Results>
#lorem(500)

#heading(numbering: none)[Acknowledgements] <Acknowledgements>

#outline(target: figure, title: "List of Figures")

#bibliography("paper.bib", style: "iso-690-numeric", title: "References")
// #bibliography("paper.bib", style: "ieee", title: "References")

#heading(numbering: none)[Appendix] <Appendix>
#set heading(numbering: appendix_numbering)

== Rest
=== Test
== Rest 2
=== Test 2

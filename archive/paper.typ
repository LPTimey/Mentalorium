/*
 Text boxes from < https://www.infyways.com/tools/text-box-generator/ >
 ╔══════════════════════════════════ Section ═══════════════════════════════════╗
 ║                                                                              ║
 ║                                Document Setup                                ║
 ║                                                                              ║
 ╚══════════════════════════════════════════════════════════════════════════════╝
*/

#import "setup.typ": *
#import "glossary.typ": glossary
/// from https://typst.app/universe/package/glossarium/
#import "../vendor/glossarium-0.5.9/glossarium.typ": (
  agls, gls, gls-description, gls-long, gls-longplural, gls-plural, gls-short, glspl, print-glossary,
)

#let prototype = (
  name: "Mentalorium",
  url: link("https://lptimey.github.io/Mentalorium/"),
  pictures: (),
)
#let date = datetime.today()
// #let date = datetime(day: 27, month: 2, year: 2026) // Manuelles Datum
#let studiengang = ("User Experience Design", "User Experience Design Bachelor", "UXD", "UXD_B")
#let semester = "SoSe26"
#let school = ("Technische Hochschule Ingolstadt", "THI")

#set document(
  author: ("Tim Ruland", "Marc Obst", "Nicolas Weber"),
  date: date,
  title: [
    The long-term effect of indicating AI fallibility on automation bias in mental health application users.
  ],
  description: "//TODO: Description",
  keywords: (
    ..school,
    ..studiengang,
    semester,
    date.display("[year]-[month]-[day]"),
    "Mental Health",
    "AI",
    "Artificial Intelligence",
    "FWS",
    "STUD",
    "Automation Bias",
    "Fallibility",
    "Mental Health Application",
    "AI Assistant",
    "Long-Term",
    "Long-Term Effects",
    "Priming",
    "Trust",
    "Confidence",
  ),
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

      [#studiengang.at(3) #semester], context here().page(), date.display("[day].[month].[year]"),
    )
  ],
)

/*
 ╔══════════════════════════════════ Section ═══════════════════════════════════╗
 ║                                                                              ║
 ║                                 Add Template                                 ║
 ║                                                                              ║
 ╚══════════════════════════════════════════════════════════════════════════════╝
*/

#show: setup(glossary)

/*
 ╔══════════════════════════════════ Section ═══════════════════════════════════╗
 ║                                                                              ║
 ║                                Document Start                                ║
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

#heading(numbering: no_numbering)[Abstract] <Abstract>
#lorem(100)

#heading(numbering: no_numbering)[Keywords] <Keywords>
#context document.keywords.sorted().join("; ")

#outline(title: "Table of Contents")

#heading(numbering: no_numbering)[Glossary] <Glossary>
#print-glossary(
  glossary,
  // show-all: true, // Zeigt auch nicht-verwendete Glossar-Einträge an
)

#set page(columns: 2)

= Introduction <Intro>
#lorem(500)

= Methods <Methods>
#lorem(215)
#figure(image("../assets/imgs/design/Result.jpg", width: 50%))
$ x = 1 $
$ x = 1 $
$x = 1$
#lorem(215)

= Results <Results>
#lorem(500)

#heading(numbering: no_numbering)[Acknowledgements] <Acknowledgements>

#outline(target: figure, title: "List of Figures")

#bibliography("paper.bib", style: "iso-690-numeric", title: "References")
// #bibliography("paper.bib", style: "ieee", title: "References")

#heading(numbering: no_numbering)[Appendix] <Appendix>
#set heading(numbering: appendix_numbering)

== Rest
=== Test
== Rest 2
=== Test 2

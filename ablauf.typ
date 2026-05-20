#set page(
  paper: "a4",
  margin: (x: 1.8cm, y: 1.5cm),
  numbering: "1",
)

#outline()

= Plan

== Introduction

The goal of our study will be investigating the long-term effect of indicating the
fallibility of Artificial Intelligence (AI) in users when using mental-health applications.

To do that we are going to have a mock app and patient case vignettes prepared.
The mock app will play the roll of an AI application for mental health, but with pregenerated text.
Then we will ask questions related to the vignettes, and measure correctness,
time needed, and confidence of the answers with the AI.

The study will be carried out as a split-plot design. The between-groups factor being the presence of an AI disclaimer in the first group, while a control group will not have this disclaimer, and the within-groups factor being a time gap of one week between sessions 1 and 2.

The two sessions will be conducted in the lab, which allows us to use the thinking-out loud method for our study, and also allows deeper attention/insights to the user's decision making. After each case vignette there will be a post test questionnaire.

The tests will use the following layout:

+ Patient vignette will be given to the participants
+ _Test specific_
+ (Prototype) Participants will ask AI with a given prompt
+ _Test specific_
+ Participants will chose whether to trust the given answer (2/3 wrong AI-answers)
+ Participants will rate their confidence of the chosen answer (0..=100)
+ Participants will answer post-test-survey

The participants cannot change the given prompt, as this may result in an unfitting answer, thus lowering believability that the answer was given by a real AI-Chatbot.
The 2 to 3 split is present as a sanity check. As we have 5 different cases, one case will be the same in the second round and 2 will be new.
We tried to choose cases as comparable as possible with our limited expertise in mental health. Every participant will do all the cases, which should regulate the severity of cases being too different compared to each other.

These questions will be answered through a survey format (with the web app tally).

When collecting participants, there will not be any special restrictions or other preferences. The goal will be approximately 20-30 subjects.
We will recruit participants in person. To ensure that everybody is treated equally, we will ask everybody the same question: "Do you want to participate in a study, concerning the use of AI in mental health applications? We have created a mock app that we want to test". We are not going to tell them about the study's actual purpose of investigating the long-term effect of indicating the fallibility of AI. People that quit before the second session will be excluded from the main calculations and only be noted in the filtered out participants section and the discussion about our findings. The latter mostly if notable findings have been found.

Unequal inter-group distributions will be dealt with by the mathematical concepts of quartiles etc. This works best if they are roughly equal, which we will make sure to take into account when randomly assigning them with LSD \
(Latin Square Design).

=== Vignette example (1 of 5)

*Name:* Amina

*Src:* https://www.dbjr.de/fileadmin/PDFtmp/Jugendreisen/Stoerungsbilder-und-Fallbeispiele.pdf

*Situation:*\
18-jährige Patientin, bisexuell, bosnischer Herkunft, aus einem engen bis sehr symbiotischen Familiensystem. Sie hat eine eineiige Zwillingsschwester sowie eine jüngere Schwester und besucht die Oberstufe der FOS. In der Familie herrscht ein enger und repressiver Erziehungsstil mit wenig Freiraum für eigene Entscheidungen. Beziehungen zu Personen anderer Herkunft als aus Albanien, Kosovo oder Bosnien werden von den Eltern nicht akzeptiert. Nach einmaligem Cannabiskonsum entwickelte die Patientin aufgrund der Angst vor der Reaktion ihrer Eltern starke Schuld- und Angstgefühle. In der Familienanamnese ist eine depressive Episode bei einer Verwandten bekannt.

Die Patientin beschreibt ein stark negatives Selbstbild und empfindet sich selbst als „hässlich“, „dick“ und „furchtbar“. Körperliche Vorerkrankungen bestehen in Form einer Hashimoto-Thyreoiditis (chronische Schilddrüsenerkrankung) sowie einer Hypertonie. Zu beachten ist die bekannte Korrelation zwischen endokrinologischen Erkrankungen und psychischen Störungen, insbesondere die mögliche Mitverursachung affektiver Störungen durch eine chronische Schilddrüsenunterfunktion.

Komorbid bestehen Panikattacken (F41.0), welche zu den neurotischen, Belastungs- und somatoformen Störungen der Gruppe F40–F48 gehören.

*Diagnose:*\
F32.1 (G) mittelgradige depressive Episode.

*Symptome:*\
anhaltende Niedergestimmtheit, verminderter Selbstwert, Antriebsverlust, Libidoverlust, massive Ein- und Durchschlafstörungen, rasche und wechselhafte Gewichtszu- und -abnahme, Leistungseinbruch in der Schule, häufige Gereiztheit, Aktivitätsverlust sowie innerer und äußerer Rückzug.

*AI-answer good:*\
Prompt: Situation von Amina eingefügt + “Erkläre warum für Amina folgende Therapie gut sein würde” + Lösung richtig eingefügt + “in 4-6 Sätzen”

Bei Amina wäre eine Kombination aus Psychotherapie, möglicher medikamentöser Unterstützung und ergänzenden Selbsthilfe-Strategien sinnvoll, da ihre mittelgradige Depression mehrere Lebensbereiche stark beeinträchtigt. Eine Psychotherapie kann ihr helfen, ihr negatives Selbstbild, die Schuldgefühle sowie den starken familiären Druck besser zu verstehen und neue Bewältigungsstrategien zu entwickeln. Antidepressiva können zusätzlich helfen, Symptome wie Schlafstörungen, Antriebslosigkeit und anhaltende Niedergeschlagenheit zu lindern, besonders da auch körperliche Faktoren wie die Hashimoto-Thyreoiditis eine Rolle spielen können. Bewegung, feste Tagesstrukturen und soziale Unterstützung wirken stabilisierend auf Stimmung, Schlaf und Selbstwertgefühl und können Rückzug und Aktivitätsverlust entgegenwirken. Da außerdem Panikattacken bestehen, kann eine therapeutische Behandlung helfen, Ängste frühzeitig zu erkennen und besser zu kontrollieren.

*AI-answer bad (Selbstgeschrieben):*\
Bei Amina wäre eine Behandlung mit Medikamenten wie Amphetaminen (Adderall) oder Methly phneidate (Ritalin) sinnvoll, da ihre mittelgradige Depression mehrere Lebensbereiche stark beeinträchtigt. Diese Behandlung kann ihr helfen, ihr negatives Selbstbild, die Schuldgefühle sowie den starken familiären Druck besser zu verkraften und neue Bewältigungsstrategien zu entwickeln. Eine Schlafentzugstherapie kann zusätzlich helfen, Symptome wie Schlafstörungen, Antriebslosigkeit und anhaltende Niedergeschlagenheit zu lindern. Das kann helfen die innere Uhr und innere Botenstoffe positiv zu beeinflussen. Bewegung, feste Tagesstrukturen und soziale Unterstützung wirken ebenfalls positiv, können im zu großen Ausmaß aber zu Überbelastung führen.

== Session 01

Session 1 will follow the already stated layout with the parameters:

4) A general disclaimer about AI will be given (full screen) \
6) A disclaimer hint will be shown during the loading time

The control group will not receive these disclaimers

=== Questionnaire

==== Consent

==== Demographics

#table(
  columns: (auto, auto),
  inset: 10pt,
  align: horizon,
  table.header([*Question*], [*Type*]),
  [age], [Number: 14..=120],

  [gender], [Group: Male, Female, Nonbinary, Other, Don't Answer],
)

==== AI context

#table(
  columns: (auto, auto),
  align: horizon,
  table.header([*Question*], [*Type*]),
  [views on AI], [Likert not useful at all <-> very useful],
  [], [Likert very innacceptable <-> very acceptable],

  [views on AI (mental health context)], [Likert very useless <-> very useful],
  [], [Likert very innacceptable <-> very acceptable],

  [AI use in mental h.], [Likert not at all <-> very often],

  [AI use otherwise ], [Personally: Likert not at all <-> very often],
  [], [Professionally: Likert not at all <-> very often],
)

=== Post-test questionnaire 1

#table(
  columns: (auto, auto),
  align: horizon,
  table.header([*Question*], [*Type*]),
  [(UEQ+) Intuitive Use / Intuitive Bedienung], [Likert],
  [(UEQ+) Trustworthiness of Content / Vertrauenswürdigkeit], [Likert],
  [(UEQ+) Response Behavior / Antwortverhalten], [Likert],
  [(UEQ+) Response Quality / Antwortqualität], [Likert],
  [(UEQ+) Comprehensibility / Verständnis], [Likert],
  [(UEQ+) Clarity / Übersichtlichkeit], [Likert],
  [(UEQ+) Risk Handling / Risikohandhabung], [Likert],
)

== Session 02

Session 2 will also follow the already stated layout like session 1, with the unilateral removal of the AI disclaimers.

The control-group will have no differences

=== Post-test questionnaire 2

#table(
  columns: (auto, auto),
  align: horizon,
  table.header([*Question*], [*Type*]),
  [(UEQ+) Intuitive Use / Intuitive Bedienung], [Likert],
  [(UEQ+) Trustworthiness of Content / Vertrauenswürdigkeit], [Likert],
  [(UEQ+) Response Behavior / Antwortverhalten], [Likert],
  [(UEQ+) Response Quality / Antwortqualität], [Likert],
  [(UEQ+) Comprehensibility / Verständnis], [Likert],
  [(UEQ+) Clarity / Übersichtlichkeit], [Likert],
  [(UEQ+) Risk Handling / Risikohandhabung], [Likert],
)

= Prototype

#link("https://lptimey.github.io/Mentalorium/")

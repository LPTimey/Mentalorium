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


= Participant allocation

In this Study we have the following "Resources"

$
          "Groups" G & := {"Active","Control"} \
  "Case Vignettes" C & := {"Amina", "Aylin", "Lena", "Martina", "Mathias"} \
    "Truthfulness" T & := {"Truth","Untruth"} \
          "Rounds" R & := T times C \
        "Sessions" S & := R^3 \
    "Participants" P & := G times S times S \
$

$forall p in P$:
- exactly one group assignment $g in G$
- two collections of three $(c in C,t in T)$ pairs

The following constraints must hold:
- each collection contains exactly one `"Correct"` entry
- no collection may contain duplicate cases
- exactly one case must be shared between the two collections

== Example of a valid Person

$
  p_"example" = & ( \
                & "Active", \
                & (("Amina","Correct"),("Lena","Incorrect"),("Mathias","Incorrect")), \
                & (("Mathias","Incorrect"),("Aylin","Correct"),("Martina","Incorrect")), \
                & )
$
Properties:
- exactly one `"Correct"` in each block
- no duplicates within blocks
- exactly one shared case between sessions: `"Mathias"`

== Allocation algorithm

To fairly allocate our Resources (Cases, Control-group and Answer-quality) to our Participants we will use the following algorithm so that

$
  P_n = F_s (n)
$
where:
- $n$ = participant index
- $s$ = global study seed (for us $403$)
- $F_s$ = deterministic pseudo-random allocation function

The generated participant has the form

$
  F_s(n) = (G_n, B_1, B_2)
$

subject to the constraints

$
  forall omega in {1,2}: abs(B_omega) = 3
$

$
  forall omega in {1,2}:
  exists! x in B_omega: "Truthful"(x) = "Correct"
$

$
  abs("Cases"(B_1) inter "Cases"(B_2)) = 1
$

The allocation procedure is:

1. initialize a pseudo-random generator using $(s,n)$
2. assign $G_n$ uniformly from:
  $
    ("Active", "Control")
  $
3. choose one shared case:
  $
    C_s in C
  $
4. distribute the remaining four cases such that:
  - two unique cases are added to $B_1$
  - two unique cases are added to $B_2$
5. independently assign exactly one `"Correct"` label per collection
6. shuffle ordering within each collection

This guarantees:
- deterministic reproducibility
- balanced randomization
- constraint satisfaction
- auditability of participant allocation

#pagebreak()

== Reference implementation (Python)

The reference implementation is provided in `./allocate.py`.

#raw(read("allocate.py"), lang: "py")

= Mathematical Definition of automation bias

Automation bias should be represented as a continuous function returning a value in the interval $[0,1]$, indicating the certainty that automation bias occurred.

The parameters are the correctness of the given answer, the rating of said answer, and the confidence in that rating.

$
  B(i,r,c) -> [0;1]
$

where:
- Bias $B$: $[0;1]$ certainty that automation bias was detected
- Integrity $i$: boolean indicating whether the answer was correct
- Rating $r$: ${1;2;dots;5}$ indicating the perceived quality of the answer (very bad $<->$ very good)
- Confidence $c$: $[0;100]$ indicating how certain the evaluator was about the rating

Implementation:

$
  B(i,r,c) = (1 - i)
  dot ((r - 1) / (max(R) - 1))
  dot (c / max(C))
$

with:
- $max(R) = 5$
- $max(C) = 100$

The term $1 - i$ ensures that automation bias can only occur when the given answer was incorrect. If the answer was correct, the resulting bias score is going to be zero independently of the remaining parameters.

The normalized rating term $(r - 1) / (max(R) - 1)$ models the perceived quality of the answer on a continuous scale between $0$ and $1$. Higher ratings increase the bias score, as automation bias is characterized by overestimating incorrect automated outputs.

The confidence term $c / max(C)$ represents the evaluator's certainty in the assigned rating. A high confidence combined with a high rating for an incorrect answer suggests higher certainty of automation bias.

By multiplying all normalized terms, the resulting function produces a continuous bias score in the interval $[0,1]$, where larger values indicate stronger evidence of automation bias.

Minimal automation bias is assumed for ratings above $r > 3$
and confidence values above $c > 50$.

Thus, the minimal acceptable automation bias threshold is:

$
  B_"acceptable" > B(0, 3, 50)
$

Substituting the values into the bias function yields:

$
  B(0, 3, 50) & = (1 - 0)
                dot ((3 - 1) / (5 - 1))
                dot (50 / 100) \
              & = 1 dot (2 / 4) dot 0.5 \
              & = 1 dot 0.5 dot 0.5 \
              & = 0.25
$

Therefore:

$
  B_"acceptable" > 0.25
$

= Evaluation: Comparisons and correlations

With the results of the two sessions, we will have a rich dataset that includes demographic information, participants' views on AI, their interactions with the AI in both sessions, and their responses to the post-test questionnaires.

To analyze the data further, we will perform comparisons and correlations of the collected data. Firstly, we will compare the results of the active group (with disclaimers) and the control group (without disclaimers) in both sessions to see if there are any significant differences in their responses.

Secondly, we will investigate if there is a correlation between the acceptance of AI and the presence of automation bias. This will help us understand if individuals who are more accepting of AI are more likely to exhibit automation bias.

Furthermore, we will compare the results of the two sessions within the active group to determine if disclaimers have a long-term effect on users.
Also, we will compare the control group with itself across the two sessions to check for any changes over time that are not influenced by the disclaimers.

Moreover, we will analyze the correlations between the different dimensions of the UEQ+ (Trustworthiness, Response Behavior, Response Quality) and the participants' ratings of the AI answers (good/bad) to see if there are any significant relationships.
Then we will analyze the correlation between the Risk Handling dimension of the UEQ+ and the presence of disclaimers to see if disclaimers influence users' perceptions of risk.

Finally, we will investigate if there are any correlations between the demographic information (age, gender) and the participants' views on AI, their interactions with the AI, and their responses to the post-test questionnaires to see if there are any demographic factors that influence these outcomes.

= Results

\*(see excel and tally for now)

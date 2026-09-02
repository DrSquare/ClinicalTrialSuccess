---
title: "Dynamic clinical trial success rates for drugs in the 21st century"
source_pdf: "Dynamic Clinical Trial Success Rates for Drugs in the 21st Century.pdf"
doi: "10.1038/s41467-025-64552-2"
article_url: "https://doi.org/10.1038/s41467-025-64552-2"
pages: 22
authors: "Ying Zhou"
generated_from_local_pdf: true
---

# Dynamic clinical trial success rates for drugs in the 21st century

> Text extracted from the local PDF in this repository. Page breaks are preserved as second-level headings for traceability.

## Page 1

Article https://doi.org/10.1038/s41467-025-64552-2
Dynamic clinical trial success rates for drugs
in the 21st century
Ying Zhou1,8, Yintao Zhang 1,8,H a n g w e iX u1,8, Zhen Chen1, Shijie Huang1,
Yinghong Li1,J i a n b oF u2, Hongning Zhang1, Donghai Zhao1, Xichen Lian1,
Yuan Zhou1,X i n y iS h e n3, Kaixuan Liu1,Y u n q i n gQ i u4, Yanzhong Wang 5,
Wanqing Xie6,L i a n y iH a n7,H a i b i nD a i1 & Feng Zhu 1
In clinical drug development, two fundamental questions must be addressed:
what is the success rate of drugs in clinical trial; how does such rate change
over time. Here, a dynamic strategy for calculatingclinical trial success rate
(ClinSR) is proposed, which identifies that: the ClinSR has been declining since
the early 21st century, yet it hits a plat eau and recently starts to increase; the
ClinSR for repurposed drugs is unexpectedly lower than that for all drugs in
recent years; and an extremely low ClinSR is found for anti-COVID-19 drugs. In-
depth analysis reports great variationsamong the ClinSRs of various diseases,
developmental strategies, and drug modalities. A platformClinSR.org(https://
ClinSR.org/), is then developed to show how ClinSRs change over time. All in
all, this work enables accurate, timely and continuous assessment of ClinSRs,
for now and the future, to aid pharmaceutical and economic decision making.
Drug discovery is characterized by a high attrition rate, resulting in
limited annual approvals1. In clinical drug developments, two funda-
mental questions must be addressed:what is the success rate of drugs in
clinical trials?2 and how do such rates change over time?3 The answers to
these questions play critical role in guiding scienti fic and economic
decisions for pharmaceutical company, investor and regulatory
agency
4. Particularly, the resulting success rates are reported to be
useful for optimizing pipeline decisions of pharmaceutical
companies5, enabling prudent resource allocations and adjusting
capital investment strategy of investors 4, and evaluating the effec-
tiveness of regulatory policies in promoting innovation and addressing
unmet medical needs
6. Many studies have been working on addressing
these questions (provided in Supplementary Table S1), and calculation
approaches, represented bypath-by-path
7 and phase transition2, have
been developed for success rate evaluation. Particularly, the path-by-
path method is capable of accurately reconstructing “drug develop-
ment path” by imputing missing clinical trials7,a n dt h ephase transition
o n ec a nc o m p u t et h e‘likelihood of approval ’ by multiplying the
probabilities observed in each clinical stage2. Based on these proposed
approaches, studies were published for measuring the clinical trial
success rates of pharmaceutical industry within certain time frame
8- 11,
w h e r e a so t h e r sf o c u s i n go nt h es p e c ific therapeutic area or disease
indication12- 18.
However, there is huge variation, ranging from 7% to 20%, in
reported clinical trial success rate (ClinSR) among the existing
studies8- 18, the underlying reasons of which may include: ( a) the het-
erogeneity of analyzed data -- the studies relied either on the data of
commercial database8, undisclosed company data9, or domain-specific
data for certain diseases13;( b) t h ed i f f e r e n c ei nc o m p u t i n gp r o t o c o l-- the
calculations were distinct in the size of assessed time-window 8,14,
methodology for imputation of missing data7,11,12,e t c . ;(c) the shift of
studied time frames -- some study targeted the turn of the century 10,
while other analyzed the recent time frame 15. In other words, direct
comparison among those previously-reported ClinSRs can provide
Received: 22 January 2025
Accepted: 19 September 2025
Check for updates
1College of Pharmaceutical Sciences, The Second Affiliated Hospital, Zhejiang University School of Medicine, State Key Laboratory of Advanced Drug Delivery
and Release Systems, Zhejiang University, Hangzhou, China.2Institute of Translational Medicine, Department of Health Sciences and Technology, ETH Zurich,
Zurich, Switzerland.3Yale School of Public Health, Yale University, New Haven, USA.4School of Medicine, Westlake University, Hangzhou, China.5School of
Life Course and Population Sciences, King’s College London, London, UK.6Department of Intelligent Medical Engineering, School of Biomedical Engineering,
Anhui Medical University, Hefei, China.7Department of Dermatology, Huashan Hospital, Fudan University, Shanghai, China.8These authors contributed
equally: Ying Zhou, Yintao Zhang, Hangwei Xu. e-mail: zhufeng@zju.edu.cn
Nature Communications| (2025) 16:9537 1
1234567890():,;
1234567890():,;

## Page 2

limited insight into how investments and technologies affect the pro-
gression of drug development2- 4, and a uni fied standard for data col-
lection and ClinSRs calculation is thus demanded. Furthermore, due to
the lag of time and termination in data collection, it is challenging for
previous studies to timely report the ClinSRs of their publication year,
and it is also impossible to update the ClinSRs for the coming decade.
Thus, great interest lies in developing new strategy facilitating timely
and continuous data collection, as well as the automated assessment of
the latest ClinSRs.
Herein, a systematic analysis on dynamicclinical trial success rate
(ClinSR) of drugs in the 21st century was thus conducted. First,ar i g -
orous and reproducible procedure for data collection and ClinSR
evaluation was established, which worked out the shift over time (from
2001 to 2023) of ClinSRs using 20,398 clinical development programs
(CDPs) involving 9682 molecule entities. To cope with issue of data
heterogeneity, several public databases characterized by transparent,
accessible and up-to-date (ClinicalTrials.gov, Drugs@FDA, etc.) were
used for data collection here. Second,a dynamic strategy for calcu-
lating ClinSRs was proposed. Different from the previous static ones,
this strategy enabled continuous evaluations of and effective com-
parisons among annual ClinSRs. Third, an evaluation of ClinSR was
performed from diverse perspectives (such as various disease classes,
distinct developmental strategies, and different drug modalities),
which offered valuable insight into the current direction of pharma-
ceutical research. Finally, a multi-functional platform ClinSR.org was
developed online (https://ClinSR.org/) to realize the dynamic illustra-
tion of how ClinSRs change over time, realize the automated update of
ClinSR for coming decade, and allow the customized evaluation of
ClinSR for any drug group of interest. In summary, this study could
help to continuously support the pharmaceutical decision-making for
now and the future.
Method
Collection of drug information and procedure for data
standardization
Data collection in this study consisted of two sequential procedures:
(a) the accumulation of drug data from exiting databases, and (b)t h e
data standardization facilitating subsequent analysis.
Collection of drug data from established databases
Comparing with other existing databases, the ClinicalTrials.gov had
long been considered as one of the most in fluential resources of
clinical trial drug and clinical testing information, which had rapidly
expanded since 2007 due to the official supports from U.S. FDA (2007
FDA Amendments Act required all clinical trials to be registered into
ClinicalTrials.gov). In this study, to ensure the reliability of clinical
information and maintain the high criteria of data inclusion among
different years, ClinicalTrials.gov was adopted as the resource for
collecting the data of clinical trial drugs. To assess the diversity of
ClinicalTrials.gov data, the locations of all clinical trials were analyzed.
Supplementary Fig. S1 demonstrated the distributions of clinical trial
data among continents: North America (32.5%, USA, Canada, etc.),
Europe(39.7%, United Kingdom, France, etc.),Asia (19.5%, China, Japan,
Korea, etc.), and Others (8.3%, Australia, Brazil, etc.), which showed
that those drug development efforts started outside the United States
were also included here.
Moreover, the data of approved drugs were systematically col-
lected from the official website of U.S.FDA. As provided in Table1,t h e
explicit number of new drugs approved each year collected to this
study was given, resulting in 828 molecular entities and 142 biological
products approved and regulated by Center for Drug Evaluation and
Research (CDER) and Center for Biologics Evaluation and Research
(CBER), respectively. Notably, one molecular entity after its initial
approval by either CDER or CBER could be approved for another
indication (successful drug repurposing). Taking thealemtuzumab as
example, it was first approved in 2001 for the treatment of B-cell
chronic lymphocytic leukemia, and later approved in 2014 for multiple
sclerosis, both of which had been collected to measure ClinSRs in this
analysis. The numbers of successful repurposing projects for all drugs
and those approved prior to 2000 each year are also given in Table 1.
Particularly, a total of 98 drugs (approved before 2000 for one disease
and later approved for another after 2000) were included into this
study, and a total of 207 drugs (approved before 2000 for one disease
and later tested in the clinical trials for another after 2000) were also
collected. Taking thecladribineas an example, it was first approved in
1993 for the treatment ofhairy cell leukemiaand later approved in 2019
for multiple sclerosis. Another example would be topiramate,w h i c h
was initially approved for generalized tonic-clonic seizures in 1996,
followed by a clinical evaluation in Phase 3 for treatingobesityin 2000.
B a s e do nt h ei n f o r m a t i o ni nT a b l e1, it was obvious that the drug
repurposing was quite active in the past two decades. Another two
reputable databases included in this study for drug information col-
lection are Therapeutic Target Database
19 and DrugBank20,w h i c h
facilitated this work by confirming drug modality, key pharmaceutical
properties, physicochemical characteristics, etc. This information was
crucial for ensuring the customized analysis of ClinSR for a particular
group of clinical trial drugs.
Table 1 | The explicit numbers of annually approved drugs
analyzed in this study, collecting from the official online site
of the U.S. FDA
Year of
approval
FDA CDER FDA CBER Drug repurposing
NDA BLA BP All Repo Pre-2000
ALL 628 200 142 454 145
2023 38 17 16 23 2
2022 22 15 8 31 5
2021 36 14 10 35 4
2020 40 13 5 35 4
2019 38 10 5 28 4
2018 42 17 3 26 3
2017 34 12 9 27 3
2016 14 8 4 18 2
2015 32 13 12 9 3
2014 30 11 10 28 8
2013 25 2 7 20 7
2012 31 8 4 17 6
2011 24 6 4 8 2
2010 14 7 5 12 8
2009 19 6 8 13 7
2008 21 3 5 13 2
2007 17 2 4 19 5
2006 18 4 4 17 11
2005 15 5 5 15 11
2004 30 6 0 20 16
2003 21 6 4 12 11
2002 19 6 3 12 6
2001 24 4 3 10 9
2000 24 5 4 6 6
A total of 828 molecular entities, including 628 new drug applications (NDAs) & 200 biologics
license applications (BLAs), approved by FDACenter for Drug Evaluation and Research(FDA
CDER) were collected. Moreover, a total of 142 biological products (BPs) approved by the FDA
Center for Biologics Evaluation and Research(FDA CBER) were accumulated. The numbers of
successful repurposing projects (All Repo) and repositioning count of pre-2000 approved drugs
(Pre-2000) were provided.
Article https://doi.org/10.1038/s41467-025-64552-2
Nature Communications| (2025) 16:9537 2

## Page 3

Data standardization for the drugs in clinical trial
Clinical trial drug data were collected from ClinicalTrials.gov (version of
Jan, 2024). To make it usable for our success rates analyses, several data
standardization steps were sequentially applied.First, a number of trials
were excluded from this analysis, such as the ones with no clinical status
provided (did not indicating the phase status), the ones with no clear
trial time provided, the ones with no drug tested (dental implant, liver
transplant, aerobic exercise, etc.), the ones not designed for the efficacy-
related studies (drug-drug interaction studies, etc.), and the ones with
vague drug name. Taking the exclusion of stem-cell/other biologic-
based projects with vague drug names as an example, many trials were
identified, like NCT03259217, NCT04863066 and NCT04125329 with a
drug name of “stem cell product”, “CAR-T cells” and “human umbilical
cord mesenchymal stem cells”, respectively. Since these names were too
vague to make the determination of whether they progressed to the
next stage of development, they were excluded from this study.
Meanwhile, for the clinical trials providing concrete drug names, such as
NCT04443907, NCT05166070 and NCT04125329 with a name of
“genome-edited hematopoietic stem and progenitor cell OTQ923”, “MSLN-
CAR-T cell RD133” and “embryonic stem cells-derived mesenchymal stem
cell MR-MC-01”, respectively, they were all included in this study. Addi-
tionally, the impacts of excluded trials on the ClinSR were assessed.
Overall, 2.3% of all clinical trials retrieved from ClinicalTrials.gov were
identified as having unclear drug name. An exclusion of this subset of
trials may lead to an overestimation of ClinSR, as some of these trials
may form the independent CDPs, and would be considered as“failure” if
included into this analysis. However, we cannot arbitrarily include this
subset into our work, as it would lead to excessive ClinSR under-
e s t i m a t i o n .I no t h e rw o r d s ,t h ee x c l u s i o no ft h et r i a l sw i t hu n c l e a rn a m e
is necessary, though it will inevitably lead to a certain degree of ClinSR
overestimation (excluded trials only account for less than 2.5% of the
total trials retrieved from ClinicalTrials.gov). The in-depth analyses of
specific therapeutic areas revealed that infection, immune system dis-
ease, and oncology are three of the m ost affected areas by trials with
unclear name, which primarily originated from two drug modalities:
vaccines and cell therapies, which indicated that their ClinSRs may be
somewhat overestimated.
Second, detailed information for each trial was systematically
collected, which included trial ID, drug name, developmental status
(such as Phase 1, Phase 2/3), disease indication, master protocol,
noninferiority trial, date of trial start/study completion, recruitment
status, etc. Taking the master protocols (basket and umbrella trials)
and noninferiority trials as an example, both were carefully standar-
dized in our analysis. In particular, a basket trial (containingn diseases/
histologic features) was split to n drug-disease projects (e.g., thebar-
icitinib was tested by basket trial NCT05189106 for treating neurode-
generative Alzheimer’sd i s e a s eand amyotrophic lateral sclerosis,w h i c h
was thus split to two drug-disease projects); an umbrella trial (studying
m drugs in diverse population groups for single indication) was split to
m drug-disease projects (e.g., trastuzumab, durvalumab,a n d panitu-
mumab were clinically tested in umbrella trial NCT05845450 for
treating molecularly selected resectable colorectal cancer,w h i c hw a s
thus split into three drug-disease projects); and for noninferiority
trials, only the experimental molecular entity other than the “active
comparator” was adopted to form drug-disease projects (e.g., dapa-
conazole was tested in a noninferiority trial NCT02606383 for treating
tinea pedis,w h i l eketoconazole was used as active comparators. Only
the experimental molecular entitydapaconazolewas thus used to form
drug-disease project).
Third, the potential incompleteness in the synonyms data of
ClinicalTrials.gov could hamper the accurate tracking of the same drug
over time, particularly in cases involving sponsor acquisitions or
change in drug research codes. To address this problem, a multistep
strategy was implemented to ensure the accurate classification of the
same drug. Step-1, we leveraged the built-in synonyms library of
ClinicalTrials.gov to provide synonym mappings for interventions,
which helped us to discover most of the trials under different names
but referring to the same drug (according to our experience, the built-
in synonyms library of ClinicalTrials.gov is powerful, which can accu-
rately map the synonyms for the vast majority of the drugs).Step-2, to
further enhance the completeness of drugs’synonyms, the data from
several established databases (such as: AdisInsight, DrugBank, Drug-
MAP, Pharmaprojects, PubChem and TTD) were systematically col-
lected, which helped tofind a number of synonyms data unavailable in
the built-in synonym library of ClinicalTrials.gov. For example,
“NEOD001” is the developmental code name of “birtamimab” during
its early phase development, but they were not matched by the built-in
library of ClinicalTrials.gov. In our study, these two synonyms were
identified in AdisInsight, DrugBank, DrugMAP, TTD,e t c . ,w h i c hw e r e
then included into the synonym library of this study. In other words, in
this study these two names were classifie da st h es a m ed r u g .Step-3, an
in-depth manual checking was conducted to discover those miss-
matched by these established databases (different names belonging to
different drugs), which were then removed from the resulting syno-
nym data for ensuring the data accuracy. All in all, the multistep
strategy above could help to ensure that the trials involving the same
drug were grouped together, regardless of their naming variation.
Additionally, to deal with the data of non-new molecular entities (NME)
products, the method applied in previous publications
21,22 was adopted
in our analysis. Particularly, the formulations, dosages or biosimilars of
a drug for certain disease were merged to the same drug. That is to say,
those non-NMEs would not be reg arded as new drugs. Taking the
ivermectin clinically tested for COVID-19 as example, ivermectin pow-
der (NCT04681053) andivermectin injectable solution(NCT04472585)
were merged into a drug of ivermectin. This meant that ivermectin in
powder form was not be treated as a new drug here.
Fourth, a multistep process was further adopted in this analysis to
enable disease standardization and classification.Step-1, the synonyms
of disease indications were matched based on a built-in library of
ClinicalTrials.gov. Taking the COVID-19 as an example, Clinical-
Trials.gov offered an extensive list of synonyms (over 20), which
included SARS-CoV-2 infection, coronavirus disease 2019, 2019 nCoV
infection, 2019 novel coronavirus disease, and so on. Leveraging this
synonym library, we achieved the preliminary standardization of dis-
ease name. Step-2, standardized names were then mapped to WHO
International Classification of Disease (ICD-11). ICD-11 featured a hier-
archical classification system (spanning Chapter, Category,a n d Sub-
category) that served to standardize disease nomenclature. In this
study, we discovered theCategory-level ICD codes for all diseases after
name standardization. Taking giant cell glioblastoma as an example,
the API of ICD-11 can automatically assign a Subcategory-level code of
2A00.00 to this disease. From this, we derive correspondingCategory-
level code of 2A00, which ultimately categorized this disease under
“brain cancer”. Step-3, during the aforementioned steps, certain dis-
ease names may fail to be automatically matched. In such cases, their
corresponding ICD codes were determined through manual validation.
Additionally, the manual check was also performed to verify the
reliability of the results identi fied in previous steps. All in all, our
analysis employed a standardized procedure for disease standardiza-
tion and classi fication with minimal reliance on manual checking.
Finally, according to the approach used in previous analysis
2, Phase 1/2
trials were considered as Phase 2, and Phase 2/3 trials were regarded as
Phase 3 in the ClinSR assessments of this study.
Development program identification for a drug of distinct
disease
The CDP of a drug for the treatment of a disease was formed by
merging all trials of this drug treating the same disease, and those trials
of this drug treating other diseases were used to generated new CDPs.
In cases where a drug, particularly the anti-neoplastic one, begins its
Article https://doi.org/10.1038/s41467-025-64552-2
Nature Communications| (2025) 16:9537 3

## Page 4

early-stage trials with a broadly-defined disease indication (e.g., solid
tumor), but later continues its clinical development in a speci fically-
defined one (e.g., lung cancer ), a method to aggregate CDPs was
provided. Particularly, if the drug progresses to higher clinical phase
(e.g., from Phase 1 to Phase 2) in a speci fic indication (such as lung
cancer), the Phase 1 of solid tumor would be integrated with the Phase
2 trial of lung cancer; if the drug does not progress to a higher clinical
phase and remains at an earlier stage (e.g., Phase 1), it would be
retained with solid tumor to form a CDP of broad indication. This
approach ensured that the development trajectory of the CDP was
properly captured, particularly in cases where the drugs transitioned
from broad disease indication in early-stage trial to a speci fic one in
later phase. For speci fic CDP (treating the same indication), all trials
were then filled into CDP based on their time of trial start & com-
pletion. If multiple trials of different statuses appeared in one year,
only the one of highest phase would be considered. Taking the drug
vilaprisan as an example (offered in Fig. 1), it had been tested in
clinical trial for two indications ( endometriosis and uterine leio-
myoma), which led to two distinct CDPs for “vilaprisan”. All in all, a
total of 20,398 CDPs corresponding to 9682 unique molecular enti-
ties for treating 910 disease indications de fined by the WHO ICD-11
(acute myeloid leukemia , cholera, hyperlipoproteinemia, migraine,
thalassaemias, etc.) were collected for analysis.
Strategy for calculating the clinical trial success rate (ClinSR) of
studied drugs
Describing progression of clinical development program (CDP).T o
describe the progression of any studied CDP within a time-win-
dow, it is critical to know how drug ’s clinical status was changed.
There were three clinical statuses (Phase 1, Phase 2 and Phase 3)
that could be changed in a CDP. Taking the Phase 1 as an example,
if it successfully progressed to a higher status (Phase 2, Phase 3 or
approval) in a studied time-window, the progression under Phase
1 was considered to be “Success” in this work. There were some
circumstances in which a clinical trial was considered as “Failure” :
if a trial was labeled as discontinued or terminated in Clinical-
Trials.gov and no new trial was initiated after this discontinua-
tion/termination within the studied time-window; if a drug had
not undergone new clinical trial for a disease for over 2-years (the
rationale behind the selection of this 2-years threshold for a
period of time with no new trial were explicitly discussed in the
following section entitled “2.3.3 Determining the Threshold to
Define Trial Failure ” and Supplementary Figs. S2-S3) and had not
returned to active program in studied time-window. Otherwise,
the progression under a trial was de fined as “Ongoing” . It should
be noted that if a trial progresses to higher phase (e.g., from
Phase n to Phase n + 1) within measured time-window, even if the
time interval between the completion of Phase n and the initia-
tion of Phase n + 1 exceeds two-years, this trial would also be
treated as “Success” .T a k i n g olokizumab in the time frame of
2010- 2018 as the example, although an interval between its
completion of Phase 2 in 2013 (NCT01463059) and the initiation
of Phase 3 in 2016 (NCT02760368) exceeded 2-years, Phase 2 was
considered as “successfully progressed ” to Phase 3 in 2010 - 2018.
In other words, the CDPs brought back to active program would
not be “Failure” here. Some drugs were approved from Phase 1
and Phase 2 (like accelerated approvals), which was especially the
case for the rare disease space. Under this circumstance, a Phase
3 trial was usually missed from the CDP. To deal with this situa-
tion, the clinical progression from Phase 2 to Phase 3 was counted
in this study, and so do the clinical progression from Phase 3 to
approval. In other words, for a particular approval (e.g., acceler-
ated approval), a direct jump from Phase 2 to approval will be
regarded as the clinical progressions of both Phase 2 to Phase 3
and Phase 3 to approvals, which could effectively avoid possible
“missing” of approvals. Meanwhile, if Phase 2 was missed, a
strategy similar to the above one would be adopted, which will be
considered as the clinical progressions of both Phase 1 to Phase 2
and Phase 2 to Phase 3.
Computing rates of overall success and phase success
To systematically assess the clinical trial success rates (ClinSRs) of
drugs within a time-window ðtbegin , tend Þ,f o u rk e ym e a s u r e m e n t s
should be calculated, which included: P1SRðtbegin , tend Þ,
P2SRðtbegin , tend Þ, P3SRðtbegin , tend Þ,a n d OSRðtbegin , tend Þ.P a r t i c u l a r l y ,
the P1SR denoted the success rate of clinical progressions from Phase 1
to Phase 2, theP2SR referred to the success rate of clinical progressions
from Phase 2 to Phase 3, and the P3SR indicated the success rate of
clinical progression from Phase 3 to final approval. Taking the
P1SRðtbegin , tend Þ as an example, the n1
Success ðtbegin , tend Þ indicated the
total numbers ofSuccess Phase 1 progressions within the studied time-
window, while the n1
Failure ðtbegin , tend Þ denoted the total number of
Failure Phase 1 progressions in the same time-window. Thus, the
P1SRðtbegin , tend Þ was used to calculate the success rate of the clinical
Fig. 1 | The de finition of the clinical development programs(CDPs) based on
drugs and their corresponding diseases.The CDP of a drug for the treatment of a
disease was created by merging all trials of this drug treating same disease, and the
trials of this drug treating other diseases were used to generate new CDPs. Taking
“vilaprisan” as an example, it was clinically assessed for two diseases (endometriosis
and uterine leiomyoma), which led to two distinct CDPs for this drug.
Article https://doi.org/10.1038/s41467-025-64552-2
Nature Communications| (2025) 16:9537 4

## Page 5

progressions from Phase 1 to Phase 2 using the following equation:
P1SRðtbegin , tend Þ = n1
Success ðtbegin , tend Þ
n1
Success ðtbegin , tend Þ + n1
Failure ðtbegin , tend Þ ð2:1Þ
Similarly, the success rates of clinical progressions from Phase 2
to Phase 3 and from Phase 3 to final approvals could be assessed by
P2SRðtbegin , tend Þ and P3SRðtbegin , tend Þ. Apart from the three key mea-
surements for assessing phase success rate , OSRðtbegin , tend Þ was
adopted in this study to denote the overall success rate (OSR) from
Phase 1 to approvals, which could be calculated by multiplying three
phase success rates P1SR, P2SR,a n dP3SR using the following equation:
OSRðt
begin , tend Þ =
Y
i =1 ,2 ,3
PiSRðtbegin , tend Þ ð2:2Þ
Determining the threshold to define trial failure
Based on our comprehensive literature review, a period of time with no
new trial (PTnT) threshold of“2-years” was considered as“failures” by a
variety of existing studies 22- 24, which was, in our opinion, the sum-
marization of authors’ domain knowledge. In addition to “2-years”,a
threshold of “1-year” 11 and “1.5-years” 8,25 were also reported by pre-
vious publications. Furthermore, several commercial databases (such
as: AdisInsightand IMS Health R&D Focus) were reported to adopt 1.5-
years or 2-years as indicators of“no development reported”
25,26,w h i c h
implied that some of the available studies, such as 2 and3, without
clarifying their PTnT thresholds (but using commercial databases)
might be based on the thresholds of1.5- or 2-years in fact. All in all, our
comprehensive literature reviews found that the selection of PTnT ’s
threshold varied among existing studies, and none of them conducted
the exploration of the rationale be hind their selection of threshold.
Although most of the analyses used “1.5-years” and “2-years” as
thresholds, it remained challenging to conclude the optimal one for
PTnT when determining the“failure” of clinical trials in a studied time-
window.
Because of the possible subjec tivity introduced by authors ’
domain knowledge, it was critical to perform objective (both quanti-
tative and statistical) assessment on the robustness of our “2-years”
assumption. Therefore, a method assessing such robustness by com-
paring with thereal data was proposed. As described in Supplementary
Fig. S2, N CDPs and their progressions within theStudied Time-window
(light orange background) were illustrated. Theoretically, when cal-
culating the ClinSRs for Studied Time-window, we did not know what
would happen in Later Time-period(light blue background). However,
since thereal progression data inLater Time-periodhad been collected
f o ra l lC D P s ,w ew e r ea b l et or e l yo nt h e s ereal data to determine the
“failure” of studied CDPs. For example, according to thereal data of the
Later Time-period, Phase 2 of CDP-1 should not be considered as
“Failure” in the last year of Studied Time-windows;i fa 1-year threshold
w a su s e df o rP T n T ,P h a s e2o fC D P - 1w o u l db er e g a r d e da s“Failure”;i fa
2-year threshold was used, Phase 2 of CDP-1 would not be viewed as
‘Failures’. Under this circumstance, a2-year threshold could effectively
reflect the real failure, while the 1-year could not. Clearly, the CDP-3,
CDP-6, CDP-7, CDP-9 & CDP-N were all“Failures” based on the
real data.
In other words, the real data could be used to evaluate whether
threshold was appropriately set. The closer the OSRs (assessed based
on a threshold) to thereal OSRs, the more appropriately the threshold
was selected.
For the Later Time-period, it was also important to provide each
CDP an adequate period of time for determining the “failures”.I nt h i s
study, a Later Time-period of five years was adopted, which was 2.5
times longer than the maximum threshold reported previously
(2-years), and a sensitivity analysis on the selection of five years dura-
tion was demonstrated in Supplementary Fig. S3a. As offered on the
left side of Supplementary Fig. S3a, all lines followed a similar trend
with greatly limited variation among the OSRs of different durations.
The robustness among durations were further given on the right
side of Supplementary Fig. S3a. As shown, relative difference between
the last two adjacent durations (5 to 6 years & 6 to 7 years) were
consistently lower than 2%, which were signi ficantly lower ( p-values
< 0.05) than that of thefirst two (3 to 4 years & 4 to 5 years). Moreover,
no significant difference (ns) was found between the last two boxplots
( 5t o6y e a r s&6t o7y e a r s )o nt h er i g h ts i d eo fS u p p l e m e n t a r yF i g .S 3 a ,
which denoted that a duration of ≥5 years was large enough for Later
Time-period, and the minimum size of five years was therefore chosen
to be the most appropriate duration in this study.
Based on the real data, we were finally capable of assessing the
robustness of thresholds selection. As shown in Supplementary
Fig. S3b, the orange line with triangle provided the OSRs based onreal
data, and the OSRs calculated based on different thresholds for PTnT
were also described (three solid lines in green, black, and blue were
based on the threshold of1-year, 2-years,a n d3-years, respectively, and
the threshold of the dash lines between two adjacent solid lines
increased quarterly). As shown, the line of real OSR fell between the
lines based on 2-years and 1.75-years thresholds. Supplementary
Fig. S3c further demonstrated the relative difference between the line
of the real OSRs and each of the lines using different thresholds. As
provided, the lines based on2-years and 1.75-yearsthresholds resulted
in the lowest relative differences, when comparing with the line ofreal
OSR (consistently lower than 10%), which might denote that these two
were the most appropriate ones among all assessed thresholds.
Although no signi ficant difference was observed between the box-
plots of 2-years and 1.75-years thresholds, we would like to select the
2-years threshold to support the analyses in our study because of the
following two reasons. First
, the selection of 2-years thresholds mat-
ched better with the annual-based nature of this study than1.75-years.
Second, the lines using real data of the most recent time-windows in
Supplementary Fig. S3b were much closer to the 2-years line than the
1.75-yearsone, which might give better description on the recent time-
windows and the time-windows of the coming decades.
Finally, in-depth analysis on the intervals between the progression
from one clinical phase to the next was systematically performed, and
about 7.5% of the clinical trials were found taking longer than2-yearsto
progress to the next phase. If 7.5% were included into our study by
extending the thresholds (for example, from 2-year to 3-year), a large
number of CDPs will not be regarded as “Failure”. For example, as
descried in Supplementary Fig. S2, CDP-3, CDP-6, CDP-7, CDP-9, and
CDP-N would be regarded as“Failure” if a 2-yearsthreshold was chosen,
while only CDP- N was regarded “Failures” if shifting to a 3-years
threshold. The exclusion of four “Failure” CDPs would inevitably
overestimate the OSR, which was the reason why the 3-years-based
OSRs were obviously higher than those of the 2-years-based ones
(illustrated in Supplementary Fig. S3b; overestimated by 5.2% in
2001- 2009 time-window and 1.3% in 2010- 2018 time-window).
Determining time-window size for calculating ClinSRs
Before assessing the success rate of clinical trial drugs, it was a pre-
requisite to set a time-window ofN years size. To explore the variations
induced by the selection of different window sizes, the sensitivity
analyses were therefore performed in this study to determine the
optimal sizeN, which were explicitly offered in Supplementary Fig. S4.
Supplementary Fig. S4a provided the OSRs assessed based on seven
different window sizes (from 6 years to 12 years); Supplementary
Fig. S4b illustrated the relative differences between two colored lines
in Supplementary Fig. S4a of the adjacent time-window size (for
example, 8 to 9 years, 9 to 10 years, 10 to 11 years, etc.); and Supple-
mentary Fig. S4c demonstrated the OSR calculated based on four
window sizes (3 years, 4 years, 5 years, and 9 years). As offered in
Supplementary Fig. S4a, all lines showed similar descending trend, and
Article https://doi.org/10.1038/s41467-025-64552-2
Nature Communications| (2025) 16:9537 5

## Page 6

the lines of 9 to 12 years shared much closer shape than that of 6 to 8
years. Such results indicated that the larger the time-window size, the
more robust the dynamic OSRs. The robustness of the four lines (9 to
12 years) could be further identi fied in Supplementary Fig. S4b. As
illustrated, the relative differences between the last three adjacent
time-window sizes (9 to 10 years, 10 to 11 years & 11 to 12 years) were
consistently lower than 5%, which were signi ficantly smaller
(p-values < 0.05) than that of the first three (6 to 7 years, 7 to 8 years,
8 to 9 years; 44.4% and 13.3% of their relative differences were larger
than 5% and 10%, respectively). Meanwhile, no signi ficant difference
(ns) was found among the last three boxplots (9 to 10, 10 to 11 & 11 to 12
years) in Supplementary Fig. S4b, which indicated that the window size
of ≥9 years was large enough to calculate ClinSRs, and the minimum
size of nine years ( N = 9) was therefore chosen. Moreover, Supple-
mentary Fig. S4c provided a comparison among four different lines
(3, 4, 5 and 9 years). It was apparent that much greater fluctuations
were observed for the lines of 3- 5 years, when compared with that of
9 years. Above results aligned well with the statements in previous
study
27 that an appropriate window size should be large enough to
offer a drug adequate period of time to reach its final fate, and an
extended window was able to “draw reliable conclusions” for success
rate assessment5. Taking together, our sensitivity analyses suggested
that the selection (N = 9) here was appropriate in term of the robust-
ness of the calculated ClinSRs. However, with the increase of the time-
window size (from nine to twelve), there remained subtle differences
among the calculated success rates. This highlighted that it was critical
to maintain a consistent window size when comparing the ClinSRs,
especially for the case requiring high resolution in success rate
assessment. In other words, when it comes to a situation that the time-
window size matters, the selection of nine-year time-window may not
be appropriate enough, and our reported ClinSRs should be con-
sidered with caution.
All in all, a dynamic strategy for the measurement of ClinSR was
proposed in this analysis, which integrated three key components: (a)
publicly-available database, (b) effective data standardization, and (c)
systematic assessment of strategy’s robustness. Different from those
previous “static” ones, our strategy enabled the continuous measure-
ments of and effective comparisons among annual ClinSRs. The reason
behind such abilities was largely due to the collection of data from
publicly-accessible database (including ClinicalTrials.gov,
Drugs@FDA, etc.), which were characterized by transparent, acces-
sible and up-to-date. This data adoption approach was distinct from
that of previous analyses relying on their own company data
9,t h ed a t a
of certain diseases13, and the data of commercial database2.A sk n o w n ,
the resulting ClinSRs of those available studies were highly data-
dependent, which led to substantial difficulty in comparing the ClinSRs
among time-windows. All in all, due to the integrations of three key
components into this analysis, the assessment of the ClinSR variation
among different time-windows wasfinally realized.
Ethical statement
As this study only used de-identified data from databases and did not
have any access to potential identi fiable information, this study is
considered non-human subject research and therefore exempted by
IRB and consent.
Results
Measuring the change of ClinSRs over time-windows for
all drugs
With the dramatic investment increase and continuous technological
advance during the past two decades 28, researchers were curious
about how clinical trial success rate (ClinSR) was affected over time.
Herein, the dynamics ClinSRs of 15 time-windows from the beginning
of 21st century to now were assessed using CDPs and molecular enti-
ties (MEs). These two helped to answer the question: “what are the
probabilities that a drug developed for a speci fic indication (CDPs-
based) or any indication (MEs-based) will reach approval?”
2.
Dynamic ClinSRs evaluated based on clinical development
programs (CDPs)
Figure 2a gave the change of CDPs-based ClinSRs over time. As
shown, the phase success rates (PSRs) of P1SR, P2SR, and P3SR
were described using bars in blue, yellow, and red, respectively,
and the dark line with dots indicated the changes of OSR over
time. It was clear that the OSRs had been declining over time, and
remained stable around 5% in recent years. In other words,
d e s p i t et h ee x t e n s i v ee f f o r t sm a d et oa l m o s te v e r ys t e po fd r u g
development
29, it remains in a dilemma. Herein, literature review
was thus performed to find out potential causes driving the
decline of OSRs. First, such decline was reported to be a “natural
consequence ”30, because the low-hanging fruits being all har-
vested, leaving behind more dif ficult targets and drug candidates
to work on. Second, the ever-expanding collection of approved
drugs might introduce great complexity of new drug develop-
ment process and raise the regulatory standard for approval
31.
Third, the surge in capital investment and clinical trial activities
might further intensify the competition in drug development,
making it very dif ficult for non- first-in-class /non-best-in-class
drugs to achieve return on investment and ultimately leading to
discontinuation
32. Despite the potential causes, the falling success
rates might also re flect more appetite and room for increased
scientific risk in drug discovery, with the expectation for ef ficacy
and safety continue to rise 33. One reason behind the high OSRs at
the early 21st century might partially come from the lack of
mandatory trial registration policy. Particularly, the Clinical-
Trials.gov data became increasingly comprehensive, due to the
issuances of International Committee of Medical Journal Editor
(ICMJE) policy
34 and FDA Amendments Act (FDAAA)35 in 2004 and
2007, which indicated that some trials might be missing in Clin-
icalTrials.gov at the early time-windows, therefore likely in flating
t h eO S R sa tt h ee a r l y2 1 s tc e n t u r y .
An in-depth analysis of Fig.2ai d e n t ified that the P2SRs (yellow) of
every time-window were consistently lower than P1SR (blue) and P3SR
(red), which indicated that Phase 2 (studying drug ef ficacy, assessing
tolerability, finding appropriate dosages, evaluating safety, etc.)
remained one of the most challenging steps in clinical drug
development
36. Similar result was identi fied by a variety of available
studies2,3,7,22. Based on our literature reviews, some of the explanations
might include: Phase 2 was assessed with the most critical eye before
embarking on an expensive, resource-consuming, and risky Phase 3
trial
37, and some companies might become risk-averse to launching
Phase 3 trials due to their limited tolerance for potential clinical trial
risks. Moreover, P1SR (blue) was found to continuously decline from
~70% to ~50%, during the past two decades. As reported, the objectives
of current Phase 1 evaluation were gradually expanded to assess some
part of pharmacokinetics/pharmacodynamics and efficacy besides the
previous safety evaluation
38, and the so-called “quick-kill” strategy
rapidly adopted in pharmaceutical companies brought up more drug
candidates to terminate the inferior ones in an earlier stage, especially
Phase 1
39. All these important factors might collectively contribute to
the continuous declines of P1SR, but we had no way to know based on
the current analysis. In the meantime, a recent analysis reported that
the P1SR for clinical development of drugs in China across all diseases
was only 34% (2011 - 2015) and 20% (2016 - 2020), which was much
lower than the observation in this study (P1SR = ~50% in recent time-
window of Fig. 2a). As reported, such discrepancy might result from
the extensive variation among the regional regulatory frameworks of
different countries
40.
It was also found in Fig. 2a that P3SR (red) had gradually declined
since the beginning of this century, and in contrast to both P1SR and
Article https://doi.org/10.1038/s41467-025-64552-2
Nature Communications| (2025) 16:9537 6

## Page 7

P2SR, the P3SR demonstrated further decline in recent time-windows
(from 2013- 2021 to 2015- 2023). It was reported that comparing with
the protocol design of Phase 3 in 2001- 2005, the complexity of that in
2011- 2015, had increased by 70%41. Increased complexity also resulted
in longer cycle time, higher numbers of protocol amendments, or
lower patient recruitment/retention rate41,w h i c hg r e a t l yc o n t r i b u t e d
to the clear decline of P3SR in the first eight time-windows of Fig. 2a.
Moreover, the further decline of P3SR in the recent three windows of
Fig. 2a primarily came from the dramatic decreases of P3SR in some
major disease classes, such as infectious/parasitic disease, metabolic
disease, circulatory system disease, and so on. Taking the infectious/
parasitic diseases as example, tremendous clinical trials for COVID-19
were tested, and the majority of the Phase 3 clinical trials were
reported to end in failure
42, which contributed to the decline of P3SR in
recent years. The impact of COVID-19 related clinical trials on ClinSR
were further discussed in the following section.
Dynamic ClinSRs evaluated based on molecular entities (MEs)
Figure 2b showed the change of MEs-based ClinSRs over time, which
identified a trend of OSRs (dark line with dots) similar to that of CDPs-
based evaluation (as shown in Fig.2a). Moreover, similar to Fig.2a, the
P2SR (yellow) of each time-window was found consistently lower than
P1SR (blue) & P3SR (red), and the decline of both P1SR (blue) and P3SR
(red) was observed in the past two decades. As a result, both CDPs-
based and MEs-based evaluations revealed that the OSRs had been
declining over times. However, the resulting MEs-based OSRs were
consistently higher (almost two times) than that of the CDP ones
(Supplementary Fig. S5a), and the MEs-based PSRs were identified to
be higher than that of the CDP ones (Supplementary Fig. S5b). In other
words, the CDPs-based calculation (considering all indications) tended
to result in lower probability of success than the MEs-based one
(regardless of different diseases). Reasons behind the difference
between CDPs-based and MEs-based success rate assessments could
be explained using the following scenario. A drug is developed for two
diseases, and both progress from Phase 1 to 3, but one fails in Phase 3
and the other succeeds in gaining FDA approval. If based on MEs,
success rate will be 100%, while CDPs-based assessment will give a 50%
success for all diseases, which thus lead to a lower probability of CDPs-
based success than the MEs-based one. Moreover, a marginal but
noticeable increase in OSR were observed in 2012- 2020 and the sub-
sequent time-windows- rising from 12.9% for 2011- 2019 to about 14.5%
for the following time-windows as described in Fig. 2b, which was in
Fig. 2 | The dynamicclinical trial success rates(ClinSRs) calculated in this study.
a Dynamic ClinSR assessed based on clinical development programs (CDPs).
b Dynamic ClinSR evaluated based on molecular entities (MEs). A nine-year time-
window was adopted to evaluate the ClinSR, providing a drug adequate period of
time to reach its final fate and a total of fifteen time-windows (from 2001- 2009 to
2015- 2023, inclusive) were measured. The variations ofoverall success rate (OSR)
for all CDPs/MEs over time were given using the dark solid-line with dot,w h i l et h e
OSRs for CDPs/MEs aiming at US approval discussed in theSection 3.5.1(grey dash-
line with triangle) and for those after the collective adjustmentproposed in the
Section 3.5.3 (purple dash-line with diamond) were described. The phase success
rates (PSRs, including P1SR, P2SR and P3SR) for all CDPs/MEs were illustrated using
bars in BLUE, YELLOW and RED, respectively. Source data are provided as a Source
Data file.
Article https://doi.org/10.1038/s41467-025-64552-2
Nature Communications| (2025) 16:9537 7

## Page 8

accordance with those recent publications28,43 reporting the gradual
increase of trial success rate in recent years.
Dynamic ClinSRs evaluated based on industry-sponsored CDPs
The extra analyses differentiating the industry-sponsored CDPs from
the non-industry-sponsored ones (for example, academic trials) were
also conducted in this analysis. The funder type of trials in Clinical-
Trials.gov was carefully identified, which grouped all trials in our study
into: industry-sponsored, NIH-sponsored, and others (university/col-
lege-sponsored, hospital-sponsored, and so on). Figure 3ag a v et h e
distribution of trials among clinical statuses. The percentage of
industry-sponsored Phase 3 trial (27.4%) was much higher than non-
industry one (17.2%), which denoted that some academic trials (for
example Phase 1 and 2) were mechanistic in nature, and there was no
pre-specified intentions to progress to Phase 3
44.F i g u r e3b, c provided
overall success rates(OSR) and PSR of industry-sponsored (Green) and
all (Black) CDPs, and both types of success rate for industry-sponsored
trial were found higher than that of all trials. In other words, the above
findings denoted that, for non-industry-sponsored trials (such as lack
commercial backing), there was lower intention of pursuing regulatory
approval
45.
Moreover, ClinSRs of large pharmaceutical companies and bio-
tech firms were assessed, and the differences were further discussed.
First,t h ed a t ao fsponsor in ClinicalTrials.gov were collected for each
trial, and all those retrieved sponsors were manually checked to
determine whether they were biotech firms or not. Then, the world’s
top-20 large pharmaceutical companies released by Citeline (https://
insights.citeline.com/) were collected, and all the sponsors retrieved
above were further checked to discover the trials initiated by top-20
companies. Finally, the ClinSRs for top-20 pharma companies and
biotech firms in recent time-windows were computed. As provided in
Fig. 3d, the OSRs for leading pharma company and biotech firm
remained steady across time-windows, and the top-20 large pharma
companies gave consistently higher OSRs (between 9.2% and 9.8%)
than that of biotechfirms (between 8.0% and 9.0%). Such result aligned
roughly with recent publication
5 reporting the OSRs of 10.8% and 7.9%
Fig. 3 | The dynamic clinical trial success rates (ClinSRs) using the industry-
sponsored CDPs calculated in this study. a Distribution of industry- sponsored
and non-industry-sponsored trials among different clinical status (Phase 1, 2, and 3).
b The overall success rates(OSRs) based on industry-sponsored (dash line in green)
and all (black line with dots) CDPs.c The phase success rates(PSRs) evaluated based
on the industry-sponsored (green bar) and all (black bar) CDPs.d The OSRs for the
CDPs of large pharmaceutical company (yellow bars) and those of biotech firm
(blue bars). Source data are provided as a Source Data file. CDPs clinical develop-
ment programs, PnSR phase n success rate.
Article https://doi.org/10.1038/s41467-025-64552-2
Nature Communications| (2025) 16:9537 8

## Page 9

for leading pharma companies and biotech firms. As reported, the
potential factors contributing to the lower OSRs of biotechnology
firms included the fewer development resources/capabilities and
higher risk appetite inherent in their business models when comparing
with those large pharmaceutical companies
5.
Diverse and dynamic ClinSRs measured based on disease classes
In addition to the ClinSR for all CDPs, it was of interests to further
evaluate the ClinSR for CDPs of speci fic disease class. As shown in
Supplementary Table S2, the OSRs of 14 disease classes (de fined by
WHO ICD-11) across fifteen time-window were systematically offered.
Taking the latest time-window 2015 - 2023 as an example, there was
substantial variation in the OSRs (from 2.6% to 18.5%) of different
classes of diseases, which reminded us to perform further assessment
on disease-specific ClinSRs. Thus, a review of the data that were col-
lected to this study was conducted, which found three disease classes
that covered the highest numbers of CDPs: oncologic diseases, neuro-
logical diseasesand infectious/parasitic diseases. These classes had long
been considered to be three of the most popular research domains in
both academia and industry
46,47, which required an in-depth analysis in
the following sections.
Assessing the ClinSRs for drugs treating oncologic disease
The dynamic ClinSRs evaluated based on the CDPs of oncologic dis-
eases collected for this study were explicitly described in Supple-
mentary Fig. S6. As shown, the OSRs had been declining over time;
since the time-window of 2006 - 2014, the OSRs kept below 5% with
small fluctuations among recent time-windows. As reported, those
potential contributors to such low rate of success might include lim-
ited understanding of cancer biology, poorly predictive preclinical
models, and heterogeneity among patients
48,49.O nt h eo n eh a n d ,P 2 S R
was found consistently lower than P1SR and P3SR in recent time-win-
dows, which indicated that Phase 2 remained the largest driver of the
clinical failure for anticancer drug development
50. On the other hand,
in contrast to the clear increase of P3SR from 37.1% to 57.7% (as pro-
vided in Supplementary Fig. S6), P1SRs dramatically declined from
67.8% to 37.3%. Such declines in P1SRs indicated an increasing risk in
the early clinical development of innovative targeted drug and
immunotherapy for cancer
51, which recently prompted the U.S. FDA
Oncology Center of Excellence (OCE) to launch “Project Optimus ”
focusing on the dose optimization for Phase 1 trial of anticancer
therapy discovery
52. In addition, the increase of P3SR accompanied by
declines of P1SR identified in this study might indicate that the early
clinical evaluation of current pharmaceutical industry became
increasingly thorough, which might help to prevent the costly late-
stage (especially Phase 3) failure
22.
Anticancer drugs collected into this study consisted of the largest
proportion among other disease classes, and it was thus essential to
investigate the impacts of oncologic therapies on the ClinSRs of all
CDPs. In this study, the comparison of ClinSRs between oncologic
(red) and non-oncologic (blue) CDPs was described in Fig. 4a( y e l l o w
background). As demonstrated, the CDPs-based OSRs of anticancer
drug (oncologic) were consisten tly lower than that of the non-
anticancer one (non-oncologic). Particularly, although P1SRs of onco-
logic and non-oncologic CDPs were found comparable at the begin-
ning of 21st century, the oncologic P1SRs showed continuous decline
in recent years, which was different from the trend of slight increase of
non-oncologic P1SRs; when it came to P2SR, the evolving trends of
oncologic and non-oncologic CDPs were almost identical with the non-
oncologic P2SR consistently higher than oncologic ones; in contrast to
the declining trend of non-oncologic P3SR, the oncologic P3SR ele-
vated over time. Moreover, the comparison of ClinSRs between
oncologic (red) and non-oncologic (blue) MEs was also described in
Fig. 4a (blue background). As shown, the MEs-based OSR, P1SR and
P3SR (between anticancer and non-anticancer drugs) followed the
trends generally similar to that of the CDPs-based ones, while the P2SR
of oncologic MEs was higher than that for non-oncologic ones in the
early 21st century (different from the CDPs-based result). In other
words, the CDPs-based and MEs-based analyses revealed that in most
cases the ClinSRs of oncologic drugs were lower than that of non-
oncologic ones, but the P3SRs of oncologic drug were identified higher
comparing with non-oncologic one in recent time-windows. In sum,
great impact of oncologic therapies on ClinSR was observed.
Assessing the ClinSRs for drugs treating neurological disease
The dynamic ClinSRs evaluated using the CDPs ofneurological disease
collected to this analysis were explicitly described in Supplementary
Fig. S7. As shown, the OSRs had been declining in the early 21st century
by hitting the bottom with an extremely low OSR of 3.5% in 2008- 2016,
and, then, experienced a slow but clear increase in recent years. As
reported, such low OSRs of neurological diseases primarily originated
from the dif ficulty in crossing the blood-brain barrier, notoriously
unpredictive animal models, and poor understanding of complex CNS
condition
53. To deal with these issues, advances in drug delivery
systems54, strategies to promote successes in translating preclinical
outcome in animal model to the clinic55, and technologies elucidating
mechanisms underlying neurological diseases56 were widely used in
the past decade. All these efforts might collectively contribute to the
steady elevations in the OSRs of neurological diseases in recent years
(offered in Supplementary Fig. S7). Moreover, the evolution of phase
success ratewas also shown in Supplementary Fig. S7. Comparing with
P1SR and P2SR, there were clear elevations in recent P3SR, which
contributed the most to the recent elevation of OSR.
Assessing the ClinSRs for drugs treating infectious/parasitic
disease
The dynamic ClinSRs evaluated based on the CDPs of infectious dis-
eases collected for this study were explicitly described in Supple-
mentary Fig. S8. As shown, the OSRs had been declining over time, and
hit the bottom with a very low OSR of 2.6% in the latest time-window
2015- 2023. At the beginning of this century, the OSR of infectious
disease was more than two times as many as that of oncology, while its
OSRs in recent years became comparable to that of oncology, which
documented a dramatic decline in its ClinSR. As reported, the devel-
opment of anti-infective drug had changed its pivot from non-host
targets to the host ones, which led to increasing development difficulty
and might therefore result in the dramatic decline of clinical trial
success
48.
The drugs/candidates for treating COVID-19 had been frequently
tested in clinical trials in recent years, which consisted of a large pro-
portion of anti-infective drugs, and it was therefore essential to
investigate the impact of COVID-19 therapies on the ClinSR of all anti-
infective drugs. In this study, the comparison of ClinSRs between the
CDPs of COVID-19 and that of infectious disease excluding COVID-19
was conducted, and the findings were provided in Fig. 4b. As illu-
strated, there was no substantia l difference in P1SRs and P2SRs
between the studied two groups of CDPs. However, dramatic variation
was observed in P3SR which provided a substantially lower rate of
success (6.1%) for COVID-19 CDPs than that (34.7%) of non-COVID-19
CDPs. Moreover, such a low P3SR further resulted in a low OSR (0.7%)
of COVID-19 CDPs comparing with that (4.4%) of non-COVID-19 CDPs.
Extra analyses of the impact of FDA, EMA and NMPA on the ClinSRs of
anti-COVID-19 drugs were conducted. The resulting P3SRs presented
slight variations among FDA (6.1%), EMA (8.1%) and NMPA (8.0%),
which in turn brought about gentle fluctuation in their OSRs (0.7%,
0.9% and 0.9%, respectively).
Moreover, an in-depth analysis differentiating the industry-
sponsored COVID-19 CDPs from the non-industry-sponsored ones
(e.g., academic trials) were performed. As shown in Fig. 4b, no sub-
stantial difference in P1SRs and P2SRs between all COVID-19 CDPs and
Article https://doi.org/10.1038/s41467-025-64552-2
Nature Communications| (2025) 16:9537 9

## Page 10

industry-sponsored COVID-19 CDPs was observed. However, compar-
ing with the P3SR of all COVID CDPs (6.1%), that of the industry-
sponsored COVID CDP (9.1%) was higher, but remained signi ficantly
lower than that (34.7%) of non-COVID-19 infectious CDPs. Further-
more, such a low P3SR further led to low OSRs of both all COVID-19
CDPs (0.7%) & industry-sponsored COVID-19 CDPs (1.1%) comparing
with that of the non-COVID-19 infectious CDPs (4.4%). All the results
indicated that the OSRs of all and industry-sponsored anti-COVID
drugs were substantially lower than that of anti-infectious but non-
COVID drugs, and the non-industry sponsored anti-COVID clinical
trials were found more likely to end in failure. In the meantime, all anti-
COVID-19 drugs approved so far were shown in Supplementary
Table S3, and all anti-COVID-19 drugs analyzed in this study were also
categorized into three groups (antiviral drug, immunomodulator, and
vaccine) to assess whether there was discrepancy among the ClinSRs
of drugs in these three categories. As depicted in Fig. 4c, vaccine
resulted in the highest ClinSR, and immunomodulator gave the
lowest one.
Besides those three disease classes discussed above, the dynamic
ClinSRs assessed based on the CDPs of eleven additional classes of
disease (such as:circulatory system disease)d efined by the WHO ICD-11
were explicitly offered in Supplementary Figs. S9 - S19. The detailed
values of the calculated P1SRs, P2SRs, P3SRs were described in Sup-
plementary Tables S4- S6. Moreover, dynamic ClinSRs assessed based
on the molecular entities (MEs) of all 14 disease classes defined by the
WHO ICD-11 were also systematically described in Supplementary
Figs. S20- S33. As illustrated, the MEs-based calculations (regardless of
different diseases) tended to result in higher probabilities of success
than the CDPs-based one (considering all indications), but their
resulting time-dependent trends for the same disease class were highly
similar with each other.
Similarity among disease classes identified based on their
ClinSRs
To reveal the similarity among diseases in their ClinSRs across fifteen
time-windows, the cluster analyses based on OSRs, P1SRs, P2SRs and
Fig. 4 | Comparing ClinSRs among disease classes based on CDPs & MEs.
a Comparing the ClinSRs between the drugs for oncologic and non-oncologic
diseases based on CDP and ME. b Comparing the ClinSRs among three different
CDP groups in time-window 2015- 2023, including all COVID-19 CDPs, CDPs for
infectious disease excluding COVID-19, and industry-sponsored CDPs for COVID-19.
c Comparing the ClinSRs among different categories of anti-COVID-19 drugs in
2020-2023 (vaccine, antiviral drug and immunomodulator). Source data are pro-
vided as a Source Data file. CDPs clinical development programs, ME molecular
entity, ClinSRs clinical trial success rates, OSRs overall success rates, PnSR phase n
success rate.
Article https://doi.org/10.1038/s41467-025-64552-2
Nature Communications| (2025) 16:9537 10

## Page 11

P3SRs were carefully conducted, and corresponding results were
provided in Supplementary Figs. S34- S37. Particularly, disease classes
were first ranked based on ClinSRs across 15 time-windows, and a
complete linkage hierarchical clustering wasthen calculated using the
ranking results based on Euclidean distances. Taking the clustering
based on OSR (Supplementary Fig. S34) as example, two clustering
groups were discovered with six disease classes (BLOOD, MUSKE,
IMMUN, METAB, GENIT & VISAL) at the bottom and others (CACER,
CIRCU, NEURO, DIGST, RESPR, INFEC, SKINS & OTHER) on the top.
Particularly, although BLOOD was grouped together with the immune
system diseases (IMMUN) and musculoskeletal system/connective
tissue disease (MUSKE), its OSRs across time-windows (as described in
Supplementary Table S2) were higher than those of both IMMUN and
MUSKE. BLOOD was found with the steadily higher OSR than others.
One of the possible reasons behind the high OSRs of BLOOD might be
the fact that most (84.0%) of the BLOOD disease indications analyzed
in this study were hemophilia, anemia, thrombocytopenia,a n d blood
protein de ficiency, the underlying biology of which had been well-
characterized
57,58. Furthermore, the drugs of BLOOD were more likely
to reach the target tissues and therefore gave higher bioavailability, in
contrast to other diseases in which the target tissues (such as brain)
might be less accessible
59. As described in Supplementary Fig. S34,
oncology (CACER) and circulatory system disease (CIRCU) were found
to be the typical disease class of the top group, which provided con-
sistently the lowest OSRs acrossfifteen time-windows comparing with
other disease classes.
Assessing & analyzing the dynamic ClinSRs for
repurposed drugs
Drug repurposing is a strategy to discover new indication for drugs
beyond their initial indication60. Given its characteristic of the less risk
in safety, more rapid return on investment, and lower average cost
after failure, the enthusiasm for drug repurposing was growing
61.A n
appreciable number of pharmaceutical researchers held an optimistic
attitude that drug repurposing was more likely to be successful than
traditional ways of drug development
62. Although the ClinSRs of
repurposed drugs were quantitatively measured for certain disease63,
there remained a lack of systematic analysis on such point of view.
There were two types of drug repurposing: the
strictly-defined repur-
posing for the pursuit of unrelated disease indications, for example,
from cancer to infection 61 and the indication expansion aiming at
pursuing closely-related disease indications, commonly happened
within a disease class, for instance, from one oncological disease to
another
64. Here, as illustrated in Fig.5a, the ClinSRs for the CDPs ofall
repurposing (dash-line & bars in blue), strictly-defined repurposing
(dash-line & bars in orange), andindication expansion(dash-line & bars
in red) were explicitly provided. As described, the strictly-defined
repurposingCDPs resulted in higher OSRs than all CDPs (a solid-line in
black) in the early 21st century, but consistently lower OSRs in recent
time-windows. Different from the strictly-defined repurposing CDPs,
the all repurposingones andindication expansionones demonstrated a
stably lower OSRs compared with all CDPs. In other words, in recent
time-windows, three types of drug repurposing ( all repurposing ,
Fig. 5 | The dynamic clinical trial success rates (ClinSRs) for the repurposed
CDPs calculated in the research. aThe ClinSRs evaluated based on the CDPs ofall
repurposing(dash-line & bar in blue),strictly-defined repurposing(dash-line & bar in
orange) and indication expansion(dash-line & bar in red) together with those of all
CDPs (solid-line & bar in black). b ClinSRs assessed using industry-sponsored
repurposed (dash-line & bar in brown) and all (solid-line & bar in black) CDPs.
Source data are provided as a Source Data file. PnSR phase n success rate, OSR
overall success rate.
Article https://doi.org/10.1038/s41467-025-64552-2
Nature Communications| (2025) 16:9537 11

## Page 12

strictly-defined repurposing & indication expansion) gave similar suc-
cess rates, which were consistently lower than all CDPs. This result was,
from the perspective of ClinSR at least, contrary to the traditional
“optimistic attitude” on the success of repurposed drugs. An extra
study on the OSR of three classes of disease (neoplasm, neurology and
infection) popular in drug repurposing
64,65 was performed, which
identified a discrepancy among the OSRs of different disease classes.
Particularly, in recent time-windows, the OSRs of drugs repurposed to
neoplastic disease were relatively higher than that to the other two
d i s e a s ec l a s s e s ,b u tt h eO S R so fa l lt h r e ec l a s s e so fd i s e a s ew e r ec o n -
sistently lower than that of all disease (all CDPs in Fig.5a). Additionally,
the right side of Fig. 5a also illustrated the PSR for three types of
repurposed drugs. As shown, the P1SRs of repurposed CDP were
higher than that for all CDP in most cases, which was readily under-
standable since most of the repurposed drugs had been previously
assessed for safety.
An in-depth analysis differentiating the industry-sponsored
repurposed CDPs from non-industry-sponsored ones (e.g., academic
trials) was further conducted to discover potential reasons behind the
low ClinSRs of repurposed drugs. As provided in Fig.5b, the OSRs and
PSRs (particularly, P1SRs and P3SRs) of industry-sponsored repur-
posed CDPs (brown dash line) were identified to be consistently higher
than that of all CDPs (black line with dots). Such results indicated that
the low success rate of repurposed drugs might come from high
proportion of academic investigators undertaking drug repurposing
activities, which could dramatically pull down the success rates in
pharmaceutical R&D
64. An extra analysis of the clinical trial data used in
this work was further conducted, which found that the academia
tended to devote efforts to challenging, high-risk, and less profitable
indications (Creutzfeldt-Jakob disease, for example, has so far only been
clinically assessed by academia). These discoveries aligned with
previous works claiming that ( a) academic researchers tended to
engage in cutting-edge high-risk projects, rather than address the real-
world medical needs, making the corresponding projects less attrac-
tive to commercial investments
66;( b) compared with the academic
researchers, pharmaceutical companies accumulated much richer
real-world data, expertise, and experience in evaluating their projects,
allowing for more efficient resource allocation
67.I ns u m ,t h efindings
asked for a careful evaluation of potential challenge and an effective
avoidance of blind exploration during academia-driven drug
repurposing.
Diverse and dynamic ClinSRs measured based on drug
modalities
Drug modality had also been considered as one of the risk contributors
to the success rate of drug development11. Small molecular drug (SMD)
had long been the dominant modality and newer ones (such as
antiboday-related drug) had also been added to the drug development
toolbox
68. As demonstrated in Fig.6a, a clear shift in the research focus
on various drug modalities was observed based on assessing the
number of unique molecular entities in clinical trial. Particularly, dur-
ing the past two decades, the percentages of SMDs kept declining from
66.3% (at the beginning of 21st century) to 46.6% (currently) with
observable increase of the shares of antibody-related drugs (ARDs)
(from 10.8% to 19.5%) and other drugs (from 13.5% to 25.8%, especially
RNA-based therapies, cell therapies, gene therapies, etc.). Moreover, as
illustrated in Fig. 6b, a shift in the research focus on various drug
modalities was also observed based on assessing the number of CDPs.
Particularly, in the past two decades, the percentage of CDP of SMDs
kept declining from 72.4% (early 21st century) to 57.2% (currently) with
clear increase of the shares of ARDs (from 11.1% to 21.4%) and others
(from 6.7% to 12.8%).
Fig. 6 | The change in the research focus of drug modalities over time. aShifts in
the research focuses of drug modalities measured by the numbers of clinically
tested unique molecular entities. Percentage of small molecular drugs had been
declining from 66.3% (the start of the 21st century) to 46.6% (now) with observable
increase of the shares of antibody-related drugs (from 10.8% to 19.5%) and other
drugs (from 13.5% to 25.8%). b The shifts in research focus of drug modalities
measured by the total numbers of CDPs. The percentages of CDPs of small mole-
cular drugs kept declining from 72.4% to 57.2% with a clear increase of the share of
antibody-related drugs (from 11.1% to 21.4%) and others (from 6.7% to 12.8%). CDPs
clinical development programs.
Article https://doi.org/10.1038/s41467-025-64552-2
Nature Communications| (2025) 16:9537 12

## Page 13

In this study, the analyses on four types of major drug modality,
including: SMD, ARD, protein & peptide drug (PPD) and other drug
(OTH), were conducted, and their ClinSRs were described in Supple-
mentary Table S7, and separately shown in Supplementary
Figs. S38- S41. As depicted in Supplementary Table S7, the OSRs of
ARD were higher than those of other modalities in recent decade, while
the OSRs of PPD for the early 21st century surpassed those of the
others. The OSRs of OTH (a mixture of highly diverse classes of drug,
such as: RNA therapy and cell therapy) remained the lowest across
fifteen time-windows. As the most well-established drug modality,
three factors of SMD were considered as the primary reason leading to
its failure, including poor physicochemical property, unmeaningful
efficacy of the chosen targets and constant turmoil of strategy varia-
tion with pharmaceutical companies
68. With the increasing elucidation
of the molecular mechanism underlying the disease pathogenesis, an
extensive growth potential of ARDs was also highly anticipated 69.
Because of the unique advantages of different drug types, current
pharmaceutical industry tended to adopt a broad mixture of drug
modalities for disease treatment
68.
Furthermore, the dynamic ClinSRs measured based on molecular
entities (MEs) of four types of major drug modality were also sys-
tematically described in Supplementary Figs. S42- S45. As illustrated,
the MEs-based calculations (regardless of different diseases) tended to
result in higher probabilities of success than the CDPs-based one
(considering all indications), but their resulting time-dependent trends
for the same drug modality were highly similar with each other.
Evaluating the potential biases introduced by the analyzed
datasets
In this study, ClinicalTrials.gov and Drugs@FDA were two databases
used for analyzing ClinSR, and the potential biases introduced by the
reliance on these databases were further assessed.
Assessing the bias introduced by the drugs not aiming at US
approval
The first potential bias may come from the inclusions of early stage
academic pursuits and trials intended to bring candidates outside the
market of United States. In other words, it was necessary to reanalyze
the ClinSR of drugs that specifically targeting US approval, but no such
information could be retrieved from ClinicalTrials.gov and
Drugs@FDA. To address this issue, we integrated the information of
country, where a drug was developed in for diseases, from the Phar-
maprojects database into this study, which helped to determine whe-
ther a drug was intended for US approval or not. As a result, about
22.5% of all industry-sponsored CDPs were discovered to be developed
outside US. Based on the data ofPharmaprojectsand ClinicalTrials.gov,
ClinSRs for those drugs targeting US approvals were calculated. As
shown in Supplementary Fig. S46a, the dynamic OSRs for all CDPs,
industry-sponsored CDPs, and the CDPs aiming at US approvals were
shown using black solid-line with dots, green dash-line with diamonds,
and blue dash-line with triangles , respectively. It could be observed
that the OSRs for CDPs aiming at US approval were obviously larger
than that of all CDPs and slightly larger than that of industry-sponsored
CDPs. Meanwhile, the OSRs for the CDPs aiming at US approvals
revealed a declining trend over time, with relative stability observed in
recent years, which gave a descending trend very similar to that for all
CDPs and that for industry-sponsored CDPs (as illustrated in Supple-
mentary Fig. S46a).
Furthermore, based on the analysis above, the corresponding bias
of data inclusion was corrected using the data ofPharmaprojects,a n d
the OSRs for CDPs aiming at US approval were given in Fig. 2aa n d
Supplementary Fig. S47a (highlighted using the grey dash-line with
triangle). As provided in Fig. 2a, the OSR for CDPs aiming at US
approval (grey dash-line with triangle) had been declining over time
(this trend aligned well with that for all CDPs), and remained stable
around 8.8% in recent years (with deviations between black and grey
lines around 3.7% in recent time-windows). Similar ClinSR analysis was
conducted for MEs aiming at US approval, and the OSRs for MEs
aiming at US approvals were illustrated in Fig. 2b and Supplementary
Fig. S47b (highlighted using the grey dash-line with triangle ). As
depicted in Fig. 2b, the OSR for the MEs aiming at US approval had
been declining over time (this trend aligns well with that for all MEs),
and remained stable around 14.0% in recent years (with differences
between black and grey line around 2.2% in recent time-windows). As a
result, the bias of data inclusion was further corrected systematically.
Particularly, the OSRs for CDPs aiming at US approval were illustrated
using grey dash-line with triangle in Supplementary Figs. S48- S61 for
each disease class and Supplementary Figs. S62 - S65 for drug mod-
alities, and those for MEs aiming at US approvals were provided using
grey dash-line with trianglein Supplementary Figs. S66- S79 for disease
classes and Supplementary Figs. S80 - S83 for drug modalities. As
provided in the figures, the OSRs for CDPs/MEs aiming at US approval
were consistently higher than that for all CDPs/MEs, but the trends of
these two types of OSRs (highlighted using ablack solid-line with dots&
a grey dash-line with triangle ) were highly similar. Furthermore, the
OSRs for all CDPs/MEs (the black solid-lines with dots ) were also
depicted in those figures as references for indicating the deviation
from that aiming at US approval ( grey dash-lines with triangle). Both
t y p e so fO S R s(black solid-line and grey dash-line) were systematically
depicted in the correspondingfigures here.
Assessing the bias introduced by the incomplete drug
discontinuations
The second potential bias may originate from the non-mandatory
clinical trial registration before 2007, which might overestimate
ClinSR at the early 21st century. In other words, it was necessary to
measure the ‘survivor bias’introduced by the incomplete inclusion of
discontinuation data for drugs, especially those before year 2007. To
address the problem, we incorporated the knowledge of discontinued
time, diseases and phase for drugs from the database of Pharmapro-
jects into this analysis. Particularly, the discontinuation information
described by the Pharmaprojectsdatabase for a total of 4707 unique
molecular entities that had ever entered clinical trial were accumu-
lated, and the OSRs were then calculated by adding the collected
discontinuation data into the analyses. As shown in Supplementary
Fig. S46b, the dynamic OSRs before and after the correction of “sur-
vivor biases” were provided using a blue dash-line with trianglesand a
purple dash-line with diamonds, respectively. As illustrated, for those
time-windows containing data prior to 2007, the OSRs exhibited clear
decline with their deviation ranging from 0.7% to 4.8%. The magnitude
of the declines across each time-window became increasingly smaller
as the number of years before 2007 decreased. Additionally, it was also
observed that the OSRs after the correction of “survivor bias” (purple
dash-line with diamonds) for the time-windows after 2007 were almost
identical to that before the correction ( blue dash-line with triangle).
These findings highlighted the necessity of correcting“survivor biases”
to achieve unbiased direct comparison among time-windows.
Furthermore, based on the analysis above, the corresponding bias
of data inclusion was corrected by an approach of collective adjust-
ment, which not only focused on the CDPs/MEs aiming at US approval
but also corrected the “survivor biases ” of incomplete drug dis-
continuation. In this study, the adjustment was applied to Fig. 2a,
leading to the OSRs after collective adjustment (purple dash-line with
diamond, which were identical to the purple line demonstrated in
Supplementary Fig. S46b), and the PSRs for CDPs after the adjustments
were also offered in Supplementary Fig. S47a (shown by bars in blue,
yellow, and red). One thing we would like to discuss further was about
the prior studies reporting the OSRs of 10.4% for 2003- 2011
2,9 . 6 %f o r
2006- 2015 (BIO, https://www.bio.org/), and 7.9% for 2011- 2020 (BIO,
https://www.bio.org/). As offered in Fig. 2a, the OSRs after the
Article https://doi.org/10.1038/s41467-025-64552-2
Nature Communications| (2025) 16:9537 13

## Page 14

collective adjustments equaled to 12.3% (2003 - 2011), 9.2%
(2007- 2015) and 8.4% (2011- 2019), which were comparable to those
from the prior studies. Taking the 2011- 2020 window as example, the
P2SRs obtained in this study were 28.4% for 2012- 2020 and 28.8% for
2011- 2019, which were close to that (28.9%) ofBIO;t h eP 3 S R so b t a i n e d
in this study equaled to 53.0% for 2012- 2020 and 50.4% for 2011- 2019,
remaining comparable to that (52.4%) of BIO. Similar analysis was
conducted for MEs after the collective adjustment, and the resulting
OSRs were added to Fig. 2b( g i v e nb ypurple dash-line with diamond),
and the corresponding PSRs were also offered in Supplementary
Fig. S47b (bars in blue, yellow, and red). As shown in Fig.2b, the OSRs
for MEs after collective adjustment ( purple dash-line with diamond )
had been declining over time, with a relative stability in recent win-
dows, which aligned with that for all MEs ( black solid-line with dot ).
Furthermore, although the CDPs- and MEs-based OSRs were dis-
covered continuously declining over time, the MEs-based ones were
found consistently higher than the CDP-based ones (as shown in
Supplementary Fig. S84a), and the MEs-based P2SRs and P3SRs were
higher than the CDPs-based ones (as provided in Supplementary
Fig. S84b). In other words, the CDPs-based assessment (considering all
indications) tended to result in lower probabilities of success than the
MEs-based one (regardless of the different indications), aligning well
with the findings for all CDPs (as described in Supplementary Fig. S5).
Correcting the bias of data inclusions using the collective
adjustment
Based on the above analysis, the survivor bias in collected data was
further corrected. Particularly, the OSRs for CDPs after the collective
adjustment were shown by purple dash-line with diamond in Supple-
mentary Figs. S48 - S61 for disease classes and Supplementary
Figs. S62- S65 for drug modalities, and those for MEs after collective
adjustment were provided using purple dash-lines with diamonds in
Supplementary Figs. S66- S79 for disease classes and Supplementary
Figs. S80- S83 for drug modalities. Additionally, the PSRs for CDPs
after collective adjustment were shown byblue, yellow,a n dred bars in
Supplementary Figs. S48- S61 for disease classes and Supplementary
Figs. S62 - S65 for drug modalities, and those for MEs after the
adjustment were shown byblue, yellow,a n dred bars in Supplementary
Figs. S66- S79 for disease classes and Supplementary Figs. S80- S83 for
drug modalities. As shown in thesefigures, for the vast majority of the
disease classes (or drug modalities), the downward magnitude of the
purple dash-line (indicating the OSRs after collective adjustment)
relative to the grey dash-line (denoting the OSRs aiming at US
approval) in the time-windows before 2007 were larger than that in the
time-windows after 2007. Furthermore, the OSRs for all CDPs/MEs (a
black solid-line with dots) and for CDPs/MEs aiming at US approval (the
grey dash-line with triangle) were also shown in those figures as the
references for indicating the deviations from that for CDPs/MEs after
the collective adjustments (purple dash-lines with diamond). In other
words, to have a holistic view of ClinSRs, all three types of OSRs were
d r a w ni nt h efigures of this study. Moreover, the OSRs of 14 disease
classes after collective adjustment across 15 windows were system-
atically described in Table2, and the ClinSRs of 4 drug modalities after
collective adjustment were also shown in Table 3.
In our study, this collective adjustment was further applied to
correct those findings in Figs. 4 and 5, which could help to give an in-
depth comparison of ( a) ClinSRs between oncologic and non-
oncologic CDPs/MEs, (b)C l i n S R sa m o n gd i f f e r e n tg r o u p so fC O V I D -
19 CDPs, and (c) ClinSRs among different classes of drug repurposing.
Therefore, the adjusted versions of Figs. 4 and 5 were illustrated in
Supplementary Fig. S85 and Supplementary Fig. S86, respectively and
discussed below.
Comparison of ClinSRs between oncologic (red) and non-
oncologic (blue) CDPs after collective adjustmentswas shown in Sup-
plementary Fig. S85a (yellow background). The CDPs-based OSRs of
anticancer drug (oncologic) were consistently lower than that of the
non-anticancer one (non-oncologic). Particularly, although P1SRs and
P2SRs of oncologic and non-oncologic CDPs were found comparable
at the beginning of 21st century, the oncologic P1SRs and P2SRs
showed continuous decline in recent years, which were different from
the trend of slight increase of non-oncologic P1SRs and P2SRs; in
contrast to the gradually declining trend of non-oncologic P3SRs, the
oncologic P3SRs increased in recent time-windows. In summary, the
above trends of ClinSRs (both OSRs & PSRs) for oncologic CDPs after
collective adjustment were highly similar to those for all oncologic
CDPs (before the adjustment, which were previously shown in Fig.4a).
Furthermore, the comparison of ClinSRs between oncologic (red)
and non-oncologic (blue) MEs was also described in Supplementary
Fig. S85a (blue background). For oncologic MEs, their OSR trend is like
that of CDPs, both exhibiting a continuous downward trend. For non-
oncologic MEs, their OSR values follows a trend similar to that of CDPs,
characterized by an initial decline followed by subsequent increase.
Notably, in the early 21st century, ME-based OSR of oncologic drugs
was higher than that of non-oncologic ones. However, this was
reversed in recent windows, with oncological drugs exhibiting lower
OSRs than the non-oncological ones- a key divergence between CDPs-
based and MEs-based results. Trends of MEs-based P1SRs and P2SRs
are largely consistent with those of CDP-based ones. The main diver-
gence, however, lies in the P2SR: while oncologic CDPs had lower
P2SRs than the non-oncologic ones, MEs-based calculations initially
gave a higher P2SR for oncologic drugs. Such discrepancy may explain
why the oncologic drugs exhibited higher OSR than non-oncologic
ones at the beginning of 21st century. Regarding P3SR, there is little
difference between ME-based and CDP-based results for oncologic
drug. In contrast, non-oncologic ones showed distinct MEs-based
trend for P3SRs- initially declining, then rising, before declining again
- unlike the steady decrease observed in CDP-based analysis. In sum,
the CDPs-based and MEs-based analyses identified that in recent years
the OSRs of oncologic drugs were lower than that of non-oncologic
ones, but the P3SRs of oncologic drugs were found higher than those
of non-oncologic ones in two most recent time frames (2014- 2022 &
2015- 2023).
The ClinSRs after thecollective adjustmentfor two groups of CDPs
were analyzed: the COVID-19 CDPs and CDPs of infectious diseases
excluding COVID-19. As depicted in Supplementary Fig. S85b, there
was no substantial difference in the P2SRs between the studied two
groups. However, 10.0% difference was revealed in their P1SRs, and
dramatic variation was also observed in P3SR which described a sub-
stantially lower rate of success (12.5%) for COVID-19 CDPs than that
(46.0%) of non-COVID-19 CDPs. Moreover, such low P3SR further led to
a low OSR (1.1%) of COVID-19 CDP compared with that (5.9%) of non-
COVID-19 CDP. Many anti-COVID-19 CDPs have entered into Phase 3
42,
but most of them ended in failures. In other words, although there are
anti-COVID-19 drugs approved in very short time frame, it is apparent
that such success came at a high cost of huge number of clinical fail-
ures. Several possible reasons contributing to the low ClinSRs of anti-
COVID-19 drugs were reported.
First, the problem of poorly designed/
reported anti-COVID clinical study became serious during pandemic70.
Specifically, many small-scale trials lacked statistical power to generate
meaningful results, and were abandoned due to futility. Second,t h e
emergency use authorization (EUA) for COVID-19 treatment often
involved incomplete approval processes, which might result in the
premature clinical trials
71. For example, clinical trials on chloroquine &
hydroxychloroquine were halted after their revocations of EUA. All
these problems might collectively affect P3SRs and in turn lead to the
low OSRs in Supplementary Fig. S85b, which called for the establish-
ment of stricter design standards and implement of innovative trial
design strategy (e.g., adaptive platform trial) for clinical evaluation in
the event of a future pandemic
72.
Article https://doi.org/10.1038/s41467-025-64552-2
Nature Communications| (2025) 16:9537 14

## Page 15

T a b l e2|T h eO S R sa f t e rt h ec o l l e c t i v ea d j u s t m e n tf o ra l lC D P sc o l l e c ted for this study and the CDPs of cert ain disease class (14 classes defined by WHO ICD-11)
calculated acrossfifteen nine-year time-windows
Disease
class
2001- 2009 2002 - 2010 2003 - 2011 2004 - 2012 2005 - 2013 2006 - 2014 2007 - 2015 2008 - 2016 2009 - 2017 2010 - 2018 2011 - 2019 2012 - 2020 2013 - 2021 2014 - 2022 2015 - 2023
All 16.7% 14.3% 12.3% 11.1% 9.8% 8.9% 9.2% 8.6% 8.7% 8.6% 8.4% 8.6% 8.9% 8.6% 8.1%
01 INFEC 20.7% 20.4% 19.6% 17.1% 11.9% 10.8% 13.4% 12.3% 10.3% 8.5% 7.1% 7.1% 8.0% 6.0% 3.9%
02 CACER 15.2% 13.2% 11.6% 10.4% 9.4% 7.8% 7.4% 6.7% 6.7% 6.3% 6.0% 6.1% 6.0% 5.8% 5.7%
03 BLOOD 59.9% 58.0% 36.9% 40.7% 38.4% 32.4% 33.7% 34.8% 37.4% 35.5% 35.9% 41.9% 39.3% 32.6% 34.1%
04 IMMUN 35.1% 43.3% 33.2% 26.4% 23.7% 18.7% 15.3% 12.7% 14.6% 14.4% 11.5% 12.2% 15.3% 15.6% 15.0%
05 METAB 17.4% 14.7% 10.3% 10.0% 8.8% 8.6% 9.8% 10.0% 10.4% 12.0% 12.2% 12.2% 14.3% 13.3% 12.8%
06 NEURO 17.3% 12.4% 10.3% 7.8% 6.5% 5.5% 5.3% 6.1% 6.7% 6.6% 8.7% 10.4% 10.6% 13.0% 13.0%
07 VISAL 20.3% 18.1% 14.0% 14.0% 10.5% 10.8% 11.1% 11.1% 11.8% 11.2% 9.2% 9.3% 11.0% 10.8% 11.2%
08 CIRCU 10.3% 8.6% 6.5% 7.0% 7.4% 7.9% 8.9% 7.3% 7.4% 8.6% 6.6% 5.9% 7.1% 5.8% 4.7%
09 RESPR 9.6% 9.0% 8.9% 7.7% 7.4% 7.8% 7.5% 6.8% 6.3% 6.0% 6.2% 5.5% 7.8% 7.2% 7.0%
10 DIGST 8.6% 8.4% 10.6% 11.2% 12.1% 9.7% 10.5% 8.9% 10.1% 12.6% 13.4% 12.1% 12.5% 12.6% 9.3%
11 SKINS 8.4% 13.3% 9.9% 7.4% 5.1% 7.3% 10.6% 9.6% 10.6% 12.5% 12.0% 12.3% 13.8% 13.9% 15.0%
12 MUSKE 24.8% 19.7% 18.0% 17.6% 16.3% 14.0% 13.1% 11.6% 9.9% 9.8% 10.0% 8.9% 8.4% 8.1% 8.7%
13 GENIT 14.4% 10.9% 7.8% 5.8% 9.4% 12.2% 11.5% 13.3% 15.0% 16.6% 19.1% 21.2% 15.7% 8.8% 8.1%
14 OTHER 13.3% 9.7% 12.3% 10.7% 10.3% 9.9% 11.7% 11.0% 10.8% 9.1% 7.8% 10.8% 11.0% 10.1% 8.5%
All all diseases; INFEC: Infectious/parasitic disease; CACER: Oncology;BLOOD: Blood/blood-forming organs disease; IMMUN: Immune system disease; METAB: Endocrine, nutritional or metabolic diseases; NEURO: Neurology; VISAL: Visual system disease; CIRCU:
Circulatory system disease; RESPR: Respiratory system disease; DIGST: Digestive system disease; SKINS: Skin disease; MUSKE: Musculoskeletal system/connective tissue disease; GENIT: Genitourinary and sexual related disease; OTHER: Other disease.
Table 3 | The clinical trial success rates(ClinSRs, both overall success rateand phase success rate) after the collective adjustment for the CDPs of four major types of
drug modalities
Drug Modality 2001 - 2009 2002 - 2010 2003 - 2011 2004 - 2012 2005 - 2013 2006 - 2014 2007 - 2015 2008 - 2016 2009 - 2017 2010 - 2018 2011 - 2019 2012 - 2020 2013 - 2021 2014 - 2022 2015 - 2023
OSR SMD 15.1% 12.4% 10.6% 9.4% 8.7% 7.8% 7.8% 7.3% 7.4% 7.4% 7.4% 7.6% 7.7% 7.5% 7.2%
ARD 24.4% 23.3% 22.5% 22.8% 18.2% 14.8% 15.5% 14.1% 13.6% 12.6% 12.4% 12.5% 13.2% 13.1% 12.0%
PPD 33.1% 27.6% 21.9% 19.8% 17.4% 18.1% 18.0% 16.1% 15.1% 14.0% 12.9% 12.3% 11.5% 9.9% 9.2%
OTH 1.5% 7.1% 4.7% 3.9% 2.8% 3.7% 4.1% 4.5% 5.3% 5.2% 4.9% 5.4% 6.5% 5.9% 5.8%
P1SR SMD 70.1% 70.4% 67.3% 67.6% 66.7% 64.9% 64.4% 64.9% 64.3% 62.0% 61.0% 61.0% 60.5% 61.6% 59.9%
ARD 67.9% 69.2% 72.8% 71.9% 66.9% 64.5% 63.6% 58.6% 58.6% 56.5% 52.9% 51.5% 52.3% 51.9% 52.9%
PPD 80.4% 74.7% 70.0% 70.1% 69.0% 66.2% 69.6% 64.4% 63.1% 63.1% 64.8% 63.5% 62.2% 61.7% 60.1%
OTH 73.0% 69.4% 62.5% 56.6% 48.4% 45.2% 44.9% 45.2% 45.7% 49.5% 48.4% 45.6% 47.5% 45.0% 48.0%
P2SR SMD 37.6% 33.1% 30.8% 29.7% 29.1% 27.0% 27.2% 26.6% 26.4% 26.1% 26.3% 25.9% 26.6% 26.4% 26.6%
ARD 47.5% 46.6% 45.6% 45.2% 41.1% 38.7% 37.5% 36.1% 35.0% 34.0% 34.9% 33.9% 35.1% 35.8% 33.7%
PPD 54.6% 50.4% 47.7% 44.1% 42.9% 44.6% 42.5% 43.2% 41.6% 39.9% 38.2% 37.2% 33.3% 32.2% 30.5%
OTH 37.3% 40.7% 34.0% 33.1% 26.3% 25.7% 25.8% 26.6% 27.9% 25.9% 25.8% 27.1% 28.8% 29.9% 26.8%
P3SR SMD 57.0% 53.4% 51.0% 46.9% 44.9% 44.5% 44.6% 42.2% 43.5% 45.7% 46.4% 48.0% 47.6% 46.2% 45.1%
ARD 75.6% 72.3% 67.9% 70.2% 66.2% 59.3% 65.1% 66.7% 66.4% 65.5% 67.0% 71.6% 72.0% 70.3% 67.1%
PPD 75.6% 73.5% 65.5% 64.1% 58.7% 61.3% 60.9% 57.8% 57.4% 55.6% 52.2% 52.2% 55.4% 50.0% 50.0%
OTH 5.6% 25.0% 22.2% 20.7% 21.9% 31.6% 34.9% 37.0% 41.9% 40.3% 38.9% 44.0% 47.7% 43.8% 44.9%
SMD small molecular drug, ARD antibody-related drug,PPD protein & peptide drug, OTH other drug, OSR overall success rate, P1SR phase 1 success rate, P2SR phase 2 success rate, P3SR phase 3 success rate.
Article https://doi.org/10.1038/s41467-025-64552-2
Nature Communications| (2025) 16:9537 15

## Page 16

In the meantime, all anti-COVID-19 drugs approved so far were
shown in Supplementary Table S3, and all anti-COVID-19 drugs studied
in this research were classified to three groups (antiviral drug, immu-
nomodulator & vaccine) to assess whether there was discrepancy
among the ClinSRs of drugs in these three groups. As given in Sup-
plementary Fig. S85c, vaccine resulted in the highest ClinSRs, and
immunomodulator gave the lowest ones. To explore the reason con-
tributing to the differences above, a systematic literature review was
also conducted.
On one hand, several potential causes underlying the
higher ClinSR of anti-COVID-19 vaccine were identi fied, which inclu-
ded: (a) the effective animal models constructed prior to the pandemic
based on experiences gained from SARS-CoV73,( b) the greatly reduced
time frame for vaccine development by earlier antigen-design study on
MERS
74,a n d( c) the availability of speci fic, sensitive, and meaningful
clinical endpoints75. On the other hand , some of the potential factors
underlying the low ClinSRs of immunomodulators were also found,
which contained: ( a)t h eg r e a td i fficulty in determining key in flam-
matory mediator76,( b) the undesired adverse reaction of non-specific
immunosuppression77,( c) the complexity in patient selection due to
heterogeneous immune response78.
The ClinSRs after collective adjustmentfor the CDPs of all repur-
posing (dash-line & bars in blue) and repurposing of indication expan-
sion (dash-line & bars in red) together with those of all CDPs (a dash-
line with diamonds & bars in purple) were depicted in Supplementary
F i g .S 8 6 .A ss h o w ni nS u p p l e m e n t a r yF i g .S 8 6 a ,c o m p a r e dw i t ht h e
OSRs of all CDPs, those of “all repurposing” (as depicted using blue
dash-line)a n d“repurposing of indication expansion” (as demonstrated
by red dash-line) were higher in the early 21st century, but had recently
become lower. Such results remained, from the perspective ofclinical
trial success ratesat least, contrary to the traditional optimistic attitude
on the success of repurposed drugs. This analysis highlighted the
extremely low ClinSRs of anti-COVID-19 drugs revealed above, most of
which were the repurposed ones
79. Additionally, Supplementary
Fig. S86b also offered the illustration of the PSRs for two types of
repurposed drug. As shown, the P1SRs of repurposed CDPs were
consistently higher than those for all CDPs in all timeframes, which is
readily understandable since most of the repurposed drugs had been
previously assessed for safety. Meanwhile, unlike remaining roughly
comparable at the beginning of 21st century, in recent years, the P2SRs
for two types of the repurposed CDP (all repurposing& repurposing of
indication expansion) are substantially lower than those for all CDPs,
which contributes most to the lower OSRs for repurposed CDPs than
those for all CDPs in recent time-windows.
To investigate the potential causes underlying the low ClinSRs of
repurposed drugs, a systematic literature review was performed with
some important factors discovered.
First, spurious data can be pro-
duced in initial screening assay. Because the approved drug can show
promiscuous activity in screening assay, the evaluation of known drug
in new assay can lead to false positive outcomes, undermining drug
repurposing from the outset
64. Second, the original mechanism of
action may not be suitable for new indication. The relatively low costs
of “trial-and-error” in repurposing had promoted a large number of
trials to rush into clinical testing without a clear understanding of their
targeted mechanisms, planting the seeds of failure for drug
repurposing
80. Third, a direct knowledge transfer may result in serious
problem in clinical trial. Drug repurposing is seldom as trivial as per-
forming a clinical trial for new diseases using the same strategy
(dosage, formulation, and biomarker) as previously used, which makes
it challenging to replicate the past success in new indication
81.T h e s e
discussions highlighted the possible cause leading to the failure of
repurposed drug and in turn resulting in the low OSRs, and many
approaches have thus been propos ed to elevate the ClinSR of the
repurposing programs82, which asked for a prior evaluation in biolo-
gical assay, a sound understanding of molecular mechanism, and a
robust clinical design considering dosage, formulation & biomarker.
All in all, although drug repurposing is attractive, available evidence
suggests that cautions should be taken.
Construction of multi-functional platform for reporting ClinSRs
The ClinSRs of drugs were critical for both clinical researcher and
pharmaceutical investor when making scienti fic and economic
decisions7. However, the serious problem of “information lag” of pre-
vious studies could not effectively demonstrate the dynamic nature of
ClinSR. Furthermore, considering the diverse research interests
among researchers, a customized analysis on particular groups of
drugs was highly demanded, but no such tool had been available. In
this study, a multi-functional online platform, entitled“ClinSR.org”,w a s
thus constructed, which enabled a dynamic description of the ClinSR
of any drug group of interests. Moreover, to cope with the problem of
information lag,ClinSR.orgwas carefully designed to not only integrate
all the data collected to this analysis, but also could be further updated
for the coming decade. The characteristics of this online platform were
explicitly described as follows.
An automated platform enabling the dynamic description of
ClinSRs
A ss h o w ni nF i g .7a, a process enabling the automated data collection
and ClinSR assessment was constructed. First, drugs and their corre-
sponding clinical status were automatically collected from Clinical-
Trials.gov and the U.S. FDA website byquarterly retrieving information
using theirApplication Programming Interface(API).Second,d i v e r s ed a t a
affiliated to the newly-collected drugs were automatically retrieved by
matching with three established databases (WHO ICD-11, DrugBank and
TTD).Third, all the collected data were carefully reviewed and validated
by well-trained pharmacologists and bioinformaticians in our team to
g u a r a n t e et h ed a t aq u a l i t y ,a n dw e r et h e ni n t e g r a t e di n t ot h el a r g ep o o l
of data collected to this analysis. Finally, the change of ClinSR among
diverse time-windows was automatically calculated based on the latest
collection of drugs, which was then updated and systematically visua-
lized on the online website ofClinSR.org.
Personalized tool realizing the customized assessment of
ClinSRs
As illustrated in Fig.7b, a variety of strategies realizing the customized
assessment of ClinSR based on the user’s preference were described in
ClinSR.org. Particularly, a user was allowed to assess the ClinSR for a
particular class of disease or a speci fic modality of drug, and also
evaluate the joint contribution of multiple disease classes or drug
modalities to the success of clinical trial drugs. Moreover, the Clin-
SR.orgenabled the assessment of ClinSR for any drug group of interest.
Users canfirst upload a list of drugs (indicated by drug name, TTD drug
ID, DrugBank accession, PubChem CID, etc.), and the ClinSR of these
drugs will then be automatically calculated.
An integrated database reconstructing the CDP(s) for
studied drug
Although ClinicalTrials.gov offered extensive clinical information on
trial drugs, it lacked a clear summary of the CDP for each drug. Parti-
cularly, the information on ClinicalTrials.gov was offered in pieces,
each of which focused only on one trial, which asked for the recon-
struction of the entire CDP for each drug. As illustrated in Fig. 7c, the
CDPs were therefore systematically reconstructed for each drug col-
lected to this study, which were explicitly described in the section of
“Development Program Identification for a Drug of Distinct Disease ”.
Taking the drug vilaprisan (as described in Fig. 7c) as an example, it
had been clinically tested for two disease indications ( endometriosis
and uterine leiomyoma). This led to two distinct CDPs for this specific
drug, which were systematically described in ClinSR.org to facilitate
the decision making for the researchers and investors in the fields of
pharmaceutical sciences.
Article https://doi.org/10.1038/s41467-025-64552-2
Nature Communications| (2025) 16:9537 16

## Page 17

Discussion
Data and conceptual limitations
The limitations of the data collected to this and any other data-driven
studies should be discussed to make the readers be aware of the
potential distortion of those data on results. In this study, all analyses
were based on the clinical trial information from ClinicalTrials.gov, and
any incomplete registration of trials to this database might affect the
ClinSRs calculated in this study. Thanks to the scope and content
expansion of mandatory clinical trial registration byFDA Amendments
Act (FDAAA)
35 & trial registration policy of International Committee of
Medical Journal Editors (ICMJE)83, the data in ClinicalTrials.gov had
become increasingly comprehensive, which can in turn improve the
calculation accuracy of this work for reflecting the real trial successes.
However, as reported
83, the gaps in trial reporting databases/
system & their associated policies (e.g., lack of mandatory registration
requirement for Phase 1 trials) and unsatisfactory adherences to
existing act/policy (e.g., late registration of new trial, incomplete or
out-of-date registered trial information) suggested that there was
room for improvement. Recent effort of ClinicalTrials.gov to remind
users about the deadline for reporting trial result
84 and issuance of the
FDAAA final rule on trial reporting85 would fill some of those gaps and
generate frameworks for monitoring policy adherence, but consider-
able work remained to be done 86, which might include effective
enforcement from the regulators, open public audit of compliance for
sponsor, and so on so forth. Moreover, in this study and many pre-
ceding articles
2,3,22, the concept “success” was used to describe the
progression of drug in clinical development. However, in the real-
world clinical use of drugs, a “success” should be collectively deter-
mined by multiple factors
46, such as the sales of drugs and the net
patient benefits. In other words, this study focused on the clinical
progression of drugs and calculated their success rate in clinical
development. These calculated results should therefore not be directly
considered as a full reflection of the real-world success of drugs.
The determination of the clinical progression for some stem-cell
or other biologic-based projects was challenging, because they usually
had the vague name in early phase trial and even the same product
could vary from batch to batch. In other words, the reader was sug-
gested to be aware of the potential distortion introduced to the
assessment of ClinSRs by vague drug names.
Methodological limitations
Sensitivity analysis revealed that the selection of nine-year time-win-
dow was appropriate in term of the robustness of the calculated
ClinSRs. However, with the increase of the time-window size (from nine
to twelve), there remained subtle differences among the calculated
success rates. This indicated that it was essential to maintain a
Fig. 7 | The multi-functional platform titled ClinSR.org developed in this ana-
lysis. The unique characteristics of ClinSR.org included: a automated platform
enabling the dynamic description of ClinSRs;b personalized tool realizing the
customized measurement of ClinSR;c integrated database reconstructing the
CDP(s) for studied drug. New data and ClinSR assessment would be persistently
updated to ClinSR.orgfor the coming decade. CDP clinical development programs.
Article https://doi.org/10.1038/s41467-025-64552-2
Nature Communications| (2025) 16:9537 17

## Page 18

consistent window size, when comparing the ClinSRs, especially for
the case requiring high resolution in success rate assessment. In other
words, when it comes to a situation that the time-window size matters,
the selection of nine-year time-window may not be appropriate
enough, and our reported ClinSRs should thus be considered with
caution. In other words, this reliance on the time-window of speci fic
size cannot meet all analytical needs. Additionally, success rates were
calculated for various cohorts, and the same trial may be counted in
multiple windows, which made the studied time-windows not inde-
pendent from each other.
Moreover, with the updates of ClinicalTrials.gov, the clinical sta-
tus of some previous trials might be renewed to failures, which
reminded us to be caution with the potential bias on clinical success
rate due to boundary effect. Since insufficient time has passed to allow
us to know that a trial has failed, the ClinSRs might undergo a bias in
the latest time-windows.
Perspectives
Over the past two decades, it became obvious that the productivity
crisis of pharmaceutical R&D remained a great challenge with the
return-on-investment rates declining continuously28.T h i ss t u d yp r o -
vided a quantitative view on measuring the clinical trial success rate
and reflecting how the crisis shifts over time, which observed that the
success rates declined in the early 21st century, but then hit a plateau,
and recently underwent a marginal but noticeable increase. The
decline of success rate might be attributed to the exhaustion of easily
achievable target/candidate, tightened regulatory standard, and rising
competition that prioritized first/best-in-class drug
30- 32,w h i l et h e
recent increase of success might be considered to be driven by
advances in genetic knowledge and disease understanding, improved
decision-making process in the R&D, and lower regulatory threshold
43.
Additionally, a signi ficant increase of P3SR accompanied by a sub-
stantial decline of P1SR were discovered for the drugs treating onco-
logic diseases (illustrated in Supplementary Fig. S48). A similar but
milder trend for both P3SR and P1SR was also identified for all drugs (as
described in Supplementary Fig. S47a), which highlighted that there
may be an extensive positive contribution of anticancer drug to the
success of overall drug development. Furthermore, as depicted in
Supplementary Fig. S50, the OSRs of anti-infective drugs in the last two
time-windows were remarkably low (6.0% & 3.9%). It is of great interest
to investigate the impact of COVID-19 on such low success. After
excluding COVID-19 data, the OSRs in the last two time-windows
increased to 7.0% & 5.9%. These findings clearly demonstrated the
significant negative impacts of the anti-COVID-19 drugs on the success
of developing anti-infective drugs. Attention should be paid to the fact
that this was an effect of high acceleration of competitive efforts dri-
ven by pandemic state of necessity, and the vast majority of trial fail-
ures were an outcome of effective vaccines becoming available which
made some of the other development efforts redundant or no longer
justified by patient need. It was a unique situation that so many were
developed in parallel and accelerated to Phase 3 in short time, and thus
the effects on overall infectious diseases should be considered sepa-
rately, which may only affect the short-term trend of anti-
infective drugs.
As discovered by previous discussion, the industry-sponsored
clinical trials accounted for 70.1% of the trials analyzed in this study,
and showed much higher ClinSRs in Fig. 3 comparing with all trials
(including the industry-sponsored trials, academic-sponsored trials,
and so on). A similar phenomenon was also perceived in Fig.4bw h e n
analyzing the trials for COVID-19 (industry-sponsored trials led to a
much higher OSR than all COVID-19 trials). These results indicated that
non-industry-sponsored (especially, academic-sponsored) trials gave
substantially higher attrition rates than the industry-sponsored ones,
which suggested the academic researchers to collaborate with big
pharmaceutical company for resources
87. To realize such
collaboration, some strategies were proposed, including (a) resource
sharing platform, in which scienti fic data, physical entities, profes-
sional experiences, etc. from both academia and industry could be
openly shared
88;( b) joint research study , in which pharmaceutical
company either provided financial support for certain project at aca-
demic institution or carried out the project jointly with academia89;( c)
licensing intellectual properties, in which academic institutions granted
pharmaceutical companies the right to develop proprietary
technologies
90;( d) public-private partnership, in which multiple sta-
keholders, including pharmaceutical companies, academic institu-
tions, and so on, collaborated on large-scale research endeavors
91;( e)
joint clinical trial , in which academia and industry cooperated in
designing, carrying out and reporting their clinical trials92.
To overcome the funding limitations and regulatory barriers of
academic institutions, the seeking for industry collaboration as dis-
cussed above could partially address the challenge 67, however addi-
tional actions should be taken. The se included the integrations of
regulatory science into the educational programs of pharmaceutical
professionals
93, the early dialogues with the regulator in translational
research plan 94, the proactive communication with regulators
throughout drug discovery95, and the timely attention to translating
research findings into clinical practice96. Substantial variations in the
dynamic ClinSRs among different disease classes were observed in this
study (Supplementary Figs. S48- S61), and it was also identified that the
success rates for a disease class were not a precise predictor of the
success probabilities for individual diseases in that class, which asked
for personalized assessments for both disease class and individual
disease. Moreover, it was also of great importance to assess the
ClinSRs for a drug group of interests. For instance, in the development
of anti-COVID-19 drug (as shown in Supplementary Fig. S85c), the
ClinSRs of different categories of anti-COVID-19 drugs (such as vac-
cine, antiviral drug, and immunomodulator) varied greatly, which
asked for a measurement for any drug group of interest. Therefore, our
online platform ClinSR.org was constructed to meet such critical
demands.
A clear shift from SMDs to other dr ug modalities (e.g., antibody-
related drug) in current pharmaceutical R&D was observed in Fig. 6,
which resulted in a substantial expansion of ARD in clinical trial.
Meanwhile, as provided in Supplementary Figs. S62- S65, recent suc-
cess rates of ARDs greatly surpassed that of other drug modalities,
which might originate from its features of exquisite speci ficity, long
serum half-life, high af finity and immune effector function
97.T h e s e
features might give guidance for other drug modalities on how to
achieve a higher success rate. Moreover, SMDs remained the mainstay
of current pharmaceutical R&D, which were key for resolving the
problems ofproductivity crisis. Their poor physicochemical properties,
unmeaningful efficacy of the chosen target, and constant turmoil of
strategy changes with companies should therefore be carefully
addressed
68.
Furthermore, the sophisticated factors were identified here and
reported by previous publications29,41,44,50 to contribute to the ClinSRs
of drugs. Except for those related to pharmacology, a variety of other
invaluable factors might also substantially affect the clinical trial suc-
cess of drug. (a) Clinical trial design and execution. For example, due to
the heterogeneity of enrolled patients, the trials that could give opti-
mal therapy customization to individuals with speci fic markers were
constructed (such as basket trials and umbrella ones), which had
shown that these new trials were ushering in tremendous opportu-
nities for enhancing ‘success’
98.( b) Special FDA designations for drug
development. For example, the developments of drugs for rare/severe
medical condition could be promoted by orphan, fast track, acceler-
ated approval, priority review, and breakthrough therapy which might
affect success
31.( c) Development strategy of pharmaceutical companies.
For example, many pharmaceutical companies had taken advantages
of the depth and breadth of thecontract research organizations(CROs)
Article https://doi.org/10.1038/s41467-025-64552-2
Nature Communications| (2025) 16:9537 18

## Page 19

and outsourced many of the R&D activities as a way of reducing risks
and costs, which was also likely to affect trial successes 99.( d) ICMJE
policy and FDA regulations. Since the incomplete registrations of trials
might inflate resulting ClinSRs, the scope and content expansions of
mandatory trial registration by policies would thus make the trial data
more and more comprehensive and the calculated ClinSRs more and
more accurate.
Additionally, different stakeholders (including pharmaceutical
company, investor, and regulatory agency) might bene fit from the
online platform “ClinSR.org”.
For a pharmaceutical company, the
ClinSR.org might be useful for benchmarking its R&D project man-
agement, resource allocations, and portfolio decision 5. Particularly,
by leveraging the ClinSR.org, pharmaceutical companies could assess
the success rate of its own clinically-tested drugs, which might aid in
optimizing its pipeline decision.
For an investor, the ClinSR.org might
also be applied to guide decision-making when funding the devel-
opmental program for therapeutic candidate 4.S p e c ifically, Clin-
SR.org could be used to measure the probability of clinical trial
success for certain type of drug candidate, which might be helpful
for enabling prudent resource allocation and adjusting capital
investment strategy.
For a regulatory agency,ClinSR.org could realize
a retrospective evaluation of how the currently-implemented policy
impacted clinical trial success rates of drug discovery
6. Notably,
ClinSR.org performed a longitudinal study (spanning decades since
the beginning of this century) of clinical success rates, which might
be used to evaluate the effectiveness of formulated policies (like
orphan drug designation ) in promoting innovation or addressing
unmet medical needs.
In summary, this study tried to establish a reproducible, robust
& reliable protocol which enabled a public data-based assessment of
ClinSRs, and may be adopted as a reference by future analyses when
assessing ClinSRs. An explicit procedure for data standardization was
defined, the in-depth descriptions of which were critical for the
reproduction of our study by others; a dynamic strategy for mea-
suring ClinSRs was proposed in this study based on the assessment
of method robustness; careful analysis & correction of the inherent
bias in the data of publicly-accessible database were conducted.
Building on these contributions, some interesting findings were also
discovered.
Reporting summary
Further information on research design is available in the Nature
Portfolio Reporting Summary linked to this article.
Data availability
All data used in this study were collected from ClinicalTrials.gov
(https://clinicaltrials.gov/), Drugs@FDA ( https://www.fda.gov/drugs)
and Pharmaprojects ( https://citeline.informa.com/). The datasets
generated for calculating ClinSR during the current study are available
o nt h eo n l i n ep l a t f o r mClinSR.org (https://ClinSR.org/), which is
accessible without login requirement by user. The source data and
figures that support the findings of this study are also available in
Figshare https://doi.org/10.6084/m9.figshare.29646407) Source data
are provided with this paper.
Code availability
Python 3.10 is used for data analysis. All code supporting the analyses
is available at ClinSR.org (https://ClinSR.org/).
References
1. Zhang, K. et al. Arti ficial intelligence in drug development.Nat.
Med. 31,4 5- 59 (2025).
2. Hay, M., Thomas, D. W., Craighead, J. L., Economides, C. & Rosen-
thal, J. Clinical development success rates for investigational drugs.
Nat. Biotechnol.32,4 0- 51 (2014).
3. Dowden, H. & Munro, J. Trends in clinical success rates and ther-
apeutic focus. Nat. Rev. Drug Discov. 18, 495- 496 (2019).
4. Phares, S., Phillip, K. & Trusheim, M. Clinical development success
rates for durable cell and gene therapies.Nat. Rev. Drug Discov.24,
329- 330 (2025).
5. Schuhmacher, Hinder, A., Brief, M., Gassmann, E. & Hartl, O. D.
Benchmarking R&D success rates of leading pharmaceutical com-
panies: an empirical analysis of FDA approvals (2006-2022).Drug
Discov. Today 30, 104291 (2025).
6 . A t t w o o d ,M .M . ,R a s k - A n d e r s e n ,M .&S c h i o t h ,H .B .O r p h a nd r u g s
and their impact on pharmaceutical development.Trends Pharm.
Sci. 39,5 2 5- 535 (2018).
7 . W o n g ,C .H . ,S i a h ,K .W .&L o ,A .W .E s t i m a t i o no fc l i n i c a lt r i a l
success rates and related parameters.Biostatistics20,2 7 3- 286
(2019).
8 . D i M a s i ,J .A . ,F e l d m a n ,L . ,S e c k l e r ,A .&W i l s o n ,A .T r e n d si nr i s k s
associated with new drug development: success rates for investi-
gational drugs. Clin. Pharm. Ther. 87,2 7 2- 277 (2010).
9. Fernando, K. et al. Achieving end-to-end success in the clinic: P fi-
zer’s learnings on R&D productivity.Drug Discov. Today 27,
697- 704 (2022).
10. Kola, I. & Landis, J. Can the pharmaceutical industry reduce attrition
rates?. Nat. Rev. Drug Discov. 3,7 1 1- 715 (2004).
11. Yamaguchi, S., Kaneko, M. & Narukawa, M. Approval success rates
of drug candidates based on target, action, modality, application,
and their combinations.Clin. Transl. Sci. 14, 1113- 1122 (2021).
12. Duetz, C. et al. The wider perspective: twenty years of clinical trials
in myelodysplastic syndromes.Br. J. Haematol. 196,
329- 335 (2022).
1 3 . K i m ,C .K .e ta l .A l z h e i m e r’s disease: key insights from two decades
of clinical trial failures.J. Alzheimers Dis. 87
,8 3- 100 (2022).
14. DiMasi, J. A., Reichert, J. M., Feldman, L. & Malins, A. Clinical
approval success rates for investigational cancer drugs.Clin.
Pharm. Ther. 94,3 2 9- 335 (2013).
15. Li, N. et al. Changes in clinical trials of cancer drugs in mainland
China over the decade 2009-18: a systematic review.Lancet Oncol.
20,e 6 1 9- e626 (2019).
16. DiMasi, J. A. et al. Development times and approval success rates
for drugs to treat infectious diseases.Clin. Pharm. Ther. 107,
324- 332 (2020).
1 7 . M a h e r ,D .P . ,W o n g ,C .H . ,S i a h ,K .W .&L o ,A .W .E s t i m a t e so f
probabilities of successful development of pain medications: an
analysis of pharmaceutical clinical development programs from
2000 to 2020. Anesthesiology137,2 4 3- 251 (2022).
18. Lo, A. W., Siah, K. W. & Wong, C. H. Estimating probabilities of
success of vaccine and other anti-infective therapeutic develop-
ment programs. Harv. Data Sci. Rev. https://doi.org/10.1162/
99608f99692.e99600c99150e99608(2020).
19. Wang, Y. et al. Therapeutic target database 2020: enriched
resource for facilitating research and early development of
targeted therapeutics. Nucleic Acids Res. 48,D 1 0 3 1- D1041
(2020).
20. Wishart, D. S. et al. DrugBank 5.0: a major update to the DrugBank
database for 2018. Nucleic Acids Res. 46,D 1 0 7 4- D1082 (2018).
21. Miller, K. L., Rabinovitz, D. & Kerr, K. W. Transition probabilities for
clinical trials: investigating individual diseases.Nat. Rev. Drug Dis-
cov. 18,6 5 8( 2 0 1 9 ) .
22. Smietana, K., Siatkowski, M. & Moller, M. Trends in clinical success
rates. Nat. Rev. Drug Discov. 15,3 7 9- 380 (2016).
2 3 . T a m ,J .T . ,P a r k e r ,J .L . ,A n a s t a s o p u l o s ,D .&B a l t e r ,M .S .C l i n i c a lt r i a l
risk in chronic obstructive pulmonary disease: the effects of drug
class and inclusion criteria.Respiration91,7 9- 86 (2016).
2 4 . H u s s a i n ,H .T . ,P a r k e r ,J .L .&S h a r m a ,A .M .C l i n i c a lt r i a ls u c c e s s
rates of anti-obesity agents: the importance of combination thera-
pies. Obes. Rev. 16,7 0 7- 714 (2015).
Article https://doi.org/10.1038/s41467-025-64552-2
Nature Communications| (2025) 16:9537 19

## Page 20

25. DiMasi, J. A. Pharmaceutical R&D performance by firm size:
approval success rates and economic returns.Am. J. Ther. 21,
26- 34 (2014).
26. Arfe, A., Narang, C., DuBois, S. G., Reaman, G. & Bourgeois, F. T.
Clinical development of new drugs for adults and children with
cancer, 2010-2020.J. Natl Cancer Inst. 115,9 1 7- 925 (2023).
27. Zhang, S. X., Fergusson, D. & Kimmelman, J. Proportion of patients
in phase I oncology trials receiving treatments that are ultimately
approved. J. Natl Cancer Inst. 112,8 8 6- 892 (2020).
28. Schuhmacher, A., Hinder, M., von Stegmann Und Stein, A., Hartl, D.
& Gassmann, O. Analysis of pharma R&D productivity - a new per-
spective needed.Drug Discov. Today 28,1 0 3 7 2 6( 2 0 2 3 ) .
29. Sun, D., Gao, W., Hu, H. & Zhou, S. Why 90% of clinical drug
development fails and how to improve it?. Acta Pharm. Sin. B 12,
3049- 3062 (2022).
30. Van Norman, G. A. Phase II trials in drug development and adaptive
trial design. JACC Basic Transl. Sci. 4,4 2 8- 437 (2019).
31. Darrow, J. J., Avorn, J. & Kesselheim, A. S. FDA approval and
regulation of pharmaceuticals, 1983-2018.JAMA 323,1 6 4- 176
(2020).
32. Zhai, D. C., Zhang, Q. Y., Lu, X. L., You, Q. D. & Wang, L. Global first-
in-class drugs approved in 2023-2024: breakthroughs and insights.
Innovation6, 100801 (2024).
33. Mullard, A. R&D budgets boom, but success rates falter. Nat. Rev.
Drug Discov. 21, 249 (2022).
34. De Angelis, C. et al. Clinical trial registration: a statement from the
International Committee of Medical Journal Editors.N .E n g l .J .M e d .
351,1 2 5 0- 1251 (2004).
3 5 . A v o r n ,J . ,K e s s e l h e i m ,A .&S a r p a t w a r i ,A .T h eF D Aa m e n d m e n t sa c t
of 2007 - assessing its effects a decade later. N .E n g l .J .M e d .379,
1097- 1099 (2018).
36. Pun, F. W., Ozerov, I. V. & Zhavoronkov, A. AI-powered therapeutic
target discovery.Trends Pharm. Sci. 44,5 6 1- 572 (2023).
3 7 . P a t e l ,D .D . ,A n t o n i ,C . ,F r e e d m a n ,S .J . ,L e v e s q u e ,M .C .&S u n d y ,J .
S. Phase 2 to phase 3 clinical trial transitions: reasons for success
and failure in immunologic diseases.J. Allergy Clin. Immunol. 140,
685- 687 (2017).
3 8 . W o n g ,K .M . ,C a p a s s o ,A .&E c k h a r d t ,S .G .T h ec h a n g i n g
landscape of phase I trials in oncology. Nat. Rev. Clin. Oncol.
13,1 0 6- 117 (2016).
39. Lendrem, D. W. et al. Progression-seeking bias and rational opti-
mism in research and development.Nat. Rev. Drug Discov. 14,
219- 221 (2015).
40. Chen, C. et al. Trends of phase I clinical trials of new drugs in
mainland China over the past 10 years (2011-2020).Front. Med. 8,
777698 (2021).
41. Getz, K. A. & Campo, R. A. Trial watch: trends in clinical trial design
complexity.Nat. Rev. Drug Discov. 16, 307 (2017).
42. Park, J. J. H. et al. How COVID-19 has fundamentally changed clin-
ical research in global health.Lancet Glob. Health9,7 1 1- 720 (2021).
4 3 . R i n g e l ,M .S . ,S c a n n e l l ,J .W . ,B a e d e k e r ,M .&S c h u l z e ,U .B r e a k i n g
Eroom’sl a w .Nat. Rev. Drug Discov. 19,8 3 3- 834 (2020).
44. Kinch, M. S., Horn, C., Kraft, Z. & Schwartz, T. Expanding roles for
academic entrepreneurship in drug discovery.Drug Discov. Today
25,1 9 0 5- 1909 (2020).
4 5 . D eW i l d e ,B .e ta l .T h ec r i t i c a lr o l eo fa c a d e m i cc l i n i c a lt r i a l si n
pediatric cancer drug approvals: design, conduct, andfitf o rp u r -
pose data for positive regulatory decisions.J. Clin. Oncol. 40,
3456 (2022).
46. Schuhmacher, A., Hinder, M., Boger, N., Hartl, D. & Gassmann, O.
The significance of blockbusters in the pharmaceutical industry.
Nat. Rev. Drug Discov. 22,1 7 7- 178 (2023).
47. Takebe, T., Imai, R. & Ono, S. The current status of drug discovery
and development as originated in united states academia: the
influence of industrial and academic collaboration on drug dis-
covery and development.Clin. Transl. Sci. 11,5 9 7- 606 (2018).
48. Shih, H. P., Zhang, X. & Aronov, A. M. Drug discovery effectiveness
from the standpoint of therapeutic mechanisms and indications.
Nat. Rev. Drug Discov. 17,1 9- 33 (2018).
49. Liu, Z., Delavan, B., Roberts, R. & Tong, W. Lessons learned from two
decades of anticancer drugs.Trends Pharm. Sci. 38,
852- 872 (2017).
50. Nass, S. J. et al. Accelerating anticancer drug development -
opportunities and trade-offs.Nat. Rev. Clin. Oncol. 15,
777- 786 (2018).
51. Zhao, S. et al. Time to raise the bar: transition rate of phase 1 pro-
grams on anticancer drugs.Cancer Cell 40,2 3 3- 235 (2022).
52. Araujo, D. et al. Oncology pha se I trial design and conduct: time
for a change - MDICT guidelines 2022. Ann. Oncol. 34,4 8- 60
(2023).
5 3 . F e r n a n d e s ,D .C . ,R e i s ,R .L .&O l i v e i r a ,J .M .A d v a n c e si n3 Dn e u r a l ,
vascular and neurovascular models for drug testing and regen-
erative medicine.Drug Discov. Today 26,7 5 4- 768 (2021).
54. Zhang, W., Mehta, A., Tong, Z., Esser, L. & Voelcker, N. H. Devel-
opment of polymeric nanoparticlesfor blood-brain barrier transfer-
strategies and challenges.Adv. Sci. 8, 2003937 (2021).
55. Dawson, T. M., Golde, T. E. & Lagier-Tourenne, C. Animal models of
neurodegenerative diseases. Nat. Neurosci. 21,1 3 7 0- 1379 (2018).
56. Kumar, D., Md Ashraf, G., Bilgrami, A. L. & Imtaiyaz Hassan, M.
Emerging therapeutic developments in neurodegenerative dis-
eases: a clinical investigation.Drug Discov. Today 27,
103305 (2022).
57. Berntorp, E. et al. Haemophilia. Nat. Rev. Dis. Prim. 7,4 5( 2 0 2 1 ) .
58. Sparkenbaugh, E. & Pawlinski, R. Prothrombotic aspects of sickle
cell disease. J. Thromb. Haemost. 15,1 3 0 7- 1316 (2017).
5 9 . M a n c u s o ,M .E . ,M a h l a n g u ,J .N .&P i p e ,S .W .T h ec h a n g i n gt r e a t -
ment landscape in haemophilia: from standard half-life clotting
factor concentrates to gene editing.Lancet 397,6 3 0- 640 (2021).
60. Pushpakom, S. et al. Drug repurposing: progress, challenges and
recommendations.Nat. Rev. Drug Discov. 18,4 1- 58 (2019).
61. Tran, A. A. & Prasad, V. Drug repu rposing for cancer treatments: a
well-intentioned, but misguided strategy.Lancet Oncol. 21,
1134- 1136 (2020).
62. Papapetropoulos, A. & Szabo, C. Inventing new therapies without
reinventing the wheel: the power of drug repurposing.Br. J. Pharm.
175,1 6 5- 167 (2018).
6 3 . D eG a s p e r i s - B r i g a n t e ,C .D . ,P a r k e r ,J .L . ,O’Connor, P. W. & Bruno, T.
R. Reducing clinical trial risk in multiple sclerosis.Mult. Scler. Relat.
Disord. 5,8 1- 88 (2016).
64. Begley, C. G. et al. Drug repurposing: misconceptions, challenges,
and opportunities for academic researchers.
Sci. Transl. Med. 13,
eabd5524 (2021).
65. Cummings, J. L. et al. Drug repurposing for Alzheimer ’sd i s e a s e
and other neurodegenerative disorders.Nat. Commun. 16,1 7 5 5
(2025).
66. Parrish, M. C., Tan, Y. J., Grimes, K. V. & Mochly-Rosen, D. Surviving
in the valley of death: opportunities and challenges in translating
academic drug discoveries.Annu. Rev. Pharm. Toxicol. 59,
405- 421 (2019).
6 7 . M u r r a y ,A .J . ,C o x ,L .R . ,A d c o c k ,H .V .&R o b e r t s ,R .A .A c a d e m i c
drug discovery: challenges and opportunities.Drug Discov. Today
29, 103918 (2024).
6 8 . B e c k ,H . ,H a r t e r ,M . ,H a s s ,B . ,S c h m e c k ,C .&B a e r f a c k e r ,L .S m a l l
molecules and their impact in drug discovery: a perspective on the
occasion of the 125th anniversary of the Bayer chemical research
laboratory.Drug Discov. Today 27,1 5 6 0- 1574 (2022).
69. Lu, R. M. et al. Development of therapeutic antibodies for the
treatment of diseases.J. Biomed. Sci. 27, 1 (2020).
Article https://doi.org/10.1038/s41467-025-64552-2
Nature Communications| (2025) 16:9537 20

## Page 21

70. Janiaud, P., Hemkens, L. G. & Ioannidis, J. P. A. Challenges and
lessons learned from COVID-19 trials: should we be doing clinical
trials differently?.Can. J. Cardiol. 37,1 3 5 3- 1364 (2021).
71. Wong, L. P. et al. Investigating post-COVID-19 con fidence in
emergency use authorization vaccines: a hypothetical case of
mpox. PLoS Negl. Trop. Dis. 19, e0013037 (2025).
72. Baedeker, M., Ringel, M. & Schulze, U. 2020 FDA approvals:
momentum kept despite COVID-19, but value falls.Nat. Rev. Drug
Discov. 20,9 2( 2 0 2 1 ) .
7 3 . P a r d i ,N .&W e i s s m a n ,D .D e v e lopment of vaccines and antivirals
for combating viral pandemics.Nat. Biomed. Eng. 4, 1128- 1133
(2020).
74. Jin, L., Zhou, Y., Zhang, S. & Chen, S. J. mRNA vaccine sequence and
structure design and optimization: advances and challenges.J. Biol.
Chem. 301, 108015 (2025).
75. Mehrotra, D. V. et al. Clinical endpoints for evaluating ef ficacy in
COVID-19 vaccine trials.Ann. Intern. Med. 174, 221- 228 (2021).
76. Lowery, S. A., Sariol, A. & Perlman, S. Innate immune and in flam-
matory responses to SARS-CoV-2: implications for COVID-19.Cell
Host Microbe 29,1 0 5 2- 1062 (2021).
77. Wang, C. et al. COVID-19 in early 2021: current status and looking
forward. Signal Transduct. Target Ther.6, 114 (2021).
78. Sweeney, D. A., Lobo, S. M., Povoa, P. & Kalil, A. C. Choosing
immunomodulating therapies for the treatment of COVID-19:
recommendations based on placebo-controlled trial evidence.
Clin. Microbiol Infect.30,6 1 1- 618 (2024).
79. Slomski, A. Repurposed drugs failed to prevent severe COVID-19.
JAMA 328, 1171 (2022).
8 0 . C l o u t ,A .E . ,D e l l aP a s q u a ,O . ,H a n n a ,M .G . ,O r l u ,M .&P i t c e a t h l y ,R .
D. S. Drug repurposing in neurological diseases: an integrated
approach to reduce trial and error.J. Neurol. Neurosurg. Psychiatry
90,1 2 7 0- 1275 (2019).
81. Recino, A., Rayner, M. L. D., Rohn, J. L. & Pasqua, O. D. Therapeutic
innovation in drug repurposing: challenges and opportunities.Drug
Discov. Today 30,1 0 4 3 9 0( 2 0 2 5 ) .
82. Mittal, N. & Mittal, R. Repurpos ing old molecules for new indica-
tions: defining pillars of success from lessons in the past. Eur. J.
Pharm. 912, 174569 (2021).
83. Zarin, D. A., Tse, T., Williams, R. J. & Rajakannan, T. Update on trial
registration 11 years after the ICMJE policy was established.N. Engl.
J. Med. 376,3 8 3- 391 (2017).
84. DeVito, N. J. & Goldacre, B. Eval uation of compliance with legal
requirements under the FDA amendments act of 2007 for timely
registration of clinical trials, data verification, delayed reporting,
and trial document submission.JAMA Intern. Med. 181,
1128- 1130 (2021).
85. Zarin, D. A., Tse, T., Williams, R. J. & Carr, S. Trial reporting in
ClinicalTrials.gov - the final rule. N. Engl. J. Med. 375,
1998- 2004 (2016).
86. DeVito, N. J., Bacon, S. & Goldacre, B. Compliance with legal
requirement to report clinical trialresults on ClinicalTrials.gov: a
cohort study. Lancet 395,3 6 1- 369 (2020).
87. Lipton, S. A. & Nordstedt, C. Partnering with big pharma-what
academics need to know. Cell 165,5 1 2- 515 (2016).
88. Flier, J. S. Academia and industry: allocating credit for discovery
and development of new therapies.J. Clin. Invest. 129,
2172- 2174 (2019).
89. Ramsey, B. W., Nepom, G. T. & Lonial, S. Academic, foundation, and
industry collaboration infinding new therapies.N. Engl. J. Med.376,
1762- 1769 (2017).
90. Peeva, E. et al. Unlocking disease insights to facilitate drug devel-
opment: pharmaceutical industry-academia collaborations in
inflammation and immunology.Drug Discov. Today 30,
104317 (2025).
9 1 . Y i l d i r i m ,O . ,G o t t w a l d ,M . ,S c h u l e r ,P .&M i c h e l ,M .C .O p p o r t u n i t i e s
and challenges for drug development: public-private partnerships,
adaptive designs and big data. Front. Pharm. 7,4 6 1( 2 0 1 6 ) .
9 2 . R a s m u s s e n ,K . ,B e r o ,L . ,R e d b e r g ,R . ,G o t z s c h e ,P .C .&L u n d h ,A .
Collaboration between academics and industry in clinical trials:
cross sectional study of publications and survey of lead academic
authors. BMJ 363,k 3 6 5 4( 2 0 1 8 ) .
93. Kallio, M. J. et al. Translating academic drug discovery into clinical
development: a survey of the awareness of regulatory support and
requirements among stakeholders in Europe.Clin. Pharm. Ther.113,
349- 359 (2023).
94. Starokozhko, V. et al. Strengthening regulatory science in acade-
mia: STARS, an EU initiative to bridge the translational gap.Drug
Discov. Today 26,2 8 3- 288 (2021).
95. Everts, M. & Drew, M. Successful ly navigating the valley of death:
the importance of accelerators to support academic drug discovery
and development.Expert Opin. Drug Discov. 19,2 5 3- 258 (2024).
96. Starokozhko, V. et al. Strategic recommendations from the STARS
project to foster academic drug development.Nat. Rev. Drug Dis-
cov. 22,2 5 1- 252 (2023).
97. Zinn, S. et al. Advances in antibody-based therapy in oncology.Nat.
Cancer 4,1 6 5- 180 (2023).
98. Duan, X. P. et al. New clinical trial design in precision medicine:
discovery, development and direction.Signal Transduct. Target
Ther. 9,5 7( 2 0 2 4 ) .
99. Xia, C. & Gautam, A. Biopharma CRO industry in China: landscape
and opportunities.Drug Discov. Today 20,7 9 4- 798 (2015).
Acknowledgements
Funded by National Natural Science Foundations of China (82373790:
F.Z., 22220102001: F.Z., 62502424: Yi.Z.);Natural Science Foundations
of Zhejiang (RG25H300001: F.Z.); andNational Key R&D Programs of
China (2024YFA1307503: F.Z.). Thanks for theInformation Technology
Center of Zhejiang University.
Author contributions
F.Z. conceived the idea, and designed the entire study; Yi.Z., Y.T.Z.,
H.W.X., Z.C., S.J.H., Y.H.L., J.B.F, D.H.Z., X.Y.S., and X.C.L. collected the
data; Yi.Z., Y.T.Z. and H.N.Z. performed the data analyses; Yi.Z., Y.T.Z.,
Z.C., S.J.H., Yu.Z., K.X.L., Y.Q.Q., L.Y.H., and H.B.D. generatedfigures &
tables; Yi.Z. and Y.T.Z. designed and constructed the website ofClin-
SR.org; F.Z., Yi.Z., Y.T.Z., H.W.X., Y.Z.W. and W.Q.X. contributed to the
revision; F.Z. and Yi.Z. wrote the manuscript.
Competing interests
The authors declare no competing interests.
Additional information
Supplementary informationThe online version contains
supplementary material available at
https://doi.org/10.1038/s41467-025-64552-2.
Correspondenceand requests for materials should be addressed to
Feng Zhu.
Peer review informationNature Communicationsthanks Kang Zhang,
and the other, anonymous, reviewer(s)for their contribution to the peer
review of this work. A peer review file is available.
Reprints and permissions informationis available at
http://www.nature.com/reprints
Publisher’s note Springer Nature remains neutral with regard to jur-
isdictional claims in published maps and institutional affiliations.
Article https://doi.org/10.1038/s41467-025-64552-2
Nature Communications| (2025) 16:9537 21

## Page 22

Open Access This article is licensed under a Creative Commons
Attribution-NonCommercial-NoDerivatives 4.0 International License,
which permits any non-commercial use, sharing, distribution and
reproduction in any medium or format, as long as you give appropriate
credit to the original author(s) and the source, provide a link to the
Creative Commons licence, and indicate if you modified the licensed
material. You do not have permission under this licence to share adapted
material derived from this article or parts of it. The images or other third
party material in this article are included in the article’s Creative
Commons licence, unless indicatedotherwise in a credit line to the
material. If material is not included in the article’s Creative Commons
licence and your intended use is not permitted by statutory regulation or
exceeds the permitted use, you will need to obtain permission directly
from the copyright holder. To view a copy of this licence, visit http://
creativecommons.org/licenses/by-nc-nd/4.0/.
© The Author(s) 2025
Article https://doi.org/10.1038/s41467-025-64552-2
Nature Communications| (2025) 16:9537 22

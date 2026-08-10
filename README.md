# Supporting Calibrated Reliance in Human-AI Collaboration: Different Strategies for Different Tasks

This repository contains the materials, anonymized data, and analysis code for three human-subject studies examining how different forms of AI support affect human–AI decision making. Across the studies, we analyze human accuracy, reliance on correct AI predictions, and recovery from incorrect AI predictions.

## Studies

### Study 1: RAVEN Multi-Stage Study

A within-subjects multi-stage reveal study using RAVEN visual reasoning tasks. The design separates the effect of seeing an AI prediction from the subsequent effect of seeing an explanation. Participants encountered LLM Explanation and occlusion-sensitivity (OS) Heatmap support.

Materials: [`study_1_raven_multistage/`](study_1_raven_multistage/)

### Study 2: RAVEN Between-Subjects Study

A between-subjects comparison of AI-support formats on RAVEN visual reasoning tasks. Participant-facing conditions were **Human Only**, **Prediction Only**, **LLM Explanation**, **OS Heatmap**, and **Predicted Probabilities**. The analysis also includes a **Selective Automation** benchmark derived from Study 2 data; it was not a separate participant group.

Materials: [`study_2_raven_between_subjects/`](study_2_raven_between_subjects/)

### Study 3: LSAT Between-Subjects Study

A between-subjects study using LSAT logical-reasoning questions. Conditions were **Prediction Only**, **LLM Explanation**, **Expert Explanation**, and **Predicted Probabilities**.

Materials: [`study_3_lsat_between_subjects/`](study_3_lsat_between_subjects/)

## Repository structure

```text
.
├── README.md
├── study_1_raven_multistage/
│   └── README.md
├── study_2_raven_between_subjects/
│   └── README.md
├── study_3_lsat_between_subjects/
│   └── README.md
├── paper_images/
└── statistical_analysis_all_experiments.ipynb
```

- [`study_1_raven_multistage/`](study_1_raven_multistage/) — materials for the RAVEN Multi-Stage Study.
- [`study_2_raven_between_subjects/`](study_2_raven_between_subjects/) — materials for the RAVEN Between-Subjects Study.
- [`study_3_lsat_between_subjects/`](study_3_lsat_between_subjects/) — materials for the LSAT Between-Subjects Study.
- [`paper_images/`](paper_images/) — figures and interface images used in the paper.
- [`statistical_analysis_all_experiments.ipynb`](statistical_analysis_all_experiments.ipynb) — main statistical-analysis notebook for the three studies.

## Reproducing the analyses

The main analysis entry point is [`statistical_analysis_all_experiments.ipynb`](statistical_analysis_all_experiments.ipynb). It uses relative paths to data inside the three study folders so that the repository can be cloned and analyzed without machine-specific path changes.

Each study README identifies the relevant task materials, AI outputs/explanations, participant-facing materials, anonymized result files, and study-specific analysis code.


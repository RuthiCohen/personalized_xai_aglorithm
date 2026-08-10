# Study 3: LSAT Between-Subjects Study

## Study overview

Study 3 is a between-subjects study using LSAT logical-reasoning questions. It compares prediction-only support with three forms of additional information: an LLM Explanation, an Expert Explanation, and Predicted Probabilities.

## Participants and conditions

The study included **80 participants**, with 20 participants assigned to each condition:

- **Prediction Only**
- **LLM Explanation**
- **Expert Explanation**
- **Predicted Probabilities**

## Experimental procedure

Participants answered 10 LSAT logical-reasoning questions while receiving the support associated with their assigned condition. The AI prediction was correct on a subset of the experimental items, enabling analyses of reliance on correct AI predictions and recovery from incorrect AI predictions.

## Repository contents

```text
study_3_lsat_between_subjects/
├── README.md
├── data/
│   └── lsat_questions.json
├── general_documents/
├── participant_materials/
├── results/
└── results_analysis_experiment.ipynb
```

- `data/` — LSAT questions and task-level AI/explanation data.
- `general_documents/` — supplementary study/data documentation.
- `participant_materials/` — introduction screens, condition-specific materials, questionnaires, consent materials, and LLM prompt.
- `results/` — anonymized Study 3 result/questionnaire files.
- `results_analysis_experiment.ipynb` — Study 3-specific analysis.

## AI outputs and explanations

- **AI predictions:** stored with the task records in `data/lsat_questions.json`.
- **LLM prompt:** `participant_materials/prompt.rtf`.
- **LLM-generated explanations:** stored in the corresponding question records in `data/lsat_questions.json`.
- **Expert explanations:** stored in the corresponding question records/materials in `data/lsat_questions.json`.
- **Predicted Probabilities:** probability/confidence values used for the participant-facing support are stored with the question records in `data/lsat_questions.json`. The repository documentation refers to this condition as **Predicted Probabilities**, even where a legacy JSON field name contains the word `Conf`.
- **Task/question identifiers:** `data/lsat_questions.json` includes the released question IDs and task content.

The experimental question IDs are 1, 3, 4, 5, 11, 12, 15, 17, 20, and 22.

## Participant-facing materials

- `participant_materials/1-info.png`, `2-intro.png`, `3-intro.png` — participant-facing information/introduction screens.
- `participant_materials/group_a/` through `group_d/` — condition-specific interface/example materials.
- `participant_materials/rating.png` — rating interface material.
- `participant_materials/prompt.rtf` — LLM prompt.
- `participant_materials/questionnaires/` — questionnaires and informed-consent materials.

## Data

Task-level study content is in `data/lsat_questions.json`. The released records include question identifiers and text, answer choices, the correct answer, AI-selected answer, LLM/expert explanation fields, and probability/confidence fields used by the support condition.

Anonymized participant results are stored under `results/`, including:

- `experiment_runs_log_users_info_P7iwzVBKHYbSDrUWE.csv`
- `questionnaires_answers_log.csv`

The analysis uses anonymized identifiers (`tuid`), assigned condition (`ugroup`), participant selections, correct-answer values, and AI-selected-option values, together with questionnaire measures.

## Analysis

- `results_analysis_experiment.ipynb` — Study 3-specific analysis.
- [`../statistical_analysis_all_experiments.ipynb`](../statistical_analysis_all_experiments.ipynb) — main notebook reproducing analyses across all three studies.

# Study 2: RAVEN Between-Subjects Study

## Study overview

Study 2 is a between-subjects study comparing different forms of AI support on RAVEN visual reasoning tasks. It tests how support format affects decision accuracy and reliance, including reliance on correct AI predictions and recovery from incorrect AI predictions.

## Participants and conditions

The study included **100 participants**, with 20 participants assigned to each of five participant-facing conditions:

- **Human Only**
- **Prediction Only**
- **LLM Explanation**
- **OS Heatmap**
- **Predicted Probabilities**

The analysis additionally reports a **Selective Automation** benchmark derived from Study 2 data. Selective Automation is an analysis benchmark and **was not a separate participant group**.

## Experimental procedure

Participants completed 10 RAVEN problems under their assigned support condition. The AI was correct on a subset of the study items, enabling analyses of both appropriate reliance on correct AI predictions and recovery when AI predictions were incorrect. Participants in the explanation/probability-support conditions received the support associated with their assigned condition.

## Repository contents

```text
study_2_raven_between_subjects/
├── README.md
├── data/
├── dataset/
├── participant_materials/
├── results/
├── dataset_utility.py
├── dcnet.py
├── helpers.ipynb
├── model_new_04.pth
└── results_analysis_experiment.ipynb
```

- `data/` — RAVEN task instances and participant-facing AI-support artifacts.
- `dataset/` — RAVEN dataset categories used by the model/code.
- `participant_materials/` — experiment materials, questionnaires, and the LLM prompt.
- `results/` — anonymized participant interaction/result files.
- `dcnet.py`, `model_new_04.pth`, `dataset_utility.py` — model and dataset code/assets.
- `helpers.ipynb` — supporting notebook utilities.
- `results_analysis_experiment.ipynb` — Study 2-specific analysis.

## AI outputs and explanations

- **AI predictions:** prediction materials and task-specific outputs are in `data/`; model code/weights are in `dcnet.py` and `model_new_04.pth`.
- **LLM prompt:** `participant_materials/prompt.rtf`.
- **LLM-generated explanations:** `data/LLM_*`.
- **OS Heatmaps:** `data/OS_*`.
- **Predicted Probabilities:** participant-facing probability-support images are under `data/cPredicted Probabilities/`. 
- **Task/question identifiers:** the task folders in `data/` and `data/questions.pptx`.

## Participant-facing materials

- **Task/question set:** `data/questions.pptx` and task-specific data folders.
- **Experiment/interface materials:** `participant_materials/experiment/`.
- **Questionnaires:** `participant_materials/questionnaires/`.
- **Informed-consent materials:** see the consent/information files released under `participant_materials/`.
- **Interface images:** participant-facing examples are stored in the experiment/materials folders and in `paper_images/` at repository root.

## Data

Anonymized Study 2 results are stored under `results/`, including:

- `experiment_runs_log_users_actions_changes_only.csv` — task-level interaction/action records.
- `experiment_runs_log_users_info_P7iwzVBKHYbSDrUWE.csv` — anonymized participant/session-level information used by the analysis.

Important fields used by the analysis include anonymized participant identifiers (`tuid`), assigned group (`ugroup`), task/block identifiers, true answers, AI predictions, participant selections, and action/step information.

Legacy group codes in the released data map to the participant-facing conditions as follows:

- A → Human Only
- B → Prediction Only
- C → LLM Explanation
- D → OS Heatmap
- E → Predicted Probabilities

Any Group F object created in the analysis code represents the **derived Selective Automation benchmark**, not an additional experimental condition.

## Analysis

- `results_analysis_experiment.ipynb` — Study 2-specific analysis.
- [`../statistical_analysis_all_experiments.ipynb`](../statistical_analysis_all_experiments.ipynb) — main cross-study statistical-analysis notebook. This notebook also derives and evaluates the Selective Automation benchmark from Study 2 data.

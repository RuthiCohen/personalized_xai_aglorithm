# Study 1: RAVEN Multi-Stage Study

## Study overview

Study 1 is a within-subjects multi-stage reveal study using RAVEN visual reasoning problems. Its purpose is to separate the effect of an AI prediction from the additional effect of an explanation. For each task, participants first answered independently, then saw the AI prediction, and then saw an explanation. The explanation modality was either an **LLM Explanation** or an **OS Heatmap**.

## Participants and conditions

The study included **27 participants**. Each participant completed **16 RAVEN problems** or less, organized into two blocks of eight. One block used LLM Explanation support and the other used OS Heatmap support.

## Experimental procedure

For each RAVEN item, participants progressed through three decision stages:

1. **Human-only stage** — the participant selected an answer before seeing AI support.
2. **Prediction stage** — the AI prediction was revealed and the participant could revise the answer.
3. **Explanation stage** — either an LLM Explanation or an OS Heatmap was revealed and the participant could revise again.

Confidence/subjective ratings associated with the task are stored in the released study results where applicable.

## Repository contents

```text
study_1_raven_multistage/
├── README.md
├── data/
├── dataset/
├── participant_materials/
├── results/
├── dataset_utility.py
├── dcnet.py
├── generate_data.ipynb
├── model_new_04.pth
├── results_analysis_experiment.ipynb
├── test.py
└── train.py
```

- `data/` — selected RAVEN task instances and the AI-support artifacts shown in the experiment.
- `dataset/` — RAVEN dataset categories used by the model/code.
- `participant_materials/` — experiment materials, questionnaires, and the LLM prompt.
- `results/` — anonymized participant interaction/result files.
- `dcnet.py`, `model_new_04.pth`, `train.py`, `test.py` — model implementation, saved weights, and model utilities.
- `generate_data.ipynb` — code used to prepare model outputs/support artifacts, including OS materials.
- `results_analysis_experiment.ipynb` — study-specific analysis notebook.

## AI outputs and explanations

- **AI predictions:** task-specific prediction materials are in `data/`; model code is in `dcnet.py` and the saved model weights are in `model_new_04.pth`.
- **LLM prompt:** `participant_materials/prompt.rtf`.
- **LLM-generated explanations:** the `data/LLM_*` directories contain the task-specific LLM-support materials used for the released Study 1 items.
- **OS Heatmaps:** the `data/OS_*` directories contain the task-specific occlusion-sensitivity materials. `generate_data.ipynb` contains the associated preparation/generation code.
- **Task/question identifiers:** the item identifiers are reflected by the task-specific folders in `data/`; `data/questions.pptx` is the participant-facing question set.

## Participant-facing materials

- **Task instances / question set:** `data/questions.pptx` and the task-specific materials in `data/`.
- **Experiment/interface materials:** `participant_materials/experiment/`.
- **Questionnaires:** `participant_materials/questionnaires/`.
- **Informed-consent materials:** see the consent/information materials released under `participant_materials/`.
- **Interface/demo material:** `data/raven-experiment.mp4` and images contained in the participant-facing folders.

## Data

Anonymized Study 1 results are stored under `results/`, including:

- `experiment_runs_log_users_actions_changes_only.csv` — task-level interaction/action records.
- `experiment_runs_log_users_info_P7iwzVBKHYbSDrUWE.csv` — anonymized participant/session-level study information used by the analysis.

The analysis uses anonymized identifiers (for example `tuid`) together with task ground truth, AI predictions, participant choices at the pre-AI / post-prediction / post-explanation stages, experimental parameters, and rating variables. See the analysis notebooks for the exact columns used in each reported analysis.

## Analysis

Two analysis entry points are provided:

- `results_analysis_experiment.ipynb` — Study 1-specific analysis.
- [`../statistical_analysis_all_experiments.ipynb`](../statistical_analysis_all_experiments.ipynb) — the main notebook reproducing the statistical analyses reported across all three studies.

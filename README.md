# Personalized XAI Algorithm – Experiments Overview

This repository contains 3 experiments focused on generating data and applying explainability techniques using neural networks and reasoning datasets.


## 🧠 Experiment 1: Raven-10k with DCNet

This experiment involves creating reasoning data using the **DCNet** model, adapted from the original repository:  
🔗 https://github.com/visiontao/dcnet/tree/main

> **Note:** The required DCNet model files have already been included in this repository.  
> There is **no need to download them again** from the original source.
> We run this code to create images of 640x640.

### 📥 Dataset
The model is trained and evaluated on the **RAVEN-10k** dataset, which can be downloaded from:  
🔗 https://wellyzhang.github.io/project/raven.html#dataset  
> Click on the **Google Drive link** to download the dataset and place it in the appropriate directory.
> Place the RAVEN-10k in a directory: `raven10k-640x640`, this is a zip directory so please unzeep it before running.

### 📂 Important Files
- `generate_data.py` – Creates a folder containing visual reasoning puzzles and runs different explanation methods on them.
- `main.py` – Demonstrates example explanations for a selected Raven matrix.
- `train.py` – Trains the DCNet model across multiple folds.(DCnet repository).
- `test.py` – Test the DCNet models and returns the accuracy results. (DCnet repository).
- `results_anaylsis_experiment.ipynb` - The statistical results of the experiment.
- `results/` - This directory contains the experiment results.

### 📊 Output
- Training will result in **30 saved models**.
- The selected model used for explanations in this repository is `model_new_04.pth`, which achieved an accuracy of **~88%**.

### 🗂️ Explanations Output Folder Structure

Inside the `experiment_1_RAVEN/data/` directory:

- Contains images shown in the experiment with **LLM-generated explanations** and **Occlustion sensitivity explanations**.
  - `OS_{example_id}/`: Examples where the OS provided the answer.
  - `LLM_{example_id}/`: Examples where the LLM provided the answer.
  - Inside each, there are 2 folders: `matrix` and `choices` both for keeping the matrix and the choices images. inside the OS folders there are 2 more folders for `OS_matrix` and `OS_choices`.

- `predictions1-8.png`: A table comparing actual vs. predicted answers from both the LLM and the occlusion sensitivity method.
- `questions.pptx`: A presentation with all the questions in the experiment.
---

## 🧠 Experiment 2: Raven-10k with DCNet

This experiment involves creating reasoning data using the **DCNet** model same as experiment RAVEN 1, adapted from the original repository:  
🔗 https://github.com/visiontao/dcnet/tree/main


### 📂 Important Files/Directories
- `results_anaylsis_experiment.ipynb` - The statistical results of the experiment.
- `data/` - This directory contains 10 questions from **Experiment RAVEN 1**.
- `results/` - This directory contains the experiment results.
---

## 🧠 Experiment 3: LSAT

This experiment involves creating LSAT reasoning data using the **LLM(ChatGpt5)** model.

### 📂 Important Files/Directories
- `results_anaylsis_experiment.ipynb` - The statistical results of the experiment.
- `data/experiment-lsat-questiosn.json` - This file contains all the LSAT questions that were run in the experiment.
- `results/` - This directory contains the experiment results.

---

Feel free to open an issue or contribute if you're interested in extending the experiments or testing alternative explainability methods.

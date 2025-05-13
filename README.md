# Personalized XAI Algorithm – Experiments Overview

This repository contains two experiments focused on generating data and applying explainability techniques using neural networks and symbolic reasoning datasets.

---

## 🧪 Experiment 1: EMNIST Alphabet with CNN

This experiment involves generating data using a Convolutional Neural Network (CNN) trained on the EMNIST alphabet dataset.

### 📥 Dataset
To run the experiment, download the following files from the [EMNIST Kaggle page](https://www.kaggle.com/datasets/crawford/emnist):

- `emnist-letters-train.csv`
- `emnist-letters-test.csv`

Place both files inside the `experiment 1/` directory.

### 📂 Important File
- `eminst.ipynb` – Jupyter notebook for creating training data and generating explanations.

### 📊 Output
- After running the notebook, a model file `emnist_model.keras` will be generated with a final accuracy of **83.23%**.
  (the trained model is in the "trained_models/emnist_model.keras")
- The notebook includes the implementation of **two types of explanations** for model predictions.

---

## 🧠 Experiment 2: Raven-10k with DCNet

This experiment involves creating reasoning data using the **DCNet** model, adapted from the original repository:  
🔗 https://github.com/visiontao/dcnet/tree/main

### 📥 Dataset
The model is trained and evaluated on the **RAVEN-10k** dataset, which can be downloaded from:  
🔗 https://wellyzhang.github.io/project/raven.html#dataset  
> Click on the **Google Drive link** to download the dataset and place it in the appropriate directory.
> Place the RAVEN-10k in a directory: `experiment_2/dataset/RAVEN-10000`

### 📂 Important Files
- `generate_data.py` – Creates a folder containing visual reasoning puzzles and runs different explanation methods on them.
- `main.py` – Demonstrates example explanations for a selected Raven matrix.
- `train.py` – Trains the DCNet model across multiple folds.(DCnet repository)
- `test.py` – Test the DCNet models and returns the accuracy results. (DCnet repository)

### 📊 Output
- Training will result in **30 saved models**.
- The selected model used for explanations in this repository is `model_02.pth`, which achieved an accuracy of **87.914%**.

---

Feel free to open an issue or contribute if you're interested in extending the experiments or testing alternative explainability methods.

# Personalized XAI Algorithm – Experiments Overview

This repository contains two experiments focused on generating data and applying explainability techniques using different neural network architectures and datasets.

---

## 🧪 Experiment 1: EMNIST Alphabet with CNN

This experiment involves generating classification data using a Convolutional Neural Network (CNN) trained on the EMNIST alphabet dataset.

### 📥 Dataset
To run this experiment, download the following files from the [EMNIST Kaggle page](https://www.kaggle.com/datasets/crawford/emnist):

- `emnist-letters-train.csv`
- `emnist-letters-test.csv`

Place both files inside the `experiment 1/` directory.

### 📂 Important File
- `eminst.ipynb` – Jupyter notebook for generating and analyzing the EMNIST data.

---

## 🧠 Experiment 2: Raven-10k with DCNet

This experiment involves generating reasoning data using the DCNet model for abstract visual pattern understanding.  
The model implementation is adapted from the official DCNet repository:  
🔗 https://github.com/visiontao/dcnet/tree/main

### 📥 Dataset
Download the **RAVEN-10k dataset** from the following page:  
🔗 https://wellyzhang.github.io/project/raven.html#dataset  
Then click on the **Google Drive link**, and place the dataset in the appropriate directory.

### 📂 Important Files
- `generate_data.py` – Generates image folders of Raven-style matrix puzzles and runs various explanation types.
- `main.py` – Demonstrates an example explanation flow on a Raven puzzle instance.

---

Feel free to open an issue or contribute if you'd like to extend these experiments or apply alternative XAI methods.

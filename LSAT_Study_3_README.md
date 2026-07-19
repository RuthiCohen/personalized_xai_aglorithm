# Experiment 3: LSAT Reasoning with AI Assistance

## Overview

This directory contains the materials, stimuli, participant logs, demographic data, and analysis notebook for the third study. The study examined how different forms of AI assistance affected human performance on multiple-choice LSAT-style logical reasoning questions.

The implemented experiment used a **between-subjects design** with four assistance conditions. Each participant answered the same set of 10 questions in a participant-specific order and rated their confidence after each answer. Participants then completed three post-task Likert items concerning understanding, clarity, and trust.

The analysis retained 20 participants per condition, for a final analyzed sample of **80 participants**.

---

## Experimental design

### Conditions

| Group | Condition | Information displayed to the participant |
|---|---|---|
| A | Prediction only | The AI-selected answer choice, without an explanation or confidence distribution |
| B | Prediction + LLM explanation | The AI-selected answer and a short LLM-generated explanation for each answer choice |
| C | Prediction + expert explanation | The AI-selected answer and the available expert/reference explanation for each answer choice; choices without an explanation were displayed as `NO EXPLANATION` |
| D | Prediction + confidence | The AI-selected answer and a confidence percentage for each answer choice |

## AI system and question selection

### LLM identification

The internal study document identifies the model as **“Chat Gpt 5.”** The archive does not contain API code, an API model identifier, an access date, or generation settings such as temperature, top-p, maximum tokens, or seed. 

### Prompt used to generate choice-level explanations

The prompt preserved in `participant_materials/prompt.rtf` is:

> You are an expert in LSAT questions. Here is an LSAT question and four answer choices (A, B, C, D). For each answer choice, give me a short explanation (1-2 sentences) describing what it says and how it relates to the question or argument and your confidence for each choice to be the correct answer.

### Candidate question pool

`data/experiment-lsat-questiosn.json` contains 20 candidate questions with the following IDs:

```text
1, 3, 4, 5, 9, 11, 12, 15, 17, 19,
20, 21, 22, 24, 25, 26, 27, 28, 30, 36
```

The JSON stores, for each question:

- `id`: question identifier;
- `question`: passage or argument;
- `prompt`: question instruction;
- `choices`: answer choices A-D;
- `choices[*].text`: answer-choice text;
- `choices[*].llm`: LLM-generated explanation for that choice;
- `choices[*].explanation`: expert/reference explanation when available;
- `answer`: ground-truth answer;
- `llmAnswer`: LLM-selected answer;
- `jarvisAnswer1` and `jarvisAnswer2`: first and second predictions from the prior paper model;
- `jarvisConf1` and `jarvisConf2`: confidence values associated with those prior-model predictions.

### Questions used in the experiment

The implemented experiment used the following 10 questions:

| Question ID | Correct answer | Displayed AI answer | AI correct? | Top-choice confidence used by the analysis |
|---:|:---:|:---:|:---:|---:|
| 1 | D | D | Yes | 80% |
| 3 | A | A | Yes | 75% |
| 4 | D | A | No | 70% |
| 5 | A | A | Yes | 60% |
| 11 | A | A | Yes | 70% |
| 12 | D | A | No | 40% |
| 15 | C | C | Yes | 80% |
| 17 | A | C | No | 65% |
| 20 | B | B | Yes | 70% |
| 22 | D | B | No | 70% |

Thus, the displayed AI prediction was correct on **6 of the 10 experimental questions (60%)** and incorrect on four questions.
---

## Participant-facing materials

The `participant_materials/` directory contains:

- `1-info.png`: demographic-information and consent screen;
- `2-intro.png`: general LSAT task instructions;
- `3-intro.png`: AI-assistance introduction shown to participants;
- `group_a/group_a_example.png`: prediction-only example;
- `group_b/group_b_example.png`: LLM-explanation example;
- `group_c/group_c_example.png`: expert-explanation example;
- `group_d/group_d_example.png`: prediction-with-confidence example;
- `rating.png`: per-question confidence-rating screen;
- `prompt.rtf`: prompt used to request choice-level LLM explanations and confidence;
- `questionnaires/informed_consent.rtf`: informed-consent text;
- `questionnaires/questionnaire.rtf`: group-specific final questionnaire wording.

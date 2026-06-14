# Rule-Based Expert System Using Forward Chaining

## Overview

This project implements a Rule-Based Expert System in Python that uses Forward Chaining to infer conclusions from user-provided symptoms.

The system applies predefined IF-THEN rules to a knowledge base and generates conclusions through multi-step reasoning while displaying the complete inference path.

---

## Features

* Rule Engine using IF-THEN rules
* Facts Base for storing user inputs and inferred facts
* Forward Chaining inference mechanism
* Multi-step rule chaining
* Inference logging and reasoning path display
* Console-based user interaction

---

## How It Works

1. The user enters symptoms as facts.
2. The system checks all available rules.
3. Matching rules generate new facts.
4. Newly generated facts can trigger additional rules.
5. The process continues until no more conclusions can be inferred.
6. The system displays the reasoning steps and final conclusions.

---

## Example Input

fever,cough,body_pain

## Example Inference

Rule Fired: fever AND cough -> flu

Rule Fired: flu AND body_pain -> severe_flu

Rule Fired: severe_flu -> consult_doctor

## Example Conclusion

* flu
* severe_flu
* consult_doctor

---

## Concepts Used

* Expert Systems
* Knowledge Base
* Rule Base
* Facts Base
* Forward Chaining
* Explainable AI

---

## Technology Stack

* Python 3

---

## Project Structure

Rule-Based-Expert-System/

├── expert_system.py

└── README.md

---

## Author

Abhijeet Ghanwat

# 🌿 BioChem Eco - Cheminformatics Virtual Laboratory

## Developed By
**Abhay Raj**

## Aim
To develop a foundational understanding of Cheminformatics and Green/Botanical Chemistry by using computational tools to represent, visualize, and analyze chemical structures.

## Learning Objectives
Students will be able to:
- Convert molecular representations using SMILES notation.
- Visualize 2D and 3D molecular structures in an interactive Eco-Green interface.
- Calculate key molecular descriptors (MW, LogP, TPSA, HBD, HBA, rotatable bonds, etc.).
- Understand structure–property and structure–activity relationships.

## Molecule Library
100+ molecules categorized into 12 classes (Natural Products, Drugs, Amino Acids, Sugars, Vitamins, Industrial & Environmental, etc.). Add custom molecules in `molecules.py`.

## Features
- **Eco-Green Botanical Theme:** Custom modern dark green UI designed for scientific clarity.
- **2D & Interactive 3D Rendering:** Supports Ball & Stick, Space Filling, Wireframe, Stick, and Surface views.
- **PDF & CSV Export:** Download comprehensive property reports and personalized student project analyses.
- **Structure-Property Comparison:** Compare batch molecule inputs easily.
- **Interactive Assessment Quiz:** Self-evaluate cheminformatics concepts.

## Run Locally
```bash
pip install -r requirements.txt
streamlit run app.py
```

## Check Molecule Library Integrity
```bash
python test_molecules.py
```

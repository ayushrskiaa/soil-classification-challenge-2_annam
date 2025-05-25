# Soil Classification Challenge

This repository contains the template and starter code for the Soil Classification Hackathon Challenge organized by Annam.ai IIT Ropar.

## Project Structure

```
soil-classification-challenge-template/
├── LICENSE
├── README.md
└── challenge-2/
    ├── requirements.txt
    ├── data/
    │   └── download.sh
    ├── docs/
    │   └── cards/
    │       ├── architecture.png
    │       └── ml-metrics.json
    ├── notebooks/
    │   ├── inference.ipynb
    │   └── training.ipynb
    └── src/
        ├── postprocessing.py
        └── preprocessing.py
```

## Getting Started

1. **Clone the repository**
   ```sh
   git clone <repository_url>
   cd soil-classification-challenge-template/challenge-2
   ```

2. **Install dependencies**
   ```sh
   pip install -r requirements.txt
   ```

3. **Download the dataset**
   - Place your dataset in the `data/` directory or use the provided `download.sh` script if available.

4. **Training**
   - Use the notebook `notebooks/training.ipynb` to train your model.

5. **Inference**
   - Use the notebook `notebooks/inference.ipynb` to generate predictions.

## Code Overview

- `src/preprocessing.py`: Preprocessing utilities and custom dataset class.
- `src/postprocessing.py`: Post-processing utilities for model outputs.
- `notebooks/training.ipynb`: Model training workflow.
- `notebooks/inference.ipynb`: Model inference and submission generation.

## Team

- **Team Name:** KrishiSetu  
- **Members:** Dnyandeep Chute, Ayush Kumar, Suyash Mishra, Krish Kalgude, Yash Verma

## License

This project is licensed under the [MIT License](LICENSE).

---

**Deadline for Submissions:** 25th May, 2025, 11:59 PM IST

*Happy Coding and Hacking!*

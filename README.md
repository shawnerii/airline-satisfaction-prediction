# Airline Passenger Satisfaction

Machine learning assignment for exploring and predicting airline passenger satisfaction from demographic, travel, service-rating, and delay features.

The project covers the complete workflow:

- data cleaning and preprocessing;
- exploratory data analysis and feature engineering;
- supervised binary classification;
- PCA-based dimensionality reduction;
- unsupervised clustering;
- a Gradio application for interactive predictions.

## Dataset

The project uses the [Airline Passenger Satisfaction dataset](https://www.kaggle.com/datasets/teejmahal20/airline-passenger-satisfaction/data).

The original data contains 103,904 training rows and 25,976 test rows. The target column is `satisfaction`, encoded during preprocessing as:

- `1`: satisfied
- `0`: neutral or dissatisfied

The raw dataset files are `train.csv` and `test.csv`. Preprocessed features and labels are stored in the `data/` directory.

## Repository layout

```text
.
├── Preprocessing.ipynb
├── notebooks/
│   ├── 01_EDA_FeatureEngineering.ipynb
│   ├── 02_Supervised_Models.ipynb
│   └── 03_Unsupervised_Clustering.ipynb
├── data/
│   ├── train_full_features.csv
│   ├── test_full_features.csv
│   ├── train_pca_features.csv
│   └── test_pca_features.csv
├── models/                 # Trained estimators and preprocessing artifacts
├── html exports/           # Exported notebook reports
├── Figures/
├── app/app.py              # Interactive prediction interface
├── train.csv
└── test.csv
```

## Running the notebooks

Create a Python environment and install the main dependencies:

```bash
python -m venv .venv
source .venv/bin/activate
pip install numpy pandas scikit-learn scipy matplotlib seaborn joblib xgboost gradio jupyter
```

Run Jupyter from the repository root:

```bash
jupyter notebook
```

Run `Preprocessing.ipynb` first when regenerating the cleaned data and preprocessing artifacts. The analysis notebooks can then be run in numerical order.

## Running the prediction app

The app loads the saved preprocessing artifacts and models from `models/`. Start it from its own directory so the relative model path resolves correctly:

```bash
cd app
python app.py
```

Gradio will print a local URL where the Airline Satisfaction Predictor can be opened in a browser. Select a trained model, enter passenger and flight details, and submit the form to receive a satisfaction prediction.

## Reports and figures

The `html exports/` directory contains browser-readable exports of the preprocessing, exploratory analysis, supervised-model, and clustering notebooks. Supporting workflow diagrams and analysis figures are in `Figures/` and `notebooks/`.

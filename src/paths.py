"""
Definição centralizada dos caminhos de diretórios e arquivos do projeto CampainSense.

Este módulo descreve a topologia do repositório e fornece caminhos absolutos
para leitura e escrita de dados, modelos, relatórios e artefatos intermediários,
garantindo reprodutibilidade e evitando hardcodes espalhados pelos notebooks.
"""

from pathlib import Path

# Raiz do projeto
BASE_PATH = Path(__file__).resolve().parents[1]

# Pastas principais
DATA_FOLDER = BASE_PATH / "data"
RAW_FOLDER = DATA_FOLDER / "raw"
PROCESSED_FOLDER = DATA_FOLDER / "processed"

MODELS_FOLDER = BASE_PATH / "models"
REPORTS_FOLDER = BASE_PATH / "reports"

# data/raw
RAW_DATA = RAW_FOLDER / "customer_marketing_campaigns.csv"

# data/processed
PROCESSED_TRAIN = PROCESSED_FOLDER / "train.parquet"
PROCESSED_VALID = PROCESSED_FOLDER / "valid.parquet"
PROCESSED_TEST  = PROCESSED_FOLDER / "test.parquet"
PROCESSED_SPLIT_METADATA = PROCESSED_FOLDER / "split_metadata.json"

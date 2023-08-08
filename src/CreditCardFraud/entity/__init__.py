from dataclasses import dataclass
from pathlib import Path

@dataclass(frozen=True)
class DataIngestionConfig:
    root_dir:Path
    local_data_file:Path




@dataclass(frozen=True)
class DataValidationConfig:
    root_dir:Path
    STATUS_FILE:str
    ALL_REQUIRED_FILES:list




@dataclass(frozen=True)
class DataTransformationConfig:
    root_dir:Path
    data_path:Path




@dataclass(frozen=True)
class ModelTrainerConfig:
    root_dir:Path
    train_data_path:Path
    test_data_path:Path
    model_name: str
    criterion: str
    max_features: str
    n_estimators: int
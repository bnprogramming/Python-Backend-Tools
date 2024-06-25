import pandas as pd
from logger import logger


def data_normalizer(data):
    processed_data = []
    for key, value in data.items():
        row = {
            'key': 'value',
        }
        processed_data.append(row)
    return processed_data


def csv_saver(data, path):
    pre_processed_data = data_normalizer(data)
    df = pd.DataFrame(pre_processed_data)
    df.to_csv(path, index=False)
    logger.warning(f"Item's File saved to {path}")

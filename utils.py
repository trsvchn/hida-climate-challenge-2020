"""Utils.
"""
import xarray as xr
import pandas as pd


def load_forcing_as_df(file_path: str) -> pd.DataFrame:
    """Imports forcing time series as pandas df.
    """
    data = xr.open_dataset(file_path)
    df = data.to_dataframe()
    # Multiindex to single index
    df = df.reset_index(level=['lev', 'time', 'x'])
    # Ugly hack for a column of time
    df['time'] = (df['time'] // 10000).astype(int)
    return df


def load_geodata_as_df(file_path: str) -> pd.DataFrame:
    """Imports geodata as pandas df.
    """
    data = xr.open_dataset(file_path)
    df = data.to_dataframe()
    df = df.reset_index(level=['lat', 'lon', 'time'])
    df['time'] = (df['time'] // 10000).astype(int)  # Ugly hack for a column of time
    return df

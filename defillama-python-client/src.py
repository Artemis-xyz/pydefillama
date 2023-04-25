import pandas as pd


def convert_df_column_to_date(df, date_column="date", format=None, unit=None):
    if unit is not None:
        df[date_column] = pd.to_datetime(df[date_column], unit=unit)
    elif format is not None:
        df[date_column] = pd.to_datetime(df[date_column], format=format)
    else:
        df[date_column] = pd.to_datetime(df[date_column])
    df[date_column] = df[date_column].dt.date
    return df
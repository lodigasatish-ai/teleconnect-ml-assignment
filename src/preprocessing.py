import pandas as pd

def clean_data(df):

    df['TotalCharges'] = pd.to_numeric(
        df['TotalCharges'],
        errors='coerce'
    )

    df.dropna(inplace=True)

    if 'customerID' in df.columns:
        df.drop(columns=['customerID'], inplace=True)

    return df

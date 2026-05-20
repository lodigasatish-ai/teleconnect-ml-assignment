import pandas as pd

def test_no_missing_values():
    df = pd.read_csv("data/sample.csv")
    assert df.isnull().sum().sum() == 0

def test_required_columns():
    df = pd.read_csv("data/sample.csv")
    assert "tenure" in df.columns
    assert "MonthlyCharges" in df.columns

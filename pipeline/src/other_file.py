import pandas as pd

def pandas_tester(x):
    df = pd.DataFrame([x])
    df = df * 2
    return df[0].item()
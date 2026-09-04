import pandas as pd

def findHeavyAnimals(animals: pd.DataFrame) -> pd.DataFrame:
    df = animals[animals['weight']>100].sort_values(by =['weight'], ascending = False)
    return df[['name']]
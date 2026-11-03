import pandas as pd
def most_friends(request_accepted: pd.DataFrame) -> pd.DataFrame:
    
    values = pd.concat([request_accepted["requester_id"], request_accepted["accepter_id"]]).to_frame('id')

    df = values.groupby('id', as_index=False).agg(num=('id', 'count')).sort_values('num', ascending=False).head(1)

    return df
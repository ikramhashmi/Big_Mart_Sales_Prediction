import pandas as pd
from sklearn.impute import SimpleImputer
from .dataloading import dataloading
loader = dataloading()
PATH = r"artifacts\Train.csv"
df = loader.dataloader(PATH)
class datacleaning:
    def __init__(self):
        pass
    def cleaning(self,df):
        df.drop(['Item_Identifier','Outlet_Identifier'],axis=1,inplace=True)
        numerical = df.select_dtypes("number").columns.to_list()
        imputer = SimpleImputer(strategy='mean')
        df[numerical] = imputer.fit_transform(df[numerical])
        lf = []
        for i in df['Item_Fat_Content']:
            if 'LF' in i:
                lf.append('Low Fat')
            elif "reg" in i:
                lf.append('Regular')
            elif "low fat" in i:
                lf.append('Low Fat')
            else:
                lf.append(i)
        df['Item_Fat_Content'] = lf
        df.to_csv('./artifacts/clean_data.csv')
        return df, numerical
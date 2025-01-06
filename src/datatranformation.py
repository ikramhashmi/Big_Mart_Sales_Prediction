from .datacleaning import Cleaning
from sklearn.impute import SimpleImputer
from sklearn.preprocessing import StandardScaler
from sklearn.preprocessing import LabelEncoder

obj = Cleaning()
x, y = obj.clean()
class Transformation:
    def __init__(self):
        pass
    def transform(self,x=x,y=y):
        categorical = x.select_dtypes("object").columns.to_list()
        numerical = x.select_dtypes("number").columns.to_list()
        imputer = SimpleImputer(strategy='median')
        x['Item_Weight'] = imputer.fit_transform(x[['Item_Weight']])
        x['Outlet_Size'].fillna(x['Outlet_Size'].mode()[0], inplace=True)
        scaler =  StandardScaler()
        scaler.fit(x[numerical])
        x[numerical] = scaler.transform(x[numerical])
        label_encoder = LabelEncoder()
        categorical = x.select_dtypes(include=['object']).columns.to_list()
        for col in categorical:
             x[col] = label_encoder.fit_transform(x[col])

        return x,y     


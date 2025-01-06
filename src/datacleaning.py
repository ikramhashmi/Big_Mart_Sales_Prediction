from .dataloading import Loader



PATH=r"artifacts\Train.csv"
loader = Loader()
df=loader.data_loader(PATH)

class Cleaning:
    def __init__(self):
        pass
    def clean(self,df=df):
        x=df.drop("Item_Outlet_Sales",axis=1)
        y=df['Item_Outlet_Sales']

        x.drop(['Item_Identifier', 'Outlet_Identifier'], axis=1, inplace=True)

        return x,y


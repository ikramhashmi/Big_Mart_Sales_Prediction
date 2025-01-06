from  .datatranformation import Transformation
from sklearn.model_selection import train_test_split

obj = Transformation()
x,y=obj.transform()
class Datasplit:
    def __init__(self):
        pass
    def split(self,x=x,y=y):
        x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.3, random_state=42)
        return x_train, x_test, y_train, y_test

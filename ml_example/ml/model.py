import os
import sklearn 
import scipy.io as scio
import pymysql
import pandas as pd
import numpy as np
import time
from sklearn.utils import shuffle
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.externals import joblib
from PIL import Image
from pathlib import Path

def export_model(mode =None):
    # mysql 연결
    mydb = pymysql.connect(
        host = 'localhost',
        user = 'root',
        password = '0000',
        database = 'my_rest_db'
    )
    model_path = str(Path(__file__).parent.parent)
    cursor = mydb.cursor()
    sql = 'select * from svhn'
    df = pd.read_sql_query(sql,mydb)
    img_path = df['path']
    x = np.array([np.array(Image.open(name)) for name in img_path])
    y = df['label']
    h,w,c,b = x.shape
    x_train = x.reshape(h*w*c,b).T
    y_train = y.reshape(b,)
    x,y = shuffle(x_train,y_train, random_state =141)
    x_train, x_test,y_train,y_test = train_test_split(x,y,test_size=0.05,random_state= 141)
    rf = RandomForestClassifier()
    rf.fit(x_train,y_train)
    if not mode :
        joblib.dump(rf,model_path + '/model/model.pkl')
    else:
        if os.path.isfile(model_path+'/model/model.pkl'):
            os.rename(md_dir + '/model/model.pkl', md_dir + f'/model/model_{time.time()}.pkl')
        joblib.dump(rf,model_path + '/model/model.pkl')
if __name__ == '__main__':
    export_model()
            

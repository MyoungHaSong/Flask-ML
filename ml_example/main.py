import flask
import numpy as np
from sklearn.externals import joblib
from flask import Flask, request, render_template
from flask_restful import Api, Resource
from PIL import Image
from ml.model import export_model
from utils.sql import insert,search_last
from werkzeug.utils import secure_filename

app = Flask(__name__)
api = Api(app)
@app.route('/')
@app.route('/index')
def index():
    return flask.render_template('index.html')
@app.route('/predict',methods= ['POST'])
def prediction():
    if request.method =='POST':
        file = request.files['image']
        if not file : return render_template('index.html',ml_label = 'No Files')
        path = 'D:/new_com/data/svhn/img/'
        last_id,_,_ = search_last()
        img = Image.open(file)
        # 경로에 이미지 저장.
        img.save(path + str(last_id+1)+'.png')

        img = np.array(img)
        img = img[:,:,:3]
        img = img.reshape(1,-1)
        predict = model.predict(img)
        label = str(np.squeeze(predict))
        # db 저장
        insert(last_id+1,label,path +str(last_id+1) +'.png')

        if label =='10':label = '0'
        return render_template('index.html',ml_label =label)

@app.route('/retrain',methods = ['POST'])
def make_model():
    if request.method =='POST':
        export_model('R')
        return render_template('index.html',md_label = '모델 재생성 완료')

class RestML(Resource):
    def get(self):
        export_model('R')
        return {'result' : True, 'modelName':'model.pkl'}

# Rest 등록
api.add_resource(RestML, '/retrainModel')        
if __name__ =='__main__':
    model = joblib.load('./model/model.pkl')
    app.run(host='0.0.0.0',port=8000,debug = True)



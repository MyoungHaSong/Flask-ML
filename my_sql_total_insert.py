import pymysql

engine = create_engine("mysql+pymysql://root:"+"0000"+"@localhost:3306/my_rest_db?charset=utf8", encoding='utf-8')
data = scio.loadmat('./ml_example/ml/extra_32x32.mat')
img = data['X']
label = data['y']
img = img.transpose(3,0,1,2)
path = 'D:/new_com/data/svhn/img/'
img_path = []
for i in tqdm(range(len(img))):
    img_path.append(path +str(i)+'.png')
    cv2.imwrite(path+str(i)+'.png',img[i])
idx = list(range(label.shape[0]))
df = pd.DataFrame(list(zip(idx,label,img_path)),columns = ['id','label','path'])
df['label'] = df['label'].apply(lambda x : x[0])
df['id'] = df['id'].apply(lambda x : str(x))
# df.to_csv('./text.csv')
df.to_sql(name = 'svhn',con = engine,if_exists = 'append',index = False)
print('Sucess')
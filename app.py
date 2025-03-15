import pickle
from flask import Flask,request,app,jsonify,url_for,render_template
import numpy as np
import pandas as pd

# created basic flask app
app=Flask(__name__) 

# load the model
lrmodel=pickle.load(open('lrmodel.pkl','rb'))
scaler=pickle.load(open('scaling.pkl','rb'))
#
@app.route('/') #take to homepage
def home():
    return render_template('home.html')

#
@app.route('/predict_api',methods=['POST'])
def predict_api():
    data=request.json['data']
    print(data)
    # convert data into list
    # converting list to an array and reshaping it in single record
    print(np.array(list(data.values())).reshape(1,-1))
    new_data=scaler.transform(np.array(list(data.values())).reshape(1,-1))
    output=lrmodel.predict(new_data)
    print(output[0])
    return jsonify(output[0])

@app.route('/predict',methods=['POST'])
def predict():
    data=[float(x) for x in request.form.values()]
    final_input=scaler.transform(np.array(data).reshape(1,-1))
    print(final_input)
    prediction=lrmodel.predict(final_input)
    return render_template('home.html',prediction_text='Predicted House Price is {}'.format(prediction[0]))

if __name__=="__main__":
    app.run(debug=True)


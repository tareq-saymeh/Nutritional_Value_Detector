import os
from flask import Flask, render_template, request, jsonify
import pandas as pd
from ultralytics import YOLO
import requests
from werkzeug.utils import secure_filename

app = Flask(__name__)
names = ['Paneer_tikka', 'apple', 'apples', 'apricot', 'aubergine', 'avocado', 'banana', 'bean', 'beetroot', 'bread', 'burger', 'butter naan', 'buttter naan', 'cabbage', 'capsicum', 'carrot', 'cauliflower', 'chai', 'chapati', 'cheese', 'cherry', 'chili', 'chutney', 'coconut', 'corn', 'cucumber', 'cutlet', 'dal_makhani', 'dates', 'dhokla', 'egg', 'fig', 'friedchicken', 'garlic', 'geapes', 'ginger', 'grape', 'greapefurit', 'greenonions', 'greens', 'guva', 'idli', 'jalebi', 'kiwi', 'kulfi', 'ledisfingers', 'lemon', 'mango', 'masala_dosa', 'melon', 'momos', 'mushrooms', 'olive', 'onion', 'orange', 'paani_puri', 'pach', 'pakoda', 'papaya', 'pav_bhaji', 'pear', 'pineapple', 'pizza', 'pomegranate', 'potato', 'radish', 'raspberry', 'rice', 'sambhar', 'samosa', 'srawberry', 'sweet potato', 'tomato', 'tower burger', 'vegatable salad', 'waffle', 'watermelon']
api_url = 'https://api.calorieninjas.com/v1/nutrition?query='
model = YOLO("best.pt")

UPLOAD_FOLDER = 'uploads'
if not os.path.exists(UPLOAD_FOLDER):
    os.makedirs(UPLOAD_FOLDER)

@app.route('/')
def hello():
    return render_template('index.html')

@app.route('/upload', methods=['POST'])
def upload_file():
    img = request.files['image']
    if img:
        filename = secure_filename(img.filename)
        filepath = os.path.join(UPLOAD_FOLDER, filename)
        img.save(filepath)
        
        results = model(filepath)  # predict on an image
        output = ""
        for result in results:
            for box in result.boxes:
                cls = box.cls.item()
                output = names[int(cls)]
        
        query = output
        response = requests.get(api_url + query, headers={'X-Api-Key': '0ROAjPGhjVxNgTD7JwsE/A==QGUSQczTXqLoyIep'})
        
        if response.status_code == requests.codes.ok:
            data = response.json()
            return render_template('index.html', info=data['items'][0], image_url=filepath)
        else:
            return jsonify({"error": "API request failed", "status_code": response.status_code, "message": response.text})

if __name__ == '__main__':
    app.run(debug=True, use_reloader=False)

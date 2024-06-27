### project idea :
dervice to give Nutritional value {"القيمة الغذائية"} for foods from image

### data set 
https://universe.roboflow.com/nutriment-eazzk/-food-detection/dataset/1
("YOLOV8")
it contain 77 type of food 
['Paneer_tikka', 'apple', 'apples', 'apricot', 'aubergine', 'avocado', 'banana', 'bean', 'beetroot', 'bread', 'burger', 'butter naan', 'buttter naan', 'cabbage', 'capsicum', 'carrot', 'cauliflower', 'chai', 'chapati', 'cheese', 'cherry', 'chili', 'chutney', 'coconut', 'corn', 'cucumber', 'cutlet', 'dal_makhani', 'dates', 'dhokla', 'egg', 'fig', 'friedchicken', 'garlic', 'geapes', 'ginger', 'grape', 'greapefurit', 'greenonions', 'greens', 'guva', 'idli', 'jalebi', 'kiwi', 'kulfi', 'ledisfingers', 'lemon', 'mango', 'masala_dosa', 'melon', 'momos', 'mushrooms', 'olive', 'onion', 'orange', 'paani_puri', 'pach', 'pakoda', 'papaya', 'pav_bhaji', 'pear', 'pineapple', 'pizza', 'pomegranate', 'potato', 'radish', 'raspberry', 'rice', 'sambhar', 'samosa', 'srawberry', 'sweet potato', 'tomato', 'tower burger', 'vegatable salad', 'waffle', 'watermelon']


### how it work (generally)
the input should be image contain food on it
the model will give us the food name 
then well send the food name to api that give back json data contain Nutritional value about it .






### accuracy
according to model websit the acciracy = 74%
https://universe.roboflow.com/nutriment-eazzk/-food-detection/model/1
https://blog.roboflow.com/whats-new-in-yolov8/
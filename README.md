# Nutritional Value Detector

### Overview
The Nutritional Value Detector is a service designed to identify food items from images and provide their nutritional values. This project leverages a YOLOv8 model trained on a dataset containing 77 types of food. By submitting an image with food items, the model can detect and classify the food, and then retrieve the corresponding nutritional information through an external API.


### How It Works
1) Input: An image containing food items.
2) Detection: The YOLOv8 model identifies and classifies the food items in the image.
3) Translation: The classified food item names are translated using the googletrans library if necessary.
4) API Request: The translated food item names are sent to the CalorieNinjas API that returns the nutritional value in JSON format.
5) Output: The nutritional information for the identified food items is displayed.

### Food Types
The dataset used for training the model contains 77 different types of food: 
- Paneer_tikka
- Apple
- Apples
- Apricot
- Aubergine
- Avocado
- Banana
- Bean
- Beetroot
- Bread
- Burger
- Butter Naan
- Buttter Naan
- Cabbage
- Capsicum
- Carrot
- Cauliflower
- Chai
- Chapati
- Cheese
- Cherry
- Chili
- Chutney
- Coconut
- Corn
- Cucumber
- Cutlet
- Dal_makhani
-  Dates
- Dhokla
- Egg
- Fig
- Fried Chicken
- Garlic
- Grapes
- Ginger
- Grape
- Greapefurit
- Green Onions
- Greens
- Guava
- Idli
- Jalebi
- Kiwi
- Kulfi
- Ladies Fingers
- Lemon
- Mango
- Masala Dosa
- Melon
- Momos
- Mushrooms
- Olive
- Onion
- Orange
- Paani Puri
- Peach
- Pakoda
- Papaya
- Pav Bhaji
- Pear
- Pineapple
- Pizza
- Pomegranate
- Potato
- Radish
- Raspberry
- Rice
- Sambhar
- Samosa
- Strawberry
- Sweet Potato
- Tomato
- Tower Burger
- Vegetable Salad
- Waffle
- Watermelon

### Model Accuracy
The YOLOv8 model used in this project has an accuracy of 74%. More details about the model can be found on the [Roboflow model page](https://universe.roboflow.com/nutriment-eazzk/-food-detection/model/1) and in the [YOLOv8 blog post](https://blog.roboflow.com/whats-new-in-yolov8/).


### Dataset
The dataset used for training the YOLOv8 model is available at [Roboflow Food Detection Dataset](https://universe.roboflow.com/nutriment-eazzk/-food-detection/dataset/1).

### Requirements
- Python 3.x
- YOLOv8
- googletrans library for translation
- API key for CalorieNinjas

### Installation
- Clone the repository: git clone https://github.com/saifalaasabelaish/adv_ml.git

### License
This project is licensed under the MIT License. 

### Acknowledgements
[Roboflow](https://roboflow.com/) for providing the dataset and YOLOv8 model.
The developers and contributors of YOLOv8.

### Contact
For any questions or issues, please open an issue in the repository or contact the maintainer at [Saifalaa.099@gmail.com] or [s12112542@stu.najah.edu].

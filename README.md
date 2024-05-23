# PNEUMONIA DETECTION MODEL

![pneumonia](https://github.com/Story-data/Pneumonia_model/assets/103637488/5af66e2f-8974-4b42-9e55-d8804e5087ae)

HDSC Spring ’24 Premier Project By **Team StoryBoard**

Pneumonia is an inflammatory lung condition caused by infections, resulting in fluid or pus in the air sacs, with symptoms like cough, fever, and shortness of breath. It poses a high risk to infants, older adults, and those with weakened immune systems. Accurate and timely diagnosis, often through chest X-rays, is critical but can be subjective and error-prone. 

This study developed a deep learning model using the **`ResNet50V2`** architecture to analyze chest X-ray images, aiming to improve diagnostic accuracy and efficiency in detecting pneumonia, thereby reducing misdiagnosis and treatment delays.

## DATA
We utilized the Chest X-Ray Images (Pneumonia) dataset from [Kaggle](https://www.kaggle.com/datasets/paultimothymooney/chest-xray-pneumonia/code), consisting of 5,856 X-ray images (JPEG format) categorized as either “PNEUMONIA” or “NORMAL.” The dataset was organized into three folders (train, test, and val) with subfolders for each image category.

## PROJECT Implementation Flow

1. Import Important Libraries
2. Import the Dataset
3. Data Visualization
4. Data Preprocessing
   - Data labeling
   - Image resizing
   - Normalization
   - Data augmentation
5. Model Training
6. Model Evaluation
7. Model Deployment

## RESULT
The trained model achieved an `accuracy` of **0.753**, a `precision` of **0.721**, and a `recall` of **0.987** on the test set. These metrics indicate the model’s ability to accurately identify pneumonia cases while minimizing false positives and false negatives.

The link to deployed website can be found below:



 

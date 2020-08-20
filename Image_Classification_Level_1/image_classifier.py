import tensorflow as tf
import requests
import os
from time import strftime
from numpy import newaxis

from warnings import filterwarnings
filterwarnings('ignore')


class ImageObj:

    def __init__(self, url=None, file_name=None, shape=None, label=None, array=None):
        self.url = url
        self.path = file_name
        self.shape = shape
        self.label = label
        self.array = array
        self.array_224 = None

    def __str__(self):
        return "[Class : Image]\nURL:{}\nFile Path : {}\nShape : {}\nLabel : {}".format(self.url, self.path,
                                                                                        self.shape, self.label)


class ImageDownloader:

    def __init__(self):
        self.original_image_dir = os.path.join(os.curdir, 'Original_Images')
        self.image_for_model_dir = os.path.join(os.curdir, 'Images_For_Model')
        self.image = ImageObj()
        return

    def get_image(self, file_name):
        response = requests.get(self.image.url)
        self.image.path = os.path.join(self.original_image_dir, file_name)
        image_file = open(self.image.path, 'wb')
        image_file.write(response.content)

    def process_image(self):
        image_file = tf.keras.preprocessing.image.load_img(self.image.path)
        self.image.array = tf.keras.preprocessing.image.img_to_array(image_file)
        self.image.shape = self.image.array.shape
        self.image.array_224 = tf.image.resize(self.image.array, (224, 224))

    def url_to_array(self, url, file_name):
        self.image.url = url
        self.get_image(file_name)
        self.process_image()
        return self.image.array_224


class ImageClassifier:
    def __init__(self):
        self.model = tf.keras.applications.ResNet50()

    def classifier(self, url):
        ild = ImageDownloader()
        file_name = strftime('image_%Y-%m-%d_%H-%M-%S.jpg')
        img_array_224 = ild.url_to_array(url, file_name)
        img_array_224 = tf.constant(img_array_224[newaxis, :, :, :])
        predictions = self.model.predict(img_array_224)
        tpp5_labels = tf.keras.applications.resnet.decode_predictions(predictions, top=5)
        i = 1
        for tag, label, prob in tpp5_labels[0]:
            print(f' {i} | {label} | {prob} ')
            print('-'*50)
            i = i + 1


icf = ImageClassifier()
path = open('ImageFilePath.txt').read()
icf.classifier(path)

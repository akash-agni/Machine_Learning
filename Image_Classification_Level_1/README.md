<h1> Level 1 Image Classifier </h1>

I have been learning Convolutional Neural Networks, and wanted to attempt a very basic Image Classifier.
Building this helped learn how to fetch a Image from its URL, save it, preprocess it for consumption and make a prediction using existing model.
This is a very out of the box implementation to put into practise what I have learned recently.
More advanced and custom application are yet to come.
Keep an eye on the Repo!

<h2> Specifications </h2>
<ul>
  <li>Built on Python, using Tensorflow</li>
  <li>ResNet50 Model is implemented for classification tasks</li>
  <li>Trained over 1000 classes of imagenet</li>
  <li>Url link provided as Input through "ImageFilePath.txt" file</li>
  <li>Output is through formated Command Line</li>
</li>

<h2>Setup Instructions</h2>
<ol>
  <li>Clone the code into your system</li>
  <li>Open Powershell into the directory of code</li>
  <li>Create new Virtual Enviroment for Execution : python -m venv myenv</li>
  <li>Activate the Virtual Enviroment : <b>Linux</b>>>source activate myenv : <b>Windows</b>>>.\myenv\scripts\activate.bat</li>
  <li>execute the file : python image_classifier.py</li>
<ol>

Hope you enjoy playing around with this code, as much as I did writing it.

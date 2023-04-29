# MNIST API

This repository contains a Django web application that allows users to draw a digit and get a prediction from a convolutional neural network (CNN) trained on the MNIST dataset. The app is containerized with Docker for easy deployment.

## Table of Contents
- [Clonning the App](#clonning-the-app)
- [Dependencies](#dependencies)
- [Running the App with Docker](#running-the-app-with-docker)
- [Alternative: Running the App without Docker](#alternative-running-the-app-without-docker)
- [Model Architecture](#model-architecture)
- [API](#api)
- [Running Unit Tests](#running-unit-tests)
- [Acknowledgments](#acknowledgments)

## Clonning the App
1. Clone the repository to your local machine:
```bash
git clone https://github.com/your-username/django-mnist.git
```
2. Change into the project directory
```bash
cd django-mnist
```

## Dependencies

This app requires the following Python libraries:
- Django
- TensorFlow
- Keras
- NumPy
- Pillow

These dependencies are installed automatically when you build the Docker image or when you run
```bash
pip install -r requirements.txt.
```
## Running the App with Docker
To get started, you will need to have Docker installed on your machine. You can build and run the Docker container by running the following commands in your terminal:

```bash
# Build the Docker image
docker build -t django-mnist .

# Run the Docker container
docker run -p 8000:8000 django-mnist
```

Once the container is running, you can access the web app by opening your web browser and navigating to [http://localhost:8000](http://localhost:8000).

##Alternative: Running the App without Docker
If you prefer to run the app without Docker, you can follow these steps:

1. Create a virtual environment and activate it:
```bash
python -m venv venv
source venv/bin/activate
```
2. Install the Python dependencies:
```bash
pip install -r requirements.txt
```
3. Download the trained MNIST model from https://github.com/MichelWakim/mnist-model and place the mnist_model.h5 file in the app directory.

3. Run the Django development server:
```bash
python manage.py runserver
```
Access the web app by opening your web browser and navigating to http://localhost:8000.

##Model Architecture

The model used in this app is a simple CNN that consists of two convolutional layers, two max pooling layers, and two fully connected layers. The model achieves an accuracy of over 99% on the test set after training for 10 epochs.

## API

The app provides a RESTful API that allows you to make predictions using JSON data. The API is accessible through the /api/predict endpoint.

#### Using CURL

To make a prediction using the API with CURL, you can use the following command:

```bash
curl -X POST -H "Content-Type: application/json" \
     -d '{"image": "<base64-encoded-image>"}' \
     http://localhost:8000/api/predict/
```

Replace <base64-encoded-image> with the actual base64-encoded image of the digit you want to predict. The API will return a JSON response with the predicted digit:
```json
{
    "prediction": 5
}
```
#### Using Postman

To use the API with Postman, you can follow these steps:
1.  Open Postman and create a new POST request.
2. Set the request URL to http://localhost:8000/api/predict/.
3. Set the request header Content-Type to application/json.
4. Set the request body to JSON and provide the base64-encoded image of the digit you want to predict.
```json
{
    "image": "<base64-encoded-image>"
}
```
5. Click on the "Send" button to make the request.
6. The API will return a JSON response with the predicted digit.

Here's a GIF that shows how to make a POST request to the /api/predict endpoint using Postman:

To get the base64-encoded image of a digit, you can use the JavaScript code provided in the web app's index.html file. Simply open the file in a web browser, draw a digit, and click on the "Get Base64 Image" button. The console will log the base64-encoded image, which you can then copy and use for the API request.

## Running Unit Tests

To run the unit tests for this app, you can use the following command:
```bash
python manage.py test
```
This will run all of the unit tests in the tests directory and display the results in your terminal.

##Acknowledgments

This app is based on the TensorFlow Tutorials and the Django Documentation.

The trained MNIST model used in this app can be found in the mnist-model repository.
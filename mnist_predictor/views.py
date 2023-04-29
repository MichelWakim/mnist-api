import numpy as np
from PIL import Image, UnidentifiedImageError
from django.http import JsonResponse, HttpResponseBadRequest, HttpResponseNotAllowed
from django.views.decorators.csrf import csrf_exempt
from tensorflow.keras.models import load_model

model = load_model('mnist_predictor/model.h5')

def preprocess_image(image):
    # Convert the image to grayscale
    image = image.convert('L')
    # Resize the image to 28x28 pixels
    image = image.resize((28, 28))
    # Convert the image to a numpy array
    image = np.array(image)
    # Normalize the pixel values to be between 0 and 1
    image = image / 255.0
    # Reshape the numpy array to be a 4D tensor with shape (1, 28, 28, 1)
    image = np.reshape(image, (1, 28, 28, 1))
    return image

def make_prediction(image):
    # Use the loaded model to make a prediction for the preprocessed image
    prediction = model.predict(image)
    # Extract the index of the class with the highest probability
    predicted_class = np.argmax(prediction)
    # Convert the predicted class to an integer
    predicted_class = int(predicted_class)
    return predicted_class

@csrf_exempt
def predict(request):
    if request.method == 'POST':
        image_data = request.FILES.get('image')
        if image_data is None:
            return HttpResponseBadRequest('No image provided.')
        try:
            image = Image.open(image_data)
        except (IOError, UnidentifiedImageError):
            return HttpResponseBadRequest('Invalid image file.')
        processed_image = preprocess_image(image)
        prediction = make_prediction(processed_image)
        return JsonResponse({'prediction': prediction})
    else:
        return HttpResponseNotAllowed(['POST'])
import io
from PIL import Image
from django.test import TestCase, Client
from django.urls import reverse
import numpy as np
from unittest.mock import patch
from mnist_predictor.views import make_prediction

class PredictViewTestCase(TestCase):
    def setUp(self):
        self.client = Client()
        # Create a test image for the POST requests
        self.image = Image.new('L', (28, 28), color=255)
        self.image_bytes = io.BytesIO()
        self.image.save(self.image_bytes, format='PNG')
        self.image_bytes.seek(0)

    def test_predict_view_with_valid_data(self):
        with patch('mnist_predictor.views.make_prediction', return_value=3) as mock_make_prediction:
            response = self.client.post(reverse('predict'), {'image': self.image_bytes}, format='multipart')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json(), {'prediction': 3})

    def test_predict_view_with_invalid_data(self):
        response = self.client.post(reverse('predict'))
        self.assertEqual(response.status_code, 400)

    def test_make_prediction_function(self):
        # Create a test image to use as input
        image = np.ones((1, 28, 28, 1))
        # Make a prediction using the make_prediction function
        prediction = make_prediction(image)
        # Assert that the prediction is of the expected type and value
        self.assertIsInstance(prediction, int)
        self.assertGreaterEqual(prediction, 0)
        self.assertLessEqual(prediction, 9)
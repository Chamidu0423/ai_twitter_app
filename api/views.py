from rest_framework.decorators import api_view
from rest_framework.response import Response
from tensorflow.keras.models import load_model
import tensorflow as tf
import os
from django.conf import settings
import numpy as np

print("Loading AI Model...")

model_path = os.path.join(settings.BASE_DIR, 'toxicity_model.keras')

try:
    model = load_model(model_path)
    print("AI Model Loaded Successfully!")
except Exception as e:
    print(f"Error loading AI Model: {e}")
    model = None

@api_view(['POST'])
def create_post(request):
    data = request.data 
    tweet_text = data.get('text', '')

    if not tweet_text:
        return Response({'error': 'Please enter some text'}, status=400)
    
    if model is None:
        return Response({'error': 'AI model is not loaded'}, status=500)

    prediction = model.predict(tf.constant([tweet_text])) 

    print(f"DEBUG: TEXT = '{tweet_text}' | Score = {prediction[0][0]}")

    is_toxic = prediction[0][0] > 0.75

    if is_toxic:
        return Response({
            'is_toxic': True,
            'message': 'Warning! Your post contains offensive language! '
        })
    else:
        return Response({
            'is_toxic': False,
            'message': 'Post created successfully!'
        }) 
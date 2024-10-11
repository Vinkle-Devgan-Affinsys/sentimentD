# from django.http import JsonResponse
# from django.views.decorators.csrf import csrf_exempt
# import json
# from .sentimentmodel import load_model

# # Load the sentiment analysis model
# model = load_model()

# @csrf_exempt
# def analyze_sentiment(request):
#     if request.method == 'POST':
#         try:
#             data = json.loads(request.body)
#             text = data['text']

#             # Predict sentiment (1: Positive, 0: Negative)
#             prediction = model.predict([text])[0]

#             # Map prediction to sentiment
#             sentiment = 'Positive' if prediction == 0 else 'Negative'

#             return JsonResponse({'sentiment': sentiment}, status=200)

#         except Exception as e:
#             return JsonResponse({'error': str(e)}, status=400)

#     return JsonResponse({'message': 'Send a POST request with text data.'}, status=200)

# from django.shortcuts import render
# from django.http import JsonResponse
# import pickle

# # View for the home page
# def home(request):
#     return render(request, 'index.html')

# def analyze_sentiment(request):
#     # Load the trained sentiment analysis model
#     with open('sentiment_model.pkl', 'rb') as model_file:
#         model = pickle.load(model_file)

#     if request.method == 'POST':
#         message = request.POST.get('message')
#         data = [message]
#         prediction = model.predict(data)[0]

#         sentiment = 'Neutral'
#         if prediction == 0:
#             sentiment = 'Negative'
#         elif prediction == 1:
#             sentiment = 'Positive'

#         # Return the result back to the HTML page
#         return render(request, 'index.html', {'prediction_text': f'Sentiment: {sentiment}', 'message': message})
#     return render(request, 'index.html')


# from django.shortcuts import render
# from django.http import JsonResponse
# import pickle
# import json

# # Load the trained sentiment analysis model
# with open('sentiment_model.pkl', 'rb') as model_file:
#     model = pickle.load(model_file)

# # Function to handle both form and API-based predictions
# def analyze_sentiment(request):
#     # Handle form submission (from HTML)
#     if request.method == 'POST' and request.content_type == 'application/x-www-form-urlencoded':
#         message = request.POST.get('message')
#         data = [message]
#         prediction = model.predict(data)[0]

#         sentiment = 'Neutral'
#         if prediction == 0:
#             sentiment = 'Negative'
#         elif prediction == 1:
#             sentiment = 'Positive'

#         # Return the result back to the HTML page
#         return render(request, 'index.html', {'prediction_text': f'Sentiment: {sentiment}', 'message': message})
    
#     # Handle API submission (JSON)
#     elif request.method == 'POST' and request.content_type == 'application/json':
#         try:
#             data = json.loads(request.body)
#             message = data.get('message')
#             prediction = model.predict([message])[0]

#             sentiment = 'Neutral'
#             if prediction == 0:
#                 sentiment = 'Negative'
#             elif prediction == 1:
#                 sentiment = 'Positive'

#             # Return the prediction as a JSON response
#             return JsonResponse({'sentiment': sentiment})

#         except Exception as e:
#             return JsonResponse({'error': str(e)}, status=400)

#     # Default to returning the home page if the request method isn't POST
#     return render(request, 'index.html', {'error': 'Please submit a POST request.'})


from django.shortcuts import render
from .sentimentmodel import model_making

# View to handle form submission and return prediction on the same page
def analyze_sentiment(request):

    model = model_making()

    sentiment = '_'
    message = '_'
    prediction = 1

    if request.method == 'POST':
        # Get the message from the form
        message = request.POST.get('message')
        data = [message]
        
        # Predict sentiment
        prediction = model.predict(data)

        # Determine the sentiment label based on the prediction
        if prediction == 0:
            sentiment = 'Negative'
        elif prediction == 1:
            sentiment = 'Positive'
        else:
            sentiment = 'Neutral'

    # Render the page with the prediction result
    return render(request, 'index.html', {'sentiment': sentiment, 'message': message})

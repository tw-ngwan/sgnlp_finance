from django.shortcuts import render
from django.http import JsonResponse, HttpResponse
import json 
from .models import Book
from .model.evaluate import Evaluator
import csv 


# Evaluates the results from the model 
def handle_model_results(request):
    if request.method == 'POST':
        # Get the sentence and words from the request body
        print(request)
        body_unicode = request.body.decode('utf-8')
        body = json.loads(body_unicode)
        sentence = body['sentence']
        words = body['words']

        # Perform the calculation using the model
        evaluator = Evaluator()
        try:
            result = evaluator.gather_results(sentence, words)
            print("Get result successful", result)
            print(result)
        except Exception as e: 
            return JsonResponse({'error': f"Invalid data received: {e}"}, status=400)

        # Return the result as a JSON response
        return JsonResponse({'result': result}, status=200)
    return JsonResponse({'error': 'Invalid request method'}, status=400)


# Downloads a CSV file 
def download_csv(request):
    if request.method == 'POST':
        # Create the HttpResponse object with the CSV header
        response = HttpResponse(content_type='text/csv')
        response['Content-Disposition'] = 'attachment; filename="example.csv"'  # To be verified 

        # Write the contents of the CSV file
        # To be added

        return response


        
# Index request html 
def index(request):
    books = Book.objects.all()
    return render(request, 'sgnlp_finance_app/index.html')

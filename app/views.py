from django.shortcuts import render, HttpResponse
from rest_framework.views import APIView
from django.http import JsonResponse

from dotenv import load_dotenv
import os
import google.generativeai as genai
import re

# Create your views here.
def home(REQUEST):
    return HttpResponse('SOHAM')


class askbot(APIView):
    def post(self,request):
        user_input = request.data['question']

        response = get_carpooling_response(user_input)
        if response:
            print("\nResponse from Carpooling Assistance Bot:")
            print(response)
            return JsonResponse({'response': response})
        else:
            print("\nI'm sorry, I couldn't find relevant information about carpooling.")
            return JsonResponse({'response': "I'm sorry, I couldn't find relevant information about carpooling"})
            
        
    



load_dotenv()
genai.configure(api_key="AIzaSyAje4c-yOKwI8GcBgO0EdrnCx-uum0hW20")

def get_carpooling_response(input_text):
    model = genai.GenerativeModel('gemini-pro')
    response = model.generate_content([input_text])

    # Filter response to focus strictly on carpooling-related content
    carpooling_related_response = ""
    for paragraph in response.text.split("\n\n"):
        if "carpooling" in paragraph.lower() or "ride-sharing" in paragraph.lower():
            carpooling_related_response += paragraph + " "

    # Remove asterisks from the filtered response
    formatted_response = re.sub(r'\*', '', carpooling_related_response)
        
    return formatted_response


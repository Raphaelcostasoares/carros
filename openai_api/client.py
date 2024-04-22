import os
import google.generativeai as genai

#Caso o usuário não preencha a Bio ao cadastrar novo carro, a bio é preenchida automaticamente atraves da IA

#A chave API fica na variável de ambiente chamada.

API_KEY = os.environ.get('API_KEY') 

genai.configure(api_key=API_KEY)
model = genai.GenerativeModel('gemini-pro')

def get_car_ai_bio(model_name, brand, year):
    prompt = f'Faca uma descricao de venda para o carro {brand} {model_name} {year} em apenas 200 caracteres'
    
    response = model.generate_content(prompt)

    return response.text

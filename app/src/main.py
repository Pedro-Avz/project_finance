import os
import schedule
import time
from dotenv import load_dotenv
from data_collection import coletar_dados
from visualization import gerar_graficos
from sendler_email.send_email import enviar_email

load_dotenv()

def job():
        
    # coletar dados do mercado
    tickers = ['AAPL', 'BRL=X']
    dados_mercado = coletar_dados(tickers=tickers, periodo='5d')  

    # gerar os gráficos

    #preço de ações de grander empresas
    # gerar_graficos(dados_mercado['AAPL'], 'Apple - Última semana', 'apple.png')
    # gerar_graficos(dados_mercado['TSLA'], 'Tesla - Última semana', 'tesla.png')
    # gerar_graficos(dados_mercado['AMZN'], 'Amazon - Última semana', 'amazon.png')
    # gerar_graficos(dados_mercado['MGLU3.SA'], 'Magazine Luiza - Última semana', 'magalu.png')


    #dolar em relacao ao real 
    gerar_graficos(dados_mercado['BRL=X'], 'Dólar - Última semana', 'dolar.png')  


    # acessar as variáveis da minha .env
    email_usuario = os.getenv('EMAIL')
    email_senha = os.getenv('SENHA')

    email_destinatario = os.getenv('EMAIL')

    exec = enviar_email(email_usuario, email_senha, email_destinatario, 'Relatório de Mercado - Última semana', ['dolar.png'])

    # se enviar com sucesso exclui as imagens
    if exec == "email enviado com sucesso!":
        print("email enviado com sucesso!")
        try:
            os.remove('dolar.png')
            print("arquivos excluídos")
        except Exception as e:
            print(f"Erro ao tentar excluir os arquivos: {str(e)}")
    else:
        print(exec)

schedule.every(24).hours.do(job)
job()
while True:
    schedule.run_pending()
    time.sleep(60) 
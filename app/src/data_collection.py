import yfinance as yf

def coletar_dados(tickers, periodo):
    """
    Coleta dados financeiros de uma lista de ativos para o período especificado.
    
    :params tickers: Lista de ativos para coleta de dados.
    :params periodo: Período para coleta de dados (ex: '6mo', '1y').
    :return: DataFrame com dados ajustados de fechamento.
    """
    dados_mercado = yf.download(tickers, period=periodo)['Adj Close']
    return dados_mercado.dropna()

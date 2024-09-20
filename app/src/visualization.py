import matplotlib.pyplot as plt
import mplcyberpunk

def gerar_graficos(dados_mercado, titulo, nome_arquivo):
    """
    Gera gráficos com estilo cyberpunk e salva o resultado como imagem.
    
    :params dados_mercado: DataFrame com os dados financeiros.
    :params titulo: Título do gráfico.
    :params nome_arquivo: Nome do arquivo para salvar o gráfico.
    """
    plt.style.use("cyberpunk")
    
    # Plotar os dados
    dados_mercado.plot(figsize=(10, 6))
    plt.title(titulo)
    plt.savefig(nome_arquivo)
    
    # Adicionar efeitos cyberpunk
    mplcyberpunk.add_glow_effects()
    plt.close()

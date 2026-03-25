#Versão Final da atividade da etec
# Dicionário contendo as informações e descrições dos destinos
destinos_info = {
    "lua": "Nosso satélite natural. Um pequeno passo para o homem...",
    "mercurio": "O planeta mais rápido! Calor extremo e muitas crateras.",
    "venus": "O planeta irmão da Terra, mas com uma atmosfera tóxica e escaldante.",
    "marte": "O planeta vermelho. Próxima parada da humanidade?",
    "jupiter": "O gigante gasoso, lar da Grande Mancha Vermelha.",
    "saturno": "O senhor dos anéis. Uma joia gelada no sistema solar.",
    "urano": "O gigante de gelo que gira de lado.",
    "netuno": "O planeta mais distante, com ventos supersônicos."
}

def sistema_navegacao():
    print("🚀 🚀 SISTEMA DE NAVEGAÇÃO GALÁCTICA 🚀 🚀")
    print("-" * 50)
    
    astronauta = input("Identifique-se, Astronauta: ")
    print("\n--- DESTINOS DISPONÍVEIS ---")
    print("🌕 LUA      🪐 MERCURIO  🌟 VENUS   🔴 MARTE")
    print("🔵 JUPITER  🪐 SATURNO   💎 URANO   🌊 NETUNO")
    print("-" * 50)

    # Loop de validação do destino
    while True:
        destino_input = input("Para onde deseja viajar? ").strip().lower()

        if destino_input == "terra":
            print("🌎 Você já está na Terra! Escolha um destino espacial.")
        elif destino_input == "sol":
            print("☀️ MISSÃO IMPOSSÍVEL: O Sol destruiria a nave! Escolha um destino mais frio.")
        elif destino_input in destinos_info:
            destino = destino_input
            break # Destino válido, sai do loop
        else:
            print("🪐 Destino não encontrado. Escolha um planeta válido do Sistema Solar.")

    print(f"\nConfigurando rota para {destino.capitalize()}...")
    
    # Coletando dados numéricos
    try:
        distancia = float(input("Distância até o destino (km): "))
        velocidade = float(input("Velocidade média da nave (km/h): "))
    except ValueError:
        print("Erro: Por favor, insira apenas números válidos para distância e velocidade.")
        return

    # Cálculos
    tempo_horas = distancia / velocidade
    tempo_dias = tempo_horas / 24

    # Lógica do Status da viagem (baseado no tempo em dias)
    # Configurei para mais de 365 dias ativar a hibernação
    if tempo_dias > 365:
        status_msg = "⚠️ STATUS: Missão de longa duração! Hibernação ativada."
    else:
        status_msg = "✅ STATUS: Suprimentos OK para a duração da viagem."

    # Exibição do Relatório
    print("\n" + "="*50)
    print(f"🚀 RELATÓRIO DE MISSÃO: {destino.upper()} 🚀")
    print("="*50)
    print(f"ASTRONAUTA : {astronauta}")
    print(f"DESTINO    : {destino.capitalize()}")
    print(f"DESCRIÇÃO  : {destinos_info[destino]}")
    # Formatação com vírgula para milhares e 2 casas decimais
    print(f"DISTÂNCIA  : {distancia:,.2f} km\n") 
    
    print(f"TEMPO ESTIMADO EM HORAS : {tempo_horas:,.2f} h")
    print(f"TEMPO ESTIMADO EM DIAS  : {tempo_dias:,.2f} dias terrestres\n")
    
    print(status_msg)
    print("="*50)
    print(f"Boa sorte, {astronauta}! Que a ciência guie seu caminho. 🚀")

# Executa o programa
if __name__ == "__main__":
    sistema_navegacao()
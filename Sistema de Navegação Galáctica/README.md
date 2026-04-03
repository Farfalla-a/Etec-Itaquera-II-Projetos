# 🚀 Sistema de Navegação Galáctica

Este é um projeto desenvolvido em Python para simular um sistema de bordo de uma nave espacial. O programa permite que o usuário (astronauta) escolha um destino no sistema solar, insira dados de viagem (distância e velocidade) e receba um relatório completo da missão, incluindo tempo estimado e status de suprimentos.

> **Nota:** Projeto desenvolvido como versão final de uma atividade da Etec.

## 📋 Funcionalidades

- **Identificação do Astronauta:** O sistema saúda o usuário pelo nome.
- **Validação Inteligente de Destinos:** - Possui um catálogo de destinos válidos (Lua, planetas do sistema solar).
  - Impede que o usuário viaje para a Terra (pois já estamos nela).
  - Bloqueia viagens para o Sol (para evitar a destruição da nave).
  - Garante que o usuário digite um destino válido antes de prosseguir.
- **Tratamento de Erros:** Utiliza `try-except` para garantir que o usuário digite apenas números válidos para distância e velocidade, evitando que o programa quebre.
- **Cálculo de Tempo de Viagem:** Calcula automaticamente o tempo da viagem em horas e converte para dias terrestres.
- **Sistema de Hibernação:** Se a viagem demorar mais de 365 dias, o sistema emite um alerta de que a hibernação da tripulação foi ativada.
- **Relatório Formatado:** Exibe um relatório final de fácil leitura, com os valores numéricos formatados adequadamente (separador de milhares e duas casas decimais).

## 🛠️ Tecnologias e Conceitos Utilizados

- **Linguagem:** Python 3.x
- **Conceitos aplicados:**
  - Dicionários (`dict`)
  - Estruturas de repetição (`while True`)
  - Estruturas condicionais (`if/elif/else`)
  - Tratamento de exceções (`try/except`)
  - Formatação de strings (F-strings)

## 💻 Como executar o projeto

1. Certifique-se de ter o [Python](https://www.python.org/downloads/) instalado na sua máquina.
2. Salve o código em um arquivo com a extensão `.py` (por exemplo, `navegacao.py`).
3. Abra o terminal (ou prompt de comando) e navegue até a pasta onde o arquivo foi salvo.
4. Execute o comando:

   ```bash
   python navegacao.py

   🚀 🚀 SISTEMA DE NAVEGAÇÃO GALÁCTICA 🚀 🚀
--------------------------------------------------
Identifique-se, Astronauta: Buzz Lightyear

--- DESTINOS DISPONÍVEIS ---
🌕 LUA      🪐 MERCURIO  🌟 VENUS   🔴 MARTE
🔵 JUPITER  🪐 SATURNO   💎 URANO   🌊 NETUNO
--------------------------------------------------
Para onde deseja viajar? Marte

Configurando rota para Marte...
Distância até o destino (km): 225000000
Velocidade média da nave (km/h): 28000

==================================================
🚀 RELATÓRIO DE MISSÃO: MARTE 🚀
==================================================
ASTRONAUTA : Buzz Lightyear
DESTINO    : Marte
DESCRIÇÃO  : O planeta vermelho. Próxima parada da humanidade?
DISTÂNCIA  : 225,000,000.00 km

TEMPO ESTIMADO EM HORAS : 8,035.71 h
TEMPO ESTIMADO EM DIAS  : 334.82 dias terrestres

✅ STATUS: Suprimentos OK para a duração da viagem.
==================================================
Boa sorte, Buzz Lightyear! Que a ciência guie seu caminho. 🚀

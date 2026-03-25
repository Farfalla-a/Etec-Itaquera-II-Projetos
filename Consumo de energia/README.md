# ⚡ Calculadora de Consumo Elétrico Inteligente

## 💻Sobre o Projeto

O Sistema de Cálculo de Consumo Elétrico é uma ferramenta interativa desenvolvida em Python para ajudar usuários a monitorar o gasto de energia de seus eletrodomésticos. O programa recebe a potência do aparelho e o tempo de uso, devolvendo o consumo mensal em kWh e o valor estimado em Reais, alertando sobre o nível de consumo com sinais coloridos (🔴, 🟡, 🟢).





## 🧐Fórmula Utilizada

Para chegar ao resultado, o sistema utiliza o seguinte cálculo matemático:

Consumo Mensal (kWh):
    
    Consumo=1000Potência(W)×Horas(h)×30dias​
Custo Mensal (R$):
    
    Custo=Consumo(kWh)×0.68(Tarifa)


## ▶️ Como Executar o Programa

   Pré-requisitos: Certifique-se de ter o Python instalado em sua máquina.

  Copie o código: Salve o código em um arquivo chamado calculadora_energia.py.
    Abra o terminal: Navegue até a pasta onde o arquivo foi salvo.
    Execute o comando:

    Bash

    python calculadora_energia.py



## 🛠️ Tecnologias e indicadores

Linguagem: Python  <img align="center" alt="Laura-Python" title= "Python" height="30" width="40" src="https://raw.githubusercontent.com/devicons/devicon/master/icons/python/python-original.svg">
</div>

Interface: CLI (Linha de Comando) 💻

Alertas de Potência:

 🟢 Baixo Consumo: < 1000W

 🟡 Consumo Médio: 1000W a 2999W

 🔴 Alto Consumo: ≥ 3000W


## 📝 Exemplo de Interface

  💠 BEM-VINDO À CALCULADORA DE CONSUMO ELÉTRICO INTELIGENTE 💠

  💡 Informe o aparelho utilizado: Ar Condicionado

   ⚡ Informe a potência: 1500

   ⏳ Informe o tempo médio de uso: 8

  ...

   🟡 Esse aparelho consome uma quantia considerável de energia. ⚠️

  💵 R$ 244.80 serão gastos por mês.



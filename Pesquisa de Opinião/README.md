# 📊 Pesquisa de Satisfação - TudoWeb

Este é um script em Python desenvolvido para automatizar a coleta de avaliações de atendimento dos clientes da "TudoWeb". O sistema entrevista um número predefinido de pessoas, coleta seus dados básicos e calcula o resultado da pesquisa ao final da execução.

## 📋 Funcionalidades

- **Coleta de Dados Pessoais:** Solicita o nome e a idade de cada entrevistado.
- **Sistema de Avaliação:** Permite que o usuário classifique o atendimento em três categorias:
  - `1` - EXCELENTE
  - `2` - BOM
  - `3` - RUIM
- **Validação de Entrada:** Verifica se o usuário inseriu uma opção válida (entre 1 e 3) e dá uma segunda chance de resposta caso ele digite um número fora desse padrão.
- **Geração de Relatório Final:** Ao concluir todas as entrevistas, o programa exibe um balanço mostrando a quantidade total de avaliações "Excelente" e "Ruim".

## 🛠️ Tecnologias e Conceitos Utilizados

- **Linguagem:** Python 3.x
- **Conceitos aplicados:**
  - Laços de repetição (`for range`)
  - Estruturas condicionais (`if/elif`)
  - Operadores lógicos e relacionais (`>` e `<`)
  - Variáveis contadoras (`+= 1`)

## 💻 Como executar o projeto

1. Certifique-se de ter o [Python](https://www.python.org/downloads/) instalado no seu computador.
2. Salve o código fornecido em um arquivo com a extensão `.py` (por exemplo, `pesquisa.py`).
3. **Dica para testes:** Como o código está configurado para 50 pessoas (`total_entrevistados = 50`), você pode alterar esse número para algo menor (como `3` ou `5`) para testar o sistema mais rapidamente.
4. Abra o terminal (ou prompt de comando) e navegue até a pasta onde o arquivo foi salvo.
5. Execute o comando:

   ```bash
   python pesquisa.py

#contador
quantidade_excelente = 0
quantidade_ruim = 0

#Numero de intrevistados
total_entrevistados = 5

#fOR QUESTIONARIO
for i in range ( total_entrevistados):

 print("\n" +"="*60)
 print("--- BEM-VINDO(A) A PESQUISA DE SATISFAÇÃO DA TUDOWEB ---")
 print("="*60)

 nome = input ("Digite seu nome:")
 idade = int(input("Digite sua idade:"))

 print("="*60)
 print("DIGITE O N° DA NOTA DO SEU ATENDIMENTO:")
 print("1: EXCELENTE | 2: BOM | 3: RUIM")
 print("="*60)
 opiniao = int(input("Sua resposta: "))
 if opiniao >3 or opiniao <1:
   print("="*60)
   print("POR FAVOR, DIGITAR UMA OPÇÃO VÁLIDA (1,2 ou 3")
   print("="*60)
   print("DIGITE O N° DA NOTA DO SEU ATENDIMENTO:")
   print("1: EXCELENTE | 2: BOM | 3: RUIM")
   print("="*60)
   opiniao = int(input("Sua resposta: "))
 print("="*60)
 print("AGRADECEMOS SUA COLABORAÇÃO.")

#RESULTADO DA PESQUISA
 if opiniao == 1:
    quantidade_excelente += 1
 elif opiniao == 3:
    quantidade_ruim += 1

print("\n" +"="*60)
print(" RESULTADO DA PESQUISA")
print(f"Quanridade de respostas EXCELENTE: {quantidade_excelente}")
print(f"Quanridade de respostas RUIM: {quantidade_ruim}")
print("\n" +"="*60)
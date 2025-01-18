''' Module for calculating the results of Ruffier tests.
 
The sum of the three tries at pulse readings (before strain, right after strain, and after a short break)
ideally, there should be no more than 200 beats per minute.
We propose that the children measure their pulse for 15 seconds,
and find the result of beats per minute by multiplying by 4:
   S = 4 * (P1 + P2 + P3)
The further the result is from the ideal 200 beats, the worse it is.
Traditionally, tables are given by values divided by 10.
 
Ruffier index  
   IR = (S - 200) / 10
is evaluated corresponding to age according to the table:
        7-8             9-10                11-12               13-14               15+ (only for adolescents!)

perfect     < 6.5           < 5                 < 3.5               < 2                 < 0.5  
good    >= 6.5 и < 12   >= 5 и < 10.5       >= 3.5 и < 9        >= 2 и < 7.5        >= 0.5 и < 6
satisfactory  >= 12 и < 17    >= 10.5 и < 15.5    >= 9 и < 14         >= 7.5 и < 12.5     >= 6 и < 11
weak  >= 17 и < 21    >= 15.5 и < 19.5    >= 14 и < 18        >= 12.5 и < 16.5    >= 11 и < 15
unsatisfactory   >= 21           >= 19.5             >= 18               >= 16.5             >= 15

the result “unsatisfactory” is 4 from the result “weak” for all ages,
“weak” is separated from “satisfactory” by 5, and “good” from “satisfactory” by 5.5
 
so we will write a function ruffier_result(r_index, level) which will produce
the calculated Ruffier index and level “unsatisfactory” for the tested age, and produce a result
 
'''
# here the lines which produce the result are given
txt_index = "Your Ruffier index: "
txt_workheart = "Heart efficiency: "
txt_nodata = '''
there is no data for that age'''
txt_res = []
txt_res.append('''low.
Go see your doctor ASAP!''')
txt_res.append('''satisfactory.
Go see your doctor!''')
txt_res.append('''average.
It might be worth additional tests at the doctor.''')
txt_res.append('''
higher than average''')
txt_res.append('''
high''')

def ruffier_index(P1, P2, P3): # retorna o valor do indice de acordo com a pulsaçao para a comparacao com as informações de tabela.
    return (4 * (P1 + P2 + P3) - 200) / 10

def level(age): #level calcula os valores standard da tabela de acordo com a atividade
   '''As opcoes para idades menores que 7 e adultos devem ser processadas separadamente.
   Aqui selecionamos o nivel ''low'' apenas dentro da tabela:
   Para a idade 7, 'low' é um índice de 21. A cada 2 anos, diminui 1.5 até o nivel de 15 aos 16 anos.'''

   norm_age = (min(age,15)-7) // 2 # a cada 2 anos, a partir dos 7 anos, tranforma-se em uma unidade
   result = 21 - norm_age * 1.5
   return result

def ruffier_result(r_index, level):
   '''A função obtem um índice de Ruffier e o interpreta.
      Retornamos o nível de prontidão e o número de 0 a 4
      (Quanto maior o nível de prontidão melhor é o resulatdo)
   '''
   if r_index >= level:
      return 0 #low

      level -= 4 #decrementa 4 de level, passando de low para satisfactory, isso não será executado se já tivermos resultado
      if r_index >= level:
         return 1 #satisfactory

      level -= 5 #transição de satisfactory para average
      if r_index >= level:
         return 2 #average

      level -= 5.5 #transição de average para high
      if r_index >= level:
         return 3 #high
      
      return 4 #higher than average

def test(P1, P2, P3, age):
   '''Esta função pode ser usada fora do módulo para calcular o índice de Ruffier.
      Retornamos os textos prontos que só precisam ser escritos no lugar necessário (Ecrã
      Result).
      Utilizamos as constantes definidas no ínicio deste módulo para estruturar os textos.
   '''
   if age < 7:
      return(txt_index + "0", txt_nodata)
   else:
      ruff_index = ruffier_index(P1, P2, P3) #cálculo
      result = txt_res[ruffier_result(ruff_index,level(age))] #interpretação e conversão para texto
      res = txt_index + str(ruff_index) + '\n' + txt_workheart + result
      return res
   

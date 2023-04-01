'''
Uma pessoa do seu time de desenvolvimento está escrevendo 
várias funções que calculam diferentes formas de gerar juros. 
Veja abaixo o exemplo de uma das funções:

def juros_simples(capital, taxa, tempo):
    return capital * (taxa/100) * tempo

Ela pediu para você escrever um decorator chamado decorator_imprimir, 
que será usado para a função chamada imprima os parâmetros: capital, taxa e tempo,
 além do resultado da função.

Ao executar a função juros_simples, teríamos o seguinte resultado:

juros_simples(1000, 5, 6)
CAPITAL: 1000 TAXA: 5 TEMPO: 6
RESULTADO: 300.0
'''

def decorador(function):
  def decorator_imprimir(*args,**kwargs):
    print("calculadora de juros")
    function(*args,**kwargs)
  return decorator_imprimir
 
@decorador
def juros_simples(capital, taxa, tempo):
  resultado =  capital * (taxa/100) * tempo
  print(f"CAPITAL: {capital} TAXA: {taxa} TEMPO: {tempo}\nRESULTADO: {resultado:.1f}")
  
if __name__ == "__main__":  
  juros_simples(1000,5,6) 
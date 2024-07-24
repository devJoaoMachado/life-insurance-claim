import pandas as pd # type: ignore
import random

# Função para gerar dados
def generateData(num_samples):
    data = []
    for _ in range(num_samples):
        idade = random.randint(18, 70)
        bebe = random.choice(['sim', 'não'])
        fuma = random.choice(['sim', 'não'])
        sexo = random.choice(['M', 'F'])
        profissao = random.choice(['analista de sistemas', 'policial militar', 'engenheiro naval'])
        pratica_exercicios = random.choice(['sim', 'não'])
        checkup_anual = random.choice(['sim', 'não'])
        
        # Determinar sinistro baseado nas regras fornecidas
        sinistro2Anos = 'não'
        if idade >= 40 and idade <= 70:
            if bebe == 'sim' and fuma == 'sim' and pratica_exercicios == 'não':
                sinistro2Anos = 'sim'
        elif idade >= 30 and idade <= 50:
            if profissao == 'policial militar' and fuma == 'sim' and checkup_anual == 'não':
                sinistro2Anos = 'sim'
                
        data.append([idade, bebe, fuma, sexo, profissao, pratica_exercicios, checkup_anual, sinistro2Anos])
    
    return pd.DataFrame(data, columns=['idade', 'bebe', 'fuma', 'sexo', 'profissao', 'pratica_exercicios', 'checkup_anual', 'sinistro2Anos'])

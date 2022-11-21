import pandas as pd
import os


#os.chdir(os.path.dirname(os.path.abspath(__file__)))


def add_linha_df(df, nome, carro,placa):
    linha = {'Nome':nome,'Carro':carro,'Placa':placa}
    df = df.append(linha, ignore_index=True)
    return df 

def ler_df():
    df = pd.read_csv('./npdr.csv')
    return df

def salvar_df(df, arquivo):
    df.to_csv(arquivo,index = False)
    return 


def condicional(nome,carro,placa):
    df = pd.read_csv('./npdr.csv')
    aux = df.Placa.apply(str)
    aux = list(aux)
    if not(str(placa) in aux):

        df = add_linha_df(df,nome,carro,placa)

        salvar_df(df,'./npdr.csv')
        print(df)

        print('salvou')
        return

    else:
        print('dados ja cadastrados')
        return




if __name__ == '__main__':
    #print(type(os.getcwd()))   
   df = ler_df()
   df = pd.read_csv('./npdr.csv')
   salvar_df(df,'./npdr.csv')
   condicional('','','')

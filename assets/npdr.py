import pandas as pd
import os


#os.chdir(os.path.dirname(os.path.abspath(__file__)))

def database(nome,carro,placa):
    if not(os.path.isfile('npdr.csv')):
        data=[]
        data.append([nome,carro,placa])

        df = pd.DataFrame(data,columns=['Nome','Carro','Placa'],dtype=str)
        df.to_csv('./npdr.csv',index=False)
        return

    else:
        df = pd.read_csv('npdr.csv')
        aux = df['Placa'].apply(str)
        aux = list(aux)

        if not(str(placa) in aux):
            data=[]
            data.append([nome,carro,placa])
            df = pd.DataFrame(data)
            print(df)
            df.to_csv('npdr.csv', mode='a',index=False, header=False)
            return

        else:
            print('dados ja cadastrados')
        return

def read_database(digitosplaca):
    df = pd.read_csv('npdr.csv').astype(str)
    for i in range(len(df)):
        aux = list(df.iloc[i])
        if(aux[2] == digitosplaca):
            return aux
    aux = ["ERRO", "ERRO", "ERRO"]
    return aux


if __name__ == '__main__':
    #print(type(os.getcwd()))
    print((read_database(111)))




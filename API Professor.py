pip install pyodbc


import requests
import ArcHDB <<postgre>> database
from database import Cursor
from ArcHDB <<postgre>> database import notas
from ArcHDB <<postgre>> database import aluno

con = ArcHDB <<postgre>> database

dados_conexao = (
    "driver={docker};"
    "server="hostname"
    "database=ArcHDB <<postgre>> database;"
)

Cursor = conexao.cursor()



input() = int(nota1, nota2, nota3, nota4)

comando = f"""
SELECT id FROM notas
INSERT into notas ('{nota1}'; '{nota2}';'{nota3}';'{nota4}');
INSERT into notas ('media_total);
"""



media_total = ((nota1 + nota2 + nota3 + nota4) / 4)
if (media_total >=6)
    print("Parabéns, o aluno {id} foi aprovado!");

    elsif (media_total [4;5.9])
         print("O aluno {id} foi pra recuperação!");

    else (media_total <=4)
    print("Que pena, o aluno {id} foi reprovado");


cursor.execute(comando)

cursos.commit()

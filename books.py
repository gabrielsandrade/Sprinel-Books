from urllib.request import urlopen, urlretrieve
import pandas as pd
import requests, os

df = pd.read_excel("FreeEnglishTextbooks.xlsx")
tipos = df['English Package Name'].unique()

num = 1
for tipo in tipos :
    print(f"## {num} - {tipo}")
    num += 1
print("##\n##\n## Se preferir baixar todas as categoria digite 0.")    
tipo = int(input("## Informe o número corresponde ao tipo de livro que deseja baixar : "))
if tipo != 0: 
    tipo-= 1
    print(f"Baixando livros da categoria {tipos[tipo]}")
else:
    print("Baixando livros de todas as categorias.")
if tipo > 0 and tipo < len(df["English Package Name"].unique()):
    df = df.loc[df["English Package Name"] == tipos[tipo]]

for row in df.iterrows():
    titulo = row[1][0].replace("/", "-")
    categoria = row[1][11]
    link = row[1][18]
    print(titulo)
    print(link)
    path = os.path.join("livros",categoria)
    if not os.path.exists(path):
        os.makedirs(path)
    filename = os.path.join(path, titulo) + ".pdf"
    if not os.path.exists(filename):
        print("Baixando o livro.")
        response = requests.get(link).url
        link = response.replace("book", "content/pdf")
        req = urlopen(link)
        urlretrieve(link, filename)
    else: 
        print("Livro já foi baixado")
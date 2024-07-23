import pandas as pd


marca = {
    'marca': ['D&g Dolce & Gabbana', 'Givenchy', 'Joe Fresh', 'Mixed', 'Zara',
       'Gap', 'Banana Republic', 'Fyi', 'Sacada', 'Rag & Bone', 'Cori',
       'Forever 21', 'Tigresse', 'Tory Burch', 'Brooksfield', 'Animale',
       '284', 'Dkny', 'Cheroy', 'Canal', 'Le Lis Blanc', 'Spezzato',
       'Cantão', 'Talie Nk', 'H&M', 'Schutz', 'Jorge Bischoff', #27
       'Luisa Farani', 'Seven', 'Kipling', 'Louis Vuitton', 'Agilità',
       'Fabiana Caterina', 'Reinaldo Lourenço', 'Karmani', 'Erre Erre',
       'H&m', 'Forum', 'Ellus', 'J. Crew', "Joe's", 'Galeria Tricot',
       'Loft 747', 'Oxyfit', 'Topshop', 'A.brand', 'Isolda',
       'American Eagle', 'Colcci', 'Carter’s', 'Thay Ribas', #51
       'Carina Duek', 'Kate Spade', 'Bottega Veneta', 'Morena Rosa',
       'Luiza Barcelos', 'Lezalez', 'My Place', 'Farm', 'Armani Exchange',
       'Bcbgmaxzria', 'Dica da Ka', 'My Shoes', 'Argentum',
       'Red Valentino', 'Maria Filó', 'Marc By Marcjacobs',
       'Track & Field', 'Christian Dior', 'Toca do Coelho',
       'Barbara Bela', 'Miu Miu', 'Gregory', 'Prada', 'Steal The Look',
       'Shoulder', 'Maria Bonita', 'Isa Kulikovski', 'Ralph Lauren',
       'Camila Klein', 'Bazar Genial', 'Hollister', 'Diesel', #83
       'All Saints Spitalfields', 'Iorane', 'Felini', 'Miss Sixty',
       'Linda de Morrer', 'Vera Wang', 'Daslu', 'Adidas', 'Amaro',
       'Jimmy Choo', 'Sweet Cotton', 'Cris Barros', 'Mara Mac',
       'Paula Raia', 'Dress&co', 'Mango', 'Ateliê de Calças', 'Thelure', #101
       'Converse', "Levi's", 'Lemon Cola', 'Limone By Jade Seba',
       'Espaço Fashion', 'Seal Brasil', 'Alix Shop', 'Bo. bô.',
       'Lauren Ralph Lauren', 'Christian Louboutin', 'Saad', 'Osklen',
       'Skazi', 'Carol Bassi', 'Calvin Klein', 'Express','Bobô'],


    'marca_genero': ['U', 'F', 'F', 'F', "F", "U", "U", "U", "F", "F", "F", "F", "F", "F", "M", "F",
                              "F", "F", "F", "U", "F", "F", "F", "U", "U", "F", "F", "F", "U", "U", "U", "F", "F",
                              "F", "F", "F", "U", "M", "U", "F", "U", "F", "F", "F", "F", "F", "F", "U", "F",
                              "U", "F", "F", "F", "U", "F", "F", "F", "F", "F", "M", "F", "F", "F", "F", "U",
                              "F", "F", "F", "U", "U", "F", "F", "U", "F", "F", "F", "F", "F", "U", "F", "U",
                              "U", "U", "U", "F", "M", "F", "F", "F", "F", "U", "F", "U", "F", "F", "U", "F",
                              "F", "F", "F", "F", "U", "U", "F", "F", "F", "M", "F", "F", "F", "F", "U", "U",
                               "F", "F", "U", "U","F"]}
def marca_gen():
   df_marca_genero = pd.DataFrame(marca)
   return df_marca_genero

clasificando_productos_unisex = {
    "Oculos Metal": "F", "Bolsa Classica Roxa": "F", "Camisa Jeans Classica": "M",
    "Camisa Xadrez Azul": "F", "Regata Nude Textura": "F", "Blusinha Guipir Black": "F",
    "Calca Ziper Preto": "F", "Casaco Preto Botoes": "F", "Saia Amarela Faixa": "F",
    "Calca Jeans Basica": "F", "Tenis Xadrez Tecido": "F", "Body Estampa Coracoes": "F",
    "Conjunto Body Calca": "F", "Macaquinho Tricot Bege": "F", "Calca Preta Resinada": "F",
    "Vestido Nude Reta": "F", "Calca Veludo Cotele": "F", "Blusa Tricot Mescla": "F",
    "Blazer Cinza E Azul Marinho": "M", "Calca Estampa Flare": "F", "Blusa Babados Cats": "F",
    "Vestido Preto Franzido": "F", "Vestido Estampa Pb": "F", "Cropped Courino Texturas": "F",
    "Vestido Preto Amarracao": "F", "Regata Listras Azul": "M", "Regata Estampa Roxa": "F",
    "Calca Estampa Pb": "F", "Vestido Polo Lilas": "F", "Blusa Tricot Lilas": "F",
    "Bolsa Vermelha Brilhos": "F", "Oculos Lente Azulada": "M", "Bermuda Jeans Lavagem": "M",
    "Calca Jeans Costuras": "F", "Shorts Listras Bordados": "F", "Mala Bolsos Preta": "M",
    "Regata Bicolor Alcinha": "F", "Vestido Estampa Laco": "F", "Scarpin Bege Textura": "F",
    "Bolsa Intrecciato Caramelo": "F", "Vestido Malha Cinza": "F", "Sneaker Monograma Bege": "M",
    "Clutch Preta Pregas": "F", "Blusa Malha Azul": "F", "Bermuda Listras Bolsos": "F",
    "Vestido Listras Malha": "F", "Tenis Tecido Purple": "M", "Calca Jeans Trancada": "F"
}

def dict_prod_gen():
   return clasificando_productos_unisex

# df_all = pd.merge(df_final, df_marca_genero, on='marca', how='inner')
# df_all['product_genero']=df_all['marca_genero']
# df_all['product_genero'] = df_all.apply(lambda row: clasificando_productos_unisex.get(row['producto'], row['product_genero']),axis=1)
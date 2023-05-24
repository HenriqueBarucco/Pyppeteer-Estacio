from src.helpers.save_data import save_data
from src.entities.product import Product

teste = []

for _ in range(1000):
    product = Product()
    product['url'] = 'teste'
    product['nome'] = 'teste'
    product['preco_normal'] = 'afgadf'
    product['preco_desconto'] = '234124'
    product['duracao'] = '111'
    teste.append(product)

save_data.productToXlsx(teste,'D:')
    
from flask import Flask, jsonify
import random

app = Flask(__name__)

# Marcas Locais
marcas_locais = [
    {"nome": "Moose Coffee", "descricao": "Cafeteria familiar de Minnesota que patrocina esportes locais."},
    {"nome": "Evergreen Bank", "descricao": "Banco comunitário de Oregon, voltado para negócios locais e sustentabilidade."},
    {"nome": "Rust Valley Garage", "descricao": "Oficina independente de restauração de carros nas montanhas de Idaho."},
    {"nome": "Buffalo Creek BBQ", "descricao": "Churrascaria texana conhecida por apoiar equipes regionais de base."},
    {"nome": "Blue Ridge Outfitters", "descricao": "Loja de equipamentos de trilha da Virgínia que patrocina eventos escolares."},
    {"nome": "Sunset Vinyl", "descricao": "Gravadora independente da Califórnia com histórico de apoio a times amadores."}
]

# Marcas Nacionais
marcas_nacionais = [
    {"nome": "Trader Joe's", "descricao": "Rede nacional de supermercados alternativa, muito popular entre famílias americanas."},
    {"nome": "JetBlue Airways", "descricao": "Companhia aérea americana de baixo custo, com forte presença em cidades costeiras."},
    {"nome": "REI Co-op", "descricao": "Cooperativa americana especializada em esportes ao ar livre e sustentabilidade."},
    {"nome": "Wegmans", "descricao": "Supermercado regional do nordeste dos EUA, com reputação de excelência e apoio ao esporte juvenil."},
    {"nome": "Five Guys", "descricao": "Rede de hambúrgueres artesanais famosa nos EUA, com histórico de patrocinar ligas menores."},
    {"nome": "Tito's Handmade Vodka", "descricao": "Marca texana de vodka artesanal que patrocina eventos culturais e esportivos."},
    {"nome": "Yeti", "descricao": "Marca premium de equipamentos térmicos e de acampamento, com forte branding entre esportistas e caçadores."},
    {"nome": "Carhartt", "descricao": "Marca tradicional de roupas de trabalho e moda urbana, patrocinadora de causas comunitárias."},
    {"nome": "Allbirds", "descricao": "Marca californiana de tênis sustentáveis, popular entre jovens e empreendedores."},
    {"nome": "Ben & Jerry's", "descricao": "Marca de sorvetes com forte engajamento social e envolvimento em causas locais e ambientais."}
]

# Marcas Globais
marcas_globais = [
    {"nome": "Apple", "descricao": "Gigante da tecnologia conhecida por seus produtos icônicos como iPhone, Mac e Apple Watch."},
    {"nome": "Amazon", "descricao": "Maior varejista online do mundo, com presença em quase todos os setores."},
    {"nome": "Google", "descricao": "Líder mundial em buscas, tecnologia e inteligência artificial."},
    {"nome": "Coca-Cola", "descricao": "Marca de refrigerante mais reconhecida globalmente, com campanhas publicitárias históricas."},
    {"nome": "PepsiCo", "descricao": "Multinacional de bebidas e snacks, dona de marcas como Gatorade, Lay’s e Quaker."},
    {"nome": "McDonald's", "descricao": "Maior rede de fast-food do mundo, com restaurantes em mais de 100 países."},
    {"nome": "Samsung", "descricao": "Conglomerado sul-coreano com produtos em tecnologia, TVs, celulares e eletrônicos."},
    {"nome": "Sony", "descricao": "Multinacional japonesa de eletrônicos, entretenimento e videogames (PlayStation)."},
    {"nome": "Netflix", "descricao": "Principal serviço global de streaming de filmes, séries e documentários."},
    {"nome": "Starbucks", "descricao": "Rede de cafeterias mais famosa do mundo, com presença em centros urbanos globais."},
    {"nome": "Tesla", "descricao": "Empresa de carros elétricos e energia renovável, liderada por Elon Musk."},
    {"nome": "Toyota", "descricao": "Uma das maiores fabricantes de automóveis do mundo, com tradição em inovação."},
    {"nome": "Huawei", "descricao": "Gigante chinesa de telecomunicações e eletrônicos."},
    {"nome": "Visa", "descricao": "Uma das principais redes de pagamento e cartões de crédito do mundo."},
    {"nome": "Mastercard", "descricao": "Multinacional de serviços financeiros com foco em pagamentos digitais globais."},
    {"nome": "Nestlé", "descricao": "Maior empresa de alimentos e bebidas do mundo, dona de marcas como Nescafé e KitKat."},
    {"nome": "Heineken", "descricao": "Cervejaria holandesa com distribuição mundial e patrocínios em esportes e música."},
    {"nome": "IKEA", "descricao": "Gigante sueca de móveis e decoração com presença internacional."},
    {"nome": "Airbnb", "descricao": "Plataforma líder em aluguel de acomodações por temporada, presente em quase todo o planeta."},
    {"nome": "YouTube", "descricao": "A maior plataforma de vídeos online do mundo, pertencente ao Google."}
]

@app.route("/")
def home():
    return "Sistema de patrocínio está online!"

@app.route("/sponsorship/local")
def local():
    selecionadas = random.sample(marcas_locais, 3)
    resultado = {}
    for i, m in enumerate(selecionadas):
        resultado[f"marcaescolhida{i+1}"] = m["nome"]
        resultado[f"descricaoda{i+1}"] = m["descricao"]
    return jsonify(resultado)

@app.route("/sponsorship/national")
def national():
    selecionadas = random.sample(marcas_nacionais, 3)
    resultado = {}
    for i, m in enumerate(selecionadas):
        resultado[f"marcaescolhida{i+1}"] = m["nome"]
        resultado[f"descricaoda{i+1}"] = m["descricao"]
    return jsonify(resultado)

@app.route("/sponsorship/global")
def global_():
    selecionadas = random.sample(marcas_globais, 3)
    resultado = {}
    for i, m in enumerate(selecionadas):
        resultado[f"marcaescolhida{i+1}"] = m["nome"]
        resultado[f"descricaoda{i+1}"] = m["descricao"]
    return jsonify(resultado)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)

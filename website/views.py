from django.shortcuts import render

# Função auxiliar para dividir em grupos de n
def chunk_list(lst, n):
    return [lst[i:i+n] for i in range(0, len(lst), n)]

# Dados do elenco
elenco_completo = [
    {
        "id": 1,
        "nome": "Derek Shepherd",
        "ator": "Patrick Dempsey",
        "especialidade": "Neurocirurgia",
        "apelido": "McDreamy",
        "descricao": """
Derek Shepherd, conhecido como "McDreamy", é um dos neurocirurgiões mais renomados do Seattle Grace Hospital. Sua reputação se baseia tanto em suas habilidades cirúrgicas quanto em sua personalidade carismática e envolvente. Derek enfrenta desafios pessoais complexos, incluindo seu relacionamento turbulento com Meredith Grey. Apesar das dificuldades, ele mantém uma postura profissional exemplar e é considerado uma figura de liderança e inspiração para seus colegas. Sua jornada inclui momentos de tragédia, superação e realizações médicas que marcaram a série.""",
        "imagem": "website/img/dereksherpherd.webp",
        "imagens" : [
        {"src": "website/img/derek1.jpg", "alt": "Foto 1", "classe": "large"},
        {"src": "website/img/galeria2.jpg", "alt": "Foto 2", "classe": "small"},
        {"src": "website/img/galeria3.webp", "alt": "Foto 3", "classe": "small"},
        {"src": "website/img/galeria4.jpg", "alt": "Foto 4", "classe": "medium"},
        {"src": "website/img/galeria5.webp", "alt": "Foto 5", "classe": "small"},
        {"src": "website/img/galeria6.jpg", "alt": "Foto 6", "classe": "large"},
        {"src": "website/img/galeria7.jpg", "alt": "Foto 7", "classe": "large"},
        {"src": "website/img/galeria8.jpg", "alt": "Foto 8", "classe": "small"},
        {"src": "website/img/galeria9.jpg", "alt": "Foto 9", "classe": "small"},
        {"src": "website/img/galeria10.jpg", "alt": "Foto 10", "classe": "large"},
        {"src": "website/img/galeria11.jpg", "alt": "Foto 11", "classe": "large"},
        {"src": "website/img/galeria12.webp", "alt": "Foto 12", "classe": "small"},
        {"src": "website/img/galeria13.jpg", "alt": "Foto 13", "classe": "medium"},
        {"src": "website/img/galeria14.webp", "alt": "Foto 14", "classe": "small"},
        {"src": "website/img/galeria15.webp", "alt": "Foto 15", "classe": "small"},
        ]
    },
    {
        "id": 2,
        "nome": "Mark Sloan",
        "ator": "Eric Dane",
        "especialidade": "Cirurgia plástica",
        "apelido": "McSteamy",
        "descricao": """
Mark Sloan, apelidado de "McSteamy", é um cirurgião plástico famoso por sua habilidade técnica e personalidade extrovertida. Ele é conhecido por seu charme irresistível e relacionamentos amorosos complicados, que muitas vezes trazem tensão para o ambiente hospitalar. Apesar do seu lado mulherengo, Mark é profundamente dedicado ao seu trabalho e aos seus pacientes, sempre buscando os melhores resultados estéticos e funcionais. Sua história na série envolve redenção, amizade e momentos de vulnerabilidade que humanizam o personagem.""",
        "imagem": "website/img/marksloan.jpg",
        "imagens" : [
        {"src": "website/img/mark1.jpg", "alt": "Foto 1", "classe": "large"},
        {"src": "website/img/mark2.jpeg", "alt": "Foto 2", "classe": "small"},
        {"src": "website/img/mark3.jpeg", "alt": "Foto 3", "classe": "small"},
        {"src": "website/img/mark44.jpg", "alt": "Foto 4", "classe": "medium"},
        {"src": "website/img/mark5.jpg", "alt": "Foto 5", "classe": "small"},
        {"src": "website/img/mark6.jpg", "alt": "Foto 6", "classe": "large"},
        {"src": "website/img/mark7.avif", "alt": "Foto 7", "classe": "large"},
        {"src": "website/img/mark8.webp", "alt": "Foto 8", "classe": "small"},
        {"src": "website/img/mark9.jpg", "alt": "Foto 9", "classe": "small"},
        {"src": "website/img/mark10.avif", "alt": "Foto 10", "classe": "large"},
        {"src": "website/img/mark11.jpg", "alt": "Foto 11", "classe": "large"},
        {"src": "website/img/mark12.webp", "alt": "Foto 12", "classe": "small"},
        {"src": "website/img/mark13.jpg", "alt": "Foto 13", "classe": "medium"},
        {"src": "website/img/mark15.webp", "alt": "Foto 14", "classe": "small"},
        {"src": "website/img/mark14.jpeg", "alt": "Foto 15", "classe": "small"},
        ]
    },
    {
        "id": 3,
        "nome": "Meredith Grey",
        "ator": "Ellen Pompeo",
        "especialidade": "Cirurgia geral",
        "apelido": "Mer",
        "descricao": """
Meredith Grey é a protagonista central da série, uma cirurgiã geral cuja trajetória é marcada por desafios pessoais e profissionais. Filha de uma renomada cirurgiã, Meredith luta para se destacar e encontrar sua própria identidade dentro do hospital Seattle Grace. Sua vida é permeada por altos e baixos emocionais, relacionamentos complexos e a constante pressão da medicina de emergência. Ao longo da série, Meredith evolui, tornando-se uma médica brilhante e uma mulher resiliente, que enfrenta perdas e conquistas com coragem.""",
        "imagem": "website/img/fotomeredith.jpg",
         "imagens" : [
        {"src": "website/img/grey1.jpg", "alt": "Foto 1", "classe": "large"},
        {"src": "website/img/grey2.webp", "alt": "Foto 2", "classe": "small"},
        {"src": "website/img/grey3.jpg", "alt": "Foto 3", "classe": "small"},
        {"src": "website/img/grey4.jpg", "alt": "Foto 4", "classe": "medium"},
        {"src": "website/img/grey5.jpg", "alt": "Foto 5", "classe": "small"},
        {"src": "website/img/grey6.avif", "alt": "Foto 6", "classe": "large"},
        {"src": "website/img/grey7.jpg", "alt": "Foto 7", "classe": "large"},
        {"src": "website/img/grey8.jpg", "alt": "Foto 8", "classe": "small"},
        {"src": "website/img/grey9.jpg", "alt": "Foto 9", "classe": "small"},
        {"src": "website/img/grey10.webp", "alt": "Foto 10", "classe": "large"},
        {"src": "website/img/grey11.jpg", "alt": "Foto 11", "classe": "large"},
        {"src": "website/img/grey12.jpg", "alt": "Foto 12", "classe": "small"},
        {"src": "website/img/grey13.webp", "alt": "Foto 13", "classe": "medium"},
        {"src": "website/img/grey14.jpg", "alt": "Foto 14", "classe": "small"},
        {"src": "website/img/grey15.jpg", "alt": "Foto 15", "classe": "small"},
        ]
    },
    {
        "id": 4,
        "nome": "Lexie Grey",
        "ator": "Chyler Leigh",
        "especialidade": "Cirurgia geral",
        "apelido": "Lexie",
        "descricao": """
Lexie Grey é a irmã mais nova de Meredith e também cirurgiã geral. Conhecida por sua inteligência aguçada e memória fotográfica, Lexie traz uma combinação de vulnerabilidade e determinação para sua carreira médica. Ela luta para provar seu valor em um ambiente competitivo e para manter relacionamentos significativos, especialmente com colegas e familiares. Lexie é uma personagem sensível que passa por crescimento pessoal e profissional, deixando uma marca importante na série.""",
        "imagem": "website/img/lexiee.png",
         "imagens" : [
        {"src": "website/img/lexie01.jpeg", "alt": "Foto 1", "classe": "large"},
        {"src": "website/img/lexie2.jpg", "alt": "Foto 2", "classe": "small"},
        {"src": "website/img/lexie3.webp", "alt": "Foto 3", "classe": "small"},
        {"src": "website/img/lexie04.jpeg", "alt": "Foto 4", "classe": "medium"},
        {"src": "website/img/lexie5.jpg", "alt": "Foto 5", "classe": "small"},
        {"src": "website/img/lexie6.webp", "alt": "Foto 6", "classe": "large"},
        {"src": "website/img/lexie7.png", "alt": "Foto 7", "classe": "large"},
        {"src": "website/img/lexie8.webp", "alt": "Foto 8", "classe": "small"},
        {"src": "website/img/lexie9.jpg", "alt": "Foto 9", "classe": "small"},
        {"src": "website/img/lexie10.jpg", "alt": "Foto 10", "classe": "large"},
        {"src": "website/img/lexie11.jpg", "alt": "Foto 11", "classe": "large"},
        {"src": "website/img/lexie12.jpg", "alt": "Foto 12", "classe": "small"},
        {"src": "website/img/lexie13.jpg", "alt": "Foto 13", "classe": "medium"},
        {"src": "website/img/lexie14.jpg", "alt": "Foto 14", "classe": "small"},
        {"src": "website/img/lexie15.jpg", "alt": "Foto 15", "classe": "small"},
        ]
    },
    {
        "id": 5,
        "nome": "Cristina Yang",
        "ator": "Sandra Oh",
        "especialidade": "Cirurgia cardiotorácica",
        "apelido": "Yang",
        "descricao": """
Cristina Yang é uma cirurgiã cardiotorácica brilhante e ambiciosa, conhecida por sua dedicação extrema à carreira e sua personalidade direta e muitas vezes impetuosa. Sua amizade profunda com Meredith Grey é um dos pilares emocionais da série, mostrando um relacionamento intenso e cheio de apoio mútuo. Cristina enfrenta desafios pessoais e profissionais, buscando sempre ser a melhor em sua área, mesmo que isso custe relacionamentos e conforto pessoal. Sua jornada destaca temas de empoderamento, ética médica e auto-descoberta.""",
        "imagem": "website/img/cristina.jpg",
         "imagens" : [
        {"src": "website/img/yang1.jpg", "alt": "Foto 1", "classe": "large"},
        {"src": "website/img/yang2.jpg", "alt": "Foto 2", "classe": "small"},
        {"src": "website/img/yang3.jpg", "alt": "Foto 3", "classe": "small"},
        {"src": "website/img/yang4.avif", "alt": "Foto 4", "classe": "medium"},
        {"src": "website/img/yang5.jpeg", "alt": "Foto 5", "classe": "small"},
        {"src": "website/img/yang6.webp", "alt": "Foto 6", "classe": "large"},
        {"src": "website/img/yang7.jpeg", "alt": "Foto 7", "classe": "large"},
        {"src": "website/img/yang8.jpeg", "alt": "Foto 8", "classe": "small"},
        {"src": "website/img/yang9.jpg", "alt": "Foto 9", "classe": "small"},
        {"src": "website/img/yang10.webp", "alt": "Foto 10", "classe": "large"},
        {"src": "website/img/yang11.jpeg", "alt": "Foto 11", "classe": "large"},
        {"src": "website/img/yang12.webp", "alt": "Foto 12", "classe": "small"},
        {"src": "website/img/yang13.jpeg", "alt": "Foto 13", "classe": "medium"},
        {"src": "website/img/yang14.webp", "alt": "Foto 14", "classe": "small"},
        {"src": "website/img/yang15.webp", "alt": "Foto 15", "classe": "small"},
        ]
    },
    {
        "id": 6,
        "nome": "Callie Torres",
        "ator": "Sara Ramirez",
        "especialidade": "Ortopedia",
        "apelido": "Callie",
        "descricao": """
Callie Torres é uma cirurgiã ortopédica talentosa, que traz para a série uma forte presença feminina e diversidade. Sua personalidade vibrante e às vezes impulsiva contrasta com seu profissionalismo e cuidado com os pacientes. Ao longo da série, Callie enfrenta vários desafios pessoais, incluindo relacionamentos complexos e questões de identidade. Ela é uma personagem que demonstra crescimento, vulnerabilidade e força, contribuindo para a representação de temas sociais relevantes na narrativa.""",
        "imagem": "website/img/callie.jpg",
        "imagens" : [
        {"src": "website/img/callie1.jpg", "alt": "Foto 1", "classe": "large"},
        {"src": "website/img/callie2.webp", "alt": "Foto 2", "classe": "small"},
        {"src": "website/img/callie3.webp", "alt": "Foto 3", "classe": "small"},
        {"src": "website/img/callie4.webp", "alt": "Foto 4", "classe": "medium"},
        {"src": "website/img/callie5.webp", "alt": "Foto 5", "classe": "small"},
        {"src": "website/img/callie6.webp", "alt": "Foto 6", "classe": "large"},
        {"src": "website/img/callie7.webp", "alt": "Foto 7", "classe": "large"},
        {"src": "website/img/callie8.webp", "alt": "Foto 8", "classe": "small"},
        {"src": "website/img/callie9.webp", "alt": "Foto 9", "classe": "small"},
        {"src": "website/img/callie10.webp", "alt": "Foto 10", "classe": "large"},
        {"src": "website/img/callie11.jpg", "alt": "Foto 11", "classe": "large"},
        {"src": "website/img/callie12.jpg", "alt": "Foto 12", "classe": "small"},
        {"src": "website/img/callie13.jpg", "alt": "Foto 13", "classe": "medium"},
        {"src": "website/img/callie14.jpg", "alt": "Foto 14", "classe": "small"},
        {"src": "website/img/callie15.jpg", "alt": "Foto 15", "classe": "small"},
        ]
    },
    {
        "id": 7,
        "nome": "Miranda Bailey",
        "ator": "Chandra Wilson",
        "especialidade": "Cirurgia geral",
        "apelido": "Nazi",
        "descricao": """
Miranda Bailey é uma cirurgiã geral rigorosa, reconhecida pelo seu alto padrão profissional e por sua capacidade de liderança dentro do hospital. Embora inicialmente receba o apelido “Nazi” devido ao seu estilo autoritário, ao longo da série sua humanidade, cuidado e dedicação à formação dos residentes são evidentes. Bailey é um exemplo de força feminina na medicina, enfrentando desafios pessoais e profissionais e mantendo-se uma figura respeitada e admirada.""",
        "imagem": "website/img/mirandabailey.jpg",
        "imagens" : [
        {"src": "website/img/bailey1.jpg", "alt": "Foto 1", "classe": "large"},
        {"src": "website/img/bailey2.jpg", "alt": "Foto 2", "classe": "small"},
        {"src": "website/img/bailey3.jpg", "alt": "Foto 3", "classe": "small"},
        {"src": "website/img/bailey4.jpg", "alt": "Foto 4", "classe": "medium"},
        {"src": "website/img/bailey5.jpg", "alt": "Foto 5", "classe": "small"},
        {"src": "website/img/bailey6.jpg", "alt": "Foto 6", "classe": "large"},
        {"src": "website/img/bailey7.jpg", "alt": "Foto 7", "classe": "large"},
        {"src": "website/img/bailey8.jpg", "alt": "Foto 8", "classe": "small"},
        {"src": "website/img/bailey9.jpg", "alt": "Foto 9", "classe": "small"},
        {"src": "website/img/bailey10.jpg", "alt": "Foto 10", "classe": "large"},
        {"src": "website/img/bailey11.jpg", "alt": "Foto 11", "classe": "large"},
        {"src": "website/img/bailey12.jpg", "alt": "Foto 12", "classe": "small"},
        {"src": "website/img/bailey13.jpg", "alt": "Foto 13", "classe": "medium"},
        {"src": "website/img/bailey14.jpg", "alt": "Foto 14", "classe": "small"},
        {"src": "website/img/bailey15.jpg", "alt": "Foto 15", "classe": "small"},
        ]
    },
    {
        "id": 8,
        "nome": "Jo Wilson",
        "ator": "Camilla Luddington",
        "especialidade": "Cirurgia geral",
        "apelido": "Jo",
        "descricao": """
Jo Wilson é uma cirurgiã geral que enfrenta uma trajetória marcada por dificuldades pessoais e superação. Sua história inclui um passado difícil, que impacta suas relações e sua confiança, mas também a motiva a buscar excelência na medicina. Jo é uma personagem complexa, mostrando vulnerabilidade e força, e sua jornada aborda temas como resiliência, identidade e amor.""",
        "imagem": "website/img/jo.jpg",
        "imagens" : [
        {"src": "website/img/jo1.jpg", "alt": "Foto 1", "classe": "large"},
        {"src": "website/img/jo2.webp", "alt": "Foto 2", "classe": "small"},
        {"src": "website/img/jo3.jpg", "alt": "Foto 3", "classe": "small"},
        {"src": "website/img/jo4.avif", "alt": "Foto 4", "classe": "medium"},
        {"src": "website/img/jo5.jpg", "alt": "Foto 5", "classe": "small"},
        {"src": "website/img/jo6.jpg", "alt": "Foto 6", "classe": "large"},
        {"src": "website/img/jo7.jpg", "alt": "Foto 7", "classe": "large"},
        {"src": "website/img/jo8.webp", "alt": "Foto 8", "classe": "small"},
        {"src": "website/img/jo9.jpg", "alt": "Foto 9", "classe": "small"},
        {"src": "website/img/jo10.jpg", "alt": "Foto 10", "classe": "large"},
        {"src": "website/img/jo11.jpg", "alt": "Foto 11", "classe": "large"},
        {"src": "website/img/jo12.jpg", "alt": "Foto 12", "classe": "small"},
        {"src": "website/img/jo13.jpg", "alt": "Foto 13", "classe": "medium"},
        {"src": "website/img/jo14.jpg", "alt": "Foto 14", "classe": "small"},
        {"src": "website/img/jo15.jpg", "alt": "Foto 15", "classe": "small"},
        ]
    },
    {
        "id": 9,
        "nome": "Addison Montgomery",
        "ator": "Kate Walsh",
        "especialidade": "Obstetrícia e ginecologia / Neonatologia",
        "apelido": "Addison",
        "descricao": """
Addison Montgomery é uma especialista em obstetrícia, ginecologia e neonatologia, reconhecida por sua competência e estilo sofisticado. Sua personalidade forte e às vezes difícil cria tensões e alianças dentro do hospital. Addison traz para a série temas ligados à medicina feminina e às complexidades das relações pessoais, equilibrando carreira e vida afetiva em sua trajetória.""",
        "imagem": "website/img/addison.jpg",
         "imagens" : [
        {"src": "website/img/addison1.webp", "alt": "Foto 1", "classe": "large"},
        {"src": "website/img/addison2.webp", "alt": "Foto 2", "classe": "small"},
        {"src": "website/img/addison3.jpg", "alt": "Foto 3", "classe": "small"},
        {"src": "website/img/addison13.jpg", "alt": "Foto 4", "classe": "medium"},
        {"src": "website/img/addison5.jpg", "alt": "Foto 5", "classe": "small"},
        {"src": "website/img/addison6.avif", "alt": "Foto 6", "classe": "large"},
        {"src": "website/img/addison7.jpg", "alt": "Foto 7", "classe": "large"},
        {"src": "website/img/addison8.jpg", "alt": "Foto 8", "classe": "small"},
        {"src": "website/img/addison9.jpg", "alt": "Foto 9", "classe": "small"},
        {"src": "website/img/addison10.jpg", "alt": "Foto 10", "classe": "large"},
        {"src": "website/img/addison11.jpg", "alt": "Foto 11", "classe": "large"},
        {"src": "website/img/addison12.jpg", "alt": "Foto 12", "classe": "small"},
        {"src": "website/img/addison14.avif", "alt": "Foto 13", "classe": "medium"},
        {"src": "website/img/addison15.jpg", "alt": "Foto 14", "classe": "small"},
        {"src": "website/img/addison4.jpeg", "alt": "Foto 15", "classe": "small"},
        ]
    },
    {
        "id": 10,
        "nome": "Jackson Avery",
        "ator": "Jesse Williams",
        "especialidade": "Cirurgia plástica",
        "apelido": "Avery",
        "descricao": """
Jackson Avery é um cirurgião plástico talentoso, membro de uma família renomada na medicina. Sua busca por reconhecimento profissional e pessoal o impulsiona a desafios constantes, enquanto ele navega por complexos relacionamentos amorosos e dinâmicas familiares. Avery é conhecido por sua ética de trabalho, carisma e capacidade de inovação na área cirúrgica.""",
        "imagem": "website/img/jackson.jpg",
        "imagens" : [
        {"src": "website/img/avery13.webp", "alt": "Foto 1", "classe": "large"},
        {"src": "website/img/avery2.jpg", "alt": "Foto 2", "classe": "small"},
        {"src": "website/img/avery3.jpg", "alt": "Foto 3", "classe": "small"},
        {"src": "website/img/avery7.jpg", "alt": "Foto 4", "classe": "medium"},
        {"src": "website/img/avery5.jpg", "alt": "Foto 5", "classe": "small"},
        {"src": "website/img/avery6.jpg", "alt": "Foto 6", "classe": "large"},
        {"src": "website/img/avery8.jpg", "alt": "Foto 7", "classe": "large"},
        {"src": "website/img/avery4.webp", "alt": "Foto 8", "classe": "small"},
        {"src": "website/img/avery9.avif", "alt": "Foto 9", "classe": "small"},
        {"src": "website/img/avery10.jpg", "alt": "Foto 10", "classe": "large"},
        {"src": "website/img/avery11.avif", "alt": "Foto 11", "classe": "large"},
        {"src": "website/img/avery12.webp", "alt": "Foto 12", "classe": "small"},
        {"src": "website/img/avery1.webp", "alt": "Foto 13", "classe": "medium"},
        {"src": "website/img/avery14.webp", "alt": "Foto 14", "classe": "small"},
        {"src": "website/img/avery15.jpg", "alt": "Foto 15", "classe": "small"},
        ]
    },
    {
        "id": 11,
        "nome": "Amelia Shepherd",
        "ator": "Caterina Scorsone",
        "especialidade": "Neurocirurgia",
        "apelido": "Furacão Amelia",
        "descricao": """
Amelia Shepherd é uma neurocirurgiã talentosa e irmã de Derek Shepherd. Conhecida por sua personalidade forte e espírito independente, Amelia enfrenta batalhas pessoais, incluindo vícios e perdas, que marcam sua trajetória. Apesar das dificuldades, ela se destaca como uma médica excepcional, com uma paixão pela cirurgia e um compromisso profundo com seus pacientes.""",
        "imagem": "website/img/amelia.jpg",
        "imagens" : [
        {"src": "website/img/amelia1.webp", "alt": "Foto 1", "classe": "large"},
        {"src": "website/img/amelia2.webp", "alt": "Foto 2", "classe": "small"},
        {"src": "website/img/amelia3.webp", "alt": "Foto 3", "classe": "small"},
        {"src": "website/img/amelia4.webp", "alt": "Foto 4", "classe": "medium"},
        {"src": "website/img/amelia5.webp", "alt": "Foto 5", "classe": "small"},
        {"src": "website/img/amelia6.webp", "alt": "Foto 6", "classe": "large"},
        {"src": "website/img/amelia7.webp", "alt": "Foto 7", "classe": "large"},
        {"src": "website/img/amelia8.webp", "alt": "Foto 8", "classe": "small"},
        {"src": "website/img/amelia9.webp", "alt": "Foto 9", "classe": "small"},
        {"src": "website/img/amelia10.webp", "alt": "Foto 10", "classe": "large"},
        {"src": "website/img/amelia11.webp", "alt": "Foto 11", "classe": "large"},
        {"src": "website/img/amelia12.webp", "alt": "Foto 12", "classe": "small"},
        {"src": "website/img/amelia13.webp", "alt": "Foto 13", "classe": "medium"},
        {"src": "website/img/amelia14.webp", "alt": "Foto 14", "classe": "small"},
        {"src": "website/img/amelia15.webp", "alt": "Foto 15", "classe": "small"},
        ]
    }
]

# VIEW INDEX (página inicial)
def index(request):
    context = {
        "elenco": elenco_completo,
        "slides": chunk_list(elenco_completo, 3),
    }
    return render(request, "website/index.html", context)

# VIEW SOBRE
def sobre(request):
    return render(request, "website/sobre.html")

# VIEW DETALHE DE UM ATOR
def elenco(request, id_post):
    ator = elenco_completo[id_post - 1]

    imagens = []
    for foto in ator.get("imagens", []):  # Corrigido aqui de "galeria" para "imagens"
        imagens.append({
            "src": foto["src"],
            "alt": ator["nome"],
            "classe": foto["classe"],  # também mudou o nome para 'classe' no seu dicionário
        })

    contexto = {
        "ator": ator,
        "imagens": imagens,
    }
    return render(request, "website/elenco.html", contexto)


# VIEW LISTA COMPLETA DO ELENCO
def elenco_list(request):
    context = {
        "elenco": elenco_completo,
    }
    return render(request, "website/elenco_list.html", context)

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
        "imagem": ""
    },
    {
        "id": 2,
        "nome": "Mark Sloan",
        "ator": "Eric Dane",
        "especialidade": "Cirurgia plástica",
        "apelido": "McSteamy",
        "descricao": """
Mark Sloan, apelidado de "McSteamy", é um cirurgião plástico famoso por sua habilidade técnica e personalidade extrovertida. Ele é conhecido por seu charme irresistível e relacionamentos amorosos complicados, que muitas vezes trazem tensão para o ambiente hospitalar. Apesar do seu lado mulherengo, Mark é profundamente dedicado ao seu trabalho e aos seus pacientes, sempre buscando os melhores resultados estéticos e funcionais. Sua história na série envolve redenção, amizade e momentos de vulnerabilidade que humanizam o personagem.""",
        "imagem": ""
    },
    {
        "id": 3,
        "nome": "Meredith Grey",
        "ator": "Ellen Pompeo",
        "especialidade": "Cirurgia geral",
        "apelido": "Mer",
        "descricao": """
Meredith Grey é a protagonista central da série, uma cirurgiã geral cuja trajetória é marcada por desafios pessoais e profissionais. Filha de uma renomada cirurgiã, Meredith luta para se destacar e encontrar sua própria identidade dentro do hospital Seattle Grace. Sua vida é permeada por altos e baixos emocionais, relacionamentos complexos e a constante pressão da medicina de emergência. Ao longo da série, Meredith evolui, tornando-se uma médica brilhante e uma mulher resiliente, que enfrenta perdas e conquistas com coragem.""",
        "imagem": ""
    },
    {
        "id": 4,
        "nome": "Lexie Grey",
        "ator": "Chyler Leigh",
        "especialidade": "Cirurgia geral",
        "apelido": "Lexie",
        "descricao": """
Lexie Grey é a irmã mais nova de Meredith e também cirurgiã geral. Conhecida por sua inteligência aguçada e memória fotográfica, Lexie traz uma combinação de vulnerabilidade e determinação para sua carreira médica. Ela luta para provar seu valor em um ambiente competitivo e para manter relacionamentos significativos, especialmente com colegas e familiares. Lexie é uma personagem sensível que passa por crescimento pessoal e profissional, deixando uma marca importante na série.""",
        "imagem": ""
    },
    {
        "id": 5,
        "nome": "Cristina Yang",
        "ator": "Sandra Oh",
        "especialidade": "Cirurgia cardiotorácica",
        "apelido": "Yang",
        "descricao": """
Cristina Yang é uma cirurgiã cardiotorácica brilhante e ambiciosa, conhecida por sua dedicação extrema à carreira e sua personalidade direta e muitas vezes impetuosa. Sua amizade profunda com Meredith Grey é um dos pilares emocionais da série, mostrando um relacionamento intenso e cheio de apoio mútuo. Cristina enfrenta desafios pessoais e profissionais, buscando sempre ser a melhor em sua área, mesmo que isso custe relacionamentos e conforto pessoal. Sua jornada destaca temas de empoderamento, ética médica e auto-descoberta.""",
        "imagem": ""
    },
    {
        "id": 6,
        "nome": "Callie Torres",
        "ator": "Sara Ramirez",
        "especialidade": "Ortopedia",
        "apelido": "Callie",
        "descricao": """
Callie Torres é uma cirurgiã ortopédica talentosa, que traz para a série uma forte presença feminina e diversidade. Sua personalidade vibrante e às vezes impulsiva contrasta com seu profissionalismo e cuidado com os pacientes. Ao longo da série, Callie enfrenta vários desafios pessoais, incluindo relacionamentos complexos e questões de identidade. Ela é uma personagem que demonstra crescimento, vulnerabilidade e força, contribuindo para a representação de temas sociais relevantes na narrativa.""",
        "imagem": ""
    },
    {
        "id": 7,
        "nome": "Miranda Bailey",
        "ator": "Chandra Wilson",
        "especialidade": "Cirurgia geral",
        "apelido": "Nazi",
        "descricao": """
Miranda Bailey é uma cirurgiã geral rigorosa, reconhecida pelo seu alto padrão profissional e por sua capacidade de liderança dentro do hospital. Embora inicialmente receba o apelido “Nazi” devido ao seu estilo autoritário, ao longo da série sua humanidade, cuidado e dedicação à formação dos residentes são evidentes. Bailey é um exemplo de força feminina na medicina, enfrentando desafios pessoais e profissionais e mantendo-se uma figura respeitada e admirada.""",
        "imagem": ""
    },
    {
        "id": 8,
        "nome": "Jo Wilson",
        "ator": "Camilla Luddington",
        "especialidade": "Cirurgia geral",
        "apelido": "Jo",
        "descricao": """
Jo Wilson é uma cirurgiã geral que enfrenta uma trajetória marcada por dificuldades pessoais e superação. Sua história inclui um passado difícil, que impacta suas relações e sua confiança, mas também a motiva a buscar excelência na medicina. Jo é uma personagem complexa, mostrando vulnerabilidade e força, e sua jornada aborda temas como resiliência, identidade e amor.""",
        "imagem": ""
    },
    {
        "id": 9,
        "nome": "Addison Montgomery",
        "ator": "Kate Walsh",
        "especialidade": "Obstetrícia e ginecologia / Neonatologia",
        "apelido": "Addison",
        "descricao": """
Addison Montgomery é uma especialista em obstetrícia, ginecologia e neonatologia, reconhecida por sua competência e estilo sofisticado. Sua personalidade forte e às vezes difícil cria tensões e alianças dentro do hospital. Addison traz para a série temas ligados à medicina feminina e às complexidades das relações pessoais, equilibrando carreira e vida afetiva em sua trajetória.""",
        "imagem": ""
    },
    {
        "id": 10,
        "nome": "Jackson Avery",
        "ator": "Jesse Williams",
        "especialidade": "Cirurgia plástica",
        "apelido": "Avery",
        "descricao": """
Jackson Avery é um cirurgião plástico talentoso, membro de uma família renomada na medicina. Sua busca por reconhecimento profissional e pessoal o impulsiona a desafios constantes, enquanto ele navega por complexos relacionamentos amorosos e dinâmicas familiares. Avery é conhecido por sua ética de trabalho, carisma e capacidade de inovação na área cirúrgica.""",
        "imagem": ""
    },
    {
        "id": 11,
        "nome": "Amelia Shepherd",
        "ator": "Caterina Scorsone",
        "especialidade": "Neurocirurgia",
        "apelido": "Furacão Amelia",
        "descricao": """
Amelia Shepherd é uma neurocirurgiã talentosa e irmã de Derek Shepherd. Conhecida por sua personalidade forte e espírito independente, Amelia enfrenta batalhas pessoais, incluindo vícios e perdas, que marcam sua trajetória. Apesar das dificuldades, ela se destaca como uma médica excepcional, com uma paixão pela cirurgia e um compromisso profundo com seus pacientes.""",
        "imagem": ""
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
    contexto = {
        "ator": elenco_completo[id_post - 1]
    }
    return render(request, "website/elenco.html", contexto)

# VIEW LISTA COMPLETA DO ELENCO
def elenco_list(request):
    context = {
        "elenco": elenco_completo,
    }
    return render(request, "website/elenco_list.html", context)

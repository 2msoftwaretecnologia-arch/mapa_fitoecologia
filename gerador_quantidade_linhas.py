import pyautogui
import keyboard
import time
#1118,1044
#1232,1047


def clicar_centro_tela(quantidade=1,tempo=0.25):
    for _ in range(quantidade):
        pyautogui.click(pyautogui.size()[0]//2,pyautogui.size()[1]//2,duration=0.25)
        time.sleep(tempo)
def apertar_Tab(quantidade=1,tempo_espera=0.3):
    """Pressiona a tecla Tab."""
    for _ in range(quantidade):
        pyautogui.press('tab')
        time.sleep(tempo_espera)
def ctrl_L(quantidade=1,tempo_espera=0.1):
    """Pressiona a tecla Tab."""
    for _ in range(quantidade):
        pyautogui.hotkey('ctrl','l')
        time.sleep(tempo_espera)
tamanhos_regioes_fito_ecologias = {
    "Floresta Estacional": {
        "1 time": {"descricao":"A floresta estacional é uma formação vegetal típica de regiões de clima tropical e subtropical, caracterizada pela alternância entre períodos chuvosos e secos. Essa sazonalidade influencia diretamente a vegetação, que desenvolve adaptações para suportar a escassez de água. Durante a estação seca, muitas árvores perdem suas folhas como estratégia para reduzir a perda hídrica. Essa dinâmica transforma a paisagem ao longo do ano, conferindo à floresta um aspecto bastante distinto e sazonal. A biodiversidade dessas florestas é significativa, abrigando inúmeras espécies de fauna e flora, algumas endêmicas e outras comuns a diferentes biomas. No Brasil, esse tipo de vegetação é encontrado em áreas da Mata Atlântica e do Cerrado, formando mosaicos de grande importância ecológica. Além disso, desempenha funções ambientais essenciais, como a regulação do clima, a proteção dos solos contra a erosão e a conservação de recursos hídricos. No entanto, sofre intensa pressão devido ao desmatamento, à expansão agrícola e à urbanização, ameaçando a manutenção de seus ecossistemas e a sobrevivência de diversas espécies.",
                  "borda":"6,5","numero_linhas":19},
        "2 time": {"descricao":"A floresta estacional é uma formação vegetal típica de regiões de clima tropical e subtropical, caracterizada pela alternância entre períodos chuvosos e secos. Influenciando diretamente a vegetação, que desenvolve adaptações para suportar a escassez de água. Durante a estação seca, muitas árvores perdem suas folhas como estratégia para reduzir a perda hídrica. Essa dinâmica transforma a paisagem ao longo do ano, conferindo à floresta um aspecto bastante distinto e sazonal. A biodiversidade dessas florestas é significativa, abrigando inúmeras espécies de fauna e flora, algumas endêmicas e outras comuns a diferentes biomas.",
                    "borda":"6","numero_linhas":10},
        "3 time": {"descricao":"A floresta estacional é uma formação vegetal típica de regiões de clima tropical e subtropical, caracterizada pela alternância entre períodos chuvosos e secos. Influenciando diretamente a vegetação, que desenvolve adaptações para suportar a escassez de água. Durante a estação seca, muitas árvores perdem suas folhas como estratégia para reduzir a perda hídrica. No entanto, sofre intensa pressão devido ao desmatamento, à expansão agrícola e à urbanização",
                    "borda":"5,75","numero_linhas":8},
        "4 time": {"descricao":"A floresta estacional é uma formação vegetal típica de regiões de clima tropical e subtropical, caracterizada por alternar entre períodos chuvosos e secos, desenvolvendo adaptações para suportar a escassez de água. A perca de folhas durante a estação seca ao longo do ano confere à floresta um aspecto sazonal.",
                    "borda":"6,25","numero_linhas":5}
    },
    "Floresta Ombrófila Aberta": {
        "1 time": {"descricao":"A Floresta Ombrófila Aberta, também conhecida como floresta tropical úmida aberta, é um tipo de vegetação caracterizada por árvores de grande porte com copas espaçadas, permitindo maior entrada de luz no solo. Esse ambiente favorece o desenvolvimento de arbustos, trepadeiras e uma diversidade significativa de espécies herbáceas. Predomina em regiões de clima quente e úmido, com chuvas bem distribuídas ao longo do ano, sendo comum em áreas do Sudeste e Sul do Brasil. Essa floresta apresenta alta biodiversidade, abrigando inúmeras espécies de fauna e flora, muitas delas endêmicas. A estrutura aberta da vegetação possibilita nichos variados, favorecendo interações ecológicas complexas e a manutenção de ciclos biológicos diversos. Além disso, desempenha funções ecológicas essenciais, como regulação do clima, conservação do solo e dos recursos hídricos, e absorção de carbono, contribuindo para a mitigação das mudanças climáticas. No entanto, enfrenta pressões intensas devido ao desmatamento, expansão agrícola e ocupação urbana, que ameaçam sua integridade e a sobrevivência de espécies dependentes desse ecossistema.",
                  "borda":"6,5","numero_linhas":20},
        "2 time": {"descricao":"A Floresta Ombrófila Aberta, também conhecida como floresta tropical úmida aberta, é um tipo de vegetação caracterizada por árvores de grande porte com copas espaçadas, permitindo maior entrada de luz no solo. Esse ambiente favorece o desenvolvimento de arbustos, trepadeiras e uma diversidade significativa de espécies herbáceas. Predomina em regiões de clima quente e úmido, com chuvas bem distribuídas ao longo do ano, sendo comum em áreas do Sudeste e Sul do Brasil. A estrutura aberta da vegetação possibilita nichos variados, favorecendo interações ecológicas complexas e a manutenção de ciclos biológicos diversos.",
                    "borda":"6","numero_linhas":11},
        "3 time": {"descricao":"A Floresta Ombrófila Aberta, também conhecida como floresta tropical úmida aberta, é um tipo de vegetação caracterizada por árvores de grande porte com copas espaçadas, permitindo maior entrada de luz no solo, favorecendo o desenvolvimento de arbustos, trepadeiras e uma diversidade significativa de espécies herbáceas. Predomina em regiões de clima quente e úmido, com chuvas bem distribuídas ao longo do ano, sendo comum em áreas do Sudeste e Sul do Brasil. ",
                    "borda":"5,75","numero_linhas":8},
        "4 time": {"descricao":"A Floresta Ombrófila Aberta, conhecida como floresta tropical úmida aberta, é um tipo de vegetação caracterizada por árvores de grande porte com copas espaçadas, permitindo maior entrada de luz no solo, favorecendo o desenvolvimento de arbustos, trepadeiras e uma diversidade significativa de espécies herbáceas.",
                    "borda":"6,25","numero_linhas":6}
    },
    "Floresta Ombrófila Densa": {
        "1 time": {"descricao":"A Floresta Ombrófila Densa, também chamada de floresta tropical úmida fechada, é caracterizada por árvores de grande porte, copas contínuas e elevada densidade arbórea, o que gera sombra intensa e um microclima úmido em seu interior. Esse tipo de floresta é típico de regiões com alta pluviosidade anual, clima quente e constante umidade, sendo predominante na Amazônia e em partes da Mata Atlântica. Sua biodiversidade é extremamente rica, abrigando milhares de espécies de plantas, animais e microorganismos, muitos endêmicos. A complexidade estrutural da vegetação cria múltiplos estratos, favorecendo interações ecológicas diversas e a manutenção de ciclos naturais essenciais, como polinização, dispersão de sementes e reciclagem de nutrientes. Além disso, a floresta desempenha funções ambientais vitais, como regulação do clima, proteção do solo, preservação de recursos hídricos e absorção de carbono, contribuindo para o equilíbrio ecológico. Apesar de sua importância, enfrenta ameaças significativas pela exploração madeireira e expansão urbana, que comprometem a conservação de espécies e a integridade do ecossistema.",
                  "borda":"6,5","numero_linhas":20},
        "2 time": {"descricao":"A Floresta Ombrófila Densa, também chamada de floresta tropical úmida fechada, é caracterizada por árvores de grande porte, copas contínuas e elevada densidade arbórea, o que gera sombra intensa e um microclima úmido em seu interior. Esse tipo de floresta é típico de regiões com alta pluviosidade anual, clima quente e constante umidade, sendo predominante na Amazônia e em partes da Mata Atlântica. Sua biodiversidade é extremamente rica, abrigando milhares de espécies de plantas, e animais, muitos endêmicos. A complexidade estrutural da vegetação cria múltiplos estratos, favorecendo interações ecológicas diversas" ,
                    "borda":"6","numero_linhas":10},
        "3 time": {"descricao":"A Floresta Ombrófila Densa, chamada de floresta tropical úmida fechada, é caracterizada por árvores de grande porte e elevada densidade arbórea, o que gera sombra intensa e um microclima úmido em seu interior. Esse tipo de floresta é típico de regiões com alta pluviosidade anual, clima quente e constante umidade, principalmente na Amazônia e em partes da Mata Atlântica. Sua biodiversidade é muito rica, abrigando milhares de espécies de plantas e animais",
                    "borda":"5,75","numero_linhas":8},
        "4 time": {"descricao":"A Floresta Ombrófila Densa, chamada de floresta tropical úmida fechada, é caracterizada por árvores de grande porte e elevada densidade arbórea, o que gera sombra intensa e um microclima úmido em seu interior. Esse tipo de floresta é típico de regiões com alta pluviosidade anual, clima quente e constante umidade",
                    "borda":"6,25","numero_linhas":5}
    },
    "Savana Gramíneo Lenhosa": {
        "1 time": {"descricao":"Fitofisionomia aberta do bioma Cerrado, caracterizada pela predominância de uma extensa e densa camada herbácea, composta majoritariamente por gramíneas nativas. Essa vegetação rasteira é intercalada por arbustos e subarbustos lenhosos esparsos, geralmente com altura inferior a 2 metros. Árvores são muito raras ou completamente ausentes, o que reforça o caráter campestre dessa formação. Ocorre principalmente em áreas com solos rasos, ácidos, pedregosos ou de baixa fertilidade, o que limita o desenvolvimento de vegetação arbórea mais robusta. Essa paisagem é altamente adaptada à ocorrência periódica de fogo natural — as gramíneas, por exemplo, possuem elevada capacidade de rebrote após incêndios, o que contribui para a resiliência ecológica do ambiente. A biodiversidade, embora menos visível, é notável especialmente no estrato rasteiro, onde há grande variedade de insetos, pequenos roedores, répteis e outras formas de vida adaptadas ao microclima do solo. Esta fitofisionomia desempenha papel fundamental na formação de pastagens nativas e no suporte à pecuária extensiva tradicional, mas encontra-se ameaçada pela invasão de gramíneas exóticas africanas, que alteram a dinâmica ecológica, e pela crescente conversão do solo para a agricultura mecanizada.",
                    "borda":"6,5","numero_linhas":22},
        "2 time": {"descricao":"Fitofisionomia aberta do bioma Cerrado, caracterizada principalmente por uma extensa e densa camada herbácea, composta majoritariamente por gramíneas nativas. Essa vegetação rasteira é intercalada por arbustos e subarbustos lenhosos esparsos, geralmente com altura inferior a 2 metros. Árvores são muito raras ou completamente ausentes, o que reforça o caráter campestre dessa formação. Ocorre principalmente em áreas com solos rasos, ácidos ou de baixa fertilidade, o que limita o desenvolvimento de vegetação arbórea mais robusta. Essa paisagem é altamente adaptada à ocorrência periódica de fogo natural, as gramíneas, por exemplo, possuem elevada capacidade de rebrote após incêndios, o que contribui para a resiliência ecológica do ambiente. A biodiversidade, é notada especialmente no estrato rasteiro, onde há grande variedade de insetos, pequenos roedores, répteis e outras formas de vida adaptadas ao microclima do solo. Esta fitofisionomia desempenha papel fundamental na formação de pastagens nativas e no suporte à pecuária extensiva tradicional, mas encontra-se ameaçada pela invasão de gramíneas exóticas africanas",
                    "borda":"6","numero_linhas":20},
        "3 time": {"descricao":"Fitofisionomia aberta do bioma Cerrado, caracterizada principalmente por uma extensa e densa camada herbácea, composta em maioria por gramíneas nativas. Essa vegetação rasteira é revezada em arbustos e subarbustos lenhosos esparsos. Árvores são muito raras ou mesmo ausentes, o que reforça o caráter campestre. Ocorre principalmente em áreas com solos rasos, ácidos ou de baixa fertilidade, o que limita o desenvolvimento de vegetação arbórea mais robusta.",
                    "borda":"5,75","numero_linhas":8},
        "4 time": {"descricao":"Fitofisionomia aberta do bioma Cerrado, caracterizada principalmente por uma extensa e densa camada herbácea, composta em maioria por gramíneas nativas. Essa vegetação rasteira é revezada em arbustos e subarbustos lenhosos esparsos. Árvores são muito raras ou mesmo ausentes, o que reforça o caráter campestre.",
                    "borda":"6,25","numero_linhas":6}
    },
    "Savana Arborizada/Arbórea": {
        "1 time": {"descricao":"Trata-se da savana arborizada típica e mais representativa do bioma Cerrado, conhecida como sua fitofisionomia clássica. É caracterizada por um estrato herbáceo-arbustivo contínuo, dominado por gramíneas nativas e pequenos arbustos. Acima desse estrato, desenvolve-se um componente arbóreo descontínuo, composto por árvores espaçadas, retorcidas, com alturas variando entre 3 e 8 metros e copas irregulares. A cobertura arbórea é intermediária, o que permite significativa entrada de luz até o sub-bosque. As árvores apresentam adaptações marcantes às condições ambientais restritivas: casca espessa e corticosa, resistência ao fogo natural e raízes profundas que lhes permitem acessar a umidade em solos ácidos e de baixa fertilidade. Essa estrutura complexa sustenta uma biodiversidade extremamente alta, com destaque para a flora adaptada e uma diversidade notável de insetos, fundamentais para a polinização e o equilíbrio ecológico. É considerada o núcleo ecológico do Cerrado e ocupa a maior parte da área do bioma. No entanto, essa fitofisionomia é a mais afetada pela expansão agrícola e pela intensificação da pecuária.",
                    "borda":"6,5","numero_linhas":20},
        "2 time": {"descricao":"Trata-se da savana arborizada típica e mais representativa do bioma Cerrado, conhecida como sua fitofisionomia clássica. É caracterizada por um estrato herbáceo-arbustivo contínuo, dominado por gramíneas nativas e pequenos arbustos. Acima desse estrato, desenvolve-se um componente arbóreo descontínuo, composto por árvores espaçadas e retorcidas. A cobertura arbórea é mediana, o que permite entrada de luz até o sub-bosque. As árvores apresentam adaptações marcantes às condições ambientais restritivas: casca espessa e corticosa e raízes profundas que lhes permitem acessar a umidade em solos ácidos e de baixa fertilidade. ",
                    "borda":"6","numero_linhas":11},
        "3 time": {"descricao":"Trata-se da savana arborizada típica e mais representativa do bioma Cerrado, conhecida como sua fitofisionomia clássica. É caracterizada por um estrato herbáceo-arbustivo contínuo, dominado por gramíneas nativas e pequenos arbustos, que cobre o solo de forma densa. Acima desse estrato, desenvolve-se um componente arbóreo descontínuo, composto por árvores espaçadas, retorcidas, com alturas variando entre 3 e 8 metros e copas irregulares.",
                    "borda":"5,75","numero_linhas":8},
        "4 time": {"descricao":"Trata-se da savana arborizada típica e mais representativa do bioma Cerrado, conhecida como sua fitofisionomia clássica. É caracterizada por um estrato herbáceo-arbustivo contínuo, dominado por gramíneas nativas e pequenos arbustos, que cobre o solo de forma densa.",
                    "borda":"6,25","numero_linhas":5}
    },
    "Savana Florestada": {
        "1 time": {"descricao":"Essa fitofisionomia representa uma zona de transição ecológica entre o Cerrado stricto sensu e as formações florestais adjacentes, como matas de galeria ou florestas estacionais. Caracteriza-se por um dossel mais fechado do que nas savanas típicas, com cobertura arbórea variando entre 50% e 90%, formada por árvores com altura média entre 8 e 15 metros. Apesar desse aspecto mais florestal, o sub-bosque ainda mantém elementos típicos das savanas, com presença significativa de gramíneas e arbustos lenhosos, criando um ambiente híbrido. Os solos são semelhantes aos do Cerrado típico — ácidos, com baixa fertilidade —, embora essa fitofisionomia ocorra preferencialmente em áreas com solos um pouco mais profundos. Ao contrário das formações savânicas mais abertas, sua vegetação é menos adaptada ao fogo, sendo mais suscetível a danos por queimadas frequentes. A biodiversidade é mista e rica, abrigando espécies tanto do Cerrado quanto de formações florestais, o que confere alto valor ecológico às suas manchas de vegetação. Com distribuição em mosaico, geralmente formando manchas irregulares dentro da paisagem cerratense",
                    "borda":"6,5","numero_linhas":20},
        "2 time": {"descricao":"Essa fitofisionomia representa uma zona de transição ecológica entre o Cerrado stricto sensu e as formações florestais adjacentes, como matas de galeria ou florestas estacionais. Caracteriza-se por um dossel mais fechado do que nas savanas típicas, com cobertura arbórea variando entre 50% e 90%, formada por árvores com altura média entre 8 e 15 metros. Apesar desse aspecto mais florestal, o sub-bosque ainda mantém elementos típicos das savanas, com presença significativa de gramíneas e arbustos lenhosos, criando um ambiente híbrido. Os solos são semelhantes aos do Cerrado típico.",
                    "borda":"6","numero_linhas":10},
        "3 time": {"descricao":"Essa fitofisionomia representa uma zona de transição ecológica entre o Cerrado stricto sensu e as formações florestais adjacentes, como matas de galeria ou florestas estacionais. Caracteriza-se por um dossel mais fechado do que nas savanas típicas, com cobertura arbórea variando entre 50% e 90%, formada por árvores com altura média entre 8 e 15 metros. Apesar desse aspecto mais florestal, o sub-bosque ainda mantém elementos típicos das savanas.",
                    "borda":"5,75","numero_linhas":7},
        "4 time": {"descricao":"Essa fitofisionomia representa uma zona de transição ecológica entre o Cerrado stricto sensu e as formações florestais adjacentes, como matas de galeria ou florestas estacionais. Caracteriza-se por um dossel mais fechado do que nas savanas típicas.",
                    "borda":"6,25","numero_linhas":5}
    },
    "Savana Parque": {
        "1 time": {"descricao":"Fitofisionomia úmida típica do bioma Cerrado, conhecida por sua forte associação a ambientes com solos hidromórficos — constantemente encharcados devido à proximidade do lençol freático ou à presença de nascentes. Essa formação vegetacional é marcada por agrupamentos densos da palmeira buriti (Mauritia flexuosa), que se destacam visualmente na paisagem por sua altura, podendo ultrapassar os 15 metros, e por emergirem sobre um estrato herbáceo contínuo, formado principalmente por gramíneas e ciperáceas adaptadas à saturação hídrica. Os buritizais ocorrem preferencialmente ao longo de vales úmidos e margens de cursos d'água, formando verdadeiros corredores ecológicos que desempenham papel essencial na conservação dos recursos hídricos — atuando como áreas de recarga e proteção de nascentes — e como refúgio para a fauna durante os períodos de seca. A biodiversidade é especializada e restrita a espécies adaptadas às condições úmidas, tanto da flora quanto da fauna, incluindo aves, anfíbios e insetos endêmicos desses ambientes. No entanto, trata-se de uma das fitofisionomias mais sensíveis à ação antrópica",
                    "borda":"6,5","numero_linhas":20},
        "2 time": {"descricao":"Fitofisionomia úmida típica do bioma Cerrado, conhecida por sua forte associação a ambientes com solos hidromórficos — constantemente encharcados devido à proximidade do lençol freático ou à presença de nascentes. Essa formação vegetacional é marcada por agrupamentos densos da palmeira buriti (Mauritia flexuosa), que se destacam visualmente na paisagem por sua altura, podendo ultrapassar os 15 metros, e por emergirem sobre um estrato herbáceo contínuo, formado principalmente por gramíneas e ciperáceas adaptadas à saturação hídrica. Os buritizais ocorrem preferencialmente ao longo de vales úmidos e margens de cursos d'água.",
                    "borda":"6","numero_linhas":11},
        "3 time": {"descricao":"Fitofisionomia úmida típica do bioma Cerrado, conhecida por sua forte associação a ambientes com solos hidromórficos — constantemente encharcados devido à proximidade do lençol freático ou à presença de nascentes. Essa formação vegetacional é marcada por agrupamentos densos da palmeira buriti (Mauritia flexuosa), que se destacam visualmente na paisagem por sua altura, podendo ultrapassar os 15 metros, e por emergirem sobre um estrato herbáceo contínuo.",
                    "borda":"5,75","numero_linhas":8},
        "4 time": {"descricao":"Fitofisionomia úmida típica do bioma Cerrado, conhecida por sua forte associação a ambientes com solos hidromórficos constantemente encharcados devido à proximidade do lençol freático ou à presença de nascentes.",
                    "borda":"6,25","numero_linhas":4}
    },
    "Rio": {
        "1 time": {"descricao":"Embora os rios não sejam considerados uma fitofisionomia terrestre propriamente dita, eles desempenham um papel estruturante e essencial na organização da paisagem natural. Estão sempre acompanhados por vegetação ripária especializada como as matas ciliares ou florestas de galeria, que se desenvolvem ao longo de suas margens, adaptadas às condições de alta umidade do solo e às inundações periódicas. Essas matas formam corredores ecológicos contínuos, cruciais para a conectividade entre diferentes ecossistemas, facilitando o deslocamento da fauna, a dispersão de sementes e o fluxo genético entre populações. A vegetação ripária abriga uma biodiversidade única, com espécies vegetais e animais que dependem diretamente desse ambiente de transição entre o terrestre e o aquático."
                    ,"borda":"6,5","numero_linhas":14},
        "2 time": {"descricao":"Embora os rios não sejam considerados uma fitofisionomia terrestre propriamente dita, eles desempenham um papel estruturante e essencial na organização da paisagem natural. Estão sempre acompanhados por vegetação ripária especializada como as matas ciliares ou florestas de galeria, que se desenvolvem ao longo de suas margens, adaptadas às condições de alta umidade do solo e às inundações periódicas. Essas matas formam corredores ecológicos contínuos, cruciais para a conectividade entre diferentes ecossistemas.",
                    "borda":"6","numero_linhas":9},
        "3 time": {"descricao":"Embora os rios não sejam considerados uma fitofisionomia terrestre propriamente dita, eles desempenham um papel estruturante e essencial na organização da paisagem natural. Estão sempre acompanhados por vegetação ripária especializada como as matas ciliares ou florestas de galeria, que se desenvolvem ao longo de suas margens, adaptadas às condições de alta umidade do solo e às inundações periódicas.",
                    "borda":"5,75","numero_linhas":7},
        "4 time": {"descricao":"Embora os rios não sejam considerados uma fitofisionomia terrestre propriamente dita, eles desempenham um papel estruturante e essencial na organização da paisagem natural. Estão sempre acompanhados por vegetação ripária especializada como as matas ciliares ou florestas de galeria.",
                    "borda":"6,25","numero_linhas":5}
    }
}
pyautogui.click(1232,1047,interval=0.1) 
# Estrutura para imprimir todos os textos em sequência
contagem = 1
for regiao_nome, regiao_dados in tamanhos_regioes_fito_ecologias.items():
    
    for tamanho in ["1 time", "2 time", "3 time", "4 time"]:
        if tamanho in regiao_dados:
            
            texto = regiao_dados[tamanho]["descricao"]
            borda = regiao_dados[tamanho]["borda"]
            clicar_centro_tela()
            pyautogui.hotkey("ctrl","t")
            ctrl_L(tempo_espera=0.3)
            apertar_Tab(3,0.1)
            keyboard.write(borda,delay=0.001)
            pyautogui.press('enter')
            time.sleep(0.4)
            keyboard.write(texto,delay=0.001)
            quantidade =  pyautogui.prompt("quantidade de linhas")
            pyautogui.click(1118,1044,interval=0.1)
            time.sleep(0.4)
            clicar_centro_tela()
            pyautogui.hotkey("ctrl","h")
            time.sleep(0.3)
            keyboard.write(f'"random{contagem}"',delay=0.01)
            apertar_Tab(tempo_espera=0.1)
            pyautogui.hotkey("ctrl","a")
            time.sleep(0.3)
            keyboard.write(f'{str(quantidade)}',delay=0.01)
            time.sleep(0.3)
            pyautogui.press('enter')
            time.sleep(0.3)
            pyautogui.press('esc')
            time.sleep(0.3)
            pyautogui.click(1232,1047,interval=0.1) 
            contagem+=1
                                    
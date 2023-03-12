from functools import partial

import toga
from toga.style import Pack
from toga.style.pack import COLUMN, ROW
import random


t_5charS = ['sagaz', 'amago', 'negro', 'exito', 'mexer', 'termo', 'nobre', 'senso', 'algoz', 'afeto', 'etica', 'plena', 'mutua', 'tenue', 'sutil', 'fazer', 'vigor', 'aquem', 'assim', 'porem', 'secao', 'audaz', 'sanar', 'fosse', 'cerne', 'inato', 'ideia', 'poder', 'moral', 'desde', 'justo', 'muito', 'sobre', 'torpe', 'honra', 'quica', 'futil', 'razao', 'anexo', 'etnia', 'icone', 'sonho', 'egide',
            'tange', 'amigo', 'lapso', 'mutuo', 'expor', 'haver', 'casal', 'habil', 'dengo', 'tempo', 'seara', 'entao', 'avido', 'pesar', 'bocal', 'ardil', 'genro', 'posse', 'causa', 'paria', 'coser', 'dizer', 'corja', 'prole', 'saber', 'dever', 'graca', 'obice', 'brado', 'tenaz', 'crivo', 'detem', 'animo', 'apice', 'comum', 'digno', 'ansia', 'temor', 'sendo', 'ceder', 'culto', 'assaz', 'atroz',
            'pauta', 'gleba', 'ainda', 'mundo', 'fugaz', 'censo', 'estar', 'valha', 'vicio', 'forte', 'cozer', 'vulgo', 'nenem', 'denso', 'reves', '\n', 'xibiu', 'pudor', 'regra', 'dogma', 'louco', 'criar', 'banal', 'saude', 'round', 'jeito', 'atras', 'clava', 'impor', 'ordem', 'merce', 'pedir', 'tenro', 'apraz', 'pifio', 'desse', 'feliz', 'usura', 'mesmo', 'homem', 'servo', 'reaca', 'sabio',
            'juizo', 'coisa', 'prosa', 'viril', 'presa', 'ontem', 'cunho', 'forma', 'limbo', 'manso', 'falar', 'devir', 'meiga', 'posso', 'fluir', 'afago', 'vendo', 'ebrio', 'plato', 'serio', 'magoa', 'guisa', 'heroi', 'todos', 'puder', 'visar', 'acaso', 'valor', 'certo', 'temer', 'pleno', 'impio', 'cisma', 'lugar', 'afins', 'bruma', 'obvio', 'gerar', 'exodo', 'obter', 'falso', 'crise', 'matiz',
            'abrir', 'praxe', 'garbo', 'senil', 'fluxo', 'havia', 'venia', 'enfim', 'facil', 'tedio', 'legal', 'uniao', 'ritmo', 'burro', 'alibi', 'tomar', 'visao', 'pulha', 'parvo', 'bravo', 'valia', 'reter', 'vital', 'favor', 'olhar', 'genio', 'prumo', 'grato', 'levar', 'parco', 'vivaz', 'casta', 'laico', 'reles', 'morte', 'possa', 'ameno', 'tecer', 'linda', 'obito', 'brega', 'prime', 'ranco',
            'nocao', 'falta', 'sabia', 'selar', 'cabal', 'ajuda', 'facam', 'fator', 'nicho', 'anelo', 'noite', 'achar', 'farsa', 'rogar', 'ouvir', 'viver', 'coeso', 'citar', 'forca', 'epico', 'fardo', 'adiar', 'cisao', 'ativo', 'sinto', 'carma', 'calma', 'passo', 'unico', 'tendo', 'dubio', 'leigo', 'sonso', 'gente', 'haste', 'outro', 'pobre', 'exato', 'rever', 'sesta', 'amplo', 'cesta', 'revel',
            'deter', 'sulco', 'humor', 'imune', 'vemos', 'lavra', 'tende', 'labor', 'arduo', 'ciume', 'gesto', 'atuar', 'velho', 'feixe', 'claro', 'igual', 'ponto', 'ideal', 'otica', 'hiato', 'debil', 'sonsa', 'toada', 'terra', 'terno', 'vacuo', 'ambos', 'varao', 'marco', 'remir', 'cauda', 'fonte', 'senao', 'lider', 'capaz', 'jovem', 'fusao', 'inata', 'ficar', 'probo', 'leito', 'horda', 'advem',
            'tenra', 'velar', 'farao', 'doido', 'xeque', 'cocar', 'algum', 'relva', 'vazio', 'serie', 'apoio', 'tanto', 'cacar', 'papel', 'entre', 'pouco', 'vimos', 'sente', 'anuir', 'raiva', 'frase', 'coesa', 'torco', 'rigor', 'botar', 'verso', 'dorso', 'signo', 'cruel', 'feito', 'massa', 'minha', 'mocao', 'prece', 'brisa', 'impar', 'credo', 'nossa', 'covil', 'preso', 'casto', 'fauna', 'ambas',
            'ciclo', 'blase', 'chata', 'morar', 'lazer', 'peste', 'virus', 'furor', 'trama', 'docil', 'faina', 'maior', 'flora', 'pegar', 'arido', 'adeus', 'vetor', 'chuva', 'houve', 'beata', 'setor', 'seita', 'manha', 'meses', 'liame', 'aceso', 'banzo', 'sorte', 'senda', 'livro', 'vulto', 'pecha', 'carro', 'ardor', 'salvo', 'breve', 'visse', 'vasto', 'peixe', 'birra', 'comer', 'plano', 'antro',
            'morro', 'saiba', 'ocaso', 'nunca', 'prado', 'reger', 'alias', 'pajem', 'rezar', 'atomo', 'segue', 'avaro', 'saida', 'otimo', 'junto', 'mudar', 'aureo', 'chulo', 'sinal', 'serao', 'acima', 'lenda', 'grupo', 'opcao', 'parar', 'treta', 'fruir', 'fugir', 'ancia', 'jazia', 'andar', 'brava', 'fitar', 'nacao', 'parte', 'campo', 'leite', 'prazo', 'puxar', 'rapaz', 'bando', 'gerir', 'tenso',
            'tosco', 'alude', 'norma', 'praia', 'motim', 'idolo', 'epoca', 'risco', 'anais', 'agora', 'exame', 'vilao', 'sinha', 'tirar', 'malta', 'arcar', 'reino', 'antes', 'psico', 'aviao', 'praga', 'venal', 'indio', 'aurea', 'quota', 'aonde', 'soldo', 'corpo', 'preto', 'texto', 'traga', 'logro', 'quase', 'cheio', 'voraz', 'sumir', 'certa', 'filho', 'conta', 'fixar', 'pompa', 'turba', 'prova',
            'apego', 'verbo', 'virao', 'copia', 'estao', 'oasis', 'acesa', 'nodoa', 'ligar', 'atrio', 'alado', 'solto', 'exijo', 'caixa', 'oxala', 'coito', 'festa', 'messe', 'nivel', 'manha', 'perda', 'turva', 'fatal', 'tocar', 'fatos', 'lindo', 'verve', 'grave', 'apelo', 'fraco', 'afora', 'livre', 'doido', 'mente', 'parca', 'dessa', 'trupe', 'parva', 'pardo', 'magia', 'opaco', 'fenda', 'tinha',
            'elite', 'sabia', 'alcar', 'jirau', 'lidar', 'viria', 'firme', 'navio', 'faixa', 'astro', 'grata', 'glosa', 'ficha', 'autor', 'supra', 'bater', 'salve', 'etico', 'retem', 'longe', 'cioso', 'pique', 'verba', 'reses', 'vezes', 'junco', 'deixa', 'calda', 'sarca', 'cousa', 'macio', 'irmao', 'douto', 'prive', 'atual', 'pagao', 'sexta', 'bicho', 'nosso', 'posto', 'porta', 'canon', 'molho',
            'torso', 'abriu', 'supor', 'light', 'judeu', 'besta', 'curso', 'extra', 'locus', 'caber', 'abuso', 'asilo', 'bioma', 'video', 'orfao', 'igneo', 'turvo', 'drops', 'bonus', 'radio', 'vosso', 'combo', 'desta', 'zelar', 'culpa', 'vinha', 'menos', 'rouca', 'pisar', 'ruina', 'julia', 'baixo', 'calao', 'ereto', 'agudo', 'advir', 'paira', 'gosto', 'finda', 'facho', 'super', 'estio', 'suave',
            'traco', 'sitio', 'facto', 'meigo', 'surja', 'feudo', 'urgia', 'cutis', 'tetra', 'amena', 'turma', 'pilar', 'tento', 'louca', 'autos', 'rumor', 'chama', 'mosto', 'acoes', 'podio', 'clean', 'museu', 'cocho', 'acola', 'local', 'lapis', 'chato', 'hobby', 'lasso', 'geral', 'boato', 'optar', 'brabo', 'pareo', 'peito', 'refem', 'aluno', 'medir', 'drama', 'piada', 'rubro', 'mesma', 'folga',
            'pacto', 'avida', 'metie', 'crime', 'penta', 'poema', 'ponha', 'teste', 'golpe', 'clima', 'movel', 'letal', 'feroz', 'coral', 'passa', 'cacho', 'vigia', 'aroma', 'hoste', 'monte', 'vetar', 'poeta', 'pasmo', 'acude', 'cetro', 'riste', 'rival', 'daqui', 'ateia', 'forem', 'fazia', 'ecoar', 'verde', 'licao', 'cover', 'troca', 'tacha', 'forum', 'swing', 'carta', 'finjo', 'busca', 'axila',
            'monge', 'calmo', 'idoso', 'plebe', 'artur', 'plumo', 'sucia', 'aviso', 'ebano', 'falha', 'briga', 'escol', 'tribo', 'venha', 'lesse', 'conto', 'roupa', 'pedra', 'tarde', 'amiga', 'macro', 'chefe', 'perco', 'plaga', 'cargo', 'sarau', 'fruto', 'unica', 'civil', 'atimo', 'vento', 'farta', 'grama', 'viram', 'sosia', 'legua', 'virar', 'benca', 'manga', 'berro', 'saldo', 'casar', 'ornar',
            'catre', 'seixo', 'arado', 'troca', 'uteis', 'itens', 'fosso', 'magna', 'surto', 'bruta', 'beijo', 'traje', 'corso', 'tiver', 'assar', 'nuvem', 'estro', 'manga', 'giria', 'deste', 'vazao', 'ticao', 'recem', 'trato', 'jejum', 'porte', 'pinho', 'amado', 'canso', 'tutor', 'vedar', 'perto', 'renda', 'arfar', 'silvo', 'bruto', 'depor', 'amada', 'bazar', 'gabar', 'irado', 'inter', 'midia',
            'ambar', 'natal', 'grota', 'feita', 'areia', 'deram', 'cifra', 'rural', 'orgao', 'tchau', 'nesse', 'laudo', 'pavor', 'stand', 'bucho', 'fossa', 'odiar', 'regio', 'guria', 'pasma', 'vadio', 'segar', 'clero', 'minar', 'pomar', 'vagar', 'close', 'molde', 'xucro', 'aviar', 'troco', 'negar', 'jogar', 'rocha', 'cenho', 'canto', 'mamae', 'lesao', 'sotao', 'visto', 'densa', 'proto', 'bolsa',
            'chula', 'cinto', 'lesto', 'largo', 'volta', 'morfo', 'horto', 'marca', 'inves', 'paiol', 'ruido', 'vista', 'penso', 'urdir', 'pugna', 'podar', 'ileso', 'tenha', 'vasta', 'ferpa', 'ufano', 'varoa', 'logos', 'velha', 'cheia', 'santo', 'mocho', 'ubere', 'nesta', 'nessa', 'civel', 'frota', 'esgar', 'etapa', 'bulir', 'umido', 'agape', 'piche', 'cerca', 'linha', 'fundo', 'apear', 'verao',
            'resto', 'narco', 'simio', 'polis', 'peita', 'jazer', 'final', 'coroa', 'ceita', 'misto', 'todas', 'manto', 'ardis', 'trago', 'preco', 'letra', 'monta', 'salmo', 'burra', 'troco', 'demao', 'alamo', 'labia', 'canil', 'chaga', 'matar', 'banto', 'campa', 'redor', 'cosmo', 'mover', 'barao', 'gemer', 'findo', 'seiva', 'album', 'audio', 'fazes', 'folia', 'venho', 'danca', 'folha', 'bolso',
            'porca', 'barro', 'retro', 'neste', 'punha', 'axial', 'queda', 'limpo', 'sabor', 'louro', 'calor', 'calvo', 'rente', 'firma', 'farol', 'salva', 'mimar', 'lousa', 'lutar', 'zumbi', 'macho', 'arroz', 'calca', 'coevo', 'baixa', 'sigla', 'enjoo', 'torna', 'justa', 'miope', 'veloz', 'logia', 'solta', 'fugiu', 'gueto', 'ousar', 'bedel', 'nacar', 'chave', 'tumba', 'longo', 'reler', 'vazia',
            'corar', 'forro', 'farto', 'fatuo', 'penca', 'vario', 'sexto', 'lucro', 'cacto', 'sofia', 'obtem', 'mania', 'subir', 'urgir', 'repor', 'sugar', 'custo', 'valer', 'quite', 'louca', 'harem', 'passe', 'puido', 'ultra', 'sadio', 'staff', 'cardo', 'nariz', 'versa', 'dados', 'outra', 'usual', 'lento', 'modal', 'corte', 'hifen', 'refil', 'viger', 'socio', 'falsa', 'diabo', 'choca', 'ceifa',
            'ferir', 'redea', 'garra', 'nesga', 'abade', 'pagar', 'mouro', 'grife', 'xampu', 'aereo', 'voila', 'patio'
            ]
t_5charC = ['sagaz', 'âmago', 'negro', 'êxito', 'mexer', 'termo', 'nobre', 'senso', 'algoz', 'afeto', 'ética', 'plena', 'mútua', 'tênue', 'sutil', 'fazer', 'vigor', 'aquém', 'assim', 'porém', 'seção', 'audaz', 'sanar', 'fosse', 'cerne', 'inato', 'ideia', 'poder', 'moral', 'desde', 'justo', 'muito', 'sobre', 'torpe', 'honra', 'quiçá', 'fútil', 'razão', 'anexo', 'etnia', 'ícone', 'sonho', 'égide',
            'tange', 'amigo', 'lapso', 'mútuo', 'expor', 'haver', 'casal', 'hábil', 'dengo', 'tempo', 'seara', 'então', 'ávido', 'pesar', 'boçal', 'ardil', 'genro', 'posse', 'causa', 'pária', 'coser', 'dizer', 'corja', 'prole', 'saber', 'dever', 'graça', 'óbice', 'brado', 'tenaz', 'crivo', 'detém', 'ânimo', 'ápice', 'comum', 'digno', 'ânsia', 'temor', 'sendo', 'ceder', 'culto', 'assaz', 'atroz',
            'pauta', 'gleba', 'ainda', 'mundo', 'fugaz', 'censo', 'estar', 'valha', 'vício', 'forte', 'cozer', 'vulgo', 'neném', 'denso', 'revés', '', 'xibiu', 'pudor', 'regra', 'dogma', 'louco', 'criar', 'banal', 'saúde', 'round', 'jeito', 'atrás', 'clava', 'impor', 'ordem', 'mercê', 'pedir', 'tenro', 'apraz', 'pífio', 'desse', 'feliz', 'usura', 'mesmo', 'homem', 'servo', 'reaça', 'sábio',
            'juízo', 'coisa', 'prosa', 'viril', 'presa', 'ontem', 'cunho', 'forma', 'limbo', 'manso', 'falar', 'devir', 'meiga', 'posso', 'fluir', 'afago', 'vendo', 'ébrio', 'platô', 'sério', 'mágoa', 'guisa', 'herói', 'todos', 'puder', 'visar', 'acaso', 'valor', 'certo', 'temer', 'pleno', 'ímpio', 'cisma', 'lugar', 'afins', 'bruma', 'óbvio', 'gerar', 'êxodo', 'obter', 'falso', 'crise', 'matiz',
            'abrir', 'praxe', 'garbo', 'senil', 'fluxo', 'havia', 'vênia', 'enfim', 'fácil', 'tédio', 'legal', 'união', 'ritmo', 'burro', 'álibi', 'tomar', 'visão', 'pulha', 'parvo', 'bravo', 'valia', 'reter', 'vital', 'favor', 'olhar', 'gênio', 'prumo', 'grato', 'levar', 'parco', 'vivaz', 'casta', 'laico', 'reles', 'morte', 'possa', 'ameno', 'tecer', 'linda', 'óbito', 'brega', 'prime', 'ranço',
            'noção', 'falta', 'sábia', 'selar', 'cabal', 'ajuda', 'façam', 'fator', 'nicho', 'anelo', 'noite', 'achar', 'farsa', 'rogar', 'ouvir', 'viver', 'coeso', 'citar', 'força', 'épico', 'fardo', 'adiar', 'cisão', 'ativo', 'sinto', 'carma', 'calma', 'passo', 'único', 'tendo', 'dúbio', 'leigo', 'sonso', 'gente', 'haste', 'outro', 'pobre', 'exato', 'rever', 'sesta', 'amplo', 'cesta', 'revel',
            'deter', 'sulco', 'humor', 'imune', 'vemos', 'lavra', 'tende', 'labor', 'árduo', 'ciúme', 'gesto', 'atuar', 'velho', 'feixe', 'claro', 'igual', 'ponto', 'ideal', 'ótica', 'hiato', 'débil', 'sonsa', 'toada', 'terra', 'terno', 'vácuo', 'ambos', 'varão', 'marco', 'remir', 'cauda', 'fonte', 'senão', 'líder', 'capaz', 'jovem', 'fusão', 'inata', 'ficar', 'probo', 'leito', 'horda', 'advém',
            'tenra', 'velar', 'farão', 'doido', 'xeque', 'coçar', 'algum', 'relva', 'vazio', 'série', 'apoio', 'tanto', 'caçar', 'papel', 'entre', 'pouco', 'vimos', 'sente', 'anuir', 'raiva', 'frase', 'coesa', 'torço', 'rigor', 'botar', 'verso', 'dorso', 'signo', 'cruel', 'feito', 'massa', 'minha', 'moção', 'prece', 'brisa', 'ímpar', 'credo', 'nossa', 'covil', 'preso', 'casto', 'fauna', 'ambas',
            'ciclo', 'blasé', 'chata', 'morar', 'lazer', 'peste', 'vírus', 'furor', 'trama', 'dócil', 'faina', 'maior', 'flora', 'pegar', 'árido', 'adeus', 'vetor', 'chuva', 'houve', 'beata', 'setor', 'seita', 'manha', 'meses', 'liame', 'aceso', 'banzo', 'sorte', 'senda', 'livro', 'vulto', 'pecha', 'carro', 'ardor', 'salvo', 'breve', 'visse', 'vasto', 'peixe', 'birra', 'comer', 'plano', 'antro',
            'morro', 'saiba', 'ocaso', 'nunca', 'prado', 'reger', 'aliás', 'pajem', 'rezar', 'átomo', 'segue', 'avaro', 'saída', 'ótimo', 'junto', 'mudar', 'áureo', 'chulo', 'sinal', 'serão', 'acima', 'lenda', 'grupo', 'opção', 'parar', 'treta', 'fruir', 'fugir', 'anciã', 'jazia', 'andar', 'brava', 'fitar', 'nação', 'parte', 'campo', 'leite', 'prazo', 'puxar', 'rapaz', 'bando', 'gerir', 'tenso',
            'tosco', 'alude', 'norma', 'praia', 'motim', 'ídolo', 'época', 'risco', 'anais', 'agora', 'exame', 'vilão', 'sinhá', 'tirar', 'malta', 'arcar', 'reino', 'antes', 'psico', 'avião', 'praga', 'venal', 'índio', 'áurea', 'quota', 'aonde', 'soldo', 'corpo', 'preto', 'texto', 'traga', 'logro', 'quase', 'cheio', 'voraz', 'sumir', 'certa', 'filho', 'conta', 'fixar', 'pompa', 'turba', 'prova',
            'apego', 'verbo', 'virão', 'cópia', 'estão', 'oásis', 'acesa', 'nódoa', 'ligar', 'átrio', 'alado', 'solto', 'exijo', 'caixa', 'oxalá', 'coito', 'festa', 'messe', 'nível', 'manhã', 'perda', 'turva', 'fatal', 'tocar', 'fatos', 'lindo', 'verve', 'grave', 'apelo', 'fraco', 'afora', 'livre', 'doído', 'mente', 'parca', 'dessa', 'trupe', 'parva', 'pardo', 'magia', 'opaco', 'fenda', 'tinha',
            'elite', 'sabia', 'alçar', 'jirau', 'lidar', 'viria', 'firme', 'navio', 'faixa', 'astro', 'grata', 'glosa', 'ficha', 'autor', 'supra', 'bater', 'salve', 'ético', 'retém', 'longe', 'cioso', 'pique', 'verba', 'reses', 'vezes', 'junco', 'deixa', 'calda', 'sarça', 'cousa', 'macio', 'irmão', 'douto', 'privê', 'atual', 'pagão', 'sexta', 'bicho', 'nosso', 'posto', 'porta', 'cânon', 'molho',
            'torso', 'abriu', 'supor', 'light', 'judeu', 'besta', 'curso', 'extra', 'locus', 'caber', 'abuso', 'asilo', 'bioma', 'vídeo', 'órfão', 'ígneo', 'turvo', 'drops', 'bônus', 'rádio', 'vosso', 'combo', 'desta', 'zelar', 'culpa', 'vinha', 'menos', 'rouca', 'pisar', 'ruína', 'júlia', 'baixo', 'calão', 'ereto', 'agudo', 'advir', 'paira', 'gosto', 'finda', 'facho', 'super', 'estio', 'suave',
            'traço', 'sítio', 'facto', 'meigo', 'surja', 'feudo', 'urgia', 'cútis', 'tetra', 'amena', 'turma', 'pilar', 'tento', 'louça', 'autos', 'rumor', 'chama', 'mosto', 'ações', 'pódio', 'clean', 'museu', 'cocho', 'acolá', 'local', 'lápis', 'chato', 'hobby', 'lasso', 'geral', 'boato', 'optar', 'brabo', 'páreo', 'peito', 'refém', 'aluno', 'medir', 'drama', 'piada', 'rubro', 'mesma', 'folga',
            'pacto', 'ávida', 'metiê', 'crime', 'penta', 'poema', 'ponha', 'teste', 'golpe', 'clima', 'móvel', 'letal', 'feroz', 'coral', 'passa', 'cacho', 'vigia', 'aroma', 'hoste', 'monte', 'vetar', 'poeta', 'pasmo', 'açude', 'cetro', 'riste', 'rival', 'daqui', 'ateia', 'forem', 'fazia', 'ecoar', 'verde', 'lição', 'cover', 'troça', 'tacha', 'fórum', 'swing', 'carta', 'finjo', 'busca', 'axila',
            'monge', 'calmo', 'idoso', 'plebe', 'artur', 'plumo', 'súcia', 'aviso', 'ébano', 'falha', 'briga', 'escol', 'tribo', 'venha', 'lesse', 'conto', 'roupa', 'pedra', 'tarde', 'amiga', 'macro', 'chefe', 'perco', 'plaga', 'cargo', 'sarau', 'fruto', 'única', 'civil', 'átimo', 'vento', 'farta', 'grama', 'viram', 'sósia', 'légua', 'virar', 'bença', 'manga', 'berro', 'saldo', 'casar', 'ornar',
            'catre', 'seixo', 'arado', 'troca', 'úteis', 'itens', 'fosso', 'magna', 'surto', 'bruta', 'beijo', 'traje', 'corso', 'tiver', 'assar', 'nuvem', 'estro', 'mangá', 'gíria', 'deste', 'vazão', 'tição', 'recém', 'trato', 'jejum', 'porte', 'pinho', 'amado', 'canso', 'tutor', 'vedar', 'perto', 'renda', 'arfar', 'silvo', 'bruto', 'depor', 'amada', 'bazar', 'gabar', 'irado', 'inter', 'mídia',
            'âmbar', 'natal', 'grota', 'feita', 'areia', 'deram', 'cifra', 'rural', 'órgão', 'tchau', 'nesse', 'laudo', 'pavor', 'stand', 'bucho', 'fossa', 'odiar', 'régio', 'guria', 'pasma', 'vadio', 'segar', 'clero', 'minar', 'pomar', 'vagar', 'close', 'molde', 'xucro', 'aviar', 'troco', 'negar', 'jogar', 'rocha', 'cenho', 'canto', 'mamãe', 'lesão', 'sótão', 'visto', 'densa', 'proto', 'bolsa',
            'chula', 'cinto', 'lesto', 'largo', 'volta', 'morfo', 'horto', 'marca', 'invés', 'paiol', 'ruído', 'vista', 'penso', 'urdir', 'pugna', 'podar', 'ileso', 'tenha', 'vasta', 'ferpa', 'ufano', 'varoa', 'logos', 'velha', 'cheia', 'santo', 'mocho', 'úbere', 'nesta', 'nessa', 'cível', 'frota', 'esgar', 'etapa', 'bulir', 'úmido', 'ágape', 'piche', 'cerca', 'linha', 'fundo', 'apear', 'verão',
            'resto', 'narco', 'símio', 'pólis', 'peita', 'jazer', 'final', 'coroa', 'ceita', 'misto', 'todas', 'manto', 'ardis', 'trago', 'preço', 'letra', 'monta', 'salmo', 'burra', 'troço', 'demão', 'álamo', 'lábia', 'canil', 'chaga', 'matar', 'banto', 'campa', 'redor', 'cosmo', 'mover', 'barão', 'gemer', 'findo', 'seiva', 'álbum', 'áudio', 'fazes', 'folia', 'venho', 'dança', 'folha', 'bolso',
            'porca', 'barro', 'retro', 'neste', 'punha', 'axial', 'queda', 'limpo', 'sabor', 'louro', 'calor', 'calvo', 'rente', 'firma', 'farol', 'salva', 'mimar', 'lousa', 'lutar', 'zumbi', 'macho', 'arroz', 'calça', 'coevo', 'baixa', 'sigla', 'enjoo', 'torna', 'justa', 'míope', 'veloz', 'logia', 'solta', 'fugiu', 'gueto', 'ousar', 'bedel', 'nácar', 'chave', 'tumba', 'longo', 'reler', 'vazia',
            'corar', 'forro', 'farto', 'fátuo', 'penca', 'vário', 'sexto', 'lucro', 'cacto', 'sofia', 'obtém', 'mania', 'subir', 'urgir', 'repor', 'sugar', 'custo', 'valer', 'quite', 'louca', 'harém', 'passe', 'puído', 'ultra', 'sadio', 'staff', 'cardo', 'nariz', 'versa', 'dados', 'outra', 'usual', 'lento', 'modal', 'corte', 'hífen', 'refil', 'viger', 'sócio', 'falsa', 'diabo', 'choça', 'ceifa',
            'ferir', 'rédea', 'garra', 'nesga', 'abade', 'pagar', 'mouro', 'grife', 'xampu', 'aéreo', 'voilà', 'pátio'
            ]

#base de dados
palavras_5char_existentes = ('sagaz', 'amago', 'negro', 'exito', 'mexer', 'termo', 'nobre', 'senso', 'algoz', 'afeto', 'etica', 'plena', 'mutua', 'tenue', 'sutil', 'fazer', 'vigor', 'aquem', 'assim', 'porem', 'secao', 'audaz', 'sanar', 'fosse', 'cerne', 'ideia', 'inato', 'poder', 'moral', 'desde', 'justo', 'muito', 'sobre', 'torpe', 'honra', 'quica', 'futil', 'razao', 'anexo', 'etnia', 'sonho', 'icone', 'egide', 'tange', 'amigo', 'lapso', 'expor', 'mutuo', 'haver', 'casal', 'dengo', 'habil', 'tempo', 'seara', 'entao', 'avido', 'pesar', 'bocal', 'ardil', 'genro', 'posse', 'causa', 'paria', 'coser', 'dizer', 'saber', 'graca', 'prole', 'corja', 'dever', 'obice', 'tenaz', 'brado', 'crivo', 'detem', 'animo', 'comum', 'apice', 'ansia', 'digno', 'temor', 'sendo', 'ceder', 'culto', 'assaz', 'pauta', 'atroz', 'ainda', 'gleba', 'mundo', 'fugaz', 'estar', 'censo', 'forte', 'valha', 'vicio', 'vulgo', 'cozer', 'nenem', 'denso', 'reves', '', 'xibiu', 'pudor', 'regra', 'dogma', 'louco', 'criar', 'saude', 'banal', 'round', 'jeito', 'atras', 'impor', 'clava', 'ordem', 'merce', 'pedir', 'tenro', 'apraz', 'desse', 'pifio', 'feliz', 'usura', 'mesmo', 'homem', 'servo', 'sabio', 'reaca', 'juizo', 'coisa', 'prosa', 'viril', 'presa', 'ontem', 'cunho', 'forma', 'limbo', 'falar', 'manso', 'devir', 'meiga', 'posso', 'fluir', 'vendo', 'afago', 'ebrio', 'plato', 'todos', 'serio', 'magoa', 'guisa', 'heroi', 'puder', 'visar', 'certo', 'acaso', 'valor', 'temer', 'lugar', 'pleno', 'impio', 'cisma', 'afins', 'bruma', 'obvio', 'gerar', 'obter', 'exodo', 'falso', 'abrir', 'crise', 'matiz', 'praxe', 'garbo', 'senil', 'fluxo', 'havia', 'venia', 'facil', 'legal', 'enfim', 'tedio', 'uniao', 'ritmo', 'burro', 'alibi', 'tomar', 'visao', 'parvo', 'pulha', 'bravo', 'valia', 'reter', 'olhar', 'vital', 'favor', 'genio', 'prumo', 'levar', 'grato', 'parco', 'casta', 'vivaz', 'laico', 'morte', 'reles', 'possa', 'ameno', 'tecer', 'linda', 'brega', 'obito', 'prime', 'nocao', 'ranco', 'falta', 'sabia', 'ajuda', 'cabal', 'selar', 'facam', 'nicho', 'noite', 'achar', 'fator', 'anelo', 'ouvir', 'rogar', 'farsa', 'viver', 'coeso', 'forca', 'citar', 'fardo', 'epico', 'cisao', 'adiar', 'ativo', 'carma', 'calma', 'sinto', 'passo', 'dubio', 'unico', 'tendo', 'outro', 'leigo', 'sonso', 'rever', 'pobre', 'gente', 'haste', 'sesta', 'exato', 'cesta', 'amplo', 'sulco', 'deter', 'humor', 'revel', 'vemos', 'imune', 'lavra', 'tende', 'labor', 'ciume', 'arduo', 'velho', 'atuar', 'gesto', 'feixe', 'claro', 'igual', 'ponto', 'ideal', 'debil', 'otica', 'terra', 'hiato', 'sonsa', 'toada', 'terno', 'vacuo', 'ambos', 'marco', 'remir', 'varao', 'cauda', 'fonte', 'lider', 'senao', 'jovem', 'capaz', 'fusao', 'inata', 'ficar', 'probo', 'leito', 'horda', 'velar', 'tenra', 'advem', 'cocar', 'farao', 'doido', 'xeque', 'vazio', 'relva', 'algum', 'serie', 'apoio', 'papel', 'tanto', 'cacar', 'entre', 'pouco', 'vimos', 'sente', 'raiva', 'anuir', 'torco', 'coesa', 'frase', 'rigor', 'verso', 'botar', 'dorso', 'cruel', 'signo', 'feito', 'minha', 'massa', 'nossa', 'mocao', 'prece', 'brisa', 'impar', 'blase', 'credo', 'covil', 'preso', 'fauna', 'ciclo', 'casto', 'lazer', 'chata', 'ambas', 'morar', 'peste', 'trama', 'furor', 'virus', 'maior', 'docil', 'faina', 'flora', 'pegar', 'chuva', 'adeus', 'arido', 'vetor', 'houve', 'setor', 'seita', 'sorte', 'beata', 'manha', 'liame', 'meses', 'aceso', 'banzo', 'senda', 'livro', 'carro', 'vulto', 'pecha', 'ardor', 'salvo', 'visse', 'breve', 'peixe', 'vasto', 'comer', 'plano', 'birra', 'antro', 'morro', 'ocaso', 'nunca', 'saiba', 'alias', 'prado', 'reger', 'pajem', 'rezar', 'atomo', 'segue', 'avaro', 'saida', 'otimo', 'junto', 'mudar', 'aureo', 'chulo', 'sinal', 'serao', 'acima', 'lenda', 'grupo', 'opcao', 'parar', 'treta', 'fugir', 'andar', 'fruir', 'nacao', 'jazia', 'brava', 'fitar', 'ancia', 'parte', 'campo', 'leite', 'prazo', 'rapaz', 'puxar', 'praia', 'bando', 'gerir', 'tenso', 'tosco', 'alude', 'norma', 'idolo', 'motim', 'risco', 'epoca', 'anais', 'agora', 'vilao', 'exame', 'tirar', 'sinha', 'malta', 'antes', 'arcar', 'reino', 'psico', 'aviao', 'aurea', 'praga', 'venal', 'indio', 'aonde', 'quota', 'texto', 'corpo', 'preto', 'soldo', 'traga', 'logro', 'quase', 'cheio', 'voraz', 'conta', 'certa', 'filho', 'sumir', 'verbo', 'turba', 'pompa', 'fixar', 'prova', 'apego', 'copia', 'estao', 'virao', 'acesa', 'oasis', 'atrio', 'nodoa', 'alado', 'ligar', 'oxala', 'festa', 'solto', 'caixa', 'coito', 'exijo', 'nivel', 'fatal', 'manha', 'messe', 'perda', 'turva', 'fatos', 'tocar', 'lindo', 'verve', 'apelo', 'fraco', 'grave', 'mente', 'afora', 'livre', 'parca', 'doido', 'dessa', 'magia', 'trupe', 'parva', 'pardo', 'opaco', 'tinha', 'fenda', 'lidar', 'elite', 'jirau', 'sabia', 'alcar', 'firme', 'viria', 'faixa', 'navio', 'astro', 'glosa', 'grata', 'ficha', 'autor', 'bater', 'supra', 'salve', 'longe', 'etico', 'retem', 'pique', 'cioso', 'reses', 'verba', 'sarca', 'vezes', 'junco', 'deixa', 'irmao', 'cousa', 'calda', 'macio', 'nosso', 'douto', 'prive', 'atual', 'sexta', 'pagao', 'bicho', 'porta', 'posto', 'canon', 'torso', 'molho', 'abriu', 'supor', 'besta', 'curso', 'judeu', 'light', 'extra', 'locus', 'caber', 'abuso', 'video', 'asilo', 'bioma', 'bonus', 'drops', 'igneo', 'orfao', 'turvo', 'radio', 'vosso', 'desta', 'combo', 'zelar', 'culpa', 'vinha', 'menos', 'rouca', 'ruina', 'pisar', 'julia', 'baixo', 'calao', 'ereto', 'agudo', 'advir', 'gosto', 'paira', 'finda', 'super', 'facho', 'suave', 'estio', 'traco', 'sitio', 'facto', 'meigo', 'surja', 'feudo', 'cutis', 'urgia', 'amena', 'turma', 'tetra', 'pilar', 'tento', 'louca', 'mosto', 'chama', 'rumor', 'autos', 'acoes', 'podio', 'clean', 'cocho', 'museu', 'chato', 'lapis', 'acola', 'local', 'hobby', 'aluno', 'brabo', 'lasso', 'peito', 'geral', 'pareo', 'optar', 'boato', 'refem', 'medir', 'drama', 'piada', 'folga', 'mesma', 'rubro', 'avida', 'pacto', 'metie', 'poema', 'crime', 'ponha', 'teste', 'clima', 'golpe', 'penta', 'movel', 'coral', 'feroz', 'passa', 'letal', 'cacho', 'vigia', 'aroma', 'poeta', 'hoste', 'monte', 'ateia', 'pasmo', 'acude', 'vetar', 'cetro', 'forem', 'rival', 'riste', 'verde', 'daqui', 'ecoar', 'licao', 'fazia', 'troca', 'cover', 'swing', 'tacha', 'carta', 'busca', 'forum', 'finjo', 'calmo', 'idoso', 'monge', 'axila', 'plumo', 'plebe', 'aviso', 'artur', 'ebano', 'sucia', 'falha', 'briga', 'corso', 'escol', 'tribo', 'venha', 'conto', 'roupa', 'amiga', 'lesse', 'pedra', 'tarde', 'macro', 'chefe', 'plaga', 'unica', 'cargo', 'fruto', 'perco', 'sarau', 'civil', 'atimo', 'vento', 'farta', 'sosia', 'grama', 'viram', 'legua', 'manga', 'benca', 'virar', 'berro', 'saldo', 'casar', 'ornar', 'catre', 'itens', 'uteis', 'seixo', 'troca', 'arado', 'fosso', 'magna', 'bruta', 'tiver', 'beijo', 'surto', 'traje', 'nuvem', 'manga', 'assar', 'estro', 'giria', 'deste', 'vazao', 'ticao', 'jejum', 'recem', 'trato', 'porte', 'amado', 'pinho', 'canso', 'renda', 'tutor', 'perto', 'vedar', 'bruto', 'silvo', 'arfar', 'amada', 'depor', 'gabar', 'bazar', 'inter', 'midia', 'irado', 'areia', 'feita', 'ambar', 'natal', 'grota', 'orgao', 'cifra', 'rural', 'deram', 'nesse', 'tchau', 'stand', 'laudo', 'pavor', 'bucho', 'guria', 'fossa', 'odiar', 'regio', 'vadio', 'clero', 'segar', 'pasma', 'pomar', 'minar', 'close', 'vagar', 'xucro', 'aviar', 'molde', 'jogar', 'rocha', 'negar', 'troco', 'cenho', 'canto', 'mamae', 'lesao', 'visto', 'sotao', 'densa', 'volta', 'proto', 'bolsa', 'chula', 'cinto', 'largo', 'marca', 'morfo', 'inves', 'lesto', 'horto', 'paiol', 'ruido', 'vista', 'penso', 'urdir', 'podar', 'pugna', 'tenha', 'ileso', 'ferpa', 'logos', 'santo', 'varoa', 'cheia', 'vasta', 'velha', 'ufano', 'nesta', 'nessa', 'mocho', 'ubere', 'etapa', 'esgar', 'frota', 'civel', 'bulir', 'agape', 'cerca', 'umido', 'piche', 'linha', 'fundo', 'todas', 'apear', 'verao', 'simio', 'resto', 'narco', 'final', 'coroa', 'polis', 'jazer', 'peita', 'ceita', 'misto', 'ardis', 'letra', 'trago', 'manto', 'salmo', 'preco', 'burra', 'folia', 'monta', 'troco', 'alamo', 'matar', 'labia', 'chaga', 'demao', 'cosmo', 'redor', 'canil', 'banto', 'mover', 'campa', 'seiva', 'album', 'gemer', 'barao', 'findo', 'folha', 'audio', 'danca', 'venho', 'bolso', 'fazes', 'neste', 'barro', 'porca', 'retro', 'calor', 'punha', 'queda', 'axial', 'limpo', 'sabor', 'louro', 'calvo', 'farol', 'rente', 'lutar', 'macho', 'firma', 'mimar', 'salva', 'lousa', 'arroz', 'zumbi', 'calca', 'coevo', 'justa', 'enjoo', 'baixa', 'logia', 'sigla', 'torna', 'miope', 'veloz', 'bedel', 'solta', 'fugiu', 'chave', 'nacar', 'ousar', 'gueto', 'vazia', 'longo', 'reler', 'tumba', 'corar', 'forro', 'farto', 'fatuo', 'sofia', 'penca', 'sexto', 'lucro', 'vario', 'subir', 'cacto', 'mania', 'urgir', 'obtem', 'repor', 'sugar', 'custo', 'valer', 'louca', 'harem', 'quite', 'passe', 'puido', 'sadio', 'ultra', 'outra', 'nariz', 'staff', 'dados', 'cardo', 'versa', 'falsa', 'usual', 'corte', 'modal', 'hifen', 'lento', 'viger', 'socio', 'refil', 'diabo', 'ceifa', 'choca', 'ferir', 'garra', 'redea', 'nesga', 'xampu', 'disso', 'pagar', 'abade', 'patio', 'mouro',
                             'grife', 'aereo', 'emulo', 'emula', 'esimo', 'esima', 'ereis', 'epica', 'eguas', 'anodo', 'azimo', 'atono', 'atona', 'arida', 'arias', 'areas', 'ardua', 'arabe', 'aguia', 'aguas', 'agios', 'ageis', 'agata', 'acido', 'acida', 'acaro', 'abaco', 'Erico', 'Erica', 'Epiro', 'Efeso', 'Edipo', 'Avila', 'Atila', 'estas', 'estas', 'estai', 'esses', 'essas', 'esqui', 'espia', 'espia', 'espio', 'espie', 'espia', 'escoo', 'escoa', 'escoe', 'escoa', 'ervas', 'errou', 'erros', 'erres', 'errem', 'errei', 'erras', 'errar', 'erram', 'errai', 'erodo', 'erodi', 'erode', 'eroda', 'ermos', 'erica', 'erico', 'erica', 'erijo', 'erija', 'erigi', 'erige', 'erice', 'ergue', 'ergui', 'ergue', 'ergas', 'ergam', 'ereta', 'envia', 'envio', 'envie', 'envia', 'entoo', 'entra', 'entro', 'entra', 'entoa', 'entoe', 'entoa', 'entes', 'enoja', 'enojo', 'enoje', 'enoja', 'enjoo', 'enjoa', 'enjoe', 'enjoa', 'enfia', 'enfio', 'enfie', 'enfia', 'enche', 'encho', 'enchi', 'enche', 'encha', 'emula', 'emulo', 'emule', 'emula', 'emito', 'emiti', 'emite', 'emita', 'emana', 'emano', 'emane', 'emana', 'elmos', 'elixo', 'elixi', 'elixe', 'eleva', 'elevo', 'eleve', 'eleva', 'elejo', 'eleja', 'elege', 'elegi', 'elege', 'ejeta', 'ejeto', 'ejete', 'ejeta', 'eixos', 'eiras', 'educa', 'educo', 'educa', 'edita', 'edito', 'edita', 'edema', 'ecoou', 'ecoes', 'ecoem', 'ecoei', 'ecoas', 'ecoam', 'ecoai', 'duzia', 'dubia', 'dolar', 'dalia', 'dutos', 'durou', 'duros', 'durmo', 'durma', 'dures', 'durem', 'durei', 'duras', 'durar', 'duram', 'durai', 'duque', 'duplo', 'dupla', 'dunga', 'dunas', 'dumas', 'dueto', 'duela', 'duelo', 'duele', 'duela', 'ducha', 'dubla', 'dublo', 'duble', 'dubla', 'duais', 'droga', 'drogo', 'droga', 'drena', 'dreno', 'drene', 'drena', 'draga', 'drago', 'draga', 'doida', 'doias', 'doiam', 'douta', 'doura', 'douro', 'doure', 'doura', 'dotou', 'dotes', 'dotem', 'dotei', 'dotas', 'dotar', 'dotam', 'dotai', 'dosou', 'doses', 'dosem', 'dosei', 'dosas', 'dosar', 'dosam', 'dosai', 'dormi', 'dorme', 'dores', 'dopou', 'dopes', 'dopem', 'dopei', 'dopas', 'dopar', 'dopam', 'dopai', 'donos', 'donde', 'donas', 'domou', 'domes', 'domem', 'domei', 'domas', 'domar', 'domam', 'domai', 'doida', 'doera', 'doera', 'doemo', 'doeis', 'docas', 'dobra', 'dobro', 'dobre', 'dobra', 'doava', 'doara', 'doara', 'doamo', 'doais', 'doado', 'doada', 'dizia', 'dizes', 'dizem', 'dizei', 'divas', 'ditou', 'ditos', 'dites', 'ditem', 'ditei', 'ditas', 'ditar', 'ditam', 'ditai', 'dista', 'disto', 'diste', 'dista', 'disse', 'dispo', 'disca', 'disco', 'disca', 'dirao', 'diras', 'diria', 'direi', 'dique', 'diodo', 'dilui', 'diluo', 'dilui', 'dilua', 'digna', 'digne', 'digna', 'digas', 'digam', 'dieta', 'dicas', 'devia', 'deveu', 'deves', 'devem', 'devei', 'devas', 'devam', 'deusa', 'desco', 'desca', 'despi', 'despe', 'desce', 'desci', 'desce', 'dermo', 'deres', 'derem', 'deras', 'depoe', 'depos', 'depus', 'dente', 'demos', 'delta', 'deles', 'delas', 'deixa', 'deixo', 'deixe', 'deita', 'deito', 'deite', 'deita', 'dedao', 'deduz', 'dedos', 'dedal', 'decai', 'decai', 'davas', 'davam', 'datou', 'dates', 'datem', 'datei', 'datas', 'datar', 'datam', 'datai', 'darao', 'daras', 'daria', 'dares', 'darem', 'darei', 'dardo', 'danca', 'danco', 'dante', 'danou', 'danos', 'danes', 'danem', 'danei', 'dando', 'dance', 'danas', 'danar', 'danam', 'danai', 'damos', 'damas', 'dadas', 'curia', 'codea', 'colon', 'civil', 'cirio', 'cilio', 'cesio', 'celia', 'capua', 'cuica', 'custa', 'custe', 'custa', 'cuspo', 'cuspi', 'cuspa', 'curva', 'curvo', 'curve', 'curva', 'curto', 'curti', 'curte', 'curta', 'cursa', 'curse', 'cursa', 'curou', 'cures', 'curem', 'curei', 'curas', 'curar', 'curam', 'curai', 'cupom', 'cupim', 'cunha', 'cunhe', 'cunha', 'cumes', 'culta', 'culpa', 'culpo', 'culpe', 'cujus', 'cujos', 'cujas', 'cuida', 'cuido', 'cuide', 'cuida', 'cuias', 'cueca', 'cucos', 'cucas', 'cubro', 'cubra', 'cubos', 'cubas', 'creem', 'cruza', 'cruzo', 'cruze', 'cruza', 'cruas', 'croma', 'cromo', 'crome', 'croma', 'criva', 'crive', 'criva', 'criou', 'crina', 'cries', 'criem', 'criei', 'crido', 'crias', 'criam', 'criai', 'crera', 'crera', 'crema', 'cremo', 'creme', 'crema', 'creio', 'creia', 'crede', 'crava', 'cravo', 'crave', 'crava', 'coibo', 'coibe', 'coiba', 'cocou', 'cocas', 'cocam', 'cocai', 'cozia', 'cozeu', 'cozes', 'cozem', 'cozei', 'cozas', 'cozam', 'coxos', 'coxim', 'coxas', 'covas', 'couve', 'couro', 'coube', 'cotou', 'cotes', 'cotem', 'cotei', 'cotas', 'cotar', 'cotam', 'cotai', 'costa', 'cospe', 'cosia', 'coseu', 'coses', 'cosem', 'cosei', 'cosas', 'cosam', 'coroo', 'coroa', 'corca', 'corvo', 'corta', 'corto', 'corta', 'corre', 'corro', 'corri', 'corre', 'corra', 'coroa', 'corou', 'coros', 'coroe', 'corno', 'cores', 'corem', 'corei', 'corda', 'coras', 'coram', 'corai', 'copos', 'copia', 'copio', 'copie', 'copia', 'copas', 'conte', 'conta', 'conte', 'conga', 'cones', 'conde', 'compo', 'comia', 'comeu', 'comes', 'comem', 'comei', 'comas', 'comam', 'colou', 'colhe', 'colho', 'colhi', 'colhe', 'colha', 'coles', 'colem', 'colei', 'colas', 'colar', 'colam', 'colai', 'coifa', 'coice', 'coibi', 'cofre', 'coeva', 'coemo', 'coeis', 'cocos', 'coces', 'cocem', 'cocei', 'cocal', 'cobra', 'cobro', 'cobri', 'cobre', 'cobra', 'coaxa', 'coaxo', 'coaxe', 'coaxa', 'coava', 'coara', 'coara', 'coamo', 'coajo', 'coaja', 'coais', 'coagi', 'coage', 'coado', 'coada', 'clube', 'cloro', 'clone', 'clips', 'clara', 'clama', 'clamo', 'clame', 'clama', 'civis', 'citou', 'cites', 'citem', 'citei', 'citas', 'citam', 'citai', 'cisne', 'cisma', 'cismo', 'cisme', 'cisca', 'cisco', 'cisca', 'circo', 'cipos', 'ciosa', 'cinza', 'cinta', 'cinjo', 'cinja', 'cingi', 'cinge', 'cindo', 'cindi', 'cinde', 'cinda', 'cinco', 'cifra', 'cifro', 'cifre', 'cidra', 'chuta', 'chuto', 'chute', 'chuta', 'chupa', 'chupo', 'chupe', 'chupa', 'chove', 'chovo', 'chovi', 'chove', 'chova', 'chora', 'choro', 'chore', 'chora', 'choca', 'choco', 'choca', 'chiou', 'chies', 'chiem', 'chiei', 'chias', 'chiar', 'chiam', 'chiai', 'chega', 'chego', 'chega', 'chefa', 'checa', 'checo', 'checa', 'chapa', 'chama', 'chamo', 'chame', 'chale', 'chale', 'chaga', 'chago', 'cetim', 'cesto', 'cessa', 'cesso', 'cesse', 'cessa', 'cervo', 'cerra', 'cerro', 'cerre', 'cerra', 'cerol', 'cerni', 'cerda', 'cerca', 'cerco', 'ceras', 'cento', 'cenas', 'celta', 'celas', 'ceifa', 'ceifo', 'ceife', 'ceies', 'ceiem', 'ceias', 'ceiam', 'cegue', 'cegou', 'cegos', 'cegas', 'cegar', 'cegam', 'cegai', 'ceemo', 'ceeis', 'cedro', 'cedia', 'cedeu', 'cedes', 'cedem', 'cedei', 'cedas', 'cedam', 'ceava', 'ceara', 'ceamo', 'ceais', 'ceado', 'caira', 'caimo', 'caido', 'caida', 'caias', 'caiam', 'cacoo', 'cacao', 'cacoa', 'cacou', 'cacoe', 'cacoa', 'cacas', 'cacam', 'cacai', 'cavou', 'cavia', 'cavio', 'cavie', 'cavia', 'caves', 'cavem', 'cavei', 'cavas', 'cavar', 'cavam', 'cavai', 'cauto', 'cauta', 'causa', 'causo', 'cause', 'caule', 'catou', 'cates', 'catem', 'catei', 'catas', 'catar', 'catam', 'catai', 'cassa', 'casso', 'casse', 'cassa', 'caspa', 'casou', 'casos', 'cases', 'casem', 'casei', 'casco', 'casca', 'casas', 'casam', 'casai', 'carao', 'carpi', 'carpe', 'carpa', 'caros', 'carne', 'carmo', 'carga', 'caras', 'capuz', 'caput', 'capta', 'capto', 'capte', 'capta', 'capou', 'capim', 'capes', 'capem', 'capei', 'capas', 'capar', 'capam', 'capai', 'canta', 'cante', 'canta', 'cansa', 'canse', 'cansa', 'canos', 'canoa', 'canja', 'canga', 'canaa', 'canas', 'canal', 'camas', 'calca', 'calco', 'calva', 'calou', 'calos', 'calha', 'calho', 'calhe', 'calha', 'cales', 'calem', 'calei', 'caldo', 'calca', 'calco', 'calce', 'calca', 'calas', 'calar', 'calam', 'calai', 'caira', 'caiou', 'caies', 'caiem', 'caiei', 'caido', 'caibo', 'caiba', 'caias', 'caiar', 'caiam', 'caiai', 'cague', 'cagou', 'cagas', 'cagar', 'cagam', 'cagai', 'cafes', 'cacos', 'caces', 'cacem', 'cacei', 'cacas', 'cabra', 'cabos', 'cabia', 'cabes', 'cabem', 'cabei', 'buzio', 'boers', 'boies', 'boiem', 'boias', 'boiam', 'bilis', 'bario', 'buxos', 'busto', 'busca', 'busco', 'burla', 'burlo', 'burle', 'burla', 'burgo', 'bunda', 'bundo', 'bunde', 'bunda', 'bumbo', 'buliu', 'bulis', 'bulia', 'bules', 'bulbo', 'bulas', 'bulam', 'bujao', 'bufao', 'bufou', 'bufes', 'bufem', 'bufei', 'bufas', 'bufar', 'bufam', 'bufai', 'bueno', 'bucha', 'bucal', 'bruxo', 'bruxa', 'brota', 'broto', 'brote', 'brota', 'bromo', 'broca', 'broco', 'broca', 'broas', 'brito', 'brita', 'brios', 'brins', 'briga', 'brigo', 'brida', 'breve', 'breta', 'brejo', 'breca', 'breco', 'breca', 'braco', 'braca', 'brasa', 'brama', 'bramo', 'brami', 'brame', 'brama', 'brada', 'brade', 'brada', 'braba', 'boxea', 'botao', 'botou', 'botes', 'botem', 'botei', 'botas', 'botam', 'botai', 'bosta', 'bossa', 'borra', 'borro', 'borre', 'borra', 'borda', 'bordo', 'borde', 'borda', 'bones', 'bonde', 'bomba', 'bolao', 'bolou', 'bolos', 'bolha', 'boles', 'bolem', 'bolei', 'boldo', 'bolas', 'bolar', 'bolam', 'bolai', 'boiou', 'boina', 'boiei', 'boiar', 'boiai', 'bodes', 'bodas', 'bocha', 'bocas', 'bocal', 'bobos', 'bobea',
                             'bobas', 'boate', 'blusa', 'bloco', 'blefa', 'blefo', 'blefe', 'blefa', 'bisao', 'bispo', 'bique', 'bingo', 'bigas', 'biela', 'bicou', 'bicos', 'bicha', 'bicas', 'bicar', 'bicam', 'bicai', 'berco', 'berra', 'berre', 'berra', 'beque', 'benze', 'benzo', 'benzi', 'benze', 'benza', 'benta', 'bemol', 'belos', 'belga', 'belas', 'beico', 'beira', 'beiro', 'beire', 'beira', 'beija', 'beije', 'beija', 'becos', 'becas', 'bebes', 'bebia', 'bebeu', 'bebes', 'beber', 'bebem', 'bebei', 'bebas', 'bebam', 'beato', 'baias', 'bacos', 'bauru', 'batom', 'batia', 'bateu', 'bates', 'batem', 'batel', 'batei', 'batas', 'batam', 'basta', 'basto', 'baste', 'basta', 'basea', 'bases', 'barra', 'barre', 'barra', 'bares', 'bardo', 'barco', 'barca', 'barba', 'baque', 'banjo', 'baniu', 'banis', 'banir', 'bania', 'banha', 'banho', 'banhe', 'banha', 'banes', 'banem', 'banda', 'banca', 'banco', 'banca', 'bambu', 'bambo', 'bamba', 'balao', 'balsa', 'baliu', 'balis', 'balir', 'balia', 'balea', 'bales', 'balem', 'balde', 'balas', 'balam', 'baiao', 'baixa', 'baixe', 'baita', 'baila', 'bailo', 'baile', 'baila', 'baias', 'bagos', 'bagas', 'bafos', 'bacia', 'babao', 'babas', 'babou', 'babes', 'babem', 'babei', 'babas', 'babar', 'babam', 'babai', 'aerea', 'azula', 'azulo', 'azule', 'azula', 'azuis', 'azoto', 'azias', 'azeda', 'azedo', 'azede', 'azeda', 'azara', 'azaro', 'azare', 'azara', 'avens', 'aviva', 'avivo', 'avive', 'aviva', 'avisa', 'avise', 'avisa', 'avira', 'aviou', 'avimo', 'avies', 'avier', 'aviem', 'aviei', 'avias', 'aviam', 'aviai', 'avela', 'aveio', 'aveia', 'avara', 'avais', 'autua', 'autuo', 'autue', 'autua', 'auras', 'aulas', 'atens', 'ateia', 'atura', 'aturo', 'ature', 'atura', 'atuou', 'atuns', 'atues', 'atuem', 'atuei', 'atuas', 'atuam', 'atuai', 'atriz', 'atrai', 'atrai', 'atola', 'atolo', 'atole', 'atola', 'atlas', 'atica', 'atico', 'atica', 'ativa', 'ative', 'ativa', 'atira', 'atiro', 'atire', 'atira', 'atina', 'atino', 'atine', 'atina', 'atido', 'atice', 'ateve', 'ateus', 'atera', 'ateou', 'atemo', 'ateis', 'ateio', 'ateie', 'ateei', 'atear', 'ateai', 'atava', 'atara', 'atara', 'atamo', 'atais', 'atado', 'atada', 'ataca', 'ataco', 'ataca', 'assoo', 'assoa', 'assou', 'assoe', 'assoa', 'assis', 'assea', 'asses', 'assem', 'assei', 'assas', 'assam', 'assai', 'aspas', 'asnos', 'asila', 'asile', 'asila', 'artes', 'arria', 'arrio', 'arrie', 'arria', 'arrea', 'arque', 'arpoo', 'arpao', 'arpoa', 'arpoe', 'arpoa', 'armou', 'armes', 'armem', 'armei', 'armas', 'armar', 'armam', 'armai', 'argui', 'argui', 'argui', 'arguo', 'argua', 'arfou', 'arfes', 'arfem', 'arfei', 'arfas', 'arfam', 'arfai', 'arena', 'aremo', 'areja', 'arejo', 'areje', 'areja', 'areis', 'areal', 'ardia', 'ardeu', 'ardes', 'arder', 'ardem', 'ardei', 'ardas', 'ardam', 'arcou', 'arcos', 'arcas', 'arcam', 'arcai', 'araca', 'arava', 'arara', 'arara', 'aramo', 'arame', 'arais', 'arada', 'apoio', 'apoie', 'apoia', 'apura', 'apuro', 'apure', 'apura', 'aptos', 'aptas', 'apolo', 'apoia', 'apita', 'apito', 'apite', 'apita', 'apeou', 'apena', 'apeno', 'apene', 'apena', 'apela', 'apele', 'apela', 'apeio', 'apeie', 'apeia', 'apega', 'apega', 'apeei', 'apeai', 'apara', 'aparo', 'apare', 'apara', 'apaga', 'apago', 'apaga', 'aorta', 'anoes', 'aneis', 'anzol', 'anuis', 'anuia', 'anula', 'anulo', 'anule', 'anula', 'anuiu', 'anuis', 'anuem', 'anuas', 'anuam', 'anual', 'antao', 'antas', 'ansia', 'anota', 'anoto', 'anote', 'anota', 'anjos', 'anima', 'animo', 'anime', 'anima', 'angra', 'anglo', 'anexa', 'anexe', 'anexa', 'anela', 'anele', 'anela', 'andou', 'andor', 'andes', 'andem', 'andei', 'andas', 'andam', 'andai', 'ancas', 'ampla', 'amola', 'amolo', 'amole', 'amola', 'amima', 'amimo', 'amime', 'amima', 'amiga', 'amido', 'ameca', 'amemo', 'ameis', 'ameia', 'ameba', 'amava', 'amara', 'amaro', 'amara', 'amamo', 'amais', 'alcou', 'alcas', 'alcam', 'alcai', 'alvos', 'alvor', 'alves', 'alvas', 'aluna', 'aluga', 'alugo', 'aluga', 'aludo', 'aludi', 'aluda', 'altos', 'altea', 'altas', 'altar', 'aloes', 'aloja', 'alojo', 'aloje', 'aloja', 'aloca', 'aloco', 'aloca', 'almas', 'alisa', 'aliso', 'alise', 'alisa', 'aliou', 'alija', 'alijo', 'alije', 'alija', 'alies', 'aliem', 'aliei', 'alias', 'aliar', 'aliam', 'aliai', 'alhos', 'alhea', 'algas', 'alema', 'alega', 'alego', 'alega', 'aldea', 'alces', 'alcem', 'alcei', 'alaga', 'alago', 'alaga', 'alada', 'ajuda', 'ajudo', 'ajude', 'ajamo', 'ajais', 'aguca', 'aguco', 'aguca', 'aguou', 'agues', 'aguem', 'aguei', 'aguda', 'aguce', 'aguas', 'aguar', 'aguam', 'aguai', 'agita', 'agito', 'agite', 'agita', 'agira', 'agira', 'agimo', 'agido', 'agias', 'agiam', 'aftas', 'afros', 'afora', 'aforo', 'afore', 'afoga', 'afogo', 'afoga', 'afofa', 'afofo', 'afofe', 'afofa', 'afoba', 'afobo', 'afobe', 'afoba', 'aflui', 'afluo', 'aflui', 'aflua', 'afixa', 'afixo', 'afixe', 'afixa', 'afiro', 'afira', 'afiou', 'afina', 'afino', 'afine', 'afina', 'afies', 'afiem', 'afiei', 'afias', 'afiar', 'afiam', 'afiai', 'afeta', 'afete', 'afeta', 'aferi', 'afere', 'afega', 'afana', 'afano', 'afane', 'afana', 'afaga', 'afaga', 'advim', 'adula', 'adulo', 'adule', 'adula', 'aduba', 'adubo', 'adube', 'aduba', 'adoca', 'adoco', 'adoca', 'adota', 'adoto', 'adote', 'adota', 'adora', 'adoro', 'adore', 'adora', 'adoce', 'adita', 'adito', 'adite', 'adita', 'adira', 'adiro', 'adira', 'adiou', 'adimo', 'adies', 'adiem', 'adiei', 'adido', 'adida', 'adias', 'adiam', 'adiai', 'aderi', 'adere', 'adega', 'adaga', 'acusa', 'acuso', 'acuse', 'acusa', 'acuou', 'acues', 'acuem', 'acuei', 'acudo', 'acudi', 'acuda', 'acuas', 'acuar', 'acuam', 'acuai', 'acode', 'achou', 'aches', 'achem', 'achei', 'achas', 'acham', 'achai', 'aceto', 'acena', 'aceno', 'acene', 'acena', 'acata', 'acato', 'acate', 'acata', 'acaba', 'acabo', 'acabe', 'acaba', 'abusa', 'abuse', 'abusa', 'abste', 'abris', 'abril', 'abria', 'abreu', 'abres', 'abrem', 'abras', 'abram', 'abono', 'aboli', 'abole', 'ablui', 'abluo', 'ablui', 'ablua', 'abeto', 'abate', 'abato', 'abati', 'abate', 'abata', 'abana', 'abano', 'abane', 'abana', 'abala', 'abalo', 'abale', 'abala', 'abafa', 'abafo', 'abafe', 'abafa', 'Ester', 'Esopo', 'Emaus', 'Elixa', 'Elisa', 'Elias', 'Egito', 'Edite', 'Edgar', 'Delhi', 'Dacia', 'Dubai', 'Diana', 'Dhaka', 'Denis', 'Delhi', 'David', 'Dario', 'Darci', 'Dakar', 'Dafne', 'Dacca', 'Cesar', 'Catia', 'Couto', 'China', 'Chile', 'Chico', 'Chica', 'Ceara', 'Carla', 'Cairo', 'Busan', 'Bruno', 'Braga', 'Borba', 'Bielo', 'Berta', 'Berna', 'Bento', 'Belem', 'Bangu', 'Bahia', 'Bagda', 'Babel', 'Aecio', 'Artur', 'Argos', 'Argel', 'Andre', 'Amora', 'Amapa', 'Alpes', 'Aline', 'Algol', 'Alceu', 'Alair', 'Aires', 'Acker', 'Accra', 'Acaia', 'Abner', 'Aarao', 'ababa', 'Ababa', 'ababa', 'abaca', 'abaci', 'abaco', 'abada', 'abada', 'abade', 'abafe', 'abafo', 'abaix-', 'abaja', 'abaju', 'abala', 'abala', 'abale', 'abalo', 'abane', 'abano', 'abara', 'abare', 'Abare', 'abate', 'abati', 'abaxo', 'abaza', 'abcaz', 'a?beca', 'abece', 'a-be-ce', 'a-be-ce', 'abeco', 'abelh-', 'abeto', 'abezo', 'abibe', 'Abner', 'abobe', 'abobo', 'aboco', 'abofe', 'aboie', 'aboio', 'abola', 'abono', 'abota', 'Abrao', 'Abreu', 'abria', 'abril', 'Abril', 'abrir', 'abris', 'abriu', 'Abuja', 'abund-', 'abuso', 'acaba', 'acabe', 'acabo', 'a?cabo', 'acair', 'acaju', 'acalc-', 'acara', 'Acara', 'Acari', 'acaro', 'acaso', 'acata', 'Acaua', 'accao', 'aceno', 'acesa', 'aceso', 'aceta', 'acete', 'aceto', 'achai', 'acham', 'achar', 'achas', 'achei', 'achem', 'Achem', 'aches', 'achou', 'acido', 'acima', 'acino', 'a?clef', 'acoai', 'acoam', 'acoar', 'acoas', 'acode', 'acoei', 'acoem', 'acoes', 'acoes', 'acola', 'acoou', 'acoro', 'a?cote', 'actel', 'actol', 'actor', 'acuai', 'acuam', 'acuar', 'acuas', 'acude', 'acudi', 'acuei', 'acuem', 'acues', 'acule', 'aculo', 'acuou', 'acusa', 'acuse', 'acuso', 'acuta', 'acuti-', 'adaba', 'adaes', 'Adaes', 'adaga', 'adama', 'Adama', 'adame', 'adamo', 'Adamo', 'add-on', 'adega', '-adego', 'adeje', 'adejo', 'adeus', 'adiai', 'adiam', 'adiar', 'adias', 'adida', 'adido', 'adiei', 'adiem', 'adies', '-adigo', 'adiou', 'adite', 'adito', 'adito', 'adj.s.m.', 'adobe', 'adobo', 'adora', 'adore', 'adoro', 'adote', 'adoto', 'Adria', 'Adrio', 'adubo', 'adufe', 'adule', 'adulo', 'advir', 'Aecia', 'Aecio', 'a-e-i-o-u', 'A.E.I.O.U.', 'aerar', 'aerea', 'aereo', 'a?esmo', 'afago', 'afala', 'afama', 'afano', 'afare', 'afaro', 'afear', 'afete', 'afeto', 'afiar', 'afilo', 'afixo', 'aflar', 'aflui', 'afofe', 'afofo', 'afogo', 'afora', 'afoxe', 'afude', 'afulo', 'afura', 'agade', 'agape', 'agata', 'Agata', 'Agato', 'agave', 'Ageus', 'agina', 'agino', 'agite', 'agito', 'Agnes', 'agogo', 'agono', 'agora', 'agora', 'agraz', 'aguai', 'Aguai', 'aguar', 'aguas', 'aguda', 'agudo', 'Agudo', 'agues', 'aguia', 'Aguia', 'Aiace', 'aiala', 'Ainao', 'ainda', 'aipim', 'ai?sim', 'ajaja', 'ajaja', 'ajeru', 'ajuda', 'Ajuda', 'ajude', 'ajudo', 'ajuga', 'ajuru', 'alabe', 'alabo', 'alada', 'ALADI', 'alado', 'alaes', 'alaga', 'alage', 'a?laia', 'alala', 'ALALC', 'Alana', 'Alane', 'Alano', 'alaos', 'Alava',
                             'Albas', 'alboi', 'Albos', 'album', 'alcar', 'alcas', 'alcea', 'alcei', 'aleia', 'alema', 'alemo', 'ALEPA', 'ALEPE', 'ALERJ', 'ALESC', 'ALESP', 'Aleto', 'alfar', 'alfim', 'algar', 'algas', 'algia', '-algia', 'ALGOL', 'algor', 'algoz', 'alg?a', 'algum', 'algur', 'alhar', 'aliar', 'alias', 'alias', 'alibi', 'alibi', 'Alice', 'alien', 'alien', 'Alijo', 'Alina', 'Aline', 'Alino', 'alise', 'almas', 'Almas', 'Almos', 'aloes', 'aloes', 'aloja', 'alojo', 'alpes', 'altai', 'altar', 'altas', 'altos', 'Altos', 'aluar', 'aluco', 'alude', 'aluir', 'alune', 'aluno', 'alvar', 'alvas', 'Alvas', 'alveo', 'Alves', 'Alvim', 'alvor', 'alvos', 'Alvos', 'amada', 'Amada', 'amado', 'Amado', 'amago', 'amais', 'a?mais', 'amame', 'Amapa', 'amara', 'Amara', 'amara', 'amaro', 'Amaro', 'amava', 'ambar', 'ambas', 'ambos', 'amear', 'ameba', 'ameia', 'ameis', 'ameno', 'a?mesa', 'amial', 'amido', 'amiga', 'amigo', 'Amigo', 'amita', 'amito', 'amojo', 'amora', 'amplo', 'amuar', 'anaco', 'Anage', 'Anahy', 'anais', 'Anama', 'anano', 'anaos', 'Anapu', 'anata', 'ancho', 'ancia', '-ancia', 'andai', 'andam', 'andar', 'andas', 'andei', 'andem', 'andes', 'andoa', 'andor', 'andou', 'Andre', '-andro', 'andro-', 'aneis', 'anejo', 'anelo', 'anexe', 'anexo', 'anglo', 'anhar', 'aniao', 'anima', 'anima', 'anime', 'anime', 'anime', 'animo', 'anina', 'anine', 'anino', 'anion', 'anion', 'Anita', 'Anito', 'anixo', 'anjos', 'Anjos', 'anodo', 'anoes', 'anoia', 'anona', 'Anori', 'anote', 'anoto', 'ansia', 'antao', 'Antao', 'antar', 'Antas', 'antes', 'Anteu', 'antro', 'anual', 'anuir', 'anuiu', 'anule', 'anulo', 'anuro', 'anzol', 'ao?leu', 'a?olho', 'aonde', 'Aonia', 'aorta', 'apage', 'apara', 'apare', 'aparo', 'apear', 'apego', 'apela', 'apelo', 'Apiai', 'apice', 'a?pino', 'apito', 'apode', 'Apodi', 'apodo', 'apodo', 'apoio', 'apojo', 'Apolo', 'Apora', 'Apore', 'Apple', 'apupo', 'apure', 'apuro', 'aquem', 'aquem-', 'arabe', 'araca', 'Araci', 'Aracu', 'arado', 'arama', 'arame', 'Arame', 'aramo', 'arana', 'arara', 'Arara', 'Arari', 'Araua', 'Araxa', 'arcao', 'arcar', 'arcaz', 'archa', 'arcol', 'arcos', 'Arcos', 'arder', 'ardia', 'ardil', 'ardis', 'ardor', 'arduo', 'areal', 'Areal', 'arear', 'areas', 'areca', 'areia', 'Areia', 'areje', 'arejo', 'arela', 'arele', 'arelo', 'arena', 'ARENA', 'arepa', 'arere', 'areus', 'arfar', 'argan', 'argel', 'Argel', 'argon', 'Argos', 'Arial', 'arias', 'Arias', 'arido', 'Ariel', 'Aries', 'Aries', 'arigo', 'arigo', 'arilo', 'arimo', 'Arios', 'arjao', 'armai', 'armam', 'armar', 'armas', 'armei', 'armem', 'armes', 'armou', 'armur', 'arnal', 'arnaz', 'arnes', 'a?rodo', 'arola', 'arolo', 'aroma', 'aromo', 'arosi', 'arpao', 'arpar', 'arpeu', 'arqui-', 'arras', 'arrau', 'arreu', 'arroz', 'artes', 'Artur', 'Aruba', 'Aruja', 'arujo', 'arula', 'arume', 'arxar', 'asais', 'asara', 'asara', 'asava', 'ASCII', 'ascua', 'aseis', 'asilo', 'asnal', 'asnar', 'asnos', 'aspar', 'aspas', 'assai', 'Assai', 'assam', 'assar', 'assas', 'assaz', 'assei', 'assem', 'asses', 'assim', 'Assis', 'assou', 'assua', 'astro', 'astur', 'atado', 'atais', 'atara', 'atara', 'atava', 'atear', 'ateia', 'ateia', 'ateis', 'Atena', 'atese', 'ateso', 'ate?tu', 'ateus', 'atica', 'atico', 'atico', 'Atila', 'atino', 'atire', 'atiro', 'ativa', 'ative', 'ativo', 'atlas', 'Atlas', 'atomo', 'atoni', 'atono', 'atras', 'Atreu', 'a?treu', 'atril', 'atrio', 'atriz', 'atroa', 'atroo', 'atros', 'atroz', 'atuai', 'atual', 'atuam', 'atuar', 'atuas', 'atuei', 'atuem', 'atues', 'atuou', 'atxim', 'aucao', 'audaz', 'audio', 'auete', 'aueti', 'aurea', 'Aurea', 'aureo', 'aurir', 'autor', 'autos', 'avais', 'avara', 'Avare', 'avaro', 'avaro', 'avati', 'aveia', 'avela', 'a?vela', 'avena', 'a?vera', 'aviao', 'aviar', 'avido', 'avisa', 'avise', 'aviso', 'aweti', 'axila', 'Axixa', 'azado', 'azare', 'azedo', 'azeri', 'azimo', 'azoai', 'azoam', 'azoar', 'azoas', 'azoei', 'azoem', 'azoes', 'a?zoia', 'azoou', 'azoto', 'azuis', 'azule', 'azulo', 'babai', 'babam', 'babao', 'babas', 'babau', 'babei', 'babel', 'Babel', 'babem', 'babes', 'babou', 'bacar', 'bacia', 'bacio', 'bacon', 'badio', 'baeta', 'bafar', 'bafio', 'bagoa', 'bagre', 'Bagre', 'bagua', 'Bahia', 'baiao', 'Baiao', 'baiar', 'baila', 'baile', 'bailo', 'baita', 'baite', 'baixa', 'baixe', 'baixo', 'balao', 'balar', 'balas', 'balbo', 'balda', 'balde', 'bales', 'balga', 'balho', 'balir', 'baliu', 'balor', 'balsa', 'bamba', 'bambe', 'bambi', 'bambo', 'bambu', 'banal', 'banca', 'banca', 'banco', 'banda', 'Banda', 'bande', 'bando', 'bando', 'banga', 'bango', 'banha', 'banho', 'banir', 'banjo', 'banto', 'bantu', 'banza', 'banze', 'banzo', 'baoba', 'barao', 'Barao', 'barba', 'barbo', 'barca', 'barco', 'barda', 'bardo', 'Barem', 'barga', 'bario', 'barra', 'Barra', 'barre', 'barro', 'Barro', 'basaa', 'basal', 'basca', 'basco', 'bases', 'basse', 'basta', 'baste', 'basto', 'batch', 'batel', 'bater', 'batom', 'baton', 'bauru', 'Bauru', 'bazar', 'BD-ROM', 'be-a-ba', 'beata', 'beato', 'bebas', 'bebem', 'beber', 'bebeu', 'bebum', 'becas', 'becha', 'beche', 'bedel', 'beico', 'beige', 'beija', 'beije', 'beijo', 'beiju', 'beira', 'beiro', 'beita', 'belas', 'Belem', 'belga', 'belos', 'bemba', 'bemol', 'benga', 'Benim', 'Benin', 'bento', 'Bento', 'bento', 'beque', '-beque', 'berca', 'berce', 'berco', 'berma', 'Berna', 'berro', 'besta', 'beste', 'besto', 'betao', 'betar', 'Betim', 'bhili', 'biana', 'biari', 'bical', 'bicar', 'Bicas', 'bicha', 'bicho', 'bicla', 'bicos', 'biduo', 'biela', 'bifar', 'bigle', 'bigue', 'bijou', 'Bilac', 'bilar', 'biles', 'bilha', 'bilis', 'bilro', 'bimba', 'bimbe', 'bimbo', 'binar', 'binga', 'bingo', 'bioco', 'bioma', 'biota', 'bipes', 'birao', 'birra', 'bisai', 'bisam', 'bisao', 'bisar', 'bisas', 'bisca', 'bisei', 'bisel', 'bisem', 'bises', 'bisou', 'bispa', 'bispo', 'bitar', 'bivio', 'blase', 'blefe', 'blini', 'blitz', 'bloco', 'bloga', 'bluco', 'blues', 'bluff', 'blusa', 'BNDES', 'boa-fe', 'boate', 'boato', 'boava', 'bobar', 'bobot', 'bocal', 'bocal', 'bocao', 'bocas', 'bocha', 'boche', 'bocoi', 'bodao', 'bodas', 'bofas', 'boiao', 'boiar', 'boica', 'boiei', 'boiil', 'boina', 'boira', 'boita', 'bo�te', 'bojar', 'bolar', 'bolas', 'bolbo', 'bolha', 'bolor', 'bolsa', 'bolso', 'bomba', 'bombo', 'bom?de', 'bonde', 'bongo', 'bonus', 'bonus', 'bonzo', 'boras', 'boras', 'borax', 'Borba', 'borda', 'borde', 'bordo', 'bordo', 'boria', 'borla', 'borne', 'boroa', 'boroa', 'borra', 'borro', 'bosao', 'boson', 'bossa', 'bosta', 'boste', 'bosto', 'botai', 'botam', 'botao', 'botar', 'botas', 'botei', 'botem', 'botes', 'botim', 'boton', 'botou', 'botox', 'bouba', 'bouca', 'boxer', 'boxes', 'brabo', 'braca', 'braco', 'braco', 'brada', 'brado', 'braga', 'Braga', 'brama', 'brasa', 'brava', 'bravo', 'bravu', 'breca', 'brega', 'breia', 'breja', 'brejo', 'Brejo', 'Brena', 'Breno', 'brete', 'breve', 'breve', 'brial', 'brica', 'brida', 'briga', 'Brigo', 'briol', 'brisa', 'briza', 'broar', 'broas', 'broca', 'broca', 'broco', 'brodo', 'bromo', 'brota', 'brote', 'broto', 'broxa', 'broxe', 'broxo', 'bruar', 'bruma', 'bruna', 'Bruna', 'brune', 'bruni', 'bruno', 'Bruno', 'bruta', 'bruto', 'bruxa', 'bruxo', 'bucal', 'bucha', 'bucho', 'bucil', 'bucle', 'bucos', 'Bueno', 'bufao', 'bufar', 'bugar', 'bugia', 'bugie', 'bugio', 'bugre', 'Bugre', 'bugue', 'bular', 'bulas', 'bulbo', 'bulha', 'bulho', 'bulir', 'bumbo', 'bunda', 'bunda', 'bunho', 'buque', 'buque', 'burca', 'burel', 'burgo', 'buril', 'burla', 'burra', 'burro', 'busao', 'busca', 'busto', 'Butao', 'buteo', 'butes', 'butia', 'Butia', 'butim', 'butio', 'butua', 'buxao', 'buzio', 'caaba', 'Caaba', 'cabal', 'cabau', 'cabaz', 'cabem', 'caber', 'cabis', 'cabos', 'caboz', 'cabra', 'cabro', 'cabum', 'cacao', 'cacar', 'cacau', 'cacha', 'cache', 'cache', 'cache', 'cacho', 'cacre', 'cacto', 'cacua', 'cadea', 'Caete', 'cafes', 'Cafes', 'cafra', 'cafre', 'cafua', 'cagao', 'cagar', 'caiar', 'Caibi', 'caibo', 'caibo', 'caico', 'caico', 'Caico', 'caida', 'caido', '-caina', 'Cains', 'Caios', 'caira', 'cairo', 'Cairo', 'cairo', 'Cairu', 'Caiua', 'caixa', 'calai', 'calam', 'calao', 'calar', 'calas', 'calca', 'calce', 'calco', 'calco', 'calda', 'caldo', 'calei', 'calem', 'cales', 'calfe', 'calha', 'calhe', 'calix', 'Caliz', 'calma', 'calmo', 'calom', 'calor', 'calos', 'calou', 'calva', 'Calva', 'calve', 'calvo', 'Calvo', 'camal', 'camas', 'camba', 'cambe', 'Cambe', 'cambo', 'camim', 'campa', 'campa', 'campo', 'Canaa', 'canal', 'Canas', 'canca', 'canda', 'cando', 'canga', 'cango', 'canha', 'canil', 'canja', 'canle', 'canoa', 'canon', 'canos', 'canse', 'canso', 'canta', 'Canta', 'cante', 'canto', 'canza', 'canza', 'capai', 'capam', 'capao', 'capar', 'capas', 'capaz', 'capem', 'capes', 'capim', 'Capim', 'capoa', 'capot', 'capou', 'caput', 'capuz', 'caqui', 'caqui', 'Caraa', 'carai', 'Carai', 'caras', 'caras', 'caray', 'carda', 'cardo', 'carga', 'cargo', 'carie', 'caril', 'cariz', 'Carla', 'Carlo', 'carma', 'carme', 'Carmo', 'carne', 'carne', 'caros', 'carpa', 'carpe', 'carpo', 'carro', 'carta', 'carte', 'casai', 'casal', 'casam', 'casao', 'casar',
                             'casas', 'casca', 'Casca', 'casco', 'casei', 'casem', 'cases', 'casos', 'casou', 'caspa', 'cassa', 'casse', 'casso', 'casta', 'caste', 'casto', 'catai', 'catam', 'catar', 'Catar', 'catas', 'catei', 'catem', 'cates', 'catou', 'catre', 'catua', 'Cauas', 'cauda', 'Caues', 'cauim', 'caule', 'caupi', 'cauri', 'causa', 'causo', 'cauta', 'cauto', 'cavai', 'cavam', 'cavar', 'cavas', 'cavea', 'cavei', 'cavem', 'caves', 'cavou', 'CD-ROM', 'ce-aga', 'ceara', 'ceara', 'Ceara', 'cedem', 'cedem', 'ceder', 'Cedro', 'cegar', 'ceiba', 'ceifa', 'ceife', 'ceifo', 'Ceita', 'ceive', 'celga', 'celha', 'Celia', 'Celio', 'celme', 'celsa', 'Celsa', 'celso', 'Celso', 'celta', 'cemba', 'cenas', 'cenho', 'censo', 'centi-', 'cento', 'cerca', 'cerce', 'cerco', 'cerda', 'cerdo', 'Ceres', 'cerio', 'cerne', 'cerol', 'cerra', 'cerre', 'cerro', 'certa', 'certo', 'cerva', 'cervo', 'cesar', 'Cesar', 'cesio', 'cessa', 'cesse', 'cesso', 'cesta', 'cesto', 'cetim', 'cetro', 'Ceuta', 'cevar', 'chabu', 'chaco', 'chada', 'Chade', 'chaga', 'chale', 'Chale', 'chama', 'chana', 'chapa', 'chape', 'chapo', 'chara', 'charl-', 'chata', 'chato', 'chato', 'Chaul', 'chave', 'Chave', 'chavo', 'checo', 'chefa', 'chefe', 'chega', 'cheia', 'cheio', 'Cheka', 'cheva', 'chiao', 'chiar', 'chiba', 'chibe', 'chibe', 'chibo', 'chica', 'chica', 'chico', 'Chile', 'china', 'China', 'chino-', 'chipe', 'chita', 'chito', 'choca', 'choca', 'choco', 'choer', 'chola', 'cholo', 'chona', 'chope', 'chora', 'chore', 'choro', 'Choro', 'choto', 'chuca', 'chuca', 'chuco', 'chufa', 'chula', 'chule', 'chulo', 'chuca', 'chuta', 'chute', 'chuto', 'chuva', 'ciada', 'ciano', 'ciano', 'ciaos', 'cibar', 'ciber-', 'ciclo', 'cidra', 'cifra', 'cifre', 'cifro', 'cigas', 'cilha', 'cilho', 'cilio', 'cimao', 'cinco', 'cinta', 'cinto', 'cinza', 'cioso', 'Cipra', 'Cipro', 'circo', 'ciria', 'cirio', 'cirro', 'cisao', 'cisca', 'cisco', 'cisma', 'cisne', 'Cisne', 'cisto', 'citai', 'citam', 'citar', 'citas', 'Citas', 'citei', 'citem', 'cites', 'citou', 'citro', 'ciume', 'civil', 'clado', 'claim', 'clame', 'clamo', 'clara', 'Clara', 'claro', 'Claro', 'clava', 'clave', 'clean', 'clero', 'clica', 'click', 'clima', 'clina', 'clipe', 'clone', 'cloro', 'close', 'Cloto', 'clown', 'clube', 'coais', 'coala', 'coara', 'coara', 'Coari', 'coava', 'coboi', 'cobra', 'cobre', 'cobri', 'cobro', 'Cocal', 'cocao', 'cocar', 'cocar', 'cocha', 'coche', 'cocho', 'Cocos', 'codea', 'codeo', 'codex', 'coeis', 'coeso', 'coevo', 'cofre', 'coias', 'coice', 'coifa', 'coima', 'coime', 'coina', 'Coina', 'coine', 'coira', 'coira', 'coiro', 'coisa', 'coiso', 'coita', 'coite', 'coito', 'coito', 'colai', 'colam', 'colar', 'colas', 'colei', 'colem', 'coles', 'colma', 'colmo', 'colon', 'colou', 'colza', 'comam', 'comas', 'combe', 'combo', 'comer', 'comes', 'comeu', 'comia', 'comua', 'comum', 'CONAR', 'conas', 'conca', 'conde', 'Conde', 'Congo', 'conha', 'conho', 'conta', 'conte', 'conto', 'COPAM', 'copao', 'copar', 'copas', 'copia', 'copie', 'copio', 'copla', 'Copom', 'copra', 'copta', 'coque', 'corai', 'coral', 'coram', 'Corao', 'corar', 'coras', 'corca', 'corco', 'corda', 'corei', 'corem', 'cores', 'corga', 'corgo', 'corja', 'corne', 'corno', 'coroa', 'coros', 'corou', 'corpo', 'corra', 'corre', 'corri', 'corro', 'corso', 'corta', 'corte', 'corto', 'corva', 'corvo', 'Corvo', 'cosca', 'cosco', 'coser', 'coseu', 'Cosma', 'Cosme', 'cosmo', 'Cosmo', 'costa', 'Costa', 'costo', 'cotao', 'cotar', 'cotas', 'Cotia', 'cotra', 'coube', 'couce', 'coupe', 'coura', 'Coura', 'couro', 'cousa', 'couto', 'Couto', 'couve', 'covas', 'covil', 'coxia', 'coxim', 'Coxim', 'cozer', 'cozeu', 'crack', 'crase', 'crash', 'Crato', 'crave', 'cravo', 'crawl', 'crece', 'crede', 'credo', 'creem', 'crega', 'crego', 'creia', 'creio', 'creme', 'crepe', 'Creso', 'criai', 'criam', 'criar', 'crias', 'crica', 'criei', 'criem', 'cries', 'crime', 'crina', 'criou', 'crise', 'crivo', 'croac', 'croca', 'croca', 'croia', 'croio', 'cromo', 'crude', 'cruel', 'crush', 'cuais', 'cuata', 'cubar', 'cucar', 'cucho', 'cudar', 'cueca', 'cuica', 'cuida', 'cuido', 'cuite', 'cuite', 'Cuite', 'cujas', 'cujos', 'culpa', 'culpe', 'culpo', 'culto', 'Cumbe', 'cumel', 'cumim', 'cumio', 'cunca', 'cunco', 'cunha', 'Cunha', 'cunha', 'cunho', 'cupim', 'curai', 'cural', 'curam', 'curar', 'curas', 'curdo', 'curei', 'curem', 'cures', 'curia', 'curio', 'curio', 'curou', 'curra', 'curro', 'curry', 'curso', 'curta', 'curto', 'Curua', 'curva', 'curve', 'curvo', 'cusca', 'cusco', 'cuspo', 'custa', 'custe', 'custo', 'cuter', 'cutia', 'cutia', 'cutis', 'cuxiu', 'cuzao', 'dacao', 'Dacar', 'dacha', 'dadas', 'dador', 'dados', 'agua', 'daime', 'dai-me', 'Dakar', 'dalem', 'dalia', 'Dalva', 'Dalvo', 'Damao', 'damas', 'damba', 'damno', 'danai', 'danam', 'danar', 'danca', 'Danca', 'dance', 'dandi', 'dando', 'danei', 'danem', 'danes', 'danos', 'danou', 'daqui', 'darao', 'Darci', 'dardo', 'darei', 'dar?em', 'daria', 'Dario', 'darma', 'datar', 'datas', 'Datas', 'Daude', 'davam', 'David', 'Davis', 'de?a?pe', 'de?bem', 'debil', 'de?boa', 'debut', 'decam', 'decas', 'decei', 'decem', 'decer', 'deces', 'deceu', 'decia', 'de?cor', 'dedal', 'dedao', 'dedos', 'Deise', 'deita', 'deite', 'deito', 'de?Itu', 'deixa', 'deixe', 'deixo', 'dejet-', 'delas', 'delei', 'deles', 'delir', 'delta', 'Delta', 'de?lua', 'de?mal', 'demos', 'demos', 'dende', 'densa', 'denso', 'dente', 'depor', 'depre', 'deque', 'deram', 'derbi', 'derby', 'derma', '-derma', 'derme', '-derme', '-dermo', 'desar', 'desca', 'desce', 'desci', 'desco', 'desde', 'desdo', 'despi', 'dessa', 'desse', 'desta', 'deste', 'detem', 'deter', 'de?tom', 'detox', 'deusa', 'dever', 'deves', 'de?vez', 'devia', 'devir', 'de?xua', 'diaba', 'diabo', 'Diabo', 'diade', 'diafa', 'Diana', 'dicar', 'dieco', 'Diega', 'Diego', 'diese', 'diese', 'dieta', 'digna', 'digno', 'dildo', 'Dilma', 'Dilmo', 'dimer', 'dinas', 'dinda', 'dingo', 'dinka', 'diodo', 'Dioga', 'diogo', 'Diogo', 'Dione', 'dique', 'direi', 'disco', 'disel', 'disse', 'disso', 'disto', 'ditar', 'ditas', 'ditos', 'divas', 'Divas', 'divos', 'Divos', 'dizem', 'dizer', 'dizia', 'doada', 'doado', 'doais', 'doara', 'doara', 'doava', 'dobra', 'dobre', 'dobro', 'do?cao', 'docar', 'docem', 'doces', 'docil', 'dodoi', 'dodos', 'dodos', 'dodos', 'doeis', 'doera', 'doera', 'dogao', 'dogma', 'dogue', 'doiam', 'doias', 'doida', 'doida', 'doido', 'doido', 'doira', 'doiro', '-doiro', 'dolar', 'dolor', 'domar', 'donas', 'donde', 'dondo', 'dongo', 'donos', 'dopar', 'Doris', 'dorna', 'dorso', 'dorze', 'dotar', 'douda', 'doudo', 'doula', 'doura', 'doure', 'douro', '-douro', 'douto', 'draft', 'draga', 'drama', 'drene', 'dreno', 'drive', 'droga', 'drogo', 'drone', 'drope', 'drops', 'drupa', 'drusa', 'druso', 'dubia', 'dubio', 'duble', 'ducal', 'ducha', 'duche', 'ducho', 'ducto', 'duelo', 'Duere', 'dueto', 'dulci-', 'dumas', 'dumba', 'dupla', 'duplo', 'duque', 'durai', 'duram', 'durar', 'duras', 'durei', 'durem', 'dures', 'duros', 'durou', 'Dutra', 'duzia', 'ebano', 'ebola', 'ebola', 'e-book', 'ebria', 'ebrio', 'ecler', 'ecoai', 'ecoar', 'ecran', 'edeia', 'edeia', 'Edeia', 'edema', 'edens', 'edite', 'edito', 'edito', 'Ednas', 'Ednos', 'efebo', 'Efire', 'efode', 'egide', 'Egito', 'eiras', '-eiras', '-eiros', 'eivar', 'eixos', 'elemi', 'elepe', 'elfos', 'Elias', 'Elisa', 'Elise', 'Eliso', 'elite', 'Eloas', 'Elvas', 'Elzas', 'Elzos', 'email', 'e-mail', 'emane', 'emano', 'embua', 'em?dia', 'emero', 'emese', 'emico', 'em?off', 'emoji', 'empar', 'empos', 'em?vao', 'e?nada', 'enche', 'encho', '-encia', 'endes', 'endez', 'endro', 'enfia', 'enfim', 'engos', 'engua', 'enjoo', 'enjoo', 'e?nois', 'enoja', 'enojo', 'entao', 'entra', 'entre', 'entro', 'envio', 'Enzas', 'Enzos', 'epica', 'epico', 'epoca', 'epoxi', 'erado', 'erais', 'erbio', 'ereis', 'Erere', 'ereto', 'ergue', 'erica', 'erice', 'ermas', 'errai', 'erram', 'errar', 'erras', 'errei', 'errem', 'erres', 'error', 'errou', 'ervas', 'erzya', 'escol', 'esfia', 'esgar', 'esmar', 'espia', 'espie', 'espio', 'espir', 'espru', 'esqui', 'essas', 'esses', 'estao', 'estar', 'estas', 'Ester', 'ester', 'estes', 'estie', 'estio', 'estol', 'estou', 'estro', 'etano', 'etapa', 'eteno', 'ethos', 'etica', 'etico', 'etimo', 'etnia', 'etude', 'eu,?hem', 'evade', 'evite', 'evito', 'Evora', 'exalo', 'exame', 'exata', 'exato', 'exido', 'exime', 'exito', 'exodo', 'Exodo', 'expor', 'extra', 'exuma', 'exume', 'exumo', 'Fabia', 'Fabio', 'facam', 'facao', 'faces', 'facha', 'facho', 'facil', 'facto', 'fados', 'faial', 'Faial', 'faiar', 'faina', 'Faina', 'faito', 'faixa', 'falai', 'falam', 'falar', 'falas', 'falaz', 'falca', 'falda', 'falei', 'falem', 'fales', 'falha', 'falhe', 'falho', 'falir', 'falou', 'falsa', 'falso', 'falta', 'falte', 'falto', 'falus', 'fanal', 'fanar', 'fanga', 'fanha', 'fanho', 'fanta', 'farad', 'farao', 'farao', 'farda', 'fardo', 'faria', 'farol', 'Farol', 'farpa', 'farra', 'farsa', 'farta', 'farte', 'farto', 'farum', 'fasor', 'fasta', 'fasto', 'fatal', 'fatao', 'fatia', 'fatie', 'fatio', 'fator', 'fatuo', 'fauce', 'faula', 'fauna',
                             'fauno', 'favor', 'fazei', 'fazem', 'fazer', 'fazia', 'febeu', 'febra', 'febre', 'fecal', 'fecha', 'feche', 'fecho', 'feder', 'fedor', 'feias', 'Feijo', 'feios', 'feira', 'feire', 'feiro', 'feita', 'feito', 'feixe', 'felas', 'feleo', 'Felix', 'feliz', 'Feliz', 'felpa', 'felpo', 'femea', 'femeo', 'femur', 'femur', 'fenda', 'fende', 'fenix', 'fenix', 'Fenix', 'fenol', 'fento', 'fento-', 'feofo', 'feras', 'feraz', 'feria', 'feria', 'ferie', 'ferio', 'ferir', 'fermi', 'feros', 'feroz', 'ferra', 'ferra', 'ferro', 'ferve', 'fervo', 'festa', 'fetal', 'feudo', 'fezes', 'fiado', 'Fiama', 'fiapo', 'fibra', 'ficar', 'ficha', 'ficou', 'figle', 'figos', 'filao', 'filer', 'filet', 'filha', 'filho', 'Filho', 'filho', '-filia', 'filie', 'filio', 'filme', 'filmo', 'fimia', 'final', 'final-', 'finas', 'finca', 'finda', 'finde', 'findo', 'fines', 'finit-', 'finta', 'fiofo', 'fiota', 'fiote', 'fique', 'firma', 'Firma', 'firme', 'firmo', 'Firmo', 'fisco', 'fisga', 'fitar', 'fitas', 'fixai', 'fixam', 'fixar', 'fixas', 'fixei', 'fixem', 'fixes', 'fixou', 'flama', 'flape', 'flash', 'flate', 'flato', 'flava', 'Flava', 'flavo', 'Flavo', 'fleme', 'flete', 'flirt', 'floco', 'flora', 'Flora', 'flore', 'floro', 'Floro', 'fluir', 'fluor', 'flush', 'fluxo', 'fobia', '-fobia', 'focao', 'justo', 'Jutai', 'kanji', 'karbi', 'karma', 'kasha', 'kayak', 'kendo', 'khasi', 'khmer', 'kirie', 'knyaz', 'koala', 'koban', 'koine', 'kombi', 'konel', 'krill', 'Kuait', 'kudzu', 'kulak', 'kumel', 'kumyk', 'Kyoto', 'kyrie', 'Kyzyl', 'labeu', 'labia', 'labil', 'labio', 'labor', 'lacao', 'lacar', 'lacar', 'lacei', 'lacho', 'Lacio', 'lacos', 'lacre', 'lados', 'ladra', 'ladre', 'ladro', 'lagar', 'Lages', 'lagoa', 'Lagoa', 'Lagos', 'laiar', 'laico', 'laido', 'laivo', 'Lajes', 'lamas', 'lambe', 'lamen', 'lamia', 'Lamim', 'lampo', 'lanca', 'lance', 'lanco', 'lande', 'Lange', 'lanha', 'lanho', 'lapao', 'Lapao', 'lapar', 'lapia', 'Lapia', 'lapis', 'lapso', 'laque', 'lardo', 'lares', 'lareu', 'larga', 'largo', 'larpa', 'larpe', 'larpo', 'larva', 'lasca', 'laser', 'lassa', 'lasse', 'lasso', 'latao', 'latar', 'latas', 'later', 'latex', 'latia', 'latim', 'latir', '-latra', 'lauda', 'Lauda', 'laude', 'laudo', 'Laudo', 'laura', 'Laura', 'lauro', 'Lauro', 'lauta', 'lauto', 'lavai', 'lavam', 'lavar', 'lavas', 'lavei', 'lavem', 'laves', 'lavor', 'lavou', 'lavra', 'lavre', 'lavro', 'lazer', 'lebre', 'Lebre', 'ledas', 'Ledas', 'ledor', 'ledos', 'Ledos', 'legal', 'legao', 'legar', 'legra', 'legua', 'legue', 'Leide', 'leigo', 'Leila', 'leino', 'leira', 'leite', 'Leite', 'leito', 'leiva', 'leixe', 'leixo', 'lemes', 'Lemes', 'lenco', 'lenda', 'lenha', 'lenho', 'lenir', 'lenta', 'lente', 'lento', 'lepra', 'lepto', 'leque', 'lerda', 'lerdo', 'leria', 'lerpe', 'lesai', 'lesam', 'lesao', 'lesar', 'lesas', 'lesca', 'lesei', 'lesem', 'leses', 'lesim', 'lesma', 'lesme', 'lesou', 'lesta', 'leste', 'lesto', 'letal', 'letao', 'letra', 'leuco-', 'levai', 'levam', 'levar', 'levas', 'levei', 'level', 'levem', 'leves', 'levou', 'lexia', 'LGBTI', 'lhama', 'lhano', 'lhe-la', 'lhe-lo', 'liais', 'liame', 'liana', 'liara', 'liara', 'liava', 'libai', 'libam', 'libar', 'libas', 'libei', 'libem', 'LIBER', 'liber', 'libes', 'Libia', 'libio', 'libou', 'libra', 'Libra', 'libre', 'licao', 'licio', 'licor', 'licra', 'lidai', 'lidam', 'lidar', 'lidas', 'lidei', 'lidem', 'lider', 'lides', 'Lidia', 'lidio', 'lidou', 'lieis', 'ligar', 'light', 'ligre', 'lilas', 'Lilia', 'Lilio', 'limai', 'limam', 'limao', 'limar', 'limas', 'limbo', 'limei', 'limem', 'limes', 'limou', 'limpa', 'limpe', 'limpo', 'lince', 'Lince', 'linda', 'linde', 'lindo', 'linfa', 'linha', 'linho', 'Linux', 'lioes', 'liras', 'Liria', 'lirio', 'Lirio', 'lisas', 'lisco', 'lista', 'listo', 'litao', 'lites', 'litio', 'LIT-QI', 'litro', 'livel', 'Livia', 'Livio', 'livre', 'livro', 'lixar', 'lixos', 'lobby', 'lobis', 'lobos', 'local', 'locao', 'locar', 'locas', 'locro', 'locus', 'locus', 'lodao', 'loess', 'logar', '-logia', 'logos', 'logos', 'logra', 'logro', 'loica', 'loios', 'loira', 'loiro', 'lojia', 'lolio', 'lomba', 'Lomba', 'lombo', 'lonca', 'longa', 'longe', 'longo', 'lonja', 'Lopes', 'loque', 'lorda', 'lorde', 'lorfo', 'lorga', 'lorpa', 'losna', 'lotai', 'lotar', 'lotes', 'lotus', 'louca', 'louca', 'louco', 'louco', 'Loule', 'loura', 'louro', 'lousa', 'Lousa', 'luais', 'Luana', 'luara', 'luara', 'luava', 'Lucas', 'lucia', 'Lucia', 'lucio', 'Lucio', 'lucro', 'ludra', 'ludre', 'ludro', 'lueis', 'lugar', 'luges', 'lugre', 'Luigi', 'Luisa', 'luita', 'lumen', 'lumes', 'lumia', 'lunar', 'luque', 'lusco', 'lusos', 'lutai', 'lutam', 'lutar', 'lutas', 'lutei', 'lutem', 'lutes', 'lutie', 'lutou', 'luvas', 'luxai', 'luxam', 'luxar', 'luxas', 'luxei', 'luxem', 'luxes', 'luxos', 'luxou', 'luzes', 'Luzes', 'luzia', 'Luzia', 'Luzio', 'luzir', 'lycra', 'Macae', 'macao', 'Macao', 'macar', 'macas', 'macau', 'Macau', 'macha', 'macho', 'macio', 'macom', 'macro', 'macua', 'Macua', 'madre', 'Madri', 'mafia', 'mafra', 'Mafra', 'mafua', 'magas', 'Magda', 'magia', 'magma', 'magna', 'Magna', 'magno', 'Magno', 'magoa', 'magoa', 'magos', 'magra', 'magro', 'maias', 'mailu', 'Maine', 'maino', 'maior', 'maios', 'maios', 'Maira', 'Mairi', 'Mairo', 'Maisa', 'Maiso', 'major', 'malar', 'males', 'males', 'malha', 'malho', 'malho', 'malta', 'Malta', 'malte', 'malus', 'malus', 'malva', 'Malva', 'Malvo', 'mamae', 'mamal', 'mamao', 'mamar', 'mamba', 'mambo', 'mambu', 'mamis', 'mamoa', 'manar', 'manas', 'manco', 'manda', 'mande', 'mandi', 'mando', 'manes', 'manes', 'manes', 'manga', 'Manga', 'manga', 'mango', 'manha', 'manha', 'mania', '-mania', 'manir', 'manja', 'mansa', 'manso', 'manta', 'manto', 'manto', 'Maome', 'maori', 'maple', 'Maraa', 'marao', 'maras', 'Maras', 'Marau', 'Marau', 'marca', 'marco', 'Marco', 'marco', 'Marco', 'mares', 'mares', 'marga', 'maria', 'Maria', 'Maria', 'Mario', 'Mario', 'maros', 'Maros', 'marra', 'marra', 'marta', 'Marta', 'Marte', 'maser', 'massa', 'matai', 'matam', 'Matao', 'matar', 'matas', 'match', 'matei', 'matem', 'mates', 'matiz', 'matou', 'matri', 'Maues', 'maura', 'mauro', 'mause', 'meada', 'meado', 'mecha', 'media', 'media', 'medio', 'medir', 'medos', 'medra', 'medro', 'meias', 'meiga', 'meigo', 'meios', 'Meire', 'mekeo', 'melao', 'melar', 'meles', 'melga', 'melgo', 'melra', 'melro', 'Menda', 'Mendo', 'mengo', 'menir', 'menor', 'menos', 'menso', 'menta', 'mente', '-mente', 'mento', 'mento-', 'merar', 'merca', 'merce', 'merda', 'merme', 'mermo', 'mesao', 'mesas', 'meses', 'mesma', 'mesmo', 'meson', 'messe', 'mesta', 'mesto', 'metal', 'meter', 'metie', 'metro', 'metro', 'mexer', 'miado', 'miais', 'Miami', 'miara', 'miara', 'miava', 'micar', 'micha', 'miche', 'miche', 'micho', 'micro', 'micro-', 'midia', 'mieis', 'migar', 'migas', 'migre', 'migro', 'mijai', 'mijam', 'mijao', 'mijar', 'mijas', 'mijei', 'mijem', 'mijes', 'mijou', 'mikir', 'milha', 'milha', 'Milha', 'milho', 'mimar', 'mimir', 'minai', 'minam', 'minar', 'minas', 'minei', 'minem', 'mines', 'minha', 'Minix', 'MINIX', 'Minos', 'minou', 'miojo', 'miola', 'miolo', 'mioma', 'miope', 'mioto', 'mirai', 'Mirai', 'miram', 'mirar', 'miras', 'mirei', 'mirem', 'mires', 'Miria', 'mirou', 'mirra', 'mirto', 'missa', 'misse', 'misso', 'mista', 'misto', 'mitia', 'mitim', 'mitra', 'miuda', 'miudo', 'mixer', 'mixer', 'moada', 'moado', 'moais', 'mocao', 'mocar', 'mocar', 'mocas', 'mocha', 'moche', 'mocho', 'mocos', 'modal', 'modem', 'modos', 'modus', 'moeda', 'Moeda', 'moega', 'moeis', 'moela', 'Moema', 'moera', 'moera', 'mofai', 'mofam', 'mofar', 'mofas', 'mofei', 'mofem', 'mofes', 'mofou', 'mogao', 'moger', 'mogno', 'mogor', 'moiam', 'moias', 'moico', 'moido', 'moina', 'moiro', 'moita', 'Moita', 'moito', 'molar', 'molde', 'moles', 'molha', 'molhe', 'molho', 'monco', 'monda', 'monge', 'monha', 'monhe', 'monho', 'Monia', 'Moniz', 'monja', 'monso', 'monte', 'monto', 'morai', 'moral', 'moram', 'morar', 'moras', 'morca', 'morde', 'morei', 'morem', 'mores', 'morim', 'mormo', 'morno', 'Moros', 'morou', 'morre', 'morro', 'morsa', 'morso', 'morte', 'morto', 'mosca', 'mossa', 'mosto', 'motar', 'motel', 'motim', 'motor', 'Motta', 'mouco', 'moura', 'Moura', 'mouro', 'mouse', 'mouta', 'movel', '-movel', 'movem', 'mover', 'moveu', 'movia', 'moxao', 'muafo', 'Muana', 'Mucia', 'Mucio', 'mucum', 'Mucum', 'mudai', 'mudam', 'mudar', 'mudas', 'mudei', 'mudem', 'mudes', 'mudez', 'mudos', 'mudou', 'mudra', 'mufla', 'mugir', 'muita', 'muito', 'mulso', 'multa', 'multe', 'mumia', 'munde', 'mundo', 'Munio', 'munir', 'munto', 'munus', 'muque', 'Muqui', 'murar', 'murca', 'Murca', 'murco', 'muros', 'murra', 'murro', 'murta', 'musas', 'museu', 'musgo', 'musme', 'musse', 'mutua', 'Mutum', 'mutuo', 'muxao', 'nabal', 'nacao', 'nacar', 'nacem', 'nadai', 'nadam', 'nadar', 'nadas', 'nadei', 'nadem', 'nades', 'Nadia', 'nadir', 'nados', 'nadou', 'nafta', 'nagar', 'agua', 'naifa', 'naipe', 'naira', 'naite', 'nakfa', 'nalga', 'nalgo', 'nanar', 'Nanci', 'nanja', 'Naomi', 'Naque', 'nariz', 'narom', 'nasal', 'nasce', 'nassa', 'na?sua', 'natal',
                             'Natal', 'Natan', 'natro', 'natto', 'Nauns', 'Nauru', 'naval', 'navio', 'necho', 'necra', 'necro-', 'nedia', 'nedio', 'nefro-', 'negao', 'negar', 'negra', 'n�gre', 'negro', 'negue', 'nehan', 'nelas', 'Nelas', 'neles', 'nenem', 'nenia', 'nente', 'Nepal', 'Nereu', 'nerio', 'nervo', 'nesga', 'nesgo', 'nessa', 'nesse', 'nesta', 'neste', 'netos', 'nevai', 'nevam', 'nevar', 'nevas', 'nevei', 'nevem', 'neves', 'Neves', 'nevoa', 'nevou', 'nhama', 'nhoca', 'nicar', 'nicha', 'nicho', 'nielo', 'Niger', 'nigua', 'Nilas', 'Nilos', 'Nilza', 'nimbo', 'nimio', 'ninai', 'ninam', 'ninar', 'ninas', 'ninei', 'ninem', 'nines', 'ninfa', 'ninho', 'ninja', 'ninou', 'niple', 'Nipoa', 'niqab', 'nisco', 'nisso', 'nisto', 'nitro', 'nivea', 'Nivea', 'nivel', 'niveo', 'Niveo', 'niver', 'niver', 'no?ato', 'nobel', 'nobel', 'nobre', 'nocao', 'nodar', 'nodoa', 'Noemi', 'nogai', 'noiro', 'noite', 'noiva', 'Noiva', 'noivo', 'Noivo', 'nojar', 'no-las', 'no-los', 'nomes', 'nonas', 'nonde', 'nonos', 'nonos', 'noras', 'norma', 'Norma', 'Normo', 'norsa', 'norte', 'nossa', 'nosso', 'notar', 'notas', 'notem', 'notou', 'nouca', 'noute', 'novas', 'novel', 'noves', 'novos', 'no?way', 'noxio', 'nubea', 'nubeo', 'nubia', 'Nubia', 'nubil', 'nubio', 'Nubio', 'nucao', 'nudes', 'nudez', 'Nuele', 'nuelo', 'numas', 'nunca', 'nuper-', 'nuvem', 'nuveo', 'nuvre', 'nylon', 'oasis', 'obeso', 'obice', 'obito', 'oboes', 'obolo', 'obrai', 'obram', 'obrar', 'obras', 'obrei', 'obrem', 'obres', 'obrou', 'obsta', 'obste', 'obsto', 'obter', 'obvio', 'ocapi', 'Ocara', 'ocaso', 'octal', 'oculo', 'ocupa', 'odeao', 'odeom', 'odeon', 'odiar', 'odios', 'oeste', 'ofuro', 'ofuro', 'ogham', 'ogiva', 'oirar', 'oitao', 'oitos', 'olear', 'olhai', 'Olhao', 'olhar', 'olhos', 'oliva', 'Oliva', 'olive', 'olivo', 'Olivo', 'ombro', 'omega', 'omega', 'omega', 'omnia', 'oncas', 'ondas', 'ontem', 'opaca', 'opaco', 'opala', 'opcao', 'opera', 'opere', 'opero', 'opimo', 'opine', 'opino', '-opsia', 'optai', 'optam', 'optar', 'optas', 'optei', 'optem', 'optes', 'optou', 'oquei', 'oraca', 'orais', '-orama', 'orara', 'orara', 'orate', 'orava', 'orcar', 'ordem', 'oreis', 'orfao', 'orfas', 'Orfeu', 'orgao', 'orgia', 'Oriao', 'oribi', 'orina', 'Orion', 'Orion', 'Orion', 'Orixa', 'orixa', 'orlar', 'ornai', 'ornam', 'ornar', 'ornas', 'ornei', 'ornem', 'ornes', 'ornis', 'ornou', 'Orobo', 'Oroco', 'oromo', 'Osaca', 'Osaka', 'Oscar', 'oscar', 'Oscar', 'osmar', 'Osmar', 'osmio', 'osram', 'ossea', 'osseo', 'ossos', 'ostra', 'ostro', 'otaku', 'Otava', 'otica', 'otico', 'otimo', 'otite', 'ougar', 'ouija', 'ourai', 'ouram', 'ourar', 'ouras', 'ourei', 'ourem', 'Ourem', 'oures', 'ouros', 'ourou', 'ousar', 'ousas', 'ousou', 'outao', 'outra', 'outro', 'ouvia', 'ouvir', 'ouviu', 'ovino', 'ovulo', 'oxala', 'oxide', 'oxido', 'oxido', 'Pabla', 'Pablo', 'pacas', 'pacer', 'pacos', 'pacto', 'padel', 'padre', 'paeja', 'pafia', 'pafio', 'Pafos', 'pagao', 'pagar', 'pager', 'pague', 'Paial', 'paiba', 'paica', 'Pains', 'paiol', 'paire', 'pairo', 'Paiva', 'paixa', 'pajem', 'palao', 'Palas', 'Palau', 'palco', 'palha', 'palie', 'palio', 'palio', 'palma', 'Palma', 'palme', 'palmo', 'PALOP', 'palor', 'palpo', 'palra', 'palue', 'pampa', 'pampo', 'panal', 'panca', 'panca', 'panda', 'pando', 'pandu', 'pango', 'panos', 'panta', 'Paola', 'Paolo', 'papai', 'papal', 'papao', 'papar', 'papel', 'paper', 'pa-pum', 'parai', 'Parai', 'param', 'parar', 'paras', 'Parau', 'parba', 'parca', 'parco', 'pardo', 'parea', 'parei', 'parem', 'pareo', 'pareo', 'pares', 'parga', 'pargo', 'paria', 'pario', 'parir', 'Paris', 'pariu', 'parla', 'parou', 'parra', 'parro', 'parte', 'parto', 'parva', 'parvo', 'pasmo', 'passa', 'passe', 'passo', 'paste', 'pasto', 'pasto', 'patas', 'patau', 'patch', 'patia', '-patia', 'patim', 'patio', 'Patis', 'patoa', 'patos', 'Patos', 'patua', 'pauis', 'Paula', 'Paulo', 'pausa', 'pauta', 'paute', 'pauto', 'pavao', 'Pavao', 'pavia', 'pavio', 'pavoa', 'pavor', 'pazes', 'PCdoB', 'pecar', 'pecas', 'pecha', 'pedal', 'pedes', 'pedia', 'pedir', 'pediu', 'pedra', 'Pedra', 'Pedro', 'pegar', 'pegou', 'peida', 'peido', 'peina', 'peite', 'peito', 'peixa', 'peixe', 'Peixe', 'pejar', 'pelai', 'pelai', 'pelam', 'pelar', 'pelas', 'pelei', 'pelem', 'peles', 'Peleu', 'pelos', 'pelos', 'pelou', 'pemba', 'penai', 'penal', 'penam', 'penar', 'penas', 'penca', 'pence', 'pende', 'penei', 'penem', 'penes', 'penha', 'Penha', 'penis', 'penis', 'penny', 'penou', 'pense', 'penso', 'pente', 'peoes', 'peona', 'pequi', 'Pequi', 'peras', 'peras', 'perca', 'perda', 'perde', 'perdi', 'perla', 'Perla', 'perle', 'perlo', 'Perlo', 'perna', 'perro', 'persa', 'per?se', 'per?si', 'perto', 'perua', 'perus', 'pesai', 'pesam', 'pesar', 'pesas', 'pesca', 'pesco', 'pesei', 'pesem', 'peses', 'pesou', 'peste', 'petar', 'petiz', 'Petra', 'peuga', 'peuva', 'piaba', 'piada', 'pialo', 'piano', 'piara', 'piara', 'Piata', 'Piaui', 'piava', 'picao', 'picar', 'picas', 'picha', 'piche', 'picho', 'picle', 'Picos', 'Picui', 'picum', 'pieis', 'piema', 'piese', 'pifao', 'pifar', 'pifio', '-pigio', 'pilai', 'pilam', 'pilao', 'pilar', 'Pilar', 'pilas', 'pilei', 'pilem', 'piles', 'pilha', 'pilhe', 'pilho', 'pilio', 'pilou', 'pilum', 'pimba', 'pinca', 'pinel', 'pineu', 'pinga', 'pingo', 'pinha', 'pinho', 'pinta', 'pinte', 'pinto', 'Pinto', 'Pio?IX', 'piola', 'piora', 'piore', 'pioro', 'pique', 'piqui', 'Pirai', 'pirao', 'pirar', 'pires', 'Pires', 'pirex', 'pirou', 'Pirro', 'pirua', 'pisai', 'pisam', 'pisar', 'pisas', 'pisca', 'pisci-', 'pisco', 'pisei', 'pisem', 'pises', 'pisou', 'pista', 'pisto', 'pitao', 'piteu', 'Piuma', 'pivot', 'pixel', 'pixel', 'pizza', 'placa', 'plaga', 'plana', 'plane', 'plano', 'plato', 'plebe', 'plena', 'pleno', 'plica', 'pluma', 'pluri-', 'pneus', 'pobre', 'Pocao', 'pocar', 'pocha', 'pocos', 'podao', 'podar', 'podem', 'poder', 'podia', 'podio', 'podoa', 'podre', 'poejo', 'poema', 'poeta', 'Poeta', 'pogon-', 'poial', 'poisa', 'poita', 'poite', 'poito', 'pojai', 'pojam', 'pojar', 'pojas', 'pojei', 'pojem', 'pojes', 'pojou', 'polar', 'polas', 'polca', 'polen', 'polho', 'polia', 'polir', 'polis', 'polos', 'polos', 'polpa', 'polvo', 'pomar', 'pomba', 'pombo', 'pomes', 'pomos', 'pompa', 'ponde', 'ponei', 'ponei', '-ponga', 'ponho', 'ponta', 'ponte', 'ponto', 'popos', 'popos', 'porao', 'poras', 'porca', 'porco', 'porem', 'porno', 'porno', 'porno-', 'porra', 'porre', 'porri-', 'porro', 'por?si', 'porta', 'porta-', 'porte', 'porto', 'Porto', 'posar', 'posem', 'possa', 'posse', 'Posse', 'posso', 'posta', 'poste', 'posto', 'Potim', 'potra', 'potro', 'pouca', 'pouco', 'poula', 'poule', 'poulo', 'pound', 'poupa', 'poupe', 'poupo', 'pousa', 'pouso', 'pouta', 'Povoa', 'povos', 'praca', 'prado', 'Prado', 'praga', 'Praga', 'praia', 'Praia', 'prali', 'prata', 'Prata', 'prato', 'Prato', 'praxa', 'praxe', 'prazo', 'preao', 'prebe', 'prece', 'preco', 'prega', 'prego', 'preia', 'preju', 'prelo', 'presa', 'prese', 'preso', 'preta', 'preto', 'preza', 'preze', 'prezo', 'prima', 'primo', 'prior', 'proas', 'probo', 'proce', 'proer', 'profe', 'prois', 'prole', 'PRONA', 'prono', 'prosa', 'proto', 'prova', 'prove', 'provo', 'pruir', 'prumo', 'psico-', 'psoas', 'PTdoB', '-ptero', 'ptose', 'puara', 'puava', 'pubis', 'pucha', 'puder', 'pudim', 'pudor', 'puela', 'puera', 'pugil', 'pujai', 'pujam', 'pujar', 'pujas', 'pujei', 'pujem', 'pujes', 'pujou', 'pular', 'pulga', 'pulgo', 'pulha', 'pulse', 'pulso', 'punas', 'punga', 'punha', 'punho', 'punir', 'puras', 'purga', 'putao', 'putas', 'putos', 'puxai', 'puxam', 'puxao', 'puxar', 'puxas', 'puxei', 'puxem', 'puxes', 'puxou', 'Qatar', 'quais', 'quare', 'quark', 'quaro', 'quase', 'quasi', 'Quata', 'quati', 'queca', 'queda', 'quede', 'quede', 'quedo', 'quepe', 'quero', 'que?so', 'queto', 'quibe', 'quica', 'quico', 'quilo', 'quilo-', 'quina', 'quipa', 'quite', 'Quito', 'quiui', 'quivi', 'quixo', 'quota', 'rabao', 'Rabat', 'rabaz', 'rabil', 'racao', 'racas', 'racha', 'rache', 'racho', 'racum', 'radao', 'radar', 'radio', 'radio-', 'radon', 'rafai', 'rafam', 'rafar', 'rafas', 'rafei', 'rafem', 'rafes', 'rafou', 'raial', 'raiar', 'raide', 'raion', 'raios', 'raio-x', 'raio?X', 'raiva', 'rajar', 'ralai', 'ralam', 'ralar', 'ralas', 'ralei', 'ralem', 'rales', 'ralho', 'rally', 'ralou', 'ramai', 'ramal', 'ramam', 'Ramao', 'ramar', 'ramas', 'ramei', 'ramem', 'rames', 'ramos', 'Ramos', 'ramou', 'rampa', 'ranca', 'ranco', 'ranco', 'rango', 'ranho', 'rapai', 'rapam', 'rapar', 'rapas', 'rapaz', 'rapei', 'rapel', 'rapem', 'rapes', 'rapou', 'rapto', 'raque', 'rasar', 'rasas', 'rasca', 'rasga', 'rasgo', 'rasos', 'raspa', 'raspe', 'raspo', 'rasto', 'ratai', 'ratam', 'ratao', 'ratar', 'ratas', 'ratei', 'ratem', 'rates', 'ratos', 'ratou', 'razao', 'razia', 'reaca', 'reais', 'rebar', 'reboo', 'recem', 'recho', 'recta', 'recto', 'recua', 'recua', 'recuo', 'redea', 'redes', 'redil', 'redor', 'refem', 'refil', 'refri', 'regai', 'regal', 'regar', 'regas', 'reger', 'regia', 'regia', 'Regia', 'regio', 'Regio', 'Regis', 'regra', 'regre', 'regro', 'regua', 'reide', 'reima', 'reine', 'reino',
                             'rejao', 'relao', 'relar', 'reler', 'reles', 'relha', 'relho', 'reluz', 'relva', 'remai', 'remam', 'remar', 'remas', 'remei', 'remem', 'remes', 'remir', 'remix', 'remoa', 'remoi', 'remoi', 'remoo', 'remos', 'remou', 'renal', 'Renan', 'renca', 'renda', 'rende', 'rengo', 'renio', 'renio', 'rente', 'repor', 'repos', 'repto', 'resma', 'reste', 'resto', 'retas', 'reter', 'retos', 'retro', 'retro', 'retro', 'reuso', 'revel', 'rever', 'reves', 'rexio', 'rezai', 'rezam', 'rezar', 'rezas', 'rezei', 'rezem', 'rezes', 'rezou', 'riade', 'riana', 'ribas', 'ricar', 'ricas', 'ricos', 'rifao', 'rifar', 'rifle', 'rifte', 'rigor', 'rijao', 'rijar', 'rijos', 'rilex', 'rimai', 'rimam', 'rimar', 'rimas', 'rimei', 'rimel', 'rimem', 'rimes', 'rimou', 'rindo', 'rinha', 'rinso', 'ripar', 'risca', 'risco', 'risse', 'riste', 'ritao', 'Ritas', 'ritmo', 'ritos', 'Ritos', 'riuta', 'rival', 'rober', 'robot', 'rocar', 'rocar', 'rocas', 'rocas', 'rocaz', 'rocha', 'rocia', 'rocie', 'rocim', 'rocio', 'rodai', 'rodam', 'rodar', 'rodas', 'rodei', 'rodem', 'rodes', 'Rodes', 'rodio', 'rodou', 'rogar', 'rogue', 'roiam', 'roido', 'rojai', 'rojam', 'rojao', 'rojar', 'rojas', 'rojei', 'rojem', 'rojes', 'rojos', 'rojou', 'rolai', 'rolam', 'rolao', 'rolar', 'rolas', 'rolda', 'rolde', 'roldo', 'rolei', 'rolem', 'roles', 'rolha', 'rolhe', 'rolho', 'rolou', 'romai', 'romam', 'romao', 'Romao', 'romar', 'romas', 'Romas', 'romas', 'rombo', 'romei', 'romem', 'romes', 'romeu', 'romou', 'ronco', 'ronda', 'ronde', 'rondo', 'ronha', 'roque', 'rosai', 'rosal', 'rosam', 'rosar', 'rosas', 'Rosas', 'rosca', 'rosea', 'rosei', 'rosem', 'roseo', 'roses', 'rosna', 'rosne', 'rosno', 'Rosos', 'rosou', 'rosto', 'rotar', 'rouba', 'roube', 'roubo', 'rouca', 'rouco', 'roupa', 'roxas', 'roxos', 'ruada', 'rubia', 'Rubia', 'rubim', 'Rubim', 'rubis', 'rublo', 'rubor', 'rubra', 'rubro', 'rudos', 'ruela', 'rufar', 'rufie', 'rufio', 'rufos', 'rugbi', 'rugby', 'rugir', 'ruide', 'ruido', 'ruido', 'ruina', 'ruivo', 'rumai', 'rumam', 'rumar', 'rumas', 'rumba', 'rumei', 'rumem', 'rumes', 'rumor', 'rumou', 'rupia', 'rural', 'rusga', 'russa', 'russo', 'rutar', 'Rutes', 'saami', 'sabao', 'sabei', 'saber', 'sabia', 'sabia', 'sabia', 'sabio', 'sable', 'sabor', 'sabra', 'sabre', 'sacal', 'sacar', 'sacho', 'sacie', 'sacio', 'sacra', 'sacro', 'sacue', 'sadra', 'saeta', 'safar', 'safos', 'safra', 'sagaz', 'sagra', 'sagre', 'sagro', 'sagui', 'Sahel', 'saiam', 'saias', 'saiba', 'saibo', 'saida', 'saido', 'Saire', 'saite', 'salai', 'salao', 'salar', 'salas', 'salaz', 'saldo', 'salei', 'salem', 'sales', 'Sales', 'salga', 'salho', 'Saloa', 'salou', 'salsa', 'salso', 'salta', 'salte', 'salto', 'Salto', 'salva', 'Salva', 'salve', 'salvo', 'Salvo', 'samba', 'samio', 'Samoa', 'Sampa', 'Sanca', 'sande', 'sando', 'sanei', 'sanga', 'sanha', 'sanie', 'sanja', 'Sanja', 'santa', 'Santa', 'santa', 'santo', 'Santo', 'sapao', 'sapos', 'saque', 'saque', 'saque', 'sarai', 'saram', 'sarao', 'sarar', 'saras', 'Saras', 'sarau', 'sarca', 'sarda', 'sardo', 'sarei', 'sarem', 'sares', 'sarga', 'sarja', 'sarna', 'saros', 'Saros', 'sarou', 'Sarra', 'sarro', 'sarta', 'sarta', 'Satao', 'Satao', 'sauco', 'saude', 'Saude', 'Sauis', 'Saula', 'Saulo', 'sauna', 'sauva', 'savel', 'Savia', 'Savio', 'saxao', 'sazao', 'schwa', 'scifi', 'sci-fi', 'scout', 'seara', 'Seara', 'secao', 'secar', 'secos', 'sedan', 'sedas', 'sedes', 'SEDEX', 'sedia', 'segar', 'segre', 'segue', 'sei?ca', 'sei?la', 'seios', 'seira', 'seita', 'seita', 'seiva', 'seixo', 'sejam', 'sejas', 'selar', 'selem', 'selha', 'SELIC', 'selim', 'selva', 'semen', 'semen', 'semis', 'semis', 'senao', 'senas', 'senda', 'sendo', 'senha', 'senil', 'senio', 'senio', 'Senna', 'senra', 'senso', 'sente', 'sento', 'sepia', 'serao', 'seras', 'serei', 'serem', 'seres', 'seria', 'seria', 'serie', 'serio', 'Serio', 'Serpa', 'serra', 'Serra', 'serre', 'serro', 'Serro', 'serta', 'Serta', 'serva', 'serve', 'servi', 'servo', 'sesgo', 'sesma', 'sesso', 'sesta', 'setar', 'setas', 'setes', 'setor', 'seu?cu', 'sevai', 'sevam', 'sevar', 'sevas', 'sevei', 'sevem', 'seves', 'sevou', 'sexos', 'sexta', 'sexti-', 'sexto', '-sfera', 'shape', 'sheik', 'shojo', 'short', 'shoyu', 'siclo', 'sidas', 'sidos', 'sidra', 'Siene', 'sifao', 'sigla', 'sigma', 'signo', 'Silas', 'silex', 'silfo', 'silha', 'silte', 'silva', 'Silva', 'simao', 'Simao', 'simil', 'simio', 'sinal', 'sinao', 'sindi', 'Sines', 'sinha', 'Sinop', 'sinta', 'sinto', 'sioux', 'SIPAM', 'sique', 'sirga', 'sirgo', 'siria', 'Siria', 'sirim', 'sirio', 'sirte', 'sirvo', 'sismo', 'Sista', 'Sisto', 'sitio', 'SIVAM', 'skate', 'skiff', 'slack', 'slang', 'slick', 'slide', 'snack', 'soada', 'soado', 'soais', 'soara', 'soara', 'soava', 'sobem', 'sobes', 'sobeu', 'sobpe', 'sobra', 'sobre', 'sobre-', 'socar', 'socio', 'sodio', 'soeis', 'soera', 'soera', 'sofas', 'Sofia', 'Sofia', 'Sofio', 'sofre', 'sogra', 'sogro', 'soiam', 'soias', 'soito', 'solao', 'solar', 'solaz', 'solda', 'solde', 'soldo', 'soles', 'solha', 'solho', 'solio', 'solta', 'solte', 'solto', 'somai', 'somam', 'somar', 'somas', 'somei', 'somem', 'somes', 'somos', 'somou', 'sonar', 'sonda', 'sonha', 'sonhe', 'sonho', 'sonsa', 'sonso', 'sopas', 'sopor', 'sopre', 'sopro', 'so?que', 'sorca', 'sorgo', 'sorna', 'soror', 'soror', 'soros', 'sorte', 'sorva', 'sorvo', 'sosia', 'sosso', 'sotao', 'soube', 'Soure', 'Sousa', 'souta', 'souto', 'Souza', 'sovai', 'sovam', 'sovar', 'sovas', 'sovei', 'sovem', 'soves', 'sovou', 'sport', 'spray', 'sprue', 'staff', 'stand', 'stick', 'stock', 'stoll', 'stout', 'suabe', 'suado', 'suave', 'suazi', 'subam', 'subas', 'subia', 'subir', 'subis', 'subiu', 'subst.', 'sucho', 'sucia', 'sucre', 'Sucre', 'SUDAM', 'Sudao', 'sudro', 'sueco', 'Sueli', 'sueto', 'suevo', 'sufle', 'sugar', 'suica', 'Suica', 'suico', 'suino', 'suite', 'sujai', 'sujam', 'sujar', 'sujas', 'sujei', 'sujem', 'sujes', 'sujos', 'sujou', 'sulco', 'sumir', 'SUNAB', 'Sunda', 'super', 'super-', 'supor', 'supre', 'surca', 'surda', 'surdo', 'surfe', 'surfo', 'surra', 'surro', 'surto', 'susao', 'susas', 'sushi', 'sussa', 'susta', 'suste', 'susto', 'sutia', 'sutil', 'sutil', 'sutis', 'swing', 'Tabai', 'tabao', 'ta?bem', 'ta?bom', 'tabua', 'Tabua', 'tabus', 'tacar', 'tacha', 'tache', 'tacho', 'taful', 'taier', 'taiga', 'taiko', 'taina', 'Taina', 'taipa', 'Taipu', 'Taise', 'Taiua', 'talai', 'talam', 'talao', 'talar', 'talas', 'talco', 'talei', 'talem', 'tales', 'Tales', 'talha', 'talhe', 'talho', 'Talia', 'Talia', 'talim', 'Talim', 'Talio', 'talio', 'Talio', 'talou', 'tamao', 'tamem', 'tamil', 'tamos', 'tampa', 'tampe', 'tampo', 'tanas', 'tanca', 'tanga', 'tange', 'tango', 'tanha', 'tanho', 'tansa', 'tanso', 'tanta', 'tanta', 'tanto', 'taoca', 'tao-so', 'taoso', 'tapai', 'tapam', 'tapar', 'tapas', 'tapei', 'tapem', 'tapes', 'Tapes', 'tapir', 'tapou', 'tapua', 'taqui-', 'tarar', 'tarda', 'tarde', 'tardo', 'tarja', 'tarot', 'tarro', 'tarso', 'tasca', 'tasco', 'tasto', 'tatil', 'Tatui', 'tauro-', 'tavao', 'taxai', 'taxam', 'taxar', 'taxas', 'taxei', 'taxem', 'taxes', 'taxis', 'taxon', 'taxou', 'tchau', 'Tebas', 'tecer', 'tecla', 'tecle', 'teclo', 'tecno', 'tecto', 'tedio', 'Teera', 'teiga', 'teima', 'teime', 'teimo', 'teipe', 'teito', 'teixo', 'telai', 'telam', 'telao', 'telar', 'telas', 'Telas', 'telei', 'telem', 'teles', 'Teles', 'telex', 'telha', 'Telha', 'telho', 'Telos', 'telou', 'temao', 'temas', 'temba', 'temer', 'temia', 'temor', 'temos', 'tempo', 'tenaz', 'tenca', 'tenca', 'tenda', 'tende', 'tendo', 'tenha', 'tenho', 'tenia', 'tenis', 'tenis', 'tenor', 'tenra', 'tenro', 'tensa', 'tenso', 'tenta', 'tente', 'tento', 'tenue', 'tenue', 'tenui-', 'terao', 'teras', 'terca', 'terco', 'terco', 'terei', 'tergo', 'teria', '-terio', 'terma', 'termo', 'termo-', 'terna', 'terno', 'terra', 'Terra', 'terso', 'tesai', 'tesam', 'tesao', 'tesar', 'tesas', 'tesei', 'tesem', 'teses', 'Teseu', 'tesla', 'tesou', 'tesse', 'testa', 'teste', 'testo', 'tetas', 'Tetis', 'tetra', 'tetro', 'tetum', 'teudo', 'teuto', 'Texas', 'texto', 'Tiaga', 'Tiago', 'tiara', 'tibar', 'Tibau', 'tibio', 'tibum', 'ticao', 'ticar', 'tidas', 'tidos', 'tiete', 'Tiete', 'Tifeu', 'tigre', 'tilar', 'tilia', 'tilte', 'timao', 'Timao', 'timba', 'timbo', 'Timbo', 'timer', 'Timon', 'tiner', 'tinge', 'Tinge', 'tinha', 'tinir', 'tinta', 'tinto', 'tiple', 'tipoi', 'tique', 'tirai', 'tiram', 'tirar', 'tiras', 'tirei', 'tirem', 'tires', 'tiros', 'Tiros', 'tirou', 'tirso', 'tisne', 'tisso', 'tissu', 'titia', 'titio', 'tiver', 'tmese', 'toada', 'toari', 'tocam', 'tocar', 'tocha', 'tocho', 'tocou', 'todas', 'todos', 'togar', 'toica', 'toira', 'toiro', 'tojal', 'token', 'Tokyo', 'tolar', 'tolda', 'toldo', 'tolho', 'tomai', 'tomam', 'tomar', 'Tomar', 'tomas', 'tomba', 'tombe', 'tombo', 'tomei', 'tomem', 'tomes', 'tomos', 'tomou', 'tonal', 'tonar', 'tonas', 'tonel', 'toner', 'toner', 'tonga', 'Tonga', 'tonho', 'tonta', 'tonto', 'topai', 'topam', 'topar', 'topas', 'topei', 'topem', 'topes', 'topou', 'toque', 'toral', 'torar', 'torax', 'torco', 'torda', 'tordo', 'torga', 'torgo', 'torio',
                             'torna', 'torne', 'torno', 'torpe', 'torre', 'torso', 'torta', 'torto', 'torvo', 'tosar', 'tosco', 'tosse', 'tosta', 'toste', 'total', 'totos', 'touca', 'touca', 'touco', 'toupa', 'toura', 'touro', 'Touro', 'touta', 'toxia', 'traca', 'trace', 'traco', 'traem', 'trago', 'trair', 'traje', 'trajo', 'trama', 'trame', 'trans-', 'trapo', 'trara', 'trash', 'trata', 'trate', 'trato', 'trave', 'travo', 'treco', 'trela', 'trema', 'treme', 'tremi', 'trena', 'treno', 'treno', 'trens', 'trepa', 'trepe', 'trepo', 'tresa', 'treta', 'treus', 'treva', 'trevo', 'treze', 'trial', 'tribo', 'trica', 'trick', 'triga', 'trigo', 'trilo', 'trina', 'trino', 'trios', 'tripa', 'tripe', 'troar', 'troba', 'troca', 'troca', 'troco', 'troco', 'Trofa', 'Troia', 'Troia', 'trole', 'troll', 'trono', 'tropa', 'tropo', 'trote', 'trova', 'truao', 'truco', 'trufa', 'truta', 'tuaca', 'tubas', 'tubos', 'tufao', 'tugir', 'tugue', 'tuide', 'tuite', 'tulha', 'Tulia', 'tulio', 'Tulio', 'tumba', 'tumor', 'tunar', 'Tunas', 'tunda', 'tunel', 'Tunes', 'tunga', 'Tunis', 'tupas', 'tupas', 'tupis', 'turba', 'turbe', 'turbo', 'turco', 'turfa', 'turma', 'turne', 'turno', 'turuq', 'turve', 'turvo', 'Turvo', 'tusco', 'tutai', 'tutam', 'tutar', 'tutas', 'tutei', 'tutem', 'tutes', 'tutia', 'tutor', 'tutou', 'tutum', 'tweed', 'twist', 'uaica', 'uambe', 'uaura', 'ubaia', 'Ubata', 'ubere', 'UCCLA', 'Uchoa', 'ufano', 'UFRGS', 'Uibai', 'uiste', 'uivai', 'uivam', 'uivar', 'uivas', 'uivei', 'uivem', 'uives', 'uivos', 'uivou', 'ulear', 'Ulpia', 'Ulpio', 'ultra-', 'ulula', 'ulule', 'ululo', 'umami', 'Umari', 'umbro', 'umero', 'umido', 'uncao', 'ungir', 'unhar', 'unhas', 'Unhos', 'uniao', 'Uniao', 'unica', 'unico', 'unida', 'unido', 'untar', 'uolof', 'Urano', 'Urano', 'urdia', 'urdir', 'ureia', 'urgir', 'Uribe', 'urico', 'urina', 'urine', 'urino', 'urnas', 'urrar', 'urrul', 'ursas', 'ursos', 'urubu', 'urupa', 'Urupa', 'urupe', 'urutu', 'urzal', 'usada', 'usado', 'usais', 'usara', 'usara', 'usava', 'useis', 'usina', 'usmar', 'Ustra', 'usual', 'usura', 'utero', 'uvaia', 'uviar', 'uvula', 'uyezd', 'vacao', 'vacar', 'vacua', 'vacum', 'vacuo', 'vadia', 'vadio', 'Vaduz', 'vagao', 'vagar', 'vagem', 'vagir', 'Vagos', 'vaiar', 'vaibe', 'valao', 'valar', 'valas', 'Valda', 'Valdo', 'valer', 'vales', 'valha', 'valia', 'valor', 'valsa', 'valse', 'valso', 'valva', 'vamos', 'vampe', 'Vanda', 'Vando', 'Vania', 'Vanio', 'vao-se', 'vapor', 'varai', 'varam', 'varao', 'varar', 'varas', 'varei', 'varem', 'vares', 'varga', 'varge', 'varia', 'varia', 'vario', 'vario', 'variz', 'varja', 'varou', 'vasco', 'Vasco', 'vasos', 'vasto', 'vatel', 'vates', 'vatio', 'vazai', 'vazam', 'vazao', 'vazar', 'vazas', 'vazei', 'vazem', 'vazes', 'Vazes', 'vazia', 'vazio', 'vazou', 'veada', 'veado', 'vedar', 'vedes', 'vedor', 'vedra', 'vedro', 'vegan', 'veias', 'Veiga', 'veiro', 'vejam', 'velai', 'velai', 'velam', 'velar', 'velas', 'Velas', 'velei', 'velem', 'veles', 'velha', 'velho', 'velou', 'veloz', 'vem?ca', 'venal', 'vence', 'venci', 'venda', 'vende', 'vendo', 'venha', 'venho', 'venia', 'venia', 'venta', 'vento', 'venus', 'venus', 'Venus', 'Venus', 'vepsa', 'vepso', 'verao', 'Verao', 'veras', 'Veras', 'veras', 'veraz', 'verba', 'verbo', 'Verbo', 'verca', 'verde', 'verei', 'verga', 'verge', 'veria', 'verme', 'veros', 'Veros', 'verso', 'verte', 'vesgo', 'vespa', 'Vesta', 'veste', 'vesti', 'vetao', 'vetar', 'vetor', 'vexar', 'vezes', 'viada', 'viado', 'viaja', 'viaje', 'viajo', 'Viana', 'vibra', 'vicio', 'vidar', 'vidas', 'video', 'vides', 'vidra', 'vidro', 'viela', 'Viena', 'viera', 'vigar', 'viger', 'vigia', 'Vigia', 'vigie', 'vigil', 'vigio', 'vigor', 'vilao', 'vilas', 'viloa', 'vimos', 'vinca', 'vinco', 'vinda', 'vinde', 'vindo', 'vinga', 'vinha', 'vinho', 'vinil', 'vinis', 'vinte', 'viola', 'virai', 'viral', 'viram', 'virao', 'virar', 'viras', 'viras', 'virei', 'virem', 'vires', 'Virgo', 'viria', 'viril', 'viris', 'virol', 'virou', 'virus', 'visao', 'visar', 'visco', 'Viseu', 'visgo', 'visom', 'vison', 'visse', 'vista', 'viste', 'visto', 'vital', 'Vitor', 'viuva', 'viuvo', 'vivas', 'vivaz', 'viver', 'vivia', 'vivos', 'voava', 'vocal', 'voces', 'VOCLP', 'vodca', 'vodka', 'voeja', 'vogal', 'vogam', 'vogar', 'vogas', 'voile', 'vo-las', 'volei', 'volei', 'vo-los', 'volpe', 'VOLPs', 'volta', 'volte', 'volto', 'volts', 'vomer', 'vomer', 'voraz', 'vosco', 'vossa', 'vosso', 'votai', 'votam', 'votar', 'votas', 'votei', 'votem', 'votes', 'votos', 'votou', 'vougo', 'vozes', 'vulgo', 'vulto', 'vulva', 'vurmo', 'waika', 'wolof', 'xabre', 'xacho', 'xacra', 'xador', 'xaile', 'xamas', 'xampu', 'Xango', 'xarda', 'xardo', 'xarel', 'xarem', 'xaria', 'xaria', 'xaual', 'xaxar', 'xaxim', 'Xaxim', 'xebra', 'xebre', 'xeica', 'xelim', 'xenao', 'xenio', 'xenon', 'xenon', 'xeque', 'xerem', 'xerez', 'Xerez', 'xerox', 'xerox', 'xerpa', 'Xexeu', 'xhosa', 'xiita', 'ximbe', 'xinga', 'xinto', 'Xista', 'xisto', 'Xisto', 'x-nove', 'xocar', 'xofar', 'xofre', 'xogum', 'xopim', 'xorca', 'xordo', 'xorte', 'xotai', 'xotam', 'xotar', 'xotas', 'xotei', 'xotem', 'xotes', 'xotou', 'xouva', 'x-tudo', 'xuate', 'xucro', 'xurro', 'yacht', 'zagal', 'zagre', 'zaino', 'Zaira', 'Zairo', 'zamba', 'zambi', 'Zambi', 'zambi', 'zambo', 'zanga', 'zanze', 'zanzo', 'zapar', 'zavar', 'zazao', 'zebra', 'zebro', 'Zeila', 'zelam', 'zelar', 'Zelia', 'Zelio', 'zelos', 'zepto-', 'zerar', 'zeros', 'zeugo', 'zicha', 'zicho', 'zinco', 'zinga', 'zinir', 'zipai', 'zipam', 'zipar', 'zipas', 'zipei', 'zipem', 'ziper', 'zipes', 'zipou', 'zloti', 'zloty', 'zoeia', 'zoiao', 'zoico', 'zoico', 'zoilo', 'zoira', 'zomba', 'zombe', 'zombo', 'zonar', 'zonca', 'zorra', 'zorro', 'zoupo', 'zoura', 'zuate', 'zucar', 'zuela', 'zumbi', 'Zumbi', 'zunge', 'zunia', 'zunir', 'zupar', 'zurra', 'zurre', 'zurro', 'zuruo', 'zurza', 'abrir', 'adiar', 'afiar', 'aguar', 'andar', 'arder', 'assar', 'babar', 'bater', 'boiar', 'cacar', 'calar', 'casar', 'cavar', 'cocar', 'comer', 'curar', 'domar', 'falar', 'falir', 'ferir', 'frear', 'fugir', 'guiar', 'lavar', 'ligar', 'lixar', 'lutar', 'mirar', 'nadar', 'negar', 'nevar', 'odiar', 'olhar', 'ouvir', 'pagar', 'pisar', 'podar', 'polir', 'pular', 'puxar', 'ralar', 'regar', 'rezar', 'rodar', 'rolar', 'secar', 'socar', 'sujar', 'sumir', 'tocar', 'trair', 'uivar', 'votar', 'mexer', 'fazer', 'vigor', 'sanar', 'poder', 'expor', 'haver', 'pesar', 'coser', 'dizer', 'saber', 'dever', 'temor', 'ceder', 'estar', 'cozer', 'pudor', 'criar', 'impor', 'pedir', 'falar', 'devir', 'fluir', 'puder', 'visar', 'valor', 'temer', 'lugar', 'gerar', 'obter', 'abrir', 'tomar', 'reter', 'olhar', 'favor', 'levar', 'tecer', 'selar', 'achar', 'fator', 'ouvir', 'rogar', 'viver', 'citar', 'adiar', 'rever', 'deter', 'humor', 'labor', 'atuar', 'remir', 'lider', 'ficar', 'velar', 'cocar', 'cacar', 'anuir', 'rigor', 'botar', 'impar', 'lazer', 'morar', 'furor', 'maior', 'pegar', 'vetor', 'setor', 'ardor', 'comer', 'reger', 'rezar', 'mudar', 'parar', 'fugir', 'andar', 'fruir', 'fitar', 'puxar', 'gerir', 'tirar', 'arcar', 'sumir', 'fixar', 'ligar', 'tocar', 'lidar', 'alcar', 'autor', 'bater', 'supor', 'caber', 'zelar', 'pisar', 'advir', 'super', 'pilar', 'rumor', 'optar', 'medir', 'vetar', 'ecoar', 'cover', 'artur', 'virar', 'casar', 'ornar', 'tiver', 'assar', 'tutor', 'vedar', 'arfar', 'depor', 'gabar', 'bazar', 'inter', 'ambar', 'pavor', 'odiar', 'segar', 'pomar', 'minar', 'vagar', 'aviar', 'jogar', 'negar', 'urdir', 'podar', 'esgar', 'bulir', 'apear', 'jazer', 'matar', 'redor', 'mover', 'gemer', 'calor', 'sabor', 'lutar', 'mimar', 'nacar', 'ousar', 'reler', 'corar', 'subir', 'urgir', 'repor', 'sugar', 'valer', 'viger', 'ferir', 'pagar', 'trair', 'raiar', 'pular', 'notar', 'beber', 'domar', 'focar', 'untar', 'mofar', 'regar', 'errar', 'taxar', 'vazar', 'rolar', 'hiper', 'banir', 'menor', 'sacar', 'polir', 'soror', 'rubor', 'danar', 'fedor', 'gofer', 'relar', 'afear', 'altar', 'sarar', 'ungir', 'mater', 'guiar', 'dotar', 'munir', 'curar', 'solar', 'cegar', 'lesar', 'mijar', 'atear', 'rocar', 'aliar', 'cotar', 'chiar', 'lagar', 'punir', 'vogar', 'somar', 'lavor', 'locar', 'logar', '', 'catar', 'jurar', 'aguar', 'luzir', 'tinir', 'colar', 'mirar', 'legar', 'fucar', 'tosar', 'mixar', 'topar', 'parir', 'falir', 'meter', 'lixar', 'rugir', 'tacar', 'mugir', 'bolor', 'rufar', 'secar', 'orcar', 'posar', 'bufar', 'vizir', 'penar', 'calar', 'cagar', 'gorar', 'jugar', 'durar', 'alvor', 'sedar', 'lavar', 'varar', 'ziper', 'votar', 'arder', 'eivar', 'pecar', 'polar', 'frear', 'vapor', 'talar', 'cevar', 'amuar', 'vaiar', 'laser', 'vexar', 'acuar', 'manar', 'tenor', 'ditar', 'afiar', 'decor', 'decor', 'picar', 'zunir', 'balir', 'urrar', 'andor', 'dosar', 'girar', 'safar', 'major', 'tapar', 'palor', 'prior', 'ganir', 'furar', 'vicar', 'nadar', 'datar', 'radar', 'ralar', 'cavar', 'sujar', 'motor', 'nadir', 'aluir', 'gavar', 'arear', 'socar', 'latir', 'pirar', 'dopar', 'uivar', 'sitar', 'toner', 'horar', 'femur', 'rumar', 'sovar', 'boiar', 'toler', 'fadar', 'dolar', 'limar', 'rodar', 'gizar', 'obrar', 'foyer', 'armar', 'rimar',
                             'ledor', 'mamar', 'ticar', 'pocar', 'feder', 'torar', 'licor', 'babar', 'idear', 'rapar', 'pelar', 'remar', 'filar', 'pejar', 'lunar', 'avoar', 'aster', 'poser', 'cocar', 'albor', 'desar', 'caiar', 'acoar', 'sonar', 'tumor', 'troar', 'altor', 'fugar', 'pitar', 'oscar', 'fanar', 'fumar', 'alvar', 'ninar', 'aurir', 'paper', 'bolar', 'novar', 'zerar', 'bisar', 'delir', 'atoar', 'timer', 'color', 'lenir', 'impar', 'luxar', 'macar', 'tarar', 'visor', 'revir', 'rojar', 'melar', 'capar', 'dolor', 'libar', 'rifar', 'vitor', 'pinar', 'tugir', 'lotar', 'sevar', 'alter', 'retar', 'angor', 'dador', 'mitar', 'gamar', 'malar', 'mocar', 'liber', 'bicar', 'balar', 'nevar', 'bular', 'molar', 'pifar', 'retor', 'rotar', 'xotar', 'tesar', 'triar', 'algar', 'finar', 'cesar', 'dobar', 'papar', 'lacar', 'sinar', 'vidar', 'agrar', 'tapir', 'fogar', 'Edgar', 'antar', 'incar', 'vedor', 'esmar', 'orlar', 'volar', 'vagir', 'honor', 'bajar', 'seder', 'fluor', 'later', 'rasar', 'sucar', 'empar', 'unhar', 'prear', 'redar', 'eluir', 'bodar', 'gomor', 'rotor', 'nanar', 'gelar', 'gadar', 'lizar', 'pager', 'duzir', 'rajar', 'tonar', 'mojar', 'telar', 'cerar', 'lufar', 'sopor', 'aluar', 'pujar', 'arpar', 'livor', 'engar', 'aptar', 'alear', 'aflar', 'bogar', 'murar', 'vigar', 'lacar', 'airar', 'menir', 'faiar', 'suber', 'Vitor', 'galar', 'tepor', 'farar', 'tufar', 'olear', 'weber', 'algor', 'ester', 'lupar', 'ermar', 'tunar', 'Oscar', 'marar', 'gular', 'tubar', 'rijar', 'rafar', 'pojar', 'dedar', 'cubar', 'aziar', 'piper', 'rizar', 'Artur', 'dicar', 'ilhar', 'sorar', 'alfar', 'ultor', 'rarar', 'ratar', 'betar', 'sutar', 'camar', 'turar', 'ripar', 'gafar', 'zefir', 'monir', 'rosar', 'aduar', 'pubar', 'bagar', 'litor', 'hilar', 'arrar', 'Heber', 'gruir', 'valar', 'binar', 'palar', 'augir', 'tanar', 'rucar', 'nicar', 'outar', 'liber', 'bifar', 'pruir', 'rocar', 'docar', 'litar', 'gomar', 'copar', 'ricar', 'sapar', 'vilar', 'iscar', 'folar', 'bitar', 'rugar', 'debar', 'migar', 'golar', 'ribar', 'gener', 'tibar', 'lemur', 'sabir', 'vezar', 'reder', 'hacer', 'aunar', 'fofar', 'aspar', 'nazir', 'tetar', 'micar', 'lurar', 'iriar', 'pigar', 'menar', 'algur', 'nutar', 'favar', 'fular', 'digar', 'vacar', 'tuber', 'vomer', 'zenir', 'tilar', 'macar', 'rixar', 'ourar', 'azoar', 'amear', 'gomor', 'rupar', 'proar', 'sisar', 'ondar', 'extar', 'sodar', 'laxar', 'manir', 'gaiar', 'padar', 'bofar', 'mocar', 'tecar', 'fagar', 'rorar', 'cisar', 'bacar', 'rober', 'bafar', 'dinar', 'panar', 'tolar', 'agror', 'timor', 'veiar', 'cucar', 'jatar', 'zinir', 'alhur', 'ricar', 'aulir', 'xador', 'bobar', 'rular', 'gemar', 'ervar', 'gatar', 'bojar', 'colir', 'bocar', 'agiar', 'ougar', 'sogar', 'eider', 'petar', 'obvir', 'cruor', 'lobar', 'sular', 'lanar', 'seter', 'bocar', 'fobar', 'opiar', 'sibar', 'eruir', 'echar', 'poiar', 'nodar', 'zonar', 'goiar', 'suxar', 'rebar', 'mazar', 'oirar', 'orear', 'biter', 'baiar', 'ostar', 'moxar', 'cuter', 'taler', 'invar', 'aboar', 'pidir', 'alfir', 'pelor', 'vimar', 'eixar', 'gajar', 'samur', 'atuir', 'tenar', 'damar', 'maser', 'zunar', 'gebar', 'tenar', 'ulnar', 'undar', 'fasor', 'vezer', 'apuar', 'alcar', 'tupir', 'fecer', 'catur', 'butir', 'cifar', 'faxar', 'dacar', 'tinor', 'nafir', 'armur', 'jacer', 'iodar', 'vicor', 'nagar', 'oigar', 'fenar', 'sisor', 'cibar', 'astur', 'nagor', 'uviar', 'bezar', 'usmar', 'bimar', 'nidor', 'buvar', 'mudir', 'mesor', 'eicar', 'ridor', 'mogor', 'arxar', 'badur', 'titor', 'robur', 'groir', 'bador', 'hepar', 'alfur', 'nufar', 'cinor', 'giaur', 'siler', 'mucor', 'mucor', 'lacar', 'neper', 'moral', 'casal', 'bocal', 'banal', 'legal', 'vital', 'cabal', 'igual', 'ideal', 'sinal', 'venal', 'fatal', 'atual', 'local', 'geral', 'coral', 'letal', 'rival', 'natal', 'rural', 'final', 'axial', 'usual', 'modal', 'canal', 'vogal', 'basal', 'total', 'anual', 'ramal', 'varal', 'areal', 'metal', 'fanal', 'nodal', 'sacal', 'vagal', 'vocal', 'nasal', 'viral', 'mural', 'penal', 'fecal', 'focal', 'naval', 'pedal', 'sisal', 'bucal', 'foral', 'dedal', 'acral', 'bocal', 'graal', 'fetal', 'bucal', 'renal', 'papal', 'Natal', 'feral', 'zagal', 'rosal', 'ileal', 'nabal', 'poial', 'seral', 'tonal', 'zonal', 'retal', 'magal', 'cocal', 'asnal', 'peral', 'urzal', 'didal', 'podal', 'horal', 'ducal', 'dotal', 'paral', 'arral', 'erval', 'olhal', 'regal', 'pural', 'datal', 'toral', 'gazal', 'sural', 'badal', 'babal', 'genal', 'sapal', 'noval', 'panal', 'dural', 'coval', 'matal', 'faial', 'camal', 'arnal', 'senal', 'fural', 'abdal', 'jugal', 'sonal', 'nogal', 'notal', 'noxal', 'irial', 'nopal', 'sedal', 'bical', 'pocal', 'arcal', 'pical', 'ligal', 'ilhal', 'lobal', 'jocal', 'copal', 'breal', 'cecal', 'rocal', 'saial', 'nanal', 'fogal', 'arval', 'boral', 'frial', 'raial', 'soral', 'gatal', 'agnal', 'faval', 'coxal', 'mamal', 'docal', 'vacal', 'argal', 'macal', 'rinal', 'hemal', 'aveal', 'rogal', 'dogal', 'pipal', 'rodal', 'tojal', 'pigal', 'molal', 'saval', 'janal', 'tecal', 'liral', 'antal', 'fumal', 'goral', 'musal', 'buxal', 'bobal', 'alhal', 'tical', 'ripal', 'tunal', 'vibal', 'sozal', 'tagal', 'nucal', 'amial', 'paual', 'rijal', 'gaial', 'nonal', 'gomal', 'sabal', 'tajal', 'ulnal', 'itral', 'urjal', 'uveal', 'pojal', 'xibiu', 'jirau', 'abriu', 'judeu', 'museu', 'sarau', 'tchau', 'fugiu', 'xampu', 'urubu', 'piteu', 'bambu', 'curau', 'valeu', 'liceu', 'lundu', 'labeu', 'cacau', 'ilheu', 'chabu', 'hindu', 'mandu', 'beiju', 'guacu', 'chiru', 'bangu', 'xexeu', 'perau', 'pineu', 'nambu', 'mitou', 'marau', 'xareu', 'babau', 'cachu', 'urutu', 'teteu', 'romeu', 'acaju', 'bauru', 'arpeu', 'tedeu', 'aratu', 'urucu', 'jambu', 'gagau', 'heteu', 'timbu', 'aqueu', 'geteu', 'pacau', 'soveu', 'abreu', 'ipadu', 'sabeu', 'coreu', 'macau', 'pireu', 'abaju', 'tambu', 'recru', 'grisu', 'solau', 'mingu', 'lareu', 'chifu', 'suacu', 'mambu', 'acapu', 'estau', 'ecuru', 'mangu', 'enteu', 'espru', 'hereu', 'Alceu', 'manau', 'calau', 'buchu', 'pilau', 'leteu', 'nemeu', 'mungu', 'cumbu', 'manju', 'itapu', 'urucu', 'parau', 'apicu', 'armeu', 'apecu', 'padeu', 'nandu', 'careu', 'amadu', 'patau', 'ajuru', 'tarau', 'acacu', 'ganau', 'iracu', 'atapu', 'jurau', 'acreu', 'arabu', 'aruru', 'etneu', 'argau', 'febeu', 'catau', 'muleu', 'aburu', 'ajeru', 'funeu', 'bairu', 'camau', 'apitu', 'sizau', 'ligeu', 'arreu', 'gundu', 'mairu', 'polau', 'aracu', 'cudzu', 'anibu', 'burnu', 'numbu', 'vileu', 'aricu', 'equeu', 'ijebu', 'tebeu', 'caicu', 'irucu', 'gabeu', 'parvu', 'ameju', 'sobeu', 'aticu', 'amamu', 'eubeu', 'cefeu', 'dundu', 'ipecu', 'puacu', 'uracu', 'ubucu', 'paleu', 'feleu', 'fareu', 'taibu', 'gruau', 'mongu', 'fruxu', 'tanau', 'fajau', 'inamu', 'remau', 'uassu', 'mecru', 'uperu', 'truxu', 'ucubu', 'icacu', 'caacu', 'paolu', 'libau', 'boiru', 'enibu', 'poacu', 'uaucu', 'uvacu', 'aquem', 'assim', 'porem', 'detem', 'comum', 'nenem', 'ordem', 'homem', 'ontem', 'enfim', 'facam', 'jovem', 'advem', 'algum', 'pajem', 'motim', 'retem', 'refem', 'forem', 'forum', 'viram', 'nuvem', 'jejum', 'recem', 'deram', 'album', 'obtem', 'harem', 'regem', 'latim', 'vagem', 'aipim', 'mirim', 'batom', 'hajam', 'capim', 'macom', 'totem', 'cupom', 'pudim', 'coxim', 'cetim', 'xaxim', 'futum', 'bagem', 'alfim', 'rocim', 'polem', 'modem', 'botim', 'cupim', 'Belem', 'butim', 'xerem', 'salem', 'bebum', 'vacum', 'patim', 'selim', 'cumim', 'setim', 'creem', 'serum', 'dalem', 'cauim', 'tamem', 'xelim', 'rubim', 'mutum', 'emfim', 'tucum', 'jetom', 'racum', 'sedem', 'terem', 'cedem', 'talim', 'simum', 'morim', 'redem', 'japim', 'rolim', 'calom', 'cecem', 'mucum', 'espim', 'marim', 'mugem', 'estim', 'motum', 'balim', 'pecem', 'calim', 'perem', 'ourem', 'ladim', 'bedum', 'petum', 'tilim', 'menim', 'lapim', 'batim', 'maxim', 'gazim', 'raiom', 'ratim', 'cecum', 'begum', 'rotim', 'ambom', 'baxim', 'molim', 'velum', 'cotim', 'ticum', 'torem', 'calum', 'caxim', 'barem', 'petim', 'tubim', 'tetum', 'andim', 'tudum', 'malim', 'navim', 'pelem', 'larim', 'petem', 'igbim', 'colim', 'velum', 'tecum', 'cacim', 'achem', 'tutum', 'ondim', 'rebem', 'bedem', 'oquim', 'armim', 'badem', 'acaem', 'lesim', 'arbim', 'homum', 'mucum', 'metim', 'gatum', 'mulum', 'achim', 'gruim', 'surim', 'perum', 'tesum', 'rodim', 'mutom', 'rutim', 'tamom', 'sagum', 'telim', 'chaem', 'astim', 'bocim', 'mamum', 'fruam', 'titim', 'tetim', 'pirum', 'bafum', 'dabom', 'cagom', 'falum', 'agrem', 'urdim', 'basim', 'anzom', 'parum', 'farum', 'pitem', 'rupim', 'oonim', 'abohm', 'sivom', 'galem', 'ietim', 'gafem', 'iguem', 'amago', 'negro', 'exito', 'termo', 'senso', 'afeto', 'secao', 'inato', 'justo', 'muito', 'razao', 'anexo', 'sonho', 'amigo', 'lapso', 'mutuo', 'dengo', 'tempo', 'entao', 'avido', 'genro', 'brado', 'crivo', 'animo', 'digno', 'sendo', 'culto', 'mundo', 'censo', 'vicio', 'vulgo', 'denso', 'louco', 'jeito', 'tenro', 'pifio', 'mesmo', 'servo', 'sabio', 'juizo', 'cunho', 'limbo', 'manso', 'posso', 'vendo', 'afago', 'ebrio', 'serio', 'certo', 'acaso', 'pleno', 'impio', 'obvio', 'exodo', 'falso', 'garbo', 'fluxo', 'tedio', 'uniao', 'ritmo', 'burro',
                             'visao', 'parvo', 'bravo', 'genio', 'prumo', 'grato', 'parco', 'laico', 'ameno', 'obito', 'nocao', 'ranco', 'nicho', 'anelo', 'coeso', 'fardo', 'epico', 'cisao', 'ativo', 'sinto', 'passo', 'dubio', 'unico', 'tendo', 'outro', 'leigo', 'sonso', 'exato', 'amplo', 'sulco', 'arduo', 'velho', 'gesto', 'claro', 'ponto', 'hiato', 'terno', 'vacuo', 'marco', 'varao', 'senao', 'fusao', 'probo', 'leito', 'farao', 'doido', 'vazio', 'apoio', 'tanto', 'pouco', 'torco', 'verso', 'dorso', 'signo', 'feito', 'mocao', 'credo', 'preso', 'ciclo', 'casto', 'arido', 'aceso', 'banzo', 'livro', 'carro', 'vulto', 'salvo', 'vasto', 'plano', 'antro', 'morro', 'ocaso', 'prado', 'atomo', 'avaro', 'otimo', 'junto', 'aureo', 'chulo', 'serao', 'grupo', 'opcao', 'nacao', 'campo', 'prazo', 'bando', 'tenso', 'tosco', 'idolo', 'risco', 'vilao', 'reino', 'psico', 'aviao', 'indio', 'texto', 'corpo', 'preto', 'soldo', 'logro', 'cheio', 'filho', 'verbo', 'apego', 'estao', 'virao', 'atrio', 'alado', 'solto', 'coito', 'exijo', 'lindo', 'apelo', 'fraco', 'doido', 'pardo', 'opaco', 'navio', 'astro', 'etico', 'cioso', 'junco', 'irmao', 'macio', 'nosso', 'douto', 'pagao', 'bicho', 'posto', 'torso', 'molho', 'curso', 'abuso', 'video', 'asilo', 'igneo', 'orfao', 'turvo', 'radio', 'vosso', 'combo', 'baixo', 'calao', 'ereto', 'agudo', 'gosto', 'facho', 'estio', 'traco', 'sitio', 'facto', 'meigo', 'feudo', 'tento', 'mosto', 'podio', 'cocho', 'chato', 'aluno', 'brabo', 'lasso', 'peito', 'pareo', 'boato', 'rubro', 'pacto', 'cacho', 'pasmo', 'cetro', 'licao', 'finjo', 'calmo', 'idoso', 'plumo', 'aviso', 'ebano', 'corso', 'tribo', 'conto', 'macro', 'cargo', 'fruto', 'perco', 'atimo', 'vento', 'berro', 'saldo', 'seixo', 'arado', 'fosso', 'beijo', 'surto', 'estro', 'vazao', 'ticao', 'trato', 'amado', 'pinho', 'canso', 'perto', 'bruto', 'silvo', 'irado', 'orgao', 'laudo', 'bucho', 'regio', 'vadio', 'clero', 'xucro', 'troco', 'cenho', 'canto', 'lesao', 'visto', 'sotao', 'proto', 'cinto', 'largo', 'morfo', 'lesto', 'horto', 'ruido', 'penso', 'ileso', 'santo', 'ufano', 'mocho', 'umido', 'fundo', 'verao', 'simio', 'resto', 'narco', 'misto', 'trago', 'manto', 'salmo', 'preco', 'troco', 'alamo', 'demao', 'cosmo', 'banto', 'barao', 'findo', 'audio', 'venho', 'bolso', 'barro', 'retro', 'limpo', 'louro', 'calvo', 'macho', 'coevo', 'enjoo', 'gueto', 'longo', 'forro', 'farto', 'fatuo', 'sexto', 'lucro', 'vario', 'cacto', 'custo', 'puido', 'sadio', 'cardo', 'lento', 'socio', 'diabo', 'disso', 'patio', 'mouro', 'aereo', 'roubo', 'pavio', 'racio', 'cervo', 'nisso', 'tibio', 'tacho', 'cisco', 'dobro', 'abono', 'volto', 'pedro', 'caibo', 'veado', 'obolo', 'ei-lo', 'curto', 'hirto', 'cedro', 'valho', 'milho', 'ibero', 'souto', 'rouco', 'ducto', 'cento', 'azedo', 'Pedro', 'magno', 'furto', 'causo', 'miudo', 'mento', 'pondo', 'guizo', 'vindo', 'botao', 'apuro', 'reuso', 'lombo', 'brejo', 'nedio', 'balao', 'tropo', 'limao', 'prelo', 'primo', 'roseo', 'bardo', 'cerco', 'fecho', 'uncao', 'sacro', 'filao', 'morto', 'ninho', 'gonzo', 'beico', 'vinco', 'nimbo', 'pinto', 'gibao', 'susto', 'cesto', 'trigo', 'burgo', 'adido', 'tanso', 'abaco', 'crido', 'folgo', 'atono', 'tonto', 'teuto', 'talho', 'couro', 'broto', 'nisto', 'bufao', 'porco', 'plexo', 'bloco', 'potro', 'bordo', 'recuo', 'duelo', 'porao', 'banco', 'lerdo', 'emulo', 'medio', 'pulso', 'suino', 'cirio', 'friso', 'prato', 'saudo', 'turno', 'barco', 'abito', 'rosto', 'fungo', 'ratio', 'lenho', 'grito', 'vinho', 'calco', 'laivo', 'rango', 'braco', 'queto', 'accao', 'quilo', 'hidro', 'fosco', 'magro', 'ferro', 'bulbo', 'gordo', 'galho', 'testo', 'choro', 'circo', 'palio', 'gemeo', 'turco', 'grifo', 'adubo', 'mamao', 'galgo', 'globo', 'cravo', 'sarro', 'beato', 'mouco', 'apoio', 'cinco', 'punho', 'palco', 'russo', 'repto', 'metro', 'grado', 'bispo', 'bolao', 'abalo', 'lhano', 'vesgo', 'suado', 'scopo', 'edito', 'busto', 'torno', 'mando', 'salto', 'acido', 'banho', 'azimo', 'moido', 'gesso', 'lauto', 'gnomo', 'labio', 'piano', 'touro', 'surdo', 'murro', 'tombo', 'capao', 'fulvo', 'siclo', 'usado', 'porto', 'visgo', 'musgo', 'apito', 'grego', 'cecao', 'pario', 'manco', 'sopro', 'disto', 'pilao', 'fogao', 'pocao', 'vidro', 'sento', 'envio', 'trapo', 'nosco', 'pasto', 'neuro', 'dardo', 'caldo', 'salao', 'casao', 'gasto', 'atico', 'tongo', 'rojao', 'melao', 'lanco', 'edito', 'rasto', 'ostio', 'unido', 'fisco', 'ombro', 'efebo', 'cesao', 'cilio', 'visco', 'imago', 'sifao', 'sezao', 'dueto', 'melro', 'racao', 'fiado', 'amido', 'xingo', 'ruivo', 'lirio', 'septo', 'treco', 'atado', 'miolo', 'travo', 'caido', 'folio', 'adito', 'tufao', 'aceno', 'pouso', 'grilo', 'etimo', 'freio', 'berco', 'agito', 'ancho', 'paulo', 'torto', 'falto', 'noivo', 'corro', 'oligo', 'baiao', 'talao', 'sabao', 'micro', 'morbo', 'anglo', 'exido', 'acabo', 'frevo', 'morno', 'ganho', 'dacao', 'doudo', 'forno', 'quedo', 'istmo', 'guapo', 'timao', 'pavao', 'falho', 'loiro', 'bruxo', 'amaro', 'zonzo', 'relho', 'bambo', 'parto', 'cerro', 'trino', 'galao', 'viuvo', 'rapto', 'pidao', 'carao', 'xisto', 'coiso', 'mixto', 'senho', 'basto', 'impio', 'casco', 'linho', 'asado', 'cicio', 'babao', 'fauno', 'invio', 'rasao', 'gorro', 'rombo', 'crono', 'erado', 'jarro', 'soado', 'alelo', 'toldo', 'prego', 'ovino', 'trono', 'otico', 'apodo', 'duplo', 'obeso', 'oculo', 'saido', 'bilro', 'tordo', 'senio', 'garfo', 'sismo', 'sorvo', 'ofato', 'peido', 'trevo', 'angio', 'litro', 'lixao', 'azado', 'bujao', 'treno', 'ganso', 'tampo', 'italo', 'ranho', 'fiapo', 'truco', 'polvo', 'jogao', 'Egito', 'perro', 'azoto', 'pisao', 'osseo', 'arpao', 'bafio', 'icaro', 'apupo', 'cisto', 'meato', 'choco', 'fujao', 'morao', 'abeto', 'mogno', 'tardo', 'sogro', 'gamao', 'mirto', 'pingo', 'mango', 'helio', 'sirio', 'utero', 'cupao', 'torvo', 'congo', 'floxo', 'ovulo', 'nervo', 'turbo', 'truao', 'sueto', 'puxao', 'rengo', 'cromo', 'golfo', 'necro', 'tramo', 'nubio', 'tecto', 'diogo', 'meado', 'cauto', 'umero', 'sodio', 'cacao', 'jorro', 'cobro', 'zimbo', 'bisao', 'pialo', 'corvo', 'grumo', 'colmo', 'terco', 'micho', 'rasgo', 'nardo', 'alveo', 'baldo', 'chamo', 'nimio', 'pombo', 'bugio', 'zurro', 'zaino', 'pirao', 'recto', 'lusco', 'floco', 'solio', 'opimo', 'acaro', 'cusco', 'tecno', 'ficto', 'chego', 'guiao', 'porro', 'cuido', 'vagao', 'fusco', 'imoto', 'fasto', 'terso', 'buzio', 'corco', 'disco', 'gajao', 'julio', 'vosco', 'pealo', 'suico', 'palmo', 'sengo', 'xibio', 'licio', 'Fabio', 'valao', 'croco', 'malho', 'guaxo', 'pravo', 'frago', 'flato', 'bocio', 'ricto', 'lepto', 'bonzo', 'teixo', 'bidao', 'ciano', 'jambo', 'histo', 'anuro', 'latao', 'catao', 'rocio', 'tacao', 'lenco', 'mario', 'acato', 'coado', 'afogo', 'Corao', 'julho', 'corto', 'Il.mo', 'ronco', 'serro', 'aporo', 'junho', 'dedao', 'doado', 'anoso', 'amino', 'apolo', 'rifao', 'birro', 'durao', 'abano', 'silfo', 'tango', 'zinco', 'aceto', 'facao', 'saxao', 'tambo', 'tinto', 'tavao', 'chico', 'titio', 'dromo', 'gatao', 'ludio', 'volvo', 'oitao', 'pielo', 'marco', 'paleo', 'trajo', 'gongo', 'curvo', 'avito', 'aparo', 'locao', 'nucao', 'grafo', 'corgo', 'tredo', 'gabao', 'ralho', 'furao', 'sazao', 'celso', 'fanho', 'chuco', 'pluto', 'clivo', 'adejo', 'niveo', 'imigo', 'edipo', 'cerdo', 'cerio', 'lismo', 'cotao', 'picho', 'folho', 'graxo', 'bingo', 'chipo', 'cordo', 'endro', 'lanho', 'nacho', 'miado', 'cloro', 'facao', 'valgo', 'vasco', 'virgo', 'saibo', 'podao', 'cuspo', 'talco', 'glifo', 'toico', 'sorro', 'burco', 'tosso', 'bento', 'tarso', 'tacto', 'finco', 'iroso', 'zesto', 'ambao', 'terio', 'meiao', 'jongo', 'zorro', 'simao', 'mauro', 'solao', 'areio', 'bruco', 'dendo', 'cagao', 'creto', 'orago', 'outao', 'aboio', 'japao', 'curro', 'dicao', 'frito', 'perno', 'flaco', 'crico', 'decho', 'balho', 'oucao', 'girio', 'zinho', 'pango', 'flavo', 'anato', 'amago', 'parro', 'basco', 'garco', 'mambo', 'caico', 'cirro', 'dreno', 'sardo', 'sorgo', 'jungo', 'vasso', 'chibo', 'oxido', 'cosco', 'panco', 'tarro', 'mingo', 'Paulo', 'polho', 'rocio', 'curdo', 'citro', 'arguo', 'modio', 'fordo', 'ofego', 'clono', 'salso', 'afixo', 'flexo', 'apero', 'comao', 'betao', 'bioco', 'litio', 'trilo', 'peplo', 'adelo', 'libio', 'crato', 'panto', 'dingo', 'alilo', 'rolao', 'couto', 'guano', 'areao', 'anodo', 'brumo', 'pitao', 'masto', 'sarco', 'telio', 'londo', 'saiao', 'socao', 'Dario', 'zarro', 'copio', 'fanio', 'acero', 'piado', 'enojo', 'atino', 'anulo', 'carpo', 'aleto', 'provo', 'povao', 'bumbo', 'nitro', 'sosso', 'mesto', 'cereo', 'romao', 'bango', 'conho'
                             )


i = random.randint(0, 1000)
termo_play = t_5charS[i] #termo sem acentuação
termo_play_Acento = t_5charC[i] #termo com acentuação

print(termo_play)



class Palavra_App(toga.App):


    def startup(self):


        button_width = 40
        t0 = '_'
        e0 = '_'
        r0 = '_'
        m0 = '_'
        o0 = '_'

        t1 = '_'
        e1 = '_'
        r1 = '_'
        m1 = '_'
        o1 = '_'

        t2 = '_'
        e2 = '_'
        r2 = '_'
        m2 = '_'
        o2 = '_'

        t3 = '_'
        e3 = '_'
        r3 = '_'
        m3 = '_'
        o3 = '_'

        t4 = '_'
        e4 = '_'
        r4 = '_'
        m4 = '_'
        o4 = '_'

        t5 = '_'
        e5 = '_'
        r5 = '_'
        m5 = '_'
        o5 = '_'

        # Janela principal do app
        main_box = toga.Box(style=Pack(direction=COLUMN, alignment='center', flex=1))


        # janela que guarda todas as box de tentativas
        termos_page_box = toga.Box(style=Pack(direction=COLUMN, alignment='center', flex=1))
        teclado_box = toga.Box(style=Pack(direction=COLUMN, alignment='center', flex=1))

        # criação de cada box que representa cada tentativa
        termo1_box = toga.Box(style=Pack(padding_top=10, padding_left=10, padding_right= 10, alignment='center', flex=1))
        termo2_box = toga.Box(style=Pack(padding_top=10, padding_left=10, padding_right= 10, alignment='center', flex=1))
        termo3_box = toga.Box(style=Pack(padding_top=10, padding_left=10, padding_right= 10, alignment='center', flex=1))
        termo4_box = toga.Box(style=Pack(padding_top=10, padding_left=10, padding_right= 10, alignment='center', flex=1))
        termo5_box = toga.Box(style=Pack(padding_top=10, padding_left=10, padding_right= 10, alignment='center', flex=1))
        termo6_box = toga.Box(style=Pack(padding_top=10, padding_left=10, padding_right= 10, alignment='center', flex=1))


        #box para cada letra *******************************
        #tentativa1
        self.letra_t0 = toga.Box(style=Pack(padding_top=10, padding_left=10, padding_right= 10, background_color='Gainsboro', alignment='center', flex=1))
        self.letra_e0 = toga.Box(style=Pack(padding_top=10, padding_left=10, padding_right= 10, background_color='Gainsboro', alignment='center', flex=1))
        self.letra_r0 = toga.Box(style=Pack(padding_top=10, padding_left=10, padding_right= 10, background_color='Gainsboro', alignment='center', flex=1))
        self.letra_m0 = toga.Box(style=Pack(padding_top=10, padding_left=10, padding_right= 10, background_color='Gainsboro', alignment='center', flex=1))
        self.letra_o0 = toga.Box(style=Pack(padding_top=10, padding_left=10, padding_right= 10, background_color='Gainsboro', alignment='center', flex=1))

        #tentativa2
        self.letra_t1 = toga.Box(style=Pack(padding_top=10, padding_left=10, padding_right= 10, background_color='Gainsboro', alignment='center', flex=1))
        self.letra_e1 = toga.Box(style=Pack(padding_top=10, padding_left=10, padding_right= 10, background_color='Gainsboro', alignment='center', flex=1))
        self.letra_r1 = toga.Box(style=Pack(padding_top=10, padding_left=10, padding_right= 10, background_color='Gainsboro', alignment='center', flex=1))
        self.letra_m1 = toga.Box(style=Pack(padding_top=10, padding_left=10, padding_right= 10, background_color='Gainsboro', alignment='center', flex=1))
        self.letra_o1 = toga.Box(style=Pack(padding_top=10, padding_left=10, padding_right= 10, background_color='Gainsboro', alignment='center', flex=1))

        #tentativa3
        self.letra_t2 = toga.Box(style=Pack(padding_top=10, padding_left=10, padding_right= 10, background_color='Gainsboro', alignment='center', flex=1))
        self.letra_e2 = toga.Box(style=Pack(padding_top=10, padding_left=10, padding_right= 10, background_color='Gainsboro', alignment='center', flex=1))
        self.letra_r2 = toga.Box(style=Pack(padding_top=10, padding_left=10, padding_right= 10, background_color='Gainsboro', alignment='center', flex=1))
        self.letra_m2 = toga.Box(style=Pack(padding_top=10, padding_left=10, padding_right= 10, background_color='Gainsboro', alignment='center', flex=1))
        self.letra_o2 = toga.Box(style=Pack(padding_top=10, padding_left=10, padding_right= 10, background_color='Gainsboro', alignment='center', flex=1))

        #tentativa4
        self.letra_t3 = toga.Box(style=Pack(padding_top=10, padding_left=10, padding_right= 10, background_color='Gainsboro', alignment='center', flex=1))
        self.letra_e3 = toga.Box(style=Pack(padding_top=10, padding_left=10, padding_right= 10, background_color='Gainsboro', alignment='center', flex=1))
        self.letra_r3 = toga.Box(style=Pack(padding_top=10, padding_left=10, padding_right= 10, background_color='Gainsboro', alignment='center', flex=1))
        self.letra_m3 = toga.Box(style=Pack(padding_top=10, padding_left=10, padding_right= 10, background_color='Gainsboro', alignment='center', flex=1))
        self.letra_o3 = toga.Box(style=Pack(padding_top=10, padding_left=10, padding_right= 10, background_color='Gainsboro', alignment='center', flex=1))

        #tentativa5
        self.letra_t4 = toga.Box(style=Pack(padding_top=10, padding_left=10, padding_right= 10, background_color='Gainsboro', alignment='center', flex=1))
        self.letra_e4 = toga.Box(style=Pack(padding_top=10, padding_left=10, padding_right= 10, background_color='Gainsboro', alignment='center', flex=1))
        self.letra_r4 = toga.Box(style=Pack(padding_top=10, padding_left=10, padding_right= 10, background_color='Gainsboro', alignment='center', flex=1))
        self.letra_m4 = toga.Box(style=Pack(padding_top=10, padding_left=10, padding_right= 10, background_color='Gainsboro', alignment='center', flex=1))
        self.letra_o4 = toga.Box(style=Pack(padding_top=10, padding_left=10, padding_right= 10, background_color='Gainsboro', alignment='center', flex=1))

        #tentativa6
        self.letra_t5 = toga.Box(style=Pack(padding_top=10, padding_left=10, padding_right= 10, background_color='Gainsboro', alignment='center', flex=1))
        self.letra_e5 = toga.Box(style=Pack(padding_top=10, padding_left=10, padding_right= 10, background_color='Gainsboro', alignment='center', flex=1))
        self.letra_r5 = toga.Box(style=Pack(padding_top=10, padding_left=10, padding_right= 10, background_color='Gainsboro', alignment='center', flex=1))
        self.letra_m5 = toga.Box(style=Pack(padding_top=10, padding_left=10, padding_right= 10, background_color='Gainsboro', alignment='center', flex=1))
        self.letra_o5 = toga.Box(style=Pack(padding_top=10, padding_left=10, padding_right= 10, background_color='Gainsboro', alignment='center', flex=1))


        #***************************************************

        # criação das janelas de input e botão

        self.contador = '0' #controle de acesso ao número de tentativas do game, condição de acesso a cada condicional da função


        # Criação de cada espaço para tentativas
        self.output1 = toga.Label(t0, style=Pack(font_size=40, padding_left=21, direction=ROW, flex=1, alignment='center', text_align='center', font_family='verdana', font_weight = 'bold'))
        self.output2 = toga.Label(e0, style=Pack(font_size=40, padding_left=21, direction=ROW, flex=1, alignment='center', text_align='center', font_family='verdana', font_weight = 'bold'))
        self.output3 = toga.Label(r0, style=Pack(font_size=40, padding_left=21, direction=ROW, flex=1, alignment='center', text_align='center', font_family='verdana', font_weight = 'bold'))
        self.output4 = toga.Label(m0, style=Pack(font_size=40, padding_left=21, direction=ROW, flex=1, alignment='center', text_align='center', font_family='verdana', font_weight = 'bold'))
        self.output5 = toga.Label(o0, style=Pack(font_size=40, padding_left=21, direction=ROW, flex=1, alignment='center', text_align='center', font_family='verdana', font_weight = 'bold'))

        self.output6 = toga.Label(t1, style=Pack(font_size=40, padding_left=21, direction=ROW, flex=1, alignment='center', text_align='center', font_family='verdana', font_weight = 'bold'))
        self.output7 = toga.Label(e1, style=Pack(font_size=40, padding_left=21, direction=ROW, flex=1, alignment='center', text_align='center', font_family='verdana', font_weight = 'bold'))
        self.output8 = toga.Label(r1, style=Pack(font_size=40, padding_left=21, direction=ROW, flex=1, alignment='center', text_align='center', font_family='verdana', font_weight = 'bold'))
        self.output9 = toga.Label(m1, style=Pack(font_size=40, padding_left=21, direction=ROW, flex=1, alignment='center', text_align='center', font_family='verdana', font_weight = 'bold'))
        self.output10 = toga.Label(o1, style=Pack(font_size=40, padding_left=21, direction=ROW, flex=1, alignment='center', text_align='center', font_family='verdana', font_weight = 'bold'))

        self.output11 = toga.Label(t2, style=Pack(font_size=40, padding_left=21, direction=ROW, flex=1, alignment='center', text_align='center', font_family='verdana', font_weight = 'bold'))
        self.output12 = toga.Label(e2, style=Pack(font_size=40, padding_left=21, direction=ROW, flex=1, alignment='center', text_align='center', font_family='verdana', font_weight = 'bold'))
        self.output13 = toga.Label(r2, style=Pack(font_size=40, padding_left=21, direction=ROW, flex=1, alignment='center', text_align='center', font_family='verdana', font_weight = 'bold'))
        self.output14 = toga.Label(m2, style=Pack(font_size=40, padding_left=21, direction=ROW, flex=1, alignment='center', text_align='center', font_family='verdana', font_weight = 'bold'))
        self.output15 = toga.Label(o2, style=Pack(font_size=40, padding_left=21, direction=ROW, flex=1, alignment='center', text_align='center', font_family='verdana', font_weight = 'bold'))

        self.output16 = toga.Label(t3, style=Pack(font_size=40, padding_left=21, direction=ROW, flex=1, alignment='center', text_align='center', font_family='verdana', font_weight = 'bold'))
        self.output17 = toga.Label(e3, style=Pack(font_size=40, padding_left=21, direction=ROW, flex=1, alignment='center', text_align='center', font_family='verdana', font_weight = 'bold'))
        self.output18 = toga.Label(r3, style=Pack(font_size=40, padding_left=21, direction=ROW, flex=1, alignment='center', text_align='center', font_family='verdana', font_weight = 'bold'))
        self.output19 = toga.Label(m3, style=Pack(font_size=40, padding_left=21, direction=ROW, flex=1, alignment='center', text_align='center', font_family='verdana', font_weight = 'bold'))
        self.output20 = toga.Label(o3, style=Pack(font_size=40, padding_left=21, direction=ROW, flex=1, alignment='center', text_align='center', font_family='verdana', font_weight = 'bold'))

        self.output21 = toga.Label(t4, style=Pack(font_size=40, padding_left=21, direction=ROW, flex=1, alignment='center', text_align='center', font_family='verdana', font_weight = 'bold'))
        self.output22 = toga.Label(e4, style=Pack(font_size=40, padding_left=21, direction=ROW, flex=1, alignment='center', text_align='center', font_family='verdana', font_weight = 'bold'))
        self.output23 = toga.Label(r4, style=Pack(font_size=40, padding_left=21, direction=ROW, flex=1, alignment='center', text_align='center', font_family='verdana', font_weight = 'bold'))
        self.output24 = toga.Label(m4, style=Pack(font_size=40, padding_left=21, direction=ROW, flex=1, alignment='center', text_align='center', font_family='verdana', font_weight = 'bold'))
        self.output25 = toga.Label(o4, style=Pack(font_size=40, padding_left=21, direction=ROW, flex=1, alignment='center', text_align='center', font_family='verdana', font_weight = 'bold'))

        self.output26 = toga.Label(t5, style=Pack(font_size=40, padding_left=21, direction=ROW, flex=1, alignment='center', text_align='center', font_family='verdana', font_weight = 'bold'))
        self.output27 = toga.Label(e5, style=Pack(font_size=40, padding_left=21, direction=ROW, flex=1, alignment='center', text_align='center', font_family='verdana', font_weight = 'bold'))
        self.output28 = toga.Label(r5, style=Pack(font_size=40, padding_left=21, direction=ROW, flex=1, alignment='center', text_align='center', font_family='verdana', font_weight = 'bold'))
        self.output29 = toga.Label(m5, style=Pack(font_size=40, padding_left=21, direction=ROW, flex=1, alignment='center', text_align='center', font_family='verdana', font_weight = 'bold'))
        self.output30 = toga.Label(o5, style=Pack(font_size=40, padding_left=21, direction=ROW, flex=1, alignment='center', text_align='center', font_family='verdana', font_weight = 'bold'))

        #************************************************************************************************************


        # adição de cada letra a cada box respectiva
        # tentativa 1
        self.letra_t0.add(self.output1)
        self.letra_e0.add(self.output2)
        self.letra_r0.add(self.output3)
        self.letra_m0.add(self.output4)
        self.letra_o0.add(self.output5)

        # tentativa 2
        self.letra_t1.add(self.output6)
        self.letra_e1.add(self.output7)
        self.letra_r1.add(self.output8)
        self.letra_m1.add(self.output9)
        self.letra_o1.add(self.output10)

        # tentativa 3
        self.letra_t2.add(self.output11)
        self.letra_e2.add(self.output12)
        self.letra_r2.add(self.output13)
        self.letra_m2.add(self.output14)
        self.letra_o2.add(self.output15)

        # tentativa 4
        self.letra_t3.add(self.output16)
        self.letra_e3.add(self.output17)
        self.letra_r3.add(self.output18)
        self.letra_m3.add(self.output19)
        self.letra_o3.add(self.output20)

        # tentativa 5
        self.letra_t4.add(self.output21)
        self.letra_e4.add(self.output22)
        self.letra_r4.add(self.output23)
        self.letra_m4.add(self.output24)
        self.letra_o4.add(self.output25)

        # tentativa 6
        self.letra_t5.add(self.output26)
        self.letra_e5.add(self.output27)
        self.letra_r5.add(self.output28)
        self.letra_m5.add(self.output29)
        self.letra_o5.add(self.output30)


        # Adicionando nas janelas de tentativas cada letra do termo
        termo1_box.add(self.letra_t0, self.letra_e0, self.letra_r0, self.letra_m0, self.letra_o0)
        termo2_box.add(self.letra_t1, self.letra_e1, self.letra_r1, self.letra_m1, self.letra_o1)
        termo3_box.add(self.letra_t2, self.letra_e2, self.letra_r2, self.letra_m2, self.letra_o2)
        termo4_box.add(self.letra_t3, self.letra_e3, self.letra_r3, self.letra_m3, self.letra_o3)
        termo5_box.add(self.letra_t4, self.letra_e4, self.letra_r4, self.letra_m4, self.letra_o4)
        termo6_box.add(self.letra_t5, self.letra_e5, self.letra_r5, self.letra_m5, self.letra_o5)
        # ***************************************************************************************

        # uma box que contem todas as box que representam cada tentativa do jogador
        termos_page_box.add(termo1_box, termo2_box, termo3_box, termo4_box, termo5_box, termo6_box)

        # Resposta do usuário/jogador
        self.resp = ['', '', '', '', '']
        self.resposta = ''

        #largura

        # Definir a largura do botão como 50% da largura da tela


        #, width=button_width


        #buttons
        self.button_enter = toga.Button('Enter', on_press=self.tentativas, style=Pack(font_size=15, alignment='center', background_color='Skyblue'))


        # Adicionas nas janelas suas respectivas funções (janelas adicionais só para fins de organização)
        #termo_input_box.add(self.resp)
        #termo_button_box.add(button)

        #teclado manual dentro do game
        keyboard_box = toga.Box(style=Pack(direction=COLUMN, alignment='center', padding_top=20, flex=1))
        superior_box = toga.Box(style=Pack(direction=ROW, alignment='center', flex=1))
        middle_box = toga.Box(style=Pack(direction=ROW, alignment='center', flex=1))
        inferior_box = toga.Box(style=Pack(direction=ROW, alignment='center', flex=1))

        #box para cada letra do teclado
        q_box = toga.Box(style=Pack(direction=ROW, alignment='center', flex=1))
        w_box = toga.Box(style=Pack(direction=ROW, alignment='center', flex=1))
        e_box = toga.Box(style=Pack(direction=ROW, alignment='center', flex=1))
        r_box = toga.Box(style=Pack(direction=ROW, alignment='center', flex=1))
        t_box = toga.Box(style=Pack(direction=ROW, alignment='center', flex=1))
        y_box = toga.Box(style=Pack(direction=ROW, alignment='center', flex=1))
        u_box = toga.Box(style=Pack(direction=ROW, alignment='center', flex=1))
        i_box = toga.Box(style=Pack(direction=ROW, alignment='center', flex=1))
        o_box = toga.Box(style=Pack(direction=ROW, alignment='center', flex=1))
        p_box = toga.Box(style=Pack(direction=ROW, alignment='center', flex=1))

        a_box = toga.Box(style=Pack(direction=ROW, alignment='center', flex=1))
        s_box = toga.Box(style=Pack(direction=ROW, alignment='center', flex=1))
        d_box = toga.Box(style=Pack(direction=ROW, alignment='center', flex=1))
        f_box = toga.Box(style=Pack(direction=ROW, alignment='center', flex=1))
        g_box = toga.Box(style=Pack(direction=ROW, alignment='center', flex=1))
        h_box = toga.Box(style=Pack(direction=ROW, alignment='center', flex=1))
        j_box = toga.Box(style=Pack(direction=ROW, alignment='center', flex=1))
        k_box = toga.Box(style=Pack(direction=ROW, alignment='center', flex=1))
        l_box = toga.Box(style=Pack(direction=ROW, alignment='center', flex=1))
        cdl_box = toga.Box(style=Pack(direction=ROW, alignment='center', flex=1))

        z_box = toga.Box(style=Pack(direction=ROW, alignment='center', flex=1))
        x_box = toga.Box(style=Pack(direction=ROW, alignment='center', flex=1))
        c_box = toga.Box(style=Pack(direction=ROW, alignment='center', flex=1))
        v_box = toga.Box(style=Pack(direction=ROW, alignment='center', flex=1))
        b_box = toga.Box(style=Pack(direction=ROW, alignment='center', flex=1))
        n_box = toga.Box(style=Pack(direction=ROW, alignment='center', flex=1))
        m_box = toga.Box(style=Pack(direction=ROW, alignment='center', flex=1))
        del_box = toga.Box(style=Pack(direction=ROW, alignment='center', flex=1))
        enter_box = toga.Box(style=Pack(direction=ROW, alignment='center', flex=1))




        #SUPERIOR
        self.b_q = toga.Button('Q', on_press=partial(self.teclado, letra='q'), style=Pack(alignment='center', flex=1, width=button_width))
        self.b_w = toga.Button('W', on_press=partial(self.teclado, letra='w'), style=Pack(alignment='center', flex=1, width=button_width))
        self.b_e = toga.Button('E', on_press=partial(self.teclado, letra='e'), style=Pack(alignment='center', flex=1, width=button_width))
        self.b_r = toga.Button('R', on_press=partial(self.teclado, letra='r'), style=Pack(alignment='center', flex=1, width=button_width))
        self.b_t = toga.Button('T', on_press=partial(self.teclado, letra='t'), style=Pack(alignment='center', flex=1, width=button_width))
        self.b_y = toga.Button('Y', on_press=partial(self.teclado, letra='y'), style=Pack(alignment='center', flex=1, width=button_width))
        self.b_u = toga.Button('U', on_press=partial(self.teclado, letra='u'), style=Pack(alignment='center', flex=1, width=button_width))
        self.b_i = toga.Button('I', on_press=partial(self.teclado, letra='i'), style=Pack(alignment='center', flex=1, width=button_width))
        self.b_o = toga.Button('O', on_press=partial(self.teclado, letra='o'), style=Pack(alignment='center', flex=1, width=button_width))
        self.b_p = toga.Button('P', on_press=partial(self.teclado, letra='p'), style=Pack(alignment='center', flex=1, width=button_width))

        #MEIO
        self.b_a = toga.Button('A', on_press=partial(self.teclado, letra='a'), style=Pack(alignment='center', flex=1, width=button_width))
        self.b_s = toga.Button('S', on_press=partial(self.teclado, letra='s'), style=Pack(alignment='center', flex=1, width=button_width))
        self.b_d = toga.Button('D', on_press=partial(self.teclado, letra='d'), style=Pack(alignment='center', flex=1, width=button_width))
        self.b_f = toga.Button('F', on_press=partial(self.teclado, letra='f'), style=Pack(alignment='center', flex=1, width=button_width))
        self.b_g = toga.Button('G', on_press=partial(self.teclado, letra='g'), style=Pack(alignment='center', flex=1, width=button_width))
        self.b_h = toga.Button('H', on_press=partial(self.teclado, letra='h'), style=Pack(alignment='center', flex=1, width=button_width))
        self.b_j = toga.Button('J', on_press=partial(self.teclado, letra='j'), style=Pack(alignment='center', flex=1, width=button_width))
        self.b_k = toga.Button('K', on_press=partial(self.teclado, letra='k'), style=Pack(alignment='center', flex=1, width=button_width))
        self.b_l = toga.Button('L', on_press=partial(self.teclado, letra='l'), style=Pack(alignment='center', flex=1, width=button_width))
        self.b_cdl = toga.Button('Ç', on_press=partial(self.teclado, letra='ç'), style=Pack(alignment='center', flex=1, width=button_width))

        #INFERIOR
        self.b_z = toga.Button('Z', on_press=partial(self.teclado, letra='z'), style=Pack(alignment='center', flex=1, width=button_width))
        self.b_x = toga.Button('X', on_press=partial(self.teclado, letra='x'), style=Pack(alignment='center', flex=1, width=button_width))
        self.b_c = toga.Button('C', on_press=partial(self.teclado, letra='c'), style=Pack(alignment='center', flex=1, width=button_width))
        self.b_v = toga.Button('V', on_press=partial(self.teclado, letra='v'), style=Pack(alignment='center', flex=1, width=button_width))
        self.b_b = toga.Button('B', on_press=partial(self.teclado, letra='b'), style=Pack(alignment='center', flex=1, width=button_width))
        self.b_n = toga.Button('N', on_press=partial(self.teclado, letra='n'), style=Pack(alignment='center', flex=1, width=button_width))
        self.b_m = toga.Button('M', on_press=partial(self.teclado, letra='m'), style=Pack(alignment='center', flex=1, width=button_width))
        self.b_delete = toga.Button('DEL', on_press=partial(self.teclado, letra='del'), style=Pack(font_size=10, background_color='Powderblue', alignment='center', flex=1, width=button_width))

        q_box.add(self.b_q)
        w_box.add(self.b_w)
        e_box.add(self.b_e)
        r_box.add(self.b_r)
        t_box.add(self.b_t)
        y_box.add(self.b_y)
        u_box.add(self.b_u)
        i_box.add(self.b_i)
        o_box.add(self.b_o)
        p_box.add(self.b_p)

        a_box.add(self.b_a)
        s_box.add(self.b_s)
        d_box.add(self.b_d)
        f_box.add(self.b_f)
        g_box.add(self.b_g)
        h_box.add(self.b_h)
        j_box.add(self.b_j)
        k_box.add(self.b_k)
        l_box.add(self.b_l)
        cdl_box.add(self.b_cdl)

        z_box.add(self.b_z)
        x_box.add(self.b_x)
        c_box.add(self.b_c)
        v_box.add(self.b_v)
        b_box.add(self.b_b)
        n_box.add(self.b_n)
        m_box.add(self.b_m)
        del_box.add(self.b_delete)
        enter_box.add(self.button_enter)

        superior_box.add(q_box, w_box, e_box, r_box, t_box, y_box, u_box, i_box, o_box, p_box)
        middle_box.add(a_box, s_box, d_box, f_box, g_box, h_box, j_box, k_box, l_box, cdl_box)
        inferior_box.add(z_box, x_box, c_box, v_box, b_box, n_box, m_box, del_box, enter_box)
        keyboard_box.add(superior_box, middle_box, inferior_box)



        # Adicionando janelas na janela principal do aplicativo:
        main_box.add(termos_page_box, keyboard_box)

        self.main_window = toga.MainWindow(title=self.formal_name)
        self.main_window.content = main_box
        self.main_window.show()




    def tentativas(self, widget):
        if (len(self.resposta) == 5):
            if ((self.contador == '0') and (self.resposta in palavras_5char_existentes)):
                if (self.resposta != termo_play):
                    if self.resp[0] == termo_play[0]:
                        self.output1.text = '' + termo_play_Acento[0].upper()
                        self.letra_t0.style.background_color = 'Springgreen'
                        if self.resp[0] == 'q':
                            self.b_q.style.background_color = 'Springgreen'
                        if self.resp[0] == 'w':
                            self.b_w.style.background_color = 'Springgreen'
                        if self.resp[0] == 'e':
                            self.b_e.style.background_color = 'Springgreen'
                        if self.resp[0] == 'r':
                            self.b_r.style.background_color = 'Springgreen'
                        if self.resp[0] == 't':
                            self.b_t.style.background_color = 'Springgreen'
                        if self.resp[0] == 'y':
                            self.b_y.style.background_color = 'Springgreen'
                        if self.resp[0] == 'u':
                            self.b_u.style.background_color = 'Springgreen'
                        if self.resp[0] == 'i':
                            self.b_i.style.background_color = 'Springgreen'
                        if self.resp[0] == 'o':
                            self.b_o.style.background_color = 'Springgreen'
                        if self.resp[0] == 'p':
                            self.b_p.style.background_color = 'Springgreen'
                        if self.resp[0] == 'a':
                            self.b_a.style.background_color = 'Springgreen'
                        if self.resp[0] == 's':
                            self.b_s.style.background_color = 'Springgreen'
                        if self.resp[0] == 'd':
                            self.b_d.style.background_color = 'Springgreen'
                        if self.resp[0] == 'f':
                            self.b_f.style.background_color = 'Springgreen'
                        if self.resp[0] == 'g':
                            self.b_g.style.background_color = 'Springgreen'
                        if self.resp[0] == 'h':
                            self.b_h.style.background_color = 'Springgreen'
                        if self.resp[0] == 'j':
                            self.b_j.style.background_color = 'Springgreen'
                        if self.resp[0] == 'k':
                            self.b_k.style.background_color = 'Springgreen'
                        if self.resp[0] == 'l':
                            self.b_l.style.background_color = 'Springgreen'
                        if self.resp[0] == 'ç':
                            self.b_cdl.style.background_color = 'Springgreen'
                        if self.resp[0] == 'z':
                            self.b_z.style.background_color = 'Springgreen'
                        if self.resp[0] == 'x':
                            self.b_x.style.background_color = 'Springgreen'
                        if self.resp[0] == 'c':
                            self.b_c.style.background_color = 'Springgreen'
                        if self.resp[0] == 'v':
                            self.b_v.style.background_color = 'Springgreen'
                        if self.resp[0] == 'b':
                            self.b_b.style.background_color = 'Springgreen'
                        if self.resp[0] == 'n':
                            self.b_n.style.background_color = 'Springgreen'
                        if self.resp[0] == 'm':
                            self.b_m.style.background_color = 'Springgreen'

                    else:
                        if self.resp[0] in termo_play:
                            self.letra_t0.style.background_color = 'Gold'
                            if ((self.resp[0] == 'q') and (self.b_q.style.background_color != 'Springgreen')):
                                self.b_q.style.background_color = 'Gold'
                            if ((self.resp[0] == 'w') and (self.b_w.style.background_color != 'Springgreen')):
                                self.b_w.style.background_color = 'Gold'
                            if ((self.resp[0] == 'e') and (self.b_e.style.background_color != 'Springgreen')):
                                self.b_e.style.background_color = 'Gold'
                            if ((self.resp[0] == 'r') and (self.b_r.style.background_color != 'Springgreen')):
                                self.b_r.style.background_color = 'Gold'
                            if ((self.resp[0] == 't') and (self.b_t.style.background_color != 'Springgreen')):
                                self.b_t.style.background_color = 'Gold'
                            if ((self.resp[0] == 'y') and (self.b_y.style.background_color != 'Springgreen')):
                                self.b_y.style.background_color = 'Gold'
                            if ((self.resp[0] == 'u') and (self.b_u.style.background_color != 'Springgreen')):
                                self.b_u.style.background_color = 'Gold'
                            if ((self.resp[0] == 'i') and (self.b_i.style.background_color != 'Springgreen')):
                                self.b_i.style.background_color = 'Gold'
                            if ((self.resp[0] == 'o') and (self.b_o.style.background_color != 'Springgreen')):
                                self.b_o.style.background_color = 'Gold'
                            if ((self.resp[0] == 'p') and (self.b_p.style.background_color != 'Springgreen')):
                                self.b_p.style.background_color = 'Gold'
                            if ((self.resp[0] == 'a') and (self.b_a.style.background_color != 'Springgreen')):
                                self.b_a.style.background_color = 'Gold'
                            if ((self.resp[0] == 's') and (self.b_s.style.background_color != 'Springgreen')):
                                self.b_s.style.background_color = 'Gold'
                            if ((self.resp[0] == 'd') and (self.b_d.style.background_color != 'Springgreen')):
                                self.b_d.style.background_color = 'Gold'
                            if ((self.resp[0] == 'f') and (self.b_f.style.background_color != 'Springgreen')):
                                self.b_f.style.background_color = 'Gold'
                            if ((self.resp[0] == 'g') and (self.b_g.style.background_color != 'Springgreen')):
                                self.b_g.style.background_color = 'Gold'
                            if ((self.resp[0] == 'h') and (self.b_h.style.background_color != 'Springgreen')):
                                self.b_h.style.background_color = 'Gold'
                            if ((self.resp[0] == 'j') and (self.b_j.style.background_color != 'Springgreen')):
                                self.b_j.style.background_color = 'Gold'
                            if ((self.resp[0] == 'k') and (self.b_k.style.background_color != 'Springgreen')):
                                self.b_k.style.background_color = 'Gold'
                            if ((self.resp[0] == 'l') and (self.b_l.style.background_color != 'Springgreen')):
                                self.b_l.style.background_color = 'Gold'
                            if ((self.resp[0] == 'ç') and (self.b_cdl.style.background_color != 'Springgreen')):
                                self.b_cdl.style.background_color = 'Gold'
                            if ((self.resp[0] == 'z') and (self.b_z.style.background_color != 'Springgreen')):
                                self.b_z.style.background_color = 'Gold'
                            if ((self.resp[0] == 'x') and (self.b_x.style.background_color != 'Springgreen')):
                                self.b_x.style.background_color = 'Gold'
                            if ((self.resp[0] == 'c') and (self.b_c.style.background_color != 'Springgreen')):
                                self.b_c.style.background_color = 'Gold'
                            if ((self.resp[0] == 'v') and (self.b_v.style.background_color != 'Springgreen')):
                                self.b_v.style.background_color = 'Gold'
                            if ((self.resp[0] == 'b') and (self.b_b.style.background_color != 'Springgreen')):
                                self.b_b.style.background_color = 'Gold'
                            if ((self.resp[0] == 'n') and (self.b_n.style.background_color != 'Springgreen')):
                                self.b_n.style.background_color = 'Gold'
                            if ((self.resp[0] == 'm') and (self.b_m.style.background_color != 'Springgreen')):
                                self.b_m.style.background_color = 'Gold'
                        else:
                            if self.resp[0] == 'q':
                                self.b_q.style.background_color = 'Gray'
                            if self.resp[0] == 'w':
                                self.b_w.style.background_color = 'Gray'
                            if self.resp[0] == 'e':
                                self.b_e.style.background_color = 'Gray'
                            if self.resp[0] == 'r':
                                self.b_r.style.background_color = 'Gray'
                            if self.resp[0] == 't':
                                self.b_t.style.background_color = 'Gray'
                            if self.resp[0] == 'y':
                                self.b_y.style.background_color = 'Gray'
                            if self.resp[0] == 'u':
                                self.b_u.style.background_color = 'Gray'
                            if self.resp[0] == 'i':
                                self.b_i.style.background_color = 'Gray'
                            if self.resp[0] == 'o':
                                self.b_o.style.background_color = 'Gray'
                            if self.resp[0] == 'p':
                                self.b_p.style.background_color = 'Gray'
                            if self.resp[0] == 'a':
                                self.b_a.style.background_color = 'Gray'
                            if self.resp[0] == 's':
                                self.b_s.style.background_color = 'Gray'
                            if self.resp[0] == 'd':
                                self.b_d.style.background_color = 'Gray'
                            if self.resp[0] == 'f':
                                self.b_f.style.background_color = 'Gray'
                            if self.resp[0] == 'g':
                                self.b_g.style.background_color = 'Gray'
                            if self.resp[0] == 'h':
                                self.b_h.style.background_color = 'Gray'
                            if self.resp[0] == 'j':
                                self.b_j.style.background_color = 'Gray'
                            if self.resp[0] == 'k':
                                self.b_k.style.background_color = 'Gray'
                            if self.resp[0] == 'l':
                                self.b_l.style.background_color = 'Gray'
                            if self.resp[0] == 'ç':
                                self.b_cdl.style.background_color = 'Gray'
                            if self.resp[0] == 'z':
                                self.b_z.style.background_color = 'Gray'
                            if self.resp[0] == 'x':
                                self.b_x.style.background_color = 'Gray'
                            if self.resp[0] == 'c':
                                self.b_c.style.background_color = 'Gray'
                            if self.resp[0] == 'v':
                                self.b_v.style.background_color = 'Gray'
                            if self.resp[0] == 'b':
                                self.b_b.style.background_color = 'Gray'
                            if self.resp[0] == 'n':
                                self.b_n.style.background_color = 'Gray'
                            if self.resp[0] == 'm':
                                self.b_m.style.background_color = 'Gray'

                    if self.resp[1] == termo_play[1]:
                        self.output2.text = '' + termo_play_Acento[1].upper()
                        self.letra_e0.style.background_color = 'Springgreen'
                        if self.resp[1] == 'q':
                            self.b_q.style.background_color = 'Springgreen'
                        if self.resp[1] == 'w':
                            self.b_w.style.background_color = 'Springgreen'
                        if self.resp[1] == 'e':
                            self.b_e.style.background_color = 'Springgreen'
                        if self.resp[1] == 'r':
                            self.b_r.style.background_color = 'Springgreen'
                        if self.resp[1] == 't':
                            self.b_t.style.background_color = 'Springgreen'
                        if self.resp[1] == 'y':
                            self.b_y.style.background_color = 'Springgreen'
                        if self.resp[1] == 'u':
                            self.b_u.style.background_color = 'Springgreen'
                        if self.resp[1] == 'i':
                            self.b_i.style.background_color = 'Springgreen'
                        if self.resp[1] == 'o':
                            self.b_o.style.background_color = 'Springgreen'
                        if self.resp[1] == 'p':
                            self.b_p.style.background_color = 'Springgreen'
                        if self.resp[1] == 'a':
                            self.b_a.style.background_color = 'Springgreen'
                        if self.resp[1] == 's':
                            self.b_s.style.background_color = 'Springgreen'
                        if self.resp[1] == 'd':
                            self.b_d.style.background_color = 'Springgreen'
                        if self.resp[1] == 'f':
                            self.b_f.style.background_color = 'Springgreen'
                        if self.resp[1] == 'g':
                            self.b_g.style.background_color = 'Springgreen'
                        if self.resp[1] == 'h':
                            self.b_h.style.background_color = 'Springgreen'
                        if self.resp[1] == 'j':
                            self.b_j.style.background_color = 'Springgreen'
                        if self.resp[1] == 'k':
                            self.b_k.style.background_color = 'Springgreen'
                        if self.resp[1] == 'l':
                            self.b_l.style.background_color = 'Springgreen'
                        if self.resp[1] == 'ç':
                            self.b_cdl.style.background_color = 'Springgreen'
                        if self.resp[1] == 'z':
                            self.b_z.style.background_color = 'Springgreen'
                        if self.resp[1] == 'x':
                            self.b_x.style.background_color = 'Springgreen'
                        if self.resp[1] == 'c':
                            self.b_c.style.background_color = 'Springgreen'
                        if self.resp[1] == 'v':
                            self.b_v.style.background_color = 'Springgreen'
                        if self.resp[1] == 'b':
                            self.b_b.style.background_color = 'Springgreen'
                        if self.resp[1] == 'n':
                            self.b_n.style.background_color = 'Springgreen'
                        if self.resp[1] == 'm':
                            self.b_m.style.background_color = 'Springgreen'
                    else:
                        if self.resp[1] in termo_play:
                            self.letra_e0.style.background_color = 'Gold'
                            if ((self.resp[1] == 'q') and (self.b_q.style.background_color != 'Springgreen')):
                                self.b_q.style.background_color = 'Gold'
                            if ((self.resp[1] == 'w') and (self.b_w.style.background_color != 'Springgreen')):
                                self.b_w.style.background_color = 'Gold'
                            if ((self.resp[1] == 'e') and (self.b_e.style.background_color != 'Springgreen')):
                                self.b_e.style.background_color = 'Gold'
                            if ((self.resp[1] == 'r') and (self.b_r.style.background_color != 'Springgreen')):
                                self.b_r.style.background_color = 'Gold'
                            if ((self.resp[1] == 't') and (self.b_t.style.background_color != 'Springgreen')):
                                self.b_t.style.background_color = 'Gold'
                            if ((self.resp[1] == 'y') and (self.b_y.style.background_color != 'Springgreen')):
                                self.b_y.style.background_color = 'Gold'
                            if ((self.resp[1] == 'u') and (self.b_u.style.background_color != 'Springgreen')):
                                self.b_u.style.background_color = 'Gold'
                            if ((self.resp[1] == 'i') and (self.b_i.style.background_color != 'Springgreen')):
                                self.b_i.style.background_color = 'Gold'
                            if ((self.resp[1] == 'o') and (self.b_o.style.background_color != 'Springgreen')):
                                self.b_o.style.background_color = 'Gold'
                            if ((self.resp[1] == 'p') and (self.b_p.style.background_color != 'Springgreen')):
                                self.b_p.style.background_color = 'Gold'
                            if ((self.resp[1] == 'a') and (self.b_a.style.background_color != 'Springgreen')):
                                self.b_a.style.background_color = 'Gold'
                            if ((self.resp[1] == 's') and (self.b_s.style.background_color != 'Springgreen')):
                                self.b_s.style.background_color = 'Gold'
                            if ((self.resp[1] == 'd') and (self.b_d.style.background_color != 'Springgreen')):
                                self.b_d.style.background_color = 'Gold'
                            if ((self.resp[1] == 'f') and (self.b_f.style.background_color != 'Springgreen')):
                                self.b_f.style.background_color = 'Gold'
                            if ((self.resp[1] == 'g') and (self.b_g.style.background_color != 'Springgreen')):
                                self.b_g.style.background_color = 'Gold'
                            if ((self.resp[1] == 'h') and (self.b_h.style.background_color != 'Springgreen')):
                                self.b_h.style.background_color = 'Gold'
                            if ((self.resp[1] == 'j') and (self.b_j.style.background_color != 'Springgreen')):
                                self.b_j.style.background_color = 'Gold'
                            if ((self.resp[1] == 'k') and (self.b_k.style.background_color != 'Springgreen')):
                                self.b_k.style.background_color = 'Gold'
                            if ((self.resp[1] == 'l') and (self.b_l.style.background_color != 'Springgreen')):
                                self.b_l.style.background_color = 'Gold'
                            if ((self.resp[1] == 'ç') and (self.b_cdl.style.background_color != 'Springgreen')):
                                self.b_cdl.style.background_color = 'Gold'
                            if ((self.resp[1] == 'z') and (self.b_z.style.background_color != 'Springgreen')):
                                self.b_z.style.background_color = 'Gold'
                            if ((self.resp[1] == 'x') and (self.b_x.style.background_color != 'Springgreen')):
                                self.b_x.style.background_color = 'Gold'
                            if ((self.resp[1] == 'c') and (self.b_c.style.background_color != 'Springgreen')):
                                self.b_c.style.background_color = 'Gold'
                            if ((self.resp[1] == 'v') and (self.b_v.style.background_color != 'Springgreen')):
                                self.b_v.style.background_color = 'Gold'
                            if ((self.resp[1] == 'b') and (self.b_b.style.background_color != 'Springgreen')):
                                self.b_b.style.background_color = 'Gold'
                            if ((self.resp[1] == 'n') and (self.b_n.style.background_color != 'Springgreen')):
                                self.b_n.style.background_color = 'Gold'
                            if ((self.resp[1] == 'm') and (self.b_m.style.background_color != 'Springgreen')):
                                self.b_m.style.background_color = 'Gold'
                        else:
                            if self.resp[1] == 'q':
                                self.b_q.style.background_color = 'Gray'
                            if self.resp[1] == 'w':
                                self.b_w.style.background_color = 'Gray'
                            if self.resp[1] == 'e':
                                self.b_e.style.background_color = 'Gray'
                            if self.resp[1] == 'r':
                                self.b_r.style.background_color = 'Gray'
                            if self.resp[1] == 't':
                                self.b_t.style.background_color = 'Gray'
                            if self.resp[1] == 'y':
                                self.b_y.style.background_color = 'Gray'
                            if self.resp[1] == 'u':
                                self.b_u.style.background_color = 'Gray'
                            if self.resp[1] == 'i':
                                self.b_i.style.background_color = 'Gray'
                            if self.resp[1] == 'o':
                                self.b_o.style.background_color = 'Gray'
                            if self.resp[1] == 'p':
                                self.b_p.style.background_color = 'Gray'
                            if self.resp[1] == 'a':
                                self.b_a.style.background_color = 'Gray'
                            if self.resp[1] == 's':
                                self.b_s.style.background_color = 'Gray'
                            if self.resp[1] == 'd':
                                self.b_d.style.background_color = 'Gray'
                            if self.resp[1] == 'f':
                                self.b_f.style.background_color = 'Gray'
                            if self.resp[1] == 'g':
                                self.b_g.style.background_color = 'Gray'
                            if self.resp[1] == 'h':
                                self.b_h.style.background_color = 'Gray'
                            if self.resp[1] == 'j':
                                self.b_j.style.background_color = 'Gray'
                            if self.resp[1] == 'k':
                                self.b_k.style.background_color = 'Gray'
                            if self.resp[1] == 'l':
                                self.b_l.style.background_color = 'Gray'
                            if self.resp[1] == 'ç':
                                self.b_cdl.style.background_color = 'Gray'
                            if self.resp[1] == 'z':
                                self.b_z.style.background_color = 'Gray'
                            if self.resp[1] == 'x':
                                self.b_x.style.background_color = 'Gray'
                            if self.resp[1] == 'c':
                                self.b_c.style.background_color = 'Gray'
                            if self.resp[1] == 'v':
                                self.b_v.style.background_color = 'Gray'
                            if self.resp[1] == 'b':
                                self.b_b.style.background_color = 'Gray'
                            if self.resp[1] == 'n':
                                self.b_n.style.background_color = 'Gray'
                            if self.resp[1] == 'm':
                                self.b_m.style.background_color = 'Gray'

                    if self.resp[2] == termo_play[2]:
                        self.output3.text = '' + termo_play_Acento[2].upper()
                        self.letra_r0.style.background_color = 'Springgreen'
                        if self.resp[2] == 'q':
                            self.b_q.style.background_color = 'Springgreen'
                        if self.resp[2] == 'w':
                            self.b_w.style.background_color = 'Springgreen'
                        if self.resp[2] == 'e':
                            self.b_e.style.background_color = 'Springgreen'
                        if self.resp[2] == 'r':
                            self.b_r.style.background_color = 'Springgreen'
                        if self.resp[2] == 't':
                            self.b_t.style.background_color = 'Springgreen'
                        if self.resp[2] == 'y':
                            self.b_y.style.background_color = 'Springgreen'
                        if self.resp[2] == 'u':
                            self.b_u.style.background_color = 'Springgreen'
                        if self.resp[2] == 'i':
                            self.b_i.style.background_color = 'Springgreen'
                        if self.resp[2] == 'o':
                            self.b_o.style.background_color = 'Springgreen'
                        if self.resp[2] == 'p':
                            self.b_p.style.background_color = 'Springgreen'
                        if self.resp[2] == 'a':
                            self.b_a.style.background_color = 'Springgreen'
                        if self.resp[2] == 's':
                            self.b_s.style.background_color = 'Springgreen'
                        if self.resp[2] == 'd':
                            self.b_d.style.background_color = 'Springgreen'
                        if self.resp[2] == 'f':
                            self.b_f.style.background_color = 'Springgreen'
                        if self.resp[2] == 'g':
                            self.b_g.style.background_color = 'Springgreen'
                        if self.resp[2] == 'h':
                            self.b_h.style.background_color = 'Springgreen'
                        if self.resp[2] == 'j':
                            self.b_j.style.background_color = 'Springgreen'
                        if self.resp[2] == 'k':
                            self.b_k.style.background_color = 'Springgreen'
                        if self.resp[2] == 'l':
                            self.b_l.style.background_color = 'Springgreen'
                        if self.resp[2] == 'ç':
                            self.b_cdl.style.background_color = 'Springgreen'
                        if self.resp[2] == 'z':
                            self.b_z.style.background_color = 'Springgreen'
                        if self.resp[2] == 'x':
                            self.b_x.style.background_color = 'Springgreen'
                        if self.resp[2] == 'c':
                            self.b_c.style.background_color = 'Springgreen'
                        if self.resp[2] == 'v':
                            self.b_v.style.background_color = 'Springgreen'
                        if self.resp[2] == 'b':
                            self.b_b.style.background_color = 'Springgreen'
                        if self.resp[2] == 'n':
                            self.b_n.style.background_color = 'Springgreen'
                        if self.resp[2] == 'm':
                            self.b_m.style.background_color = 'Springgreen'
                    else:
                        if self.resp[2] in termo_play:
                            self.letra_r0.style.background_color = 'Gold'
                            if ((self.resp[2] == 'q') and (self.b_q.style.background_color != 'Springgreen')):
                                self.b_q.style.background_color = 'Gold'
                            if ((self.resp[2] == 'w') and (self.b_w.style.background_color != 'Springgreen')):
                                self.b_w.style.background_color = 'Gold'
                            if ((self.resp[2] == 'e') and (self.b_e.style.background_color != 'Springgreen')):
                                self.b_e.style.background_color = 'Gold'
                            if ((self.resp[2] == 'r') and (self.b_r.style.background_color != 'Springgreen')):
                                self.b_r.style.background_color = 'Gold'
                            if ((self.resp[2] == 't') and (self.b_t.style.background_color != 'Springgreen')):
                                self.b_t.style.background_color = 'Gold'
                            if ((self.resp[2] == 'y') and (self.b_y.style.background_color != 'Springgreen')):
                                self.b_y.style.background_color = 'Gold'
                            if ((self.resp[2] == 'u') and (self.b_u.style.background_color != 'Springgreen')):
                                self.b_u.style.background_color = 'Gold'
                            if ((self.resp[2] == 'i') and (self.b_i.style.background_color != 'Springgreen')):
                                self.b_i.style.background_color = 'Gold'
                            if ((self.resp[2] == 'o') and (self.b_o.style.background_color != 'Springgreen')):
                                self.b_o.style.background_color = 'Gold'
                            if ((self.resp[2] == 'p') and (self.b_p.style.background_color != 'Springgreen')):
                                self.b_p.style.background_color = 'Gold'
                            if ((self.resp[2] == 'a') and (self.b_a.style.background_color != 'Springgreen')):
                                self.b_a.style.background_color = 'Gold'
                            if ((self.resp[2] == 's') and (self.b_s.style.background_color != 'Springgreen')):
                                self.b_s.style.background_color = 'Gold'
                            if ((self.resp[2] == 'd') and (self.b_d.style.background_color != 'Springgreen')):
                                self.b_d.style.background_color = 'Gold'
                            if ((self.resp[2] == 'f') and (self.b_f.style.background_color != 'Springgreen')):
                                self.b_f.style.background_color = 'Gold'
                            if ((self.resp[2] == 'g') and (self.b_g.style.background_color != 'Springgreen')):
                                self.b_g.style.background_color = 'Gold'
                            if ((self.resp[2] == 'h') and (self.b_h.style.background_color != 'Springgreen')):
                                self.b_h.style.background_color = 'Gold'
                            if ((self.resp[2] == 'j') and (self.b_j.style.background_color != 'Springgreen')):
                                self.b_j.style.background_color = 'Gold'
                            if ((self.resp[2] == 'k') and (self.b_k.style.background_color != 'Springgreen')):
                                self.b_k.style.background_color = 'Gold'
                            if ((self.resp[2] == 'l') and (self.b_l.style.background_color != 'Springgreen')):
                                self.b_l.style.background_color = 'Gold'
                            if ((self.resp[2] == 'ç') and (self.b_cdl.style.background_color != 'Springgreen')):
                                self.b_cdl.style.background_color = 'Gold'
                            if ((self.resp[2] == 'z') and (self.b_z.style.background_color != 'Springgreen')):
                                self.b_z.style.background_color = 'Gold'
                            if ((self.resp[2] == 'x') and (self.b_x.style.background_color != 'Springgreen')):
                                self.b_x.style.background_color = 'Gold'
                            if ((self.resp[2] == 'c') and (self.b_c.style.background_color != 'Springgreen')):
                                self.b_c.style.background_color = 'Gold'
                            if ((self.resp[2] == 'v') and (self.b_v.style.background_color != 'Springgreen')):
                                self.b_v.style.background_color = 'Gold'
                            if ((self.resp[2] == 'b') and (self.b_b.style.background_color != 'Springgreen')):
                                self.b_b.style.background_color = 'Gold'
                            if ((self.resp[2] == 'n') and (self.b_n.style.background_color != 'Springgreen')):
                                self.b_n.style.background_color = 'Gold'
                            if ((self.resp[2] == 'm') and (self.b_m.style.background_color != 'Springgreen')):
                                self.b_m.style.background_color = 'Gold'
                        else:
                            if self.resp[2] == 'q':
                                self.b_q.style.background_color = 'Gray'
                            if self.resp[2] == 'w':
                                self.b_w.style.background_color = 'Gray'
                            if self.resp[2] == 'e':
                                self.b_e.style.background_color = 'Gray'
                            if self.resp[2] == 'r':
                                self.b_r.style.background_color = 'Gray'
                            if self.resp[2] == 't':
                                self.b_t.style.background_color = 'Gray'
                            if self.resp[2] == 'y':
                                self.b_y.style.background_color = 'Gray'
                            if self.resp[2] == 'u':
                                self.b_u.style.background_color = 'Gray'
                            if self.resp[2] == 'i':
                                self.b_i.style.background_color = 'Gray'
                            if self.resp[2] == 'o':
                                self.b_o.style.background_color = 'Gray'
                            if self.resp[2] == 'p':
                                self.b_p.style.background_color = 'Gray'
                            if self.resp[2] == 'a':
                                self.b_a.style.background_color = 'Gray'
                            if self.resp[2] == 's':
                                self.b_s.style.background_color = 'Gray'
                            if self.resp[2] == 'd':
                                self.b_d.style.background_color = 'Gray'
                            if self.resp[2] == 'f':
                                self.b_f.style.background_color = 'Gray'
                            if self.resp[2] == 'g':
                                self.b_g.style.background_color = 'Gray'
                            if self.resp[2] == 'h':
                                self.b_h.style.background_color = 'Gray'
                            if self.resp[2] == 'j':
                                self.b_j.style.background_color = 'Gray'
                            if self.resp[2] == 'k':
                                self.b_k.style.background_color = 'Gray'
                            if self.resp[2] == 'l':
                                self.b_l.style.background_color = 'Gray'
                            if self.resp[2] == 'ç':
                                self.b_cdl.style.background_color = 'Gray'
                            if self.resp[2] == 'z':
                                self.b_z.style.background_color = 'Gray'
                            if self.resp[2] == 'x':
                                self.b_x.style.background_color = 'Gray'
                            if self.resp[2] == 'c':
                                self.b_c.style.background_color = 'Gray'
                            if self.resp[2] == 'v':
                                self.b_v.style.background_color = 'Gray'
                            if self.resp[2] == 'b':
                                self.b_b.style.background_color = 'Gray'
                            if self.resp[2] == 'n':
                                self.b_n.style.background_color = 'Gray'
                            if self.resp[2] == 'm':
                                self.b_m.style.background_color = 'Gray'

                    if self.resp[3] == termo_play[3]:
                        self.output4.text = '' + termo_play_Acento[3].upper()
                        self.letra_m0.style.background_color = 'Springgreen'
                        if self.resp[3] == 'q':
                            self.b_q.style.background_color = 'Springgreen'
                        if self.resp[3] == 'w':
                            self.b_w.style.background_color = 'Springgreen'
                        if self.resp[3] == 'e':
                            self.b_e.style.background_color = 'Springgreen'
                        if self.resp[3] == 'r':
                            self.b_r.style.background_color = 'Springgreen'
                        if self.resp[3] == 't':
                            self.b_t.style.background_color = 'Springgreen'
                        if self.resp[3] == 'y':
                            self.b_y.style.background_color = 'Springgreen'
                        if self.resp[3] == 'u':
                            self.b_u.style.background_color = 'Springgreen'
                        if self.resp[3] == 'i':
                            self.b_i.style.background_color = 'Springgreen'
                        if self.resp[3] == 'o':
                            self.b_o.style.background_color = 'Springgreen'
                        if self.resp[3] == 'p':
                            self.b_p.style.background_color = 'Springgreen'
                        if self.resp[3] == 'a':
                            self.b_a.style.background_color = 'Springgreen'
                        if self.resp[3] == 's':
                            self.b_s.style.background_color = 'Springgreen'
                        if self.resp[3] == 'd':
                            self.b_d.style.background_color = 'Springgreen'
                        if self.resp[3] == 'f':
                            self.b_f.style.background_color = 'Springgreen'
                        if self.resp[3] == 'g':
                            self.b_g.style.background_color = 'Springgreen'
                        if self.resp[3] == 'h':
                            self.b_h.style.background_color = 'Springgreen'
                        if self.resp[3] == 'j':
                            self.b_j.style.background_color = 'Springgreen'
                        if self.resp[3] == 'k':
                            self.b_k.style.background_color = 'Springgreen'
                        if self.resp[3] == 'l':
                            self.b_l.style.background_color = 'Springgreen'
                        if self.resp[3] == 'ç':
                            self.b_cdl.style.background_color = 'Springgreen'
                        if self.resp[3] == 'z':
                            self.b_z.style.background_color = 'Springgreen'
                        if self.resp[3] == 'x':
                            self.b_x.style.background_color = 'Springgreen'
                        if self.resp[3] == 'c':
                            self.b_c.style.background_color = 'Springgreen'
                        if self.resp[3] == 'v':
                            self.b_v.style.background_color = 'Springgreen'
                        if self.resp[3] == 'b':
                            self.b_b.style.background_color = 'Springgreen'
                        if self.resp[3] == 'n':
                            self.b_n.style.background_color = 'Springgreen'
                        if self.resp[3] == 'm':
                            self.b_m.style.background_color = 'Springgreen'
                    else:
                        if self.resp[3] in termo_play:
                            self.letra_m0.style.background_color = 'Gold'
                            if ((self.resp[3] == 'q') and (self.b_q.style.background_color != 'Springgreen')):
                                self.b_q.style.background_color = 'Gold'
                            if ((self.resp[3] == 'w') and (self.b_w.style.background_color != 'Springgreen')):
                                self.b_w.style.background_color = 'Gold'
                            if ((self.resp[3] == 'e') and (self.b_e.style.background_color != 'Springgreen')):
                                self.b_e.style.background_color = 'Gold'
                            if ((self.resp[3] == 'r') and (self.b_r.style.background_color != 'Springgreen')):
                                self.b_r.style.background_color = 'Gold'
                            if ((self.resp[3] == 't') and (self.b_t.style.background_color != 'Springgreen')):
                                self.b_t.style.background_color = 'Gold'
                            if ((self.resp[3] == 'y') and (self.b_y.style.background_color != 'Springgreen')):
                                self.b_y.style.background_color = 'Gold'
                            if ((self.resp[3] == 'u') and (self.b_u.style.background_color != 'Springgreen')):
                                self.b_u.style.background_color = 'Gold'
                            if ((self.resp[3] == 'i') and (self.b_i.style.background_color != 'Springgreen')):
                                self.b_i.style.background_color = 'Gold'
                            if ((self.resp[3] == 'o') and (self.b_o.style.background_color != 'Springgreen')):
                                self.b_o.style.background_color = 'Gold'
                            if ((self.resp[3] == 'p') and (self.b_p.style.background_color != 'Springgreen')):
                                self.b_p.style.background_color = 'Gold'
                            if ((self.resp[3] == 'a') and (self.b_a.style.background_color != 'Springgreen')):
                                self.b_a.style.background_color = 'Gold'
                            if ((self.resp[3] == 's') and (self.b_s.style.background_color != 'Springgreen')):
                                self.b_s.style.background_color = 'Gold'
                            if ((self.resp[3] == 'd') and (self.b_d.style.background_color != 'Springgreen')):
                                self.b_d.style.background_color = 'Gold'
                            if ((self.resp[3] == 'f') and (self.b_f.style.background_color != 'Springgreen')):
                                self.b_f.style.background_color = 'Gold'
                            if ((self.resp[3] == 'g') and (self.b_g.style.background_color != 'Springgreen')):
                                self.b_g.style.background_color = 'Gold'
                            if ((self.resp[3] == 'h') and (self.b_h.style.background_color != 'Springgreen')):
                                self.b_h.style.background_color = 'Gold'
                            if ((self.resp[3] == 'j') and (self.b_j.style.background_color != 'Springgreen')):
                                self.b_j.style.background_color = 'Gold'
                            if ((self.resp[3] == 'k') and (self.b_k.style.background_color != 'Springgreen')):
                                self.b_k.style.background_color = 'Gold'
                            if ((self.resp[3] == 'l') and (self.b_l.style.background_color != 'Springgreen')):
                                self.b_l.style.background_color = 'Gold'
                            if ((self.resp[3] == 'ç') and (self.b_cdl.style.background_color != 'Springgreen')):
                                self.b_cdl.style.background_color = 'Gold'
                            if ((self.resp[3] == 'z') and (self.b_z.style.background_color != 'Springgreen')):
                                self.b_z.style.background_color = 'Gold'
                            if ((self.resp[3] == 'x') and (self.b_x.style.background_color != 'Springgreen')):
                                self.b_x.style.background_color = 'Gold'
                            if ((self.resp[3] == 'c') and (self.b_c.style.background_color != 'Springgreen')):
                                self.b_c.style.background_color = 'Gold'
                            if ((self.resp[3] == 'v') and (self.b_v.style.background_color != 'Springgreen')):
                                self.b_v.style.background_color = 'Gold'
                            if ((self.resp[3] == 'b') and (self.b_b.style.background_color != 'Springgreen')):
                                self.b_b.style.background_color = 'Gold'
                            if ((self.resp[3] == 'n') and (self.b_n.style.background_color != 'Springgreen')):
                                self.b_n.style.background_color = 'Gold'
                            if ((self.resp[3] == 'm') and (self.b_m.style.background_color != 'Springgreen')):
                                self.b_m.style.background_color = 'Gold'
                        else:
                            if self.resp[3] == 'q':
                                self.b_q.style.background_color = 'Gray'
                            if self.resp[3] == 'w':
                                self.b_w.style.background_color = 'Gray'
                            if self.resp[3] == 'e':
                                self.b_e.style.background_color = 'Gray'
                            if self.resp[3] == 'r':
                                self.b_r.style.background_color = 'Gray'
                            if self.resp[3] == 't':
                                self.b_t.style.background_color = 'Gray'
                            if self.resp[3] == 'y':
                                self.b_y.style.background_color = 'Gray'
                            if self.resp[3] == 'u':
                                self.b_u.style.background_color = 'Gray'
                            if self.resp[3] == 'i':
                                self.b_i.style.background_color = 'Gray'
                            if self.resp[3] == 'o':
                                self.b_o.style.background_color = 'Gray'
                            if self.resp[3] == 'p':
                                self.b_p.style.background_color = 'Gray'
                            if self.resp[3] == 'a':
                                self.b_a.style.background_color = 'Gray'
                            if self.resp[3] == 's':
                                self.b_s.style.background_color = 'Gray'
                            if self.resp[3] == 'd':
                                self.b_d.style.background_color = 'Gray'
                            if self.resp[3] == 'f':
                                self.b_f.style.background_color = 'Gray'
                            if self.resp[3] == 'g':
                                self.b_g.style.background_color = 'Gray'
                            if self.resp[3] == 'h':
                                self.b_h.style.background_color = 'Gray'
                            if self.resp[3] == 'j':
                                self.b_j.style.background_color = 'Gray'
                            if self.resp[3] == 'k':
                                self.b_k.style.background_color = 'Gray'
                            if self.resp[3] == 'l':
                                self.b_l.style.background_color = 'Gray'
                            if self.resp[3] == 'ç':
                                self.b_cdl.style.background_color = 'Gray'
                            if self.resp[3] == 'z':
                                self.b_z.style.background_color = 'Gray'
                            if self.resp[3] == 'x':
                                self.b_x.style.background_color = 'Gray'
                            if self.resp[3] == 'c':
                                self.b_c.style.background_color = 'Gray'
                            if self.resp[3] == 'v':
                                self.b_v.style.background_color = 'Gray'
                            if self.resp[3] == 'b':
                                self.b_b.style.background_color = 'Gray'
                            if self.resp[3] == 'n':
                                self.b_n.style.background_color = 'Gray'
                            if self.resp[3] == 'm':
                                self.b_m.style.background_color = 'Gray'

                    if self.resp[4] == termo_play[4]:
                        self.output5.text = '' + termo_play_Acento[4].upper()
                        self.letra_o0.style.background_color = 'Springgreen'
                        if self.resp[4] == 'q':
                            self.b_q.style.background_color = 'Springgreen'
                        if self.resp[4] == 'w':
                            self.b_w.style.background_color = 'Springgreen'
                        if self.resp[4] == 'e':
                            self.b_e.style.background_color = 'Springgreen'
                        if self.resp[4] == 'r':
                            self.b_r.style.background_color = 'Springgreen'
                        if self.resp[4] == 't':
                            self.b_t.style.background_color = 'Springgreen'
                        if self.resp[4] == 'y':
                            self.b_y.style.background_color = 'Springgreen'
                        if self.resp[4] == 'u':
                            self.b_u.style.background_color = 'Springgreen'
                        if self.resp[4] == 'i':
                            self.b_i.style.background_color = 'Springgreen'
                        if self.resp[4] == 'o':
                            self.b_o.style.background_color = 'Springgreen'
                        if self.resp[4] == 'p':
                            self.b_p.style.background_color = 'Springgreen'
                        if self.resp[4] == 'a':
                            self.b_a.style.background_color = 'Springgreen'
                        if self.resp[4] == 's':
                            self.b_s.style.background_color = 'Springgreen'
                        if self.resp[4] == 'd':
                            self.b_d.style.background_color = 'Springgreen'
                        if self.resp[4] == 'f':
                            self.b_f.style.background_color = 'Springgreen'
                        if self.resp[4] == 'g':
                            self.b_g.style.background_color = 'Springgreen'
                        if self.resp[4] == 'h':
                            self.b_h.style.background_color = 'Springgreen'
                        if self.resp[4] == 'j':
                            self.b_j.style.background_color = 'Springgreen'
                        if self.resp[4] == 'k':
                            self.b_k.style.background_color = 'Springgreen'
                        if self.resp[4] == 'l':
                            self.b_l.style.background_color = 'Springgreen'
                        if self.resp[4] == 'ç':
                            self.b_cdl.style.background_color = 'Springgreen'
                        if self.resp[4] == 'z':
                            self.b_z.style.background_color = 'Springgreen'
                        if self.resp[4] == 'x':
                            self.b_x.style.background_color = 'Springgreen'
                        if self.resp[4] == 'c':
                            self.b_c.style.background_color = 'Springgreen'
                        if self.resp[4] == 'v':
                            self.b_v.style.background_color = 'Springgreen'
                        if self.resp[4] == 'b':
                            self.b_b.style.background_color = 'Springgreen'
                        if self.resp[4] == 'n':
                            self.b_n.style.background_color = 'Springgreen'
                        if self.resp[4] == 'm':
                            self.b_m.style.background_color = 'Springgreen'
                    else:
                        if self.resp[4] in termo_play:
                            self.letra_o0.style.background_color = 'Gold'
                            if ((self.resp[4] == 'q') and (self.b_q.style.background_color != 'Springgreen')):
                                self.b_q.style.background_color = 'Gold'
                            if ((self.resp[4] == 'w') and (self.b_w.style.background_color != 'Springgreen')):
                                self.b_w.style.background_color = 'Gold'
                            if ((self.resp[4] == 'e') and (self.b_e.style.background_color != 'Springgreen')):
                                self.b_e.style.background_color = 'Gold'
                            if ((self.resp[4] == 'r') and (self.b_r.style.background_color != 'Springgreen')):
                                self.b_r.style.background_color = 'Gold'
                            if ((self.resp[4] == 't') and (self.b_t.style.background_color != 'Springgreen')):
                                self.b_t.style.background_color = 'Gold'
                            if ((self.resp[4] == 'y') and (self.b_y.style.background_color != 'Springgreen')):
                                self.b_y.style.background_color = 'Gold'
                            if ((self.resp[4] == 'u') and (self.b_u.style.background_color != 'Springgreen')):
                                self.b_u.style.background_color = 'Gold'
                            if ((self.resp[4] == 'i') and (self.b_i.style.background_color != 'Springgreen')):
                                self.b_i.style.background_color = 'Gold'
                            if ((self.resp[4] == 'o') and (self.b_o.style.background_color != 'Springgreen')):
                                self.b_o.style.background_color = 'Gold'
                            if ((self.resp[4] == 'p') and (self.b_p.style.background_color != 'Springgreen')):
                                self.b_p.style.background_color = 'Gold'
                            if ((self.resp[4] == 'a') and (self.b_a.style.background_color != 'Springgreen')):
                                self.b_a.style.background_color = 'Gold'
                            if ((self.resp[4] == 's') and (self.b_s.style.background_color != 'Springgreen')):
                                self.b_s.style.background_color = 'Gold'
                            if ((self.resp[4] == 'd') and (self.b_d.style.background_color != 'Springgreen')):
                                self.b_d.style.background_color = 'Gold'
                            if ((self.resp[4] == 'f') and (self.b_f.style.background_color != 'Springgreen')):
                                self.b_f.style.background_color = 'Gold'
                            if ((self.resp[4] == 'g') and (self.b_g.style.background_color != 'Springgreen')):
                                self.b_g.style.background_color = 'Gold'
                            if ((self.resp[4] == 'h') and (self.b_h.style.background_color != 'Springgreen')):
                                self.b_h.style.background_color = 'Gold'
                            if ((self.resp[4] == 'j') and (self.b_j.style.background_color != 'Springgreen')):
                                self.b_j.style.background_color = 'Gold'
                            if ((self.resp[4] == 'k') and (self.b_k.style.background_color != 'Springgreen')):
                                self.b_k.style.background_color = 'Gold'
                            if ((self.resp[4] == 'l') and (self.b_l.style.background_color != 'Springgreen')):
                                self.b_l.style.background_color = 'Gold'
                            if ((self.resp[4] == 'ç') and (self.b_cdl.style.background_color != 'Springgreen')):
                                self.b_cdl.style.background_color = 'Gold'
                            if ((self.resp[4] == 'z') and (self.b_z.style.background_color != 'Springgreen')):
                                self.b_z.style.background_color = 'Gold'
                            if ((self.resp[4] == 'x') and (self.b_x.style.background_color != 'Springgreen')):
                                self.b_x.style.background_color = 'Gold'
                            if ((self.resp[4] == 'c') and (self.b_c.style.background_color != 'Springgreen')):
                                self.b_c.style.background_color = 'Gold'
                            if ((self.resp[4] == 'v') and (self.b_v.style.background_color != 'Springgreen')):
                                self.b_v.style.background_color = 'Gold'
                            if ((self.resp[4] == 'b') and (self.b_b.style.background_color != 'Springgreen')):
                                self.b_b.style.background_color = 'Gold'
                            if ((self.resp[4] == 'n') and (self.b_n.style.background_color != 'Springgreen')):
                                self.b_n.style.background_color = 'Gold'
                            if ((self.resp[4] == 'm') and (self.b_m.style.background_color != 'Springgreen')):
                                self.b_m.style.background_color = 'Gold'
                    self.contador = '1'
                else:
                    self.output1.text = '' + termo_play_Acento[0].upper()
                    self.letra_t0.style.background_color = 'Springgreen'
                    self.output2.text = '' + termo_play_Acento[1].upper()
                    self.letra_e0.style.background_color = 'Springgreen'
                    self.output3.text = '' + termo_play_Acento[2].upper()
                    self.letra_r0.style.background_color = 'Springgreen'
                    self.output4.text = '' + termo_play_Acento[3].upper()
                    self.letra_m0.style.background_color = 'Springgreen'
                    self.output5.text = '' + termo_play_Acento[4].upper()
                    self.letra_o0.style.background_color = 'Springgreen'
                    self.main_window.info_dialog('Você Ganhou!', f'{termo_play_Acento.upper()} era a palavra correta 🤩', )
                self.resposta = ''
                return 0
            else:
                if(self.contador=='0'):
                    self.main_window.info_dialog('Palavra inexistente!', 'A palavra digitada não é aceita 😒')
                    return 0

            if ((self.contador == '1') and (self.resposta in palavras_5char_existentes)):
                if (self.resposta != termo_play):
                    if self.resp[0] == termo_play[0]:
                        self.output6.text = '' + termo_play_Acento[0].upper()
                        self.letra_t1.style.background_color = 'Springgreen'
                        if self.resp[0] == 'q':
                            self.b_q.style.background_color = 'Springgreen'
                        if self.resp[0] == 'w':
                            self.b_w.style.background_color = 'Springgreen'
                        if self.resp[0] == 'e':
                            self.b_e.style.background_color = 'Springgreen'
                        if self.resp[0] == 'r':
                            self.b_r.style.background_color = 'Springgreen'
                        if self.resp[0] == 't':
                            self.b_t.style.background_color = 'Springgreen'
                        if self.resp[0] == 'y':
                            self.b_y.style.background_color = 'Springgreen'
                        if self.resp[0] == 'u':
                            self.b_u.style.background_color = 'Springgreen'
                        if self.resp[0] == 'i':
                            self.b_i.style.background_color = 'Springgreen'
                        if self.resp[0] == 'o':
                            self.b_o.style.background_color = 'Springgreen'
                        if self.resp[0] == 'p':
                            self.b_p.style.background_color = 'Springgreen'
                        if self.resp[0] == 'a':
                            self.b_a.style.background_color = 'Springgreen'
                        if self.resp[0] == 's':
                            self.b_s.style.background_color = 'Springgreen'
                        if self.resp[0] == 'd':
                            self.b_d.style.background_color = 'Springgreen'
                        if self.resp[0] == 'f':
                            self.b_f.style.background_color = 'Springgreen'
                        if self.resp[0] == 'g':
                            self.b_g.style.background_color = 'Springgreen'
                        if self.resp[0] == 'h':
                            self.b_h.style.background_color = 'Springgreen'
                        if self.resp[0] == 'j':
                            self.b_j.style.background_color = 'Springgreen'
                        if self.resp[0] == 'k':
                            self.b_k.style.background_color = 'Springgreen'
                        if self.resp[0] == 'l':
                            self.b_l.style.background_color = 'Springgreen'
                        if self.resp[0] == 'ç':
                            self.b_cdl.style.background_color = 'Springgreen'
                        if self.resp[0] == 'z':
                            self.b_z.style.background_color = 'Springgreen'
                        if self.resp[0] == 'x':
                            self.b_x.style.background_color = 'Springgreen'
                        if self.resp[0] == 'c':
                            self.b_c.style.background_color = 'Springgreen'
                        if self.resp[0] == 'v':
                            self.b_v.style.background_color = 'Springgreen'
                        if self.resp[0] == 'b':
                            self.b_b.style.background_color = 'Springgreen'
                        if self.resp[0] == 'n':
                            self.b_n.style.background_color = 'Springgreen'
                        if self.resp[0] == 'm':
                            self.b_m.style.background_color = 'Springgreen'
                    else:
                        if self.resp[0] in termo_play:
                            self.letra_t1.style.background_color = 'Gold'
                            if ((self.resp[0] == 'q') and (self.b_q.style.background_color != 'Springgreen')):
                                self.b_q.style.background_color = 'Gold'
                            if ((self.resp[0] == 'w') and (self.b_w.style.background_color != 'Springgreen')):
                                self.b_w.style.background_color = 'Gold'
                            if ((self.resp[0] == 'e') and (self.b_e.style.background_color != 'Springgreen')):
                                self.b_e.style.background_color = 'Gold'
                            if ((self.resp[0] == 'r') and (self.b_r.style.background_color != 'Springgreen')):
                                self.b_r.style.background_color = 'Gold'
                            if ((self.resp[0] == 't') and (self.b_t.style.background_color != 'Springgreen')):
                                self.b_t.style.background_color = 'Gold'
                            if ((self.resp[0] == 'y') and (self.b_y.style.background_color != 'Springgreen')):
                                self.b_y.style.background_color = 'Gold'
                            if ((self.resp[0] == 'u') and (self.b_u.style.background_color != 'Springgreen')):
                                self.b_u.style.background_color = 'Gold'
                            if ((self.resp[0] == 'i') and (self.b_i.style.background_color != 'Springgreen')):
                                self.b_i.style.background_color = 'Gold'
                            if ((self.resp[0] == 'o') and (self.b_o.style.background_color != 'Springgreen')):
                                self.b_o.style.background_color = 'Gold'
                            if ((self.resp[0] == 'p') and (self.b_p.style.background_color != 'Springgreen')):
                                self.b_p.style.background_color = 'Gold'
                            if ((self.resp[0] == 'a') and (self.b_a.style.background_color != 'Springgreen')):
                                self.b_a.style.background_color = 'Gold'
                            if ((self.resp[0] == 's') and (self.b_s.style.background_color != 'Springgreen')):
                                self.b_s.style.background_color = 'Gold'
                            if ((self.resp[0] == 'd') and (self.b_d.style.background_color != 'Springgreen')):
                                self.b_d.style.background_color = 'Gold'
                            if ((self.resp[0] == 'f') and (self.b_f.style.background_color != 'Springgreen')):
                                self.b_f.style.background_color = 'Gold'
                            if ((self.resp[0] == 'g') and (self.b_g.style.background_color != 'Springgreen')):
                                self.b_g.style.background_color = 'Gold'
                            if ((self.resp[0] == 'h') and (self.b_h.style.background_color != 'Springgreen')):
                                self.b_h.style.background_color = 'Gold'
                            if ((self.resp[0] == 'j') and (self.b_j.style.background_color != 'Springgreen')):
                                self.b_j.style.background_color = 'Gold'
                            if ((self.resp[0] == 'k') and (self.b_k.style.background_color != 'Springgreen')):
                                self.b_k.style.background_color = 'Gold'
                            if ((self.resp[0] == 'l') and (self.b_l.style.background_color != 'Springgreen')):
                                self.b_l.style.background_color = 'Gold'
                            if ((self.resp[0] == 'ç') and (self.b_cdl.style.background_color != 'Springgreen')):
                                self.b_cdl.style.background_color = 'Gold'
                            if ((self.resp[0] == 'z') and (self.b_z.style.background_color != 'Springgreen')):
                                self.b_z.style.background_color = 'Gold'
                            if ((self.resp[0] == 'x') and (self.b_x.style.background_color != 'Springgreen')):
                                self.b_x.style.background_color = 'Gold'
                            if ((self.resp[0] == 'c') and (self.b_c.style.background_color != 'Springgreen')):
                                self.b_c.style.background_color = 'Gold'
                            if ((self.resp[0] == 'v') and (self.b_v.style.background_color != 'Springgreen')):
                                self.b_v.style.background_color = 'Gold'
                            if ((self.resp[0] == 'b') and (self.b_b.style.background_color != 'Springgreen')):
                                self.b_b.style.background_color = 'Gold'
                            if ((self.resp[0] == 'n') and (self.b_n.style.background_color != 'Springgreen')):
                                self.b_n.style.background_color = 'Gold'
                            if ((self.resp[0] == 'm') and (self.b_m.style.background_color != 'Springgreen')):
                                self.b_m.style.background_color = 'Gold'
                        else:
                            if self.resp[0] == 'q':
                                self.b_q.style.background_color = 'Gray'
                            if self.resp[0] == 'w':
                                self.b_w.style.background_color = 'Gray'
                            if self.resp[0] == 'e':
                                self.b_e.style.background_color = 'Gray'
                            if self.resp[0] == 'r':
                                self.b_r.style.background_color = 'Gray'
                            if self.resp[0] == 't':
                                self.b_t.style.background_color = 'Gray'
                            if self.resp[0] == 'y':
                                self.b_y.style.background_color = 'Gray'
                            if self.resp[0] == 'u':
                                self.b_u.style.background_color = 'Gray'
                            if self.resp[0] == 'i':
                                self.b_i.style.background_color = 'Gray'
                            if self.resp[0] == 'o':
                                self.b_o.style.background_color = 'Gray'
                            if self.resp[0] == 'p':
                                self.b_p.style.background_color = 'Gray'
                            if self.resp[0] == 'a':
                                self.b_a.style.background_color = 'Gray'
                            if self.resp[0] == 's':
                                self.b_s.style.background_color = 'Gray'
                            if self.resp[0] == 'd':
                                self.b_d.style.background_color = 'Gray'
                            if self.resp[0] == 'f':
                                self.b_f.style.background_color = 'Gray'
                            if self.resp[0] == 'g':
                                self.b_g.style.background_color = 'Gray'
                            if self.resp[0] == 'h':
                                self.b_h.style.background_color = 'Gray'
                            if self.resp[0] == 'j':
                                self.b_j.style.background_color = 'Gray'
                            if self.resp[0] == 'k':
                                self.b_k.style.background_color = 'Gray'
                            if self.resp[0] == 'l':
                                self.b_l.style.background_color = 'Gray'
                            if self.resp[0] == 'ç':
                                self.b_cdl.style.background_color = 'Gray'
                            if self.resp[0] == 'z':
                                self.b_z.style.background_color = 'Gray'
                            if self.resp[0] == 'x':
                                self.b_x.style.background_color = 'Gray'
                            if self.resp[0] == 'c':
                                self.b_c.style.background_color = 'Gray'
                            if self.resp[0] == 'v':
                                self.b_v.style.background_color = 'Gray'
                            if self.resp[0] == 'b':
                                self.b_b.style.background_color = 'Gray'
                            if self.resp[0] == 'n':
                                self.b_n.style.background_color = 'Gray'
                            if self.resp[0] == 'm':
                                self.b_m.style.background_color = 'Gray'

                    if self.resp[1] == termo_play[1]:
                        self.output7.text = '' + termo_play_Acento[1].upper()
                        self.letra_e1.style.background_color = 'Springgreen'
                        if self.resp[1] == 'q':
                            self.b_q.style.background_color = 'Springgreen'
                        if self.resp[1] == 'w':
                            self.b_w.style.background_color = 'Springgreen'
                        if self.resp[1] == 'e':
                            self.b_e.style.background_color = 'Springgreen'
                        if self.resp[1] == 'r':
                            self.b_r.style.background_color = 'Springgreen'
                        if self.resp[1] == 't':
                            self.b_t.style.background_color = 'Springgreen'
                        if self.resp[1] == 'y':
                            self.b_y.style.background_color = 'Springgreen'
                        if self.resp[1] == 'u':
                            self.b_u.style.background_color = 'Springgreen'
                        if self.resp[1] == 'i':
                            self.b_i.style.background_color = 'Springgreen'
                        if self.resp[1] == 'o':
                            self.b_o.style.background_color = 'Springgreen'
                        if self.resp[1] == 'p':
                            self.b_p.style.background_color = 'Springgreen'
                        if self.resp[1] == 'a':
                            self.b_a.style.background_color = 'Springgreen'
                        if self.resp[1] == 's':
                            self.b_s.style.background_color = 'Springgreen'
                        if self.resp[1] == 'd':
                            self.b_d.style.background_color = 'Springgreen'
                        if self.resp[1] == 'f':
                            self.b_f.style.background_color = 'Springgreen'
                        if self.resp[1] == 'g':
                            self.b_g.style.background_color = 'Springgreen'
                        if self.resp[1] == 'h':
                            self.b_h.style.background_color = 'Springgreen'
                        if self.resp[1] == 'j':
                            self.b_j.style.background_color = 'Springgreen'
                        if self.resp[1] == 'k':
                            self.b_k.style.background_color = 'Springgreen'
                        if self.resp[1] == 'l':
                            self.b_l.style.background_color = 'Springgreen'
                        if self.resp[1] == 'ç':
                            self.b_cdl.style.background_color = 'Springgreen'
                        if self.resp[1] == 'z':
                            self.b_z.style.background_color = 'Springgreen'
                        if self.resp[1] == 'x':
                            self.b_x.style.background_color = 'Springgreen'
                        if self.resp[1] == 'c':
                            self.b_c.style.background_color = 'Springgreen'
                        if self.resp[1] == 'v':
                            self.b_v.style.background_color = 'Springgreen'
                        if self.resp[1] == 'b':
                            self.b_b.style.background_color = 'Springgreen'
                        if self.resp[1] == 'n':
                            self.b_n.style.background_color = 'Springgreen'
                        if self.resp[1] == 'm':
                            self.b_m.style.background_color = 'Springgreen'
                    else:
                        if self.resp[1] in termo_play:
                            self.letra_e1.style.background_color = 'Gold'
                            if ((self.resp[1] == 'q') and (self.b_q.style.background_color != 'Springgreen')):
                                self.b_q.style.background_color = 'Gold'
                            if ((self.resp[1] == 'w') and (self.b_w.style.background_color != 'Springgreen')):
                                self.b_w.style.background_color = 'Gold'
                            if ((self.resp[1] == 'e') and (self.b_e.style.background_color != 'Springgreen')):
                                self.b_e.style.background_color = 'Gold'
                            if ((self.resp[1] == 'r') and (self.b_r.style.background_color != 'Springgreen')):
                                self.b_r.style.background_color = 'Gold'
                            if ((self.resp[1] == 't') and (self.b_t.style.background_color != 'Springgreen')):
                                self.b_t.style.background_color = 'Gold'
                            if ((self.resp[1] == 'y') and (self.b_y.style.background_color != 'Springgreen')):
                                self.b_y.style.background_color = 'Gold'
                            if ((self.resp[1] == 'u') and (self.b_u.style.background_color != 'Springgreen')):
                                self.b_u.style.background_color = 'Gold'
                            if ((self.resp[1] == 'i') and (self.b_i.style.background_color != 'Springgreen')):
                                self.b_i.style.background_color = 'Gold'
                            if ((self.resp[1] == 'o') and (self.b_o.style.background_color != 'Springgreen')):
                                self.b_o.style.background_color = 'Gold'
                            if ((self.resp[1] == 'p') and (self.b_p.style.background_color != 'Springgreen')):
                                self.b_p.style.background_color = 'Gold'
                            if ((self.resp[1] == 'a') and (self.b_a.style.background_color != 'Springgreen')):
                                self.b_a.style.background_color = 'Gold'
                            if ((self.resp[1] == 's') and (self.b_s.style.background_color != 'Springgreen')):
                                self.b_s.style.background_color = 'Gold'
                            if ((self.resp[1] == 'd') and (self.b_d.style.background_color != 'Springgreen')):
                                self.b_d.style.background_color = 'Gold'
                            if ((self.resp[1] == 'f') and (self.b_f.style.background_color != 'Springgreen')):
                                self.b_f.style.background_color = 'Gold'
                            if ((self.resp[1] == 'g') and (self.b_g.style.background_color != 'Springgreen')):
                                self.b_g.style.background_color = 'Gold'
                            if ((self.resp[1] == 'h') and (self.b_h.style.background_color != 'Springgreen')):
                                self.b_h.style.background_color = 'Gold'
                            if ((self.resp[1] == 'j') and (self.b_j.style.background_color != 'Springgreen')):
                                self.b_j.style.background_color = 'Gold'
                            if ((self.resp[1] == 'k') and (self.b_k.style.background_color != 'Springgreen')):
                                self.b_k.style.background_color = 'Gold'
                            if ((self.resp[1] == 'l') and (self.b_l.style.background_color != 'Springgreen')):
                                self.b_l.style.background_color = 'Gold'
                            if ((self.resp[1] == 'ç') and (self.b_cdl.style.background_color != 'Springgreen')):
                                self.b_cdl.style.background_color = 'Gold'
                            if ((self.resp[1] == 'z') and (self.b_z.style.background_color != 'Springgreen')):
                                self.b_z.style.background_color = 'Gold'
                            if ((self.resp[1] == 'x') and (self.b_x.style.background_color != 'Springgreen')):
                                self.b_x.style.background_color = 'Gold'
                            if ((self.resp[1] == 'c') and (self.b_c.style.background_color != 'Springgreen')):
                                self.b_c.style.background_color = 'Gold'
                            if ((self.resp[1] == 'v') and (self.b_v.style.background_color != 'Springgreen')):
                                self.b_v.style.background_color = 'Gold'
                            if ((self.resp[1] == 'b') and (self.b_b.style.background_color != 'Springgreen')):
                                self.b_b.style.background_color = 'Gold'
                            if ((self.resp[1] == 'n') and (self.b_n.style.background_color != 'Springgreen')):
                                self.b_n.style.background_color = 'Gold'
                            if ((self.resp[1] == 'm') and (self.b_m.style.background_color != 'Springgreen')):
                                self.b_m.style.background_color = 'Gold'
                        else:
                            if self.resp[1] == 'q':
                                self.b_q.style.background_color = 'Gray'
                            if self.resp[1] == 'w':
                                self.b_w.style.background_color = 'Gray'
                            if self.resp[1] == 'e':
                                self.b_e.style.background_color = 'Gray'
                            if self.resp[1] == 'r':
                                self.b_r.style.background_color = 'Gray'
                            if self.resp[1] == 't':
                                self.b_t.style.background_color = 'Gray'
                            if self.resp[1] == 'y':
                                self.b_y.style.background_color = 'Gray'
                            if self.resp[1] == 'u':
                                self.b_u.style.background_color = 'Gray'
                            if self.resp[1] == 'i':
                                self.b_i.style.background_color = 'Gray'
                            if self.resp[1] == 'o':
                                self.b_o.style.background_color = 'Gray'
                            if self.resp[1] == 'p':
                                self.b_p.style.background_color = 'Gray'
                            if self.resp[1] == 'a':
                                self.b_a.style.background_color = 'Gray'
                            if self.resp[1] == 's':
                                self.b_s.style.background_color = 'Gray'
                            if self.resp[1] == 'd':
                                self.b_d.style.background_color = 'Gray'
                            if self.resp[1] == 'f':
                                self.b_f.style.background_color = 'Gray'
                            if self.resp[1] == 'g':
                                self.b_g.style.background_color = 'Gray'
                            if self.resp[1] == 'h':
                                self.b_h.style.background_color = 'Gray'
                            if self.resp[1] == 'j':
                                self.b_j.style.background_color = 'Gray'
                            if self.resp[1] == 'k':
                                self.b_k.style.background_color = 'Gray'
                            if self.resp[1] == 'l':
                                self.b_l.style.background_color = 'Gray'
                            if self.resp[1] == 'ç':
                                self.b_cdl.style.background_color = 'Gray'
                            if self.resp[1] == 'z':
                                self.b_z.style.background_color = 'Gray'
                            if self.resp[1] == 'x':
                                self.b_x.style.background_color = 'Gray'
                            if self.resp[1] == 'c':
                                self.b_c.style.background_color = 'Gray'
                            if self.resp[1] == 'v':
                                self.b_v.style.background_color = 'Gray'
                            if self.resp[1] == 'b':
                                self.b_b.style.background_color = 'Gray'
                            if self.resp[1] == 'n':
                                self.b_n.style.background_color = 'Gray'
                            if self.resp[1] == 'm':
                                self.b_m.style.background_color = 'Gray'

                    if self.resp[2] == termo_play[2]:
                        self.output8.text = '' + termo_play_Acento[2].upper()
                        self.letra_r1.style.background_color = 'Springgreen'
                        if self.resp[2] == 'q':
                            self.b_q.style.background_color = 'Springgreen'
                        if self.resp[2] == 'w':
                            self.b_w.style.background_color = 'Springgreen'
                        if self.resp[2] == 'e':
                            self.b_e.style.background_color = 'Springgreen'
                        if self.resp[2] == 'r':
                            self.b_r.style.background_color = 'Springgreen'
                        if self.resp[2] == 't':
                            self.b_t.style.background_color = 'Springgreen'
                        if self.resp[2] == 'y':
                            self.b_y.style.background_color = 'Springgreen'
                        if self.resp[2] == 'u':
                            self.b_u.style.background_color = 'Springgreen'
                        if self.resp[2] == 'i':
                            self.b_i.style.background_color = 'Springgreen'
                        if self.resp[2] == 'o':
                            self.b_o.style.background_color = 'Springgreen'
                        if self.resp[2] == 'p':
                            self.b_p.style.background_color = 'Springgreen'
                        if self.resp[2] == 'a':
                            self.b_a.style.background_color = 'Springgreen'
                        if self.resp[2] == 's':
                            self.b_s.style.background_color = 'Springgreen'
                        if self.resp[2] == 'd':
                            self.b_d.style.background_color = 'Springgreen'
                        if self.resp[2] == 'f':
                            self.b_f.style.background_color = 'Springgreen'
                        if self.resp[2] == 'g':
                            self.b_g.style.background_color = 'Springgreen'
                        if self.resp[2] == 'h':
                            self.b_h.style.background_color = 'Springgreen'
                        if self.resp[2] == 'j':
                            self.b_j.style.background_color = 'Springgreen'
                        if self.resp[2] == 'k':
                            self.b_k.style.background_color = 'Springgreen'
                        if self.resp[2] == 'l':
                            self.b_l.style.background_color = 'Springgreen'
                        if self.resp[2] == 'ç':
                            self.b_cdl.style.background_color = 'Springgreen'
                        if self.resp[2] == 'z':
                            self.b_z.style.background_color = 'Springgreen'
                        if self.resp[2] == 'x':
                            self.b_x.style.background_color = 'Springgreen'
                        if self.resp[2] == 'c':
                            self.b_c.style.background_color = 'Springgreen'
                        if self.resp[2] == 'v':
                            self.b_v.style.background_color = 'Springgreen'
                        if self.resp[2] == 'b':
                            self.b_b.style.background_color = 'Springgreen'
                        if self.resp[2] == 'n':
                            self.b_n.style.background_color = 'Springgreen'
                        if self.resp[2] == 'm':
                            self.b_m.style.background_color = 'Springgreen'
                    else:
                        if self.resp[2] in termo_play:
                            self.letra_r1.style.background_color = 'Gold'
                            if ((self.resp[2] == 'q') and (self.b_q.style.background_color != 'Springgreen')):
                                self.b_q.style.background_color = 'Gold'
                            if ((self.resp[2] == 'w') and (self.b_w.style.background_color != 'Springgreen')):
                                self.b_w.style.background_color = 'Gold'
                            if ((self.resp[2] == 'e') and (self.b_e.style.background_color != 'Springgreen')):
                                self.b_e.style.background_color = 'Gold'
                            if ((self.resp[2] == 'r') and (self.b_r.style.background_color != 'Springgreen')):
                                self.b_r.style.background_color = 'Gold'
                            if ((self.resp[2] == 't') and (self.b_t.style.background_color != 'Springgreen')):
                                self.b_t.style.background_color = 'Gold'
                            if ((self.resp[2] == 'y') and (self.b_y.style.background_color != 'Springgreen')):
                                self.b_y.style.background_color = 'Gold'
                            if ((self.resp[2] == 'u') and (self.b_u.style.background_color != 'Springgreen')):
                                self.b_u.style.background_color = 'Gold'
                            if ((self.resp[2] == 'i') and (self.b_i.style.background_color != 'Springgreen')):
                                self.b_i.style.background_color = 'Gold'
                            if ((self.resp[2] == 'o') and (self.b_o.style.background_color != 'Springgreen')):
                                self.b_o.style.background_color = 'Gold'
                            if ((self.resp[2] == 'p') and (self.b_p.style.background_color != 'Springgreen')):
                                self.b_p.style.background_color = 'Gold'
                            if ((self.resp[2] == 'a') and (self.b_a.style.background_color != 'Springgreen')):
                                self.b_a.style.background_color = 'Gold'
                            if ((self.resp[2] == 's') and (self.b_s.style.background_color != 'Springgreen')):
                                self.b_s.style.background_color = 'Gold'
                            if ((self.resp[2] == 'd') and (self.b_d.style.background_color != 'Springgreen')):
                                self.b_d.style.background_color = 'Gold'
                            if ((self.resp[2] == 'f') and (self.b_f.style.background_color != 'Springgreen')):
                                self.b_f.style.background_color = 'Gold'
                            if ((self.resp[2] == 'g') and (self.b_g.style.background_color != 'Springgreen')):
                                self.b_g.style.background_color = 'Gold'
                            if ((self.resp[2] == 'h') and (self.b_h.style.background_color != 'Springgreen')):
                                self.b_h.style.background_color = 'Gold'
                            if ((self.resp[2] == 'j') and (self.b_j.style.background_color != 'Springgreen')):
                                self.b_j.style.background_color = 'Gold'
                            if ((self.resp[2] == 'k') and (self.b_k.style.background_color != 'Springgreen')):
                                self.b_k.style.background_color = 'Gold'
                            if ((self.resp[2] == 'l') and (self.b_l.style.background_color != 'Springgreen')):
                                self.b_l.style.background_color = 'Gold'
                            if ((self.resp[2] == 'ç') and (self.b_cdl.style.background_color != 'Springgreen')):
                                self.b_cdl.style.background_color = 'Gold'
                            if ((self.resp[2] == 'z') and (self.b_z.style.background_color != 'Springgreen')):
                                self.b_z.style.background_color = 'Gold'
                            if ((self.resp[2] == 'x') and (self.b_x.style.background_color != 'Springgreen')):
                                self.b_x.style.background_color = 'Gold'
                            if ((self.resp[2] == 'c') and (self.b_c.style.background_color != 'Springgreen')):
                                self.b_c.style.background_color = 'Gold'
                            if ((self.resp[2] == 'v') and (self.b_v.style.background_color != 'Springgreen')):
                                self.b_v.style.background_color = 'Gold'
                            if ((self.resp[2] == 'b') and (self.b_b.style.background_color != 'Springgreen')):
                                self.b_b.style.background_color = 'Gold'
                            if ((self.resp[2] == 'n') and (self.b_n.style.background_color != 'Springgreen')):
                                self.b_n.style.background_color = 'Gold'
                            if ((self.resp[2] == 'm') and (self.b_m.style.background_color != 'Springgreen')):
                                self.b_m.style.background_color = 'Gold'
                        else:
                            if self.resp[2] == 'q':
                                self.b_q.style.background_color = 'Gray'
                            if self.resp[2] == 'w':
                                self.b_w.style.background_color = 'Gray'
                            if self.resp[2] == 'e':
                                self.b_e.style.background_color = 'Gray'
                            if self.resp[2] == 'r':
                                self.b_r.style.background_color = 'Gray'
                            if self.resp[2] == 't':
                                self.b_t.style.background_color = 'Gray'
                            if self.resp[2] == 'y':
                                self.b_y.style.background_color = 'Gray'
                            if self.resp[2] == 'u':
                                self.b_u.style.background_color = 'Gray'
                            if self.resp[2] == 'i':
                                self.b_i.style.background_color = 'Gray'
                            if self.resp[2] == 'o':
                                self.b_o.style.background_color = 'Gray'
                            if self.resp[2] == 'p':
                                self.b_p.style.background_color = 'Gray'
                            if self.resp[2] == 'a':
                                self.b_a.style.background_color = 'Gray'
                            if self.resp[2] == 's':
                                self.b_s.style.background_color = 'Gray'
                            if self.resp[2] == 'd':
                                self.b_d.style.background_color = 'Gray'
                            if self.resp[2] == 'f':
                                self.b_f.style.background_color = 'Gray'
                            if self.resp[2] == 'g':
                                self.b_g.style.background_color = 'Gray'
                            if self.resp[2] == 'h':
                                self.b_h.style.background_color = 'Gray'
                            if self.resp[2] == 'j':
                                self.b_j.style.background_color = 'Gray'
                            if self.resp[2] == 'k':
                                self.b_k.style.background_color = 'Gray'
                            if self.resp[2] == 'l':
                                self.b_l.style.background_color = 'Gray'
                            if self.resp[2] == 'ç':
                                self.b_cdl.style.background_color = 'Gray'
                            if self.resp[2] == 'z':
                                self.b_z.style.background_color = 'Gray'
                            if self.resp[2] == 'x':
                                self.b_x.style.background_color = 'Gray'
                            if self.resp[2] == 'c':
                                self.b_c.style.background_color = 'Gray'
                            if self.resp[2] == 'v':
                                self.b_v.style.background_color = 'Gray'
                            if self.resp[2] == 'b':
                                self.b_b.style.background_color = 'Gray'
                            if self.resp[2] == 'n':
                                self.b_n.style.background_color = 'Gray'
                            if self.resp[2] == 'm':
                                self.b_m.style.background_color = 'Gray'

                    if self.resp[3] == termo_play[3]:
                        self.output9.text = '' + termo_play_Acento[3].upper()
                        self.letra_m1.style.background_color = 'Springgreen'
                        if self.resp[3] == 'q':
                            self.b_q.style.background_color = 'Springgreen'
                        if self.resp[3] == 'w':
                            self.b_w.style.background_color = 'Springgreen'
                        if self.resp[3] == 'e':
                            self.b_e.style.background_color = 'Springgreen'
                        if self.resp[3] == 'r':
                            self.b_r.style.background_color = 'Springgreen'
                        if self.resp[3] == 't':
                            self.b_t.style.background_color = 'Springgreen'
                        if self.resp[3] == 'y':
                            self.b_y.style.background_color = 'Springgreen'
                        if self.resp[3] == 'u':
                            self.b_u.style.background_color = 'Springgreen'
                        if self.resp[3] == 'i':
                            self.b_i.style.background_color = 'Springgreen'
                        if self.resp[3] == 'o':
                            self.b_o.style.background_color = 'Springgreen'
                        if self.resp[3] == 'p':
                            self.b_p.style.background_color = 'Springgreen'
                        if self.resp[3] == 'a':
                            self.b_a.style.background_color = 'Springgreen'
                        if self.resp[3] == 's':
                            self.b_s.style.background_color = 'Springgreen'
                        if self.resp[3] == 'd':
                            self.b_d.style.background_color = 'Springgreen'
                        if self.resp[3] == 'f':
                            self.b_f.style.background_color = 'Springgreen'
                        if self.resp[3] == 'g':
                            self.b_g.style.background_color = 'Springgreen'
                        if self.resp[3] == 'h':
                            self.b_h.style.background_color = 'Springgreen'
                        if self.resp[3] == 'j':
                            self.b_j.style.background_color = 'Springgreen'
                        if self.resp[3] == 'k':
                            self.b_k.style.background_color = 'Springgreen'
                        if self.resp[3] == 'l':
                            self.b_l.style.background_color = 'Springgreen'
                        if self.resp[3] == 'ç':
                            self.b_cdl.style.background_color = 'Springgreen'
                        if self.resp[3] == 'z':
                            self.b_z.style.background_color = 'Springgreen'
                        if self.resp[3] == 'x':
                            self.b_x.style.background_color = 'Springgreen'
                        if self.resp[3] == 'c':
                            self.b_c.style.background_color = 'Springgreen'
                        if self.resp[3] == 'v':
                            self.b_v.style.background_color = 'Springgreen'
                        if self.resp[3] == 'b':
                            self.b_b.style.background_color = 'Springgreen'
                        if self.resp[3] == 'n':
                            self.b_n.style.background_color = 'Springgreen'
                        if self.resp[3] == 'm':
                            self.b_m.style.background_color = 'Springgreen'
                    else:
                        if self.resp[3] in termo_play:
                            self.letra_m1.style.background_color = 'Gold'
                            if ((self.resp[3] == 'q') and (self.b_q.style.background_color != 'Springgreen')):
                                self.b_q.style.background_color = 'Gold'
                            if ((self.resp[3] == 'w') and (self.b_w.style.background_color != 'Springgreen')):
                                self.b_w.style.background_color = 'Gold'
                            if ((self.resp[3] == 'e') and (self.b_e.style.background_color != 'Springgreen')):
                                self.b_e.style.background_color = 'Gold'
                            if ((self.resp[3] == 'r') and (self.b_r.style.background_color != 'Springgreen')):
                                self.b_r.style.background_color = 'Gold'
                            if ((self.resp[3] == 't') and (self.b_t.style.background_color != 'Springgreen')):
                                self.b_t.style.background_color = 'Gold'
                            if ((self.resp[3] == 'y') and (self.b_y.style.background_color != 'Springgreen')):
                                self.b_y.style.background_color = 'Gold'
                            if ((self.resp[3] == 'u') and (self.b_u.style.background_color != 'Springgreen')):
                                self.b_u.style.background_color = 'Gold'
                            if ((self.resp[3] == 'i') and (self.b_i.style.background_color != 'Springgreen')):
                                self.b_i.style.background_color = 'Gold'
                            if ((self.resp[3] == 'o') and (self.b_o.style.background_color != 'Springgreen')):
                                self.b_o.style.background_color = 'Gold'
                            if ((self.resp[3] == 'p') and (self.b_p.style.background_color != 'Springgreen')):
                                self.b_p.style.background_color = 'Gold'
                            if ((self.resp[3] == 'a') and (self.b_a.style.background_color != 'Springgreen')):
                                self.b_a.style.background_color = 'Gold'
                            if ((self.resp[3] == 's') and (self.b_s.style.background_color != 'Springgreen')):
                                self.b_s.style.background_color = 'Gold'
                            if ((self.resp[3] == 'd') and (self.b_d.style.background_color != 'Springgreen')):
                                self.b_d.style.background_color = 'Gold'
                            if ((self.resp[3] == 'f') and (self.b_f.style.background_color != 'Springgreen')):
                                self.b_f.style.background_color = 'Gold'
                            if ((self.resp[3] == 'g') and (self.b_g.style.background_color != 'Springgreen')):
                                self.b_g.style.background_color = 'Gold'
                            if ((self.resp[3] == 'h') and (self.b_h.style.background_color != 'Springgreen')):
                                self.b_h.style.background_color = 'Gold'
                            if ((self.resp[3] == 'j') and (self.b_j.style.background_color != 'Springgreen')):
                                self.b_j.style.background_color = 'Gold'
                            if ((self.resp[3] == 'k') and (self.b_k.style.background_color != 'Springgreen')):
                                self.b_k.style.background_color = 'Gold'
                            if ((self.resp[3] == 'l') and (self.b_l.style.background_color != 'Springgreen')):
                                self.b_l.style.background_color = 'Gold'
                            if ((self.resp[3] == 'ç') and (self.b_cdl.style.background_color != 'Springgreen')):
                                self.b_cdl.style.background_color = 'Gold'
                            if ((self.resp[3] == 'z') and (self.b_z.style.background_color != 'Springgreen')):
                                self.b_z.style.background_color = 'Gold'
                            if ((self.resp[3] == 'x') and (self.b_x.style.background_color != 'Springgreen')):
                                self.b_x.style.background_color = 'Gold'
                            if ((self.resp[3] == 'c') and (self.b_c.style.background_color != 'Springgreen')):
                                self.b_c.style.background_color = 'Gold'
                            if ((self.resp[3] == 'v') and (self.b_v.style.background_color != 'Springgreen')):
                                self.b_v.style.background_color = 'Gold'
                            if ((self.resp[3] == 'b') and (self.b_b.style.background_color != 'Springgreen')):
                                self.b_b.style.background_color = 'Gold'
                            if ((self.resp[3] == 'n') and (self.b_n.style.background_color != 'Springgreen')):
                                self.b_n.style.background_color = 'Gold'
                            if ((self.resp[3] == 'm') and (self.b_m.style.background_color != 'Springgreen')):
                                self.b_m.style.background_color = 'Gold'
                        else:
                            if self.resp[3] == 'q':
                                self.b_q.style.background_color = 'Gray'
                            if self.resp[3] == 'w':
                                self.b_w.style.background_color = 'Gray'
                            if self.resp[3] == 'e':
                                self.b_e.style.background_color = 'Gray'
                            if self.resp[3] == 'r':
                                self.b_r.style.background_color = 'Gray'
                            if self.resp[3] == 't':
                                self.b_t.style.background_color = 'Gray'
                            if self.resp[3] == 'y':
                                self.b_y.style.background_color = 'Gray'
                            if self.resp[3] == 'u':
                                self.b_u.style.background_color = 'Gray'
                            if self.resp[3] == 'i':
                                self.b_i.style.background_color = 'Gray'
                            if self.resp[3] == 'o':
                                self.b_o.style.background_color = 'Gray'
                            if self.resp[3] == 'p':
                                self.b_p.style.background_color = 'Gray'
                            if self.resp[3] == 'a':
                                self.b_a.style.background_color = 'Gray'
                            if self.resp[3] == 's':
                                self.b_s.style.background_color = 'Gray'
                            if self.resp[3] == 'd':
                                self.b_d.style.background_color = 'Gray'
                            if self.resp[3] == 'f':
                                self.b_f.style.background_color = 'Gray'
                            if self.resp[3] == 'g':
                                self.b_g.style.background_color = 'Gray'
                            if self.resp[3] == 'h':
                                self.b_h.style.background_color = 'Gray'
                            if self.resp[3] == 'j':
                                self.b_j.style.background_color = 'Gray'
                            if self.resp[3] == 'k':
                                self.b_k.style.background_color = 'Gray'
                            if self.resp[3] == 'l':
                                self.b_l.style.background_color = 'Gray'
                            if self.resp[3] == 'ç':
                                self.b_cdl.style.background_color = 'Gray'
                            if self.resp[3] == 'z':
                                self.b_z.style.background_color = 'Gray'
                            if self.resp[3] == 'x':
                                self.b_x.style.background_color = 'Gray'
                            if self.resp[3] == 'c':
                                self.b_c.style.background_color = 'Gray'
                            if self.resp[3] == 'v':
                                self.b_v.style.background_color = 'Gray'
                            if self.resp[3] == 'b':
                                self.b_b.style.background_color = 'Gray'
                            if self.resp[3] == 'n':
                                self.b_n.style.background_color = 'Gray'
                            if self.resp[3] == 'm':
                                self.b_m.style.background_color = 'Gray'

                    if self.resp[4] == termo_play[4]:
                        self.output10.text = '' + termo_play_Acento[4].upper()
                        self.letra_o1.style.background_color = 'Springgreen'
                        if self.resp[4] == 'q':
                            self.b_q.style.background_color = 'Springgreen'
                        if self.resp[4] == 'w':
                            self.b_w.style.background_color = 'Springgreen'
                        if self.resp[4] == 'e':
                            self.b_e.style.background_color = 'Springgreen'
                        if self.resp[4] == 'r':
                            self.b_r.style.background_color = 'Springgreen'
                        if self.resp[4] == 't':
                            self.b_t.style.background_color = 'Springgreen'
                        if self.resp[4] == 'y':
                            self.b_y.style.background_color = 'Springgreen'
                        if self.resp[4] == 'u':
                            self.b_u.style.background_color = 'Springgreen'
                        if self.resp[4] == 'i':
                            self.b_i.style.background_color = 'Springgreen'
                        if self.resp[4] == 'o':
                            self.b_o.style.background_color = 'Springgreen'
                        if self.resp[4] == 'p':
                            self.b_p.style.background_color = 'Springgreen'
                        if self.resp[4] == 'a':
                            self.b_a.style.background_color = 'Springgreen'
                        if self.resp[4] == 's':
                            self.b_s.style.background_color = 'Springgreen'
                        if self.resp[4] == 'd':
                            self.b_d.style.background_color = 'Springgreen'
                        if self.resp[4] == 'f':
                            self.b_f.style.background_color = 'Springgreen'
                        if self.resp[4] == 'g':
                            self.b_g.style.background_color = 'Springgreen'
                        if self.resp[4] == 'h':
                            self.b_h.style.background_color = 'Springgreen'
                        if self.resp[4] == 'j':
                            self.b_j.style.background_color = 'Springgreen'
                        if self.resp[4] == 'k':
                            self.b_k.style.background_color = 'Springgreen'
                        if self.resp[4] == 'l':
                            self.b_l.style.background_color = 'Springgreen'
                        if self.resp[4] == 'ç':
                            self.b_cdl.style.background_color = 'Springgreen'
                        if self.resp[4] == 'z':
                            self.b_z.style.background_color = 'Springgreen'
                        if self.resp[4] == 'x':
                            self.b_x.style.background_color = 'Springgreen'
                        if self.resp[4] == 'c':
                            self.b_c.style.background_color = 'Springgreen'
                        if self.resp[4] == 'v':
                            self.b_v.style.background_color = 'Springgreen'
                        if self.resp[4] == 'b':
                            self.b_b.style.background_color = 'Springgreen'
                        if self.resp[4] == 'n':
                            self.b_n.style.background_color = 'Springgreen'
                        if self.resp[4] == 'm':
                            self.b_m.style.background_color = 'Springgreen'
                    else:
                        if self.resp[4] in termo_play:
                            self.letra_o1.style.background_color = 'Gold'
                            if ((self.resp[4] == 'q') and (self.b_q.style.background_color != 'Springgreen')):
                                self.b_q.style.background_color = 'Gold'
                            if ((self.resp[4] == 'w') and (self.b_w.style.background_color != 'Springgreen')):
                                self.b_w.style.background_color = 'Gold'
                            if ((self.resp[4] == 'e') and (self.b_e.style.background_color != 'Springgreen')):
                                self.b_e.style.background_color = 'Gold'
                            if ((self.resp[4] == 'r') and (self.b_r.style.background_color != 'Springgreen')):
                                self.b_r.style.background_color = 'Gold'
                            if ((self.resp[4] == 't') and (self.b_t.style.background_color != 'Springgreen')):
                                self.b_t.style.background_color = 'Gold'
                            if ((self.resp[4] == 'y') and (self.b_y.style.background_color != 'Springgreen')):
                                self.b_y.style.background_color = 'Gold'
                            if ((self.resp[4] == 'u') and (self.b_u.style.background_color != 'Springgreen')):
                                self.b_u.style.background_color = 'Gold'
                            if ((self.resp[4] == 'i') and (self.b_i.style.background_color != 'Springgreen')):
                                self.b_i.style.background_color = 'Gold'
                            if ((self.resp[4] == 'o') and (self.b_o.style.background_color != 'Springgreen')):
                                self.b_o.style.background_color = 'Gold'
                            if ((self.resp[4] == 'p') and (self.b_p.style.background_color != 'Springgreen')):
                                self.b_p.style.background_color = 'Gold'
                            if ((self.resp[4] == 'a') and (self.b_a.style.background_color != 'Springgreen')):
                                self.b_a.style.background_color = 'Gold'
                            if ((self.resp[4] == 's') and (self.b_s.style.background_color != 'Springgreen')):
                                self.b_s.style.background_color = 'Gold'
                            if ((self.resp[4] == 'd') and (self.b_d.style.background_color != 'Springgreen')):
                                self.b_d.style.background_color = 'Gold'
                            if ((self.resp[4] == 'f') and (self.b_f.style.background_color != 'Springgreen')):
                                self.b_f.style.background_color = 'Gold'
                            if ((self.resp[4] == 'g') and (self.b_g.style.background_color != 'Springgreen')):
                                self.b_g.style.background_color = 'Gold'
                            if ((self.resp[4] == 'h') and (self.b_h.style.background_color != 'Springgreen')):
                                self.b_h.style.background_color = 'Gold'
                            if ((self.resp[4] == 'j') and (self.b_j.style.background_color != 'Springgreen')):
                                self.b_j.style.background_color = 'Gold'
                            if ((self.resp[4] == 'k') and (self.b_k.style.background_color != 'Springgreen')):
                                self.b_k.style.background_color = 'Gold'
                            if ((self.resp[4] == 'l') and (self.b_l.style.background_color != 'Springgreen')):
                                self.b_l.style.background_color = 'Gold'
                            if ((self.resp[4] == 'ç') and (self.b_cdl.style.background_color != 'Springgreen')):
                                self.b_cdl.style.background_color = 'Gold'
                            if ((self.resp[4] == 'z') and (self.b_z.style.background_color != 'Springgreen')):
                                self.b_z.style.background_color = 'Gold'
                            if ((self.resp[4] == 'x') and (self.b_x.style.background_color != 'Springgreen')):
                                self.b_x.style.background_color = 'Gold'
                            if ((self.resp[4] == 'c') and (self.b_c.style.background_color != 'Springgreen')):
                                self.b_c.style.background_color = 'Gold'
                            if ((self.resp[4] == 'v') and (self.b_v.style.background_color != 'Springgreen')):
                                self.b_v.style.background_color = 'Gold'
                            if ((self.resp[4] == 'b') and (self.b_b.style.background_color != 'Springgreen')):
                                self.b_b.style.background_color = 'Gold'
                            if ((self.resp[4] == 'n') and (self.b_n.style.background_color != 'Springgreen')):
                                self.b_n.style.background_color = 'Gold'
                            if ((self.resp[4] == 'm') and (self.b_m.style.background_color != 'Springgreen')):
                                self.b_m.style.background_color = 'Gold'
                        else:
                            if self.resp[4] == 'q':
                                self.b_q.style.background_color = 'Gray'
                            if self.resp[4] == 'w':
                                self.b_w.style.background_color = 'Gray'
                            if self.resp[4] == 'e':
                                self.b_e.style.background_color = 'Gray'
                            if self.resp[4] == 'r':
                                self.b_r.style.background_color = 'Gray'
                            if self.resp[4] == 't':
                                self.b_t.style.background_color = 'Gray'
                            if self.resp[4] == 'y':
                                self.b_y.style.background_color = 'Gray'
                            if self.resp[4] == 'u':
                                self.b_u.style.background_color = 'Gray'
                            if self.resp[4] == 'i':
                                self.b_i.style.background_color = 'Gray'
                            if self.resp[4] == 'o':
                                self.b_o.style.background_color = 'Gray'
                            if self.resp[4] == 'p':
                                self.b_p.style.background_color = 'Gray'
                            if self.resp[4] == 'a':
                                self.b_a.style.background_color = 'Gray'
                            if self.resp[4] == 's':
                                self.b_s.style.background_color = 'Gray'
                            if self.resp[4] == 'd':
                                self.b_d.style.background_color = 'Gray'
                            if self.resp[4] == 'f':
                                self.b_f.style.background_color = 'Gray'
                            if self.resp[4] == 'g':
                                self.b_g.style.background_color = 'Gray'
                            if self.resp[4] == 'h':
                                self.b_h.style.background_color = 'Gray'
                            if self.resp[4] == 'j':
                                self.b_j.style.background_color = 'Gray'
                            if self.resp[4] == 'k':
                                self.b_k.style.background_color = 'Gray'
                            if self.resp[4] == 'l':
                                self.b_l.style.background_color = 'Gray'
                            if self.resp[4] == 'ç':
                                self.b_cdl.style.background_color = 'Gray'
                            if self.resp[4] == 'z':
                                self.b_z.style.background_color = 'Gray'
                            if self.resp[4] == 'x':
                                self.b_x.style.background_color = 'Gray'
                            if self.resp[4] == 'c':
                                self.b_c.style.background_color = 'Gray'
                            if self.resp[4] == 'v':
                                self.b_v.style.background_color = 'Gray'
                            if self.resp[4] == 'b':
                                self.b_b.style.background_color = 'Gray'
                            if self.resp[4] == 'n':
                                self.b_n.style.background_color = 'Gray'
                            if self.resp[4] == 'm':
                                self.b_m.style.background_color = 'Gray'
                    self.contador = '2'
                else:
                    self.output6.text = '' + termo_play_Acento[0].upper()
                    self.letra_t1.style.background_color = 'Springgreen'
                    self.output7.text = '' + termo_play_Acento[1].upper()
                    self.letra_e1.style.background_color = 'Springgreen'
                    self.output8.text = '' + termo_play_Acento[2].upper()
                    self.letra_r1.style.background_color = 'Springgreen'
                    self.output9.text = '' + termo_play_Acento[3].upper()
                    self.letra_m1.style.background_color = 'Springgreen'
                    self.output10.text = '' + termo_play_Acento[4].upper()
                    self.letra_o1.style.background_color = 'Springgreen'
                    self.main_window.info_dialog('Você Ganhou!', f'{termo_play_Acento.upper()} era a palavra correta 🤩', )
                self.resposta = ''
                return 0
            else:
                if (self.contador == '1'):
                    self.main_window.info_dialog('Palavra inexistente!', 'A palavra digitada não é aceita 😒')
                    return 0

            if ((self.contador == '2') and (self.resposta in palavras_5char_existentes)):
                if (self.resposta != termo_play):
                    if self.resp[0] == termo_play[0]:
                        self.output11.text = '' + termo_play_Acento[0].upper()
                        self.letra_t2.style.background_color = 'Springgreen'
                        if self.resp[0] == 'q':
                            self.b_q.style.background_color = 'Springgreen'
                        if self.resp[0] == 'w':
                            self.b_w.style.background_color = 'Springgreen'
                        if self.resp[0] == 'e':
                            self.b_e.style.background_color = 'Springgreen'
                        if self.resp[0] == 'r':
                            self.b_r.style.background_color = 'Springgreen'
                        if self.resp[0] == 't':
                            self.b_t.style.background_color = 'Springgreen'
                        if self.resp[0] == 'y':
                            self.b_y.style.background_color = 'Springgreen'
                        if self.resp[0] == 'u':
                            self.b_u.style.background_color = 'Springgreen'
                        if self.resp[0] == 'i':
                            self.b_i.style.background_color = 'Springgreen'
                        if self.resp[0] == 'o':
                            self.b_o.style.background_color = 'Springgreen'
                        if self.resp[0] == 'p':
                            self.b_p.style.background_color = 'Springgreen'
                        if self.resp[0] == 'a':
                            self.b_a.style.background_color = 'Springgreen'
                        if self.resp[0] == 's':
                            self.b_s.style.background_color = 'Springgreen'
                        if self.resp[0] == 'd':
                            self.b_d.style.background_color = 'Springgreen'
                        if self.resp[0] == 'f':
                            self.b_f.style.background_color = 'Springgreen'
                        if self.resp[0] == 'g':
                            self.b_g.style.background_color = 'Springgreen'
                        if self.resp[0] == 'h':
                            self.b_h.style.background_color = 'Springgreen'
                        if self.resp[0] == 'j':
                            self.b_j.style.background_color = 'Springgreen'
                        if self.resp[0] == 'k':
                            self.b_k.style.background_color = 'Springgreen'
                        if self.resp[0] == 'l':
                            self.b_l.style.background_color = 'Springgreen'
                        if self.resp[0] == 'ç':
                            self.b_cdl.style.background_color = 'Springgreen'
                        if self.resp[0] == 'z':
                            self.b_z.style.background_color = 'Springgreen'
                        if self.resp[0] == 'x':
                            self.b_x.style.background_color = 'Springgreen'
                        if self.resp[0] == 'c':
                            self.b_c.style.background_color = 'Springgreen'
                        if self.resp[0] == 'v':
                            self.b_v.style.background_color = 'Springgreen'
                        if self.resp[0] == 'b':
                            self.b_b.style.background_color = 'Springgreen'
                        if self.resp[0] == 'n':
                            self.b_n.style.background_color = 'Springgreen'
                        if self.resp[0] == 'm':
                            self.b_m.style.background_color = 'Springgreen'
                    else:
                        if self.resp[0] in termo_play:
                            self.letra_t2.style.background_color = 'Gold'
                            if ((self.resp[0] == 'q') and (self.b_q.style.background_color != 'Springgreen')):
                                self.b_q.style.background_color = 'Gold'
                            if ((self.resp[0] == 'w') and (self.b_w.style.background_color != 'Springgreen')):
                                self.b_w.style.background_color = 'Gold'
                            if ((self.resp[0] == 'e') and (self.b_e.style.background_color != 'Springgreen')):
                                self.b_e.style.background_color = 'Gold'
                            if ((self.resp[0] == 'r') and (self.b_r.style.background_color != 'Springgreen')):
                                self.b_r.style.background_color = 'Gold'
                            if ((self.resp[0] == 't') and (self.b_t.style.background_color != 'Springgreen')):
                                self.b_t.style.background_color = 'Gold'
                            if ((self.resp[0] == 'y') and (self.b_y.style.background_color != 'Springgreen')):
                                self.b_y.style.background_color = 'Gold'
                            if ((self.resp[0] == 'u') and (self.b_u.style.background_color != 'Springgreen')):
                                self.b_u.style.background_color = 'Gold'
                            if ((self.resp[0] == 'i') and (self.b_i.style.background_color != 'Springgreen')):
                                self.b_i.style.background_color = 'Gold'
                            if ((self.resp[0] == 'o') and (self.b_o.style.background_color != 'Springgreen')):
                                self.b_o.style.background_color = 'Gold'
                            if ((self.resp[0] == 'p') and (self.b_p.style.background_color != 'Springgreen')):
                                self.b_p.style.background_color = 'Gold'
                            if ((self.resp[0] == 'a') and (self.b_a.style.background_color != 'Springgreen')):
                                self.b_a.style.background_color = 'Gold'
                            if ((self.resp[0] == 's') and (self.b_s.style.background_color != 'Springgreen')):
                                self.b_s.style.background_color = 'Gold'
                            if ((self.resp[0] == 'd') and (self.b_d.style.background_color != 'Springgreen')):
                                self.b_d.style.background_color = 'Gold'
                            if ((self.resp[0] == 'f') and (self.b_f.style.background_color != 'Springgreen')):
                                self.b_f.style.background_color = 'Gold'
                            if ((self.resp[0] == 'g') and (self.b_g.style.background_color != 'Springgreen')):
                                self.b_g.style.background_color = 'Gold'
                            if ((self.resp[0] == 'h') and (self.b_h.style.background_color != 'Springgreen')):
                                self.b_h.style.background_color = 'Gold'
                            if ((self.resp[0] == 'j') and (self.b_j.style.background_color != 'Springgreen')):
                                self.b_j.style.background_color = 'Gold'
                            if ((self.resp[0] == 'k') and (self.b_k.style.background_color != 'Springgreen')):
                                self.b_k.style.background_color = 'Gold'
                            if ((self.resp[0] == 'l') and (self.b_l.style.background_color != 'Springgreen')):
                                self.b_l.style.background_color = 'Gold'
                            if ((self.resp[0] == 'ç') and (self.b_cdl.style.background_color != 'Springgreen')):
                                self.b_cdl.style.background_color = 'Gold'
                            if ((self.resp[0] == 'z') and (self.b_z.style.background_color != 'Springgreen')):
                                self.b_z.style.background_color = 'Gold'
                            if ((self.resp[0] == 'x') and (self.b_x.style.background_color != 'Springgreen')):
                                self.b_x.style.background_color = 'Gold'
                            if ((self.resp[0] == 'c') and (self.b_c.style.background_color != 'Springgreen')):
                                self.b_c.style.background_color = 'Gold'
                            if ((self.resp[0] == 'v') and (self.b_v.style.background_color != 'Springgreen')):
                                self.b_v.style.background_color = 'Gold'
                            if ((self.resp[0] == 'b') and (self.b_b.style.background_color != 'Springgreen')):
                                self.b_b.style.background_color = 'Gold'
                            if ((self.resp[0] == 'n') and (self.b_n.style.background_color != 'Springgreen')):
                                self.b_n.style.background_color = 'Gold'
                            if ((self.resp[0] == 'm') and (self.b_m.style.background_color != 'Springgreen')):
                                self.b_m.style.background_color = 'Gold'
                        else:
                            if self.resp[0] == 'q':
                                self.b_q.style.background_color = 'Gray'
                            if self.resp[0] == 'w':
                                self.b_w.style.background_color = 'Gray'
                            if self.resp[0] == 'e':
                                self.b_e.style.background_color = 'Gray'
                            if self.resp[0] == 'r':
                                self.b_r.style.background_color = 'Gray'
                            if self.resp[0] == 't':
                                self.b_t.style.background_color = 'Gray'
                            if self.resp[0] == 'y':
                                self.b_y.style.background_color = 'Gray'
                            if self.resp[0] == 'u':
                                self.b_u.style.background_color = 'Gray'
                            if self.resp[0] == 'i':
                                self.b_i.style.background_color = 'Gray'
                            if self.resp[0] == 'o':
                                self.b_o.style.background_color = 'Gray'
                            if self.resp[0] == 'p':
                                self.b_p.style.background_color = 'Gray'
                            if self.resp[0] == 'a':
                                self.b_a.style.background_color = 'Gray'
                            if self.resp[0] == 's':
                                self.b_s.style.background_color = 'Gray'
                            if self.resp[0] == 'd':
                                self.b_d.style.background_color = 'Gray'
                            if self.resp[0] == 'f':
                                self.b_f.style.background_color = 'Gray'
                            if self.resp[0] == 'g':
                                self.b_g.style.background_color = 'Gray'
                            if self.resp[0] == 'h':
                                self.b_h.style.background_color = 'Gray'
                            if self.resp[0] == 'j':
                                self.b_j.style.background_color = 'Gray'
                            if self.resp[0] == 'k':
                                self.b_k.style.background_color = 'Gray'
                            if self.resp[0] == 'l':
                                self.b_l.style.background_color = 'Gray'
                            if self.resp[0] == 'ç':
                                self.b_cdl.style.background_color = 'Gray'
                            if self.resp[0] == 'z':
                                self.b_z.style.background_color = 'Gray'
                            if self.resp[0] == 'x':
                                self.b_x.style.background_color = 'Gray'
                            if self.resp[0] == 'c':
                                self.b_c.style.background_color = 'Gray'
                            if self.resp[0] == 'v':
                                self.b_v.style.background_color = 'Gray'
                            if self.resp[0] == 'b':
                                self.b_b.style.background_color = 'Gray'
                            if self.resp[0] == 'n':
                                self.b_n.style.background_color = 'Gray'
                            if self.resp[0] == 'm':
                                self.b_m.style.background_color = 'Gray'

                    if self.resp[1] == termo_play[1]:
                        self.output12.text = '' + termo_play_Acento[1].upper()
                        self.letra_e2.style.background_color = 'Springgreen'
                        if self.resp[1] == 'q':
                            self.b_q.style.background_color = 'Springgreen'
                        if self.resp[1] == 'w':
                            self.b_w.style.background_color = 'Springgreen'
                        if self.resp[1] == 'e':
                            self.b_e.style.background_color = 'Springgreen'
                        if self.resp[1] == 'r':
                            self.b_r.style.background_color = 'Springgreen'
                        if self.resp[1] == 't':
                            self.b_t.style.background_color = 'Springgreen'
                        if self.resp[1] == 'y':
                            self.b_y.style.background_color = 'Springgreen'
                        if self.resp[1] == 'u':
                            self.b_u.style.background_color = 'Springgreen'
                        if self.resp[1] == 'i':
                            self.b_i.style.background_color = 'Springgreen'
                        if self.resp[1] == 'o':
                            self.b_o.style.background_color = 'Springgreen'
                        if self.resp[1] == 'p':
                            self.b_p.style.background_color = 'Springgreen'
                        if self.resp[1] == 'a':
                            self.b_a.style.background_color = 'Springgreen'
                        if self.resp[1] == 's':
                            self.b_s.style.background_color = 'Springgreen'
                        if self.resp[1] == 'd':
                            self.b_d.style.background_color = 'Springgreen'
                        if self.resp[1] == 'f':
                            self.b_f.style.background_color = 'Springgreen'
                        if self.resp[1] == 'g':
                            self.b_g.style.background_color = 'Springgreen'
                        if self.resp[1] == 'h':
                            self.b_h.style.background_color = 'Springgreen'
                        if self.resp[1] == 'j':
                            self.b_j.style.background_color = 'Springgreen'
                        if self.resp[1] == 'k':
                            self.b_k.style.background_color = 'Springgreen'
                        if self.resp[1] == 'l':
                            self.b_l.style.background_color = 'Springgreen'
                        if self.resp[1] == 'ç':
                            self.b_cdl.style.background_color = 'Springgreen'
                        if self.resp[1] == 'z':
                            self.b_z.style.background_color = 'Springgreen'
                        if self.resp[1] == 'x':
                            self.b_x.style.background_color = 'Springgreen'
                        if self.resp[1] == 'c':
                            self.b_c.style.background_color = 'Springgreen'
                        if self.resp[1] == 'v':
                            self.b_v.style.background_color = 'Springgreen'
                        if self.resp[1] == 'b':
                            self.b_b.style.background_color = 'Springgreen'
                        if self.resp[1] == 'n':
                            self.b_n.style.background_color = 'Springgreen'
                        if self.resp[1] == 'm':
                            self.b_m.style.background_color = 'Springgreen'
                    else:
                        if self.resp[1] in termo_play:
                            self.letra_e2.style.background_color = 'Gold'
                            if ((self.resp[1] == 'q') and (self.b_q.style.background_color != 'Springgreen')):
                                self.b_q.style.background_color = 'Gold'
                            if ((self.resp[1] == 'w') and (self.b_w.style.background_color != 'Springgreen')):
                                self.b_w.style.background_color = 'Gold'
                            if ((self.resp[1] == 'e') and (self.b_e.style.background_color != 'Springgreen')):
                                self.b_e.style.background_color = 'Gold'
                            if ((self.resp[1] == 'r') and (self.b_r.style.background_color != 'Springgreen')):
                                self.b_r.style.background_color = 'Gold'
                            if ((self.resp[1] == 't') and (self.b_t.style.background_color != 'Springgreen')):
                                self.b_t.style.background_color = 'Gold'
                            if ((self.resp[1] == 'y') and (self.b_y.style.background_color != 'Springgreen')):
                                self.b_y.style.background_color = 'Gold'
                            if ((self.resp[1] == 'u') and (self.b_u.style.background_color != 'Springgreen')):
                                self.b_u.style.background_color = 'Gold'
                            if ((self.resp[1] == 'i') and (self.b_i.style.background_color != 'Springgreen')):
                                self.b_i.style.background_color = 'Gold'
                            if ((self.resp[1] == 'o') and (self.b_o.style.background_color != 'Springgreen')):
                                self.b_o.style.background_color = 'Gold'
                            if ((self.resp[1] == 'p') and (self.b_p.style.background_color != 'Springgreen')):
                                self.b_p.style.background_color = 'Gold'
                            if ((self.resp[1] == 'a') and (self.b_a.style.background_color != 'Springgreen')):
                                self.b_a.style.background_color = 'Gold'
                            if ((self.resp[1] == 's') and (self.b_s.style.background_color != 'Springgreen')):
                                self.b_s.style.background_color = 'Gold'
                            if ((self.resp[1] == 'd') and (self.b_d.style.background_color != 'Springgreen')):
                                self.b_d.style.background_color = 'Gold'
                            if ((self.resp[1] == 'f') and (self.b_f.style.background_color != 'Springgreen')):
                                self.b_f.style.background_color = 'Gold'
                            if ((self.resp[1] == 'g') and (self.b_g.style.background_color != 'Springgreen')):
                                self.b_g.style.background_color = 'Gold'
                            if ((self.resp[1] == 'h') and (self.b_h.style.background_color != 'Springgreen')):
                                self.b_h.style.background_color = 'Gold'
                            if ((self.resp[1] == 'j') and (self.b_j.style.background_color != 'Springgreen')):
                                self.b_j.style.background_color = 'Gold'
                            if ((self.resp[1] == 'k') and (self.b_k.style.background_color != 'Springgreen')):
                                self.b_k.style.background_color = 'Gold'
                            if ((self.resp[1] == 'l') and (self.b_l.style.background_color != 'Springgreen')):
                                self.b_l.style.background_color = 'Gold'
                            if ((self.resp[1] == 'ç') and (self.b_cdl.style.background_color != 'Springgreen')):
                                self.b_cdl.style.background_color = 'Gold'
                            if ((self.resp[1] == 'z') and (self.b_z.style.background_color != 'Springgreen')):
                                self.b_z.style.background_color = 'Gold'
                            if ((self.resp[1] == 'x') and (self.b_x.style.background_color != 'Springgreen')):
                                self.b_x.style.background_color = 'Gold'
                            if ((self.resp[1] == 'c') and (self.b_c.style.background_color != 'Springgreen')):
                                self.b_c.style.background_color = 'Gold'
                            if ((self.resp[1] == 'v') and (self.b_v.style.background_color != 'Springgreen')):
                                self.b_v.style.background_color = 'Gold'
                            if ((self.resp[1] == 'b') and (self.b_b.style.background_color != 'Springgreen')):
                                self.b_b.style.background_color = 'Gold'
                            if ((self.resp[1] == 'n') and (self.b_n.style.background_color != 'Springgreen')):
                                self.b_n.style.background_color = 'Gold'
                            if ((self.resp[1] == 'm') and (self.b_m.style.background_color != 'Springgreen')):
                                self.b_m.style.background_color = 'Gold'
                        else:
                            if self.resp[1] == 'q':
                                self.b_q.style.background_color = 'Gray'
                            if self.resp[1] == 'w':
                                self.b_w.style.background_color = 'Gray'
                            if self.resp[1] == 'e':
                                self.b_e.style.background_color = 'Gray'
                            if self.resp[1] == 'r':
                                self.b_r.style.background_color = 'Gray'
                            if self.resp[1] == 't':
                                self.b_t.style.background_color = 'Gray'
                            if self.resp[1] == 'y':
                                self.b_y.style.background_color = 'Gray'
                            if self.resp[1] == 'u':
                                self.b_u.style.background_color = 'Gray'
                            if self.resp[1] == 'i':
                                self.b_i.style.background_color = 'Gray'
                            if self.resp[1] == 'o':
                                self.b_o.style.background_color = 'Gray'
                            if self.resp[1] == 'p':
                                self.b_p.style.background_color = 'Gray'
                            if self.resp[1] == 'a':
                                self.b_a.style.background_color = 'Gray'
                            if self.resp[1] == 's':
                                self.b_s.style.background_color = 'Gray'
                            if self.resp[1] == 'd':
                                self.b_d.style.background_color = 'Gray'
                            if self.resp[1] == 'f':
                                self.b_f.style.background_color = 'Gray'
                            if self.resp[1] == 'g':
                                self.b_g.style.background_color = 'Gray'
                            if self.resp[1] == 'h':
                                self.b_h.style.background_color = 'Gray'
                            if self.resp[1] == 'j':
                                self.b_j.style.background_color = 'Gray'
                            if self.resp[1] == 'k':
                                self.b_k.style.background_color = 'Gray'
                            if self.resp[1] == 'l':
                                self.b_l.style.background_color = 'Gray'
                            if self.resp[1] == 'ç':
                                self.b_cdl.style.background_color = 'Gray'
                            if self.resp[1] == 'z':
                                self.b_z.style.background_color = 'Gray'
                            if self.resp[1] == 'x':
                                self.b_x.style.background_color = 'Gray'
                            if self.resp[1] == 'c':
                                self.b_c.style.background_color = 'Gray'
                            if self.resp[1] == 'v':
                                self.b_v.style.background_color = 'Gray'
                            if self.resp[1] == 'b':
                                self.b_b.style.background_color = 'Gray'
                            if self.resp[1] == 'n':
                                self.b_n.style.background_color = 'Gray'
                            if self.resp[1] == 'm':
                                self.b_m.style.background_color = 'Gray'

                    if self.resp[2] == termo_play[2]:
                        self.output13.text = '' + termo_play_Acento[2].upper()
                        self.letra_r2.style.background_color = 'Springgreen'
                        if self.resp[2] == 'q':
                            self.b_q.style.background_color = 'Springgreen'
                        if self.resp[2] == 'w':
                            self.b_w.style.background_color = 'Springgreen'
                        if self.resp[2] == 'e':
                            self.b_e.style.background_color = 'Springgreen'
                        if self.resp[2] == 'r':
                            self.b_r.style.background_color = 'Springgreen'
                        if self.resp[2] == 't':
                            self.b_t.style.background_color = 'Springgreen'
                        if self.resp[2] == 'y':
                            self.b_y.style.background_color = 'Springgreen'
                        if self.resp[2] == 'u':
                            self.b_u.style.background_color = 'Springgreen'
                        if self.resp[2] == 'i':
                            self.b_i.style.background_color = 'Springgreen'
                        if self.resp[2] == 'o':
                            self.b_o.style.background_color = 'Springgreen'
                        if self.resp[2] == 'p':
                            self.b_p.style.background_color = 'Springgreen'
                        if self.resp[2] == 'a':
                            self.b_a.style.background_color = 'Springgreen'
                        if self.resp[2] == 's':
                            self.b_s.style.background_color = 'Springgreen'
                        if self.resp[2] == 'd':
                            self.b_d.style.background_color = 'Springgreen'
                        if self.resp[2] == 'f':
                            self.b_f.style.background_color = 'Springgreen'
                        if self.resp[2] == 'g':
                            self.b_g.style.background_color = 'Springgreen'
                        if self.resp[2] == 'h':
                            self.b_h.style.background_color = 'Springgreen'
                        if self.resp[2] == 'j':
                            self.b_j.style.background_color = 'Springgreen'
                        if self.resp[2] == 'k':
                            self.b_k.style.background_color = 'Springgreen'
                        if self.resp[2] == 'l':
                            self.b_l.style.background_color = 'Springgreen'
                        if self.resp[2] == 'ç':
                            self.b_cdl.style.background_color = 'Springgreen'
                        if self.resp[2] == 'z':
                            self.b_z.style.background_color = 'Springgreen'
                        if self.resp[2] == 'x':
                            self.b_x.style.background_color = 'Springgreen'
                        if self.resp[2] == 'c':
                            self.b_c.style.background_color = 'Springgreen'
                        if self.resp[2] == 'v':
                            self.b_v.style.background_color = 'Springgreen'
                        if self.resp[2] == 'b':
                            self.b_b.style.background_color = 'Springgreen'
                        if self.resp[2] == 'n':
                            self.b_n.style.background_color = 'Springgreen'
                        if self.resp[2] == 'm':
                            self.b_m.style.background_color = 'Springgreen'
                    else:
                        if self.resp[2] in termo_play:
                            self.letra_r2.style.background_color = 'Gold'
                            if ((self.resp[2] == 'q') and (self.b_q.style.background_color != 'Springgreen')):
                                self.b_q.style.background_color = 'Gold'
                            if ((self.resp[2] == 'w') and (self.b_w.style.background_color != 'Springgreen')):
                                self.b_w.style.background_color = 'Gold'
                            if ((self.resp[2] == 'e') and (self.b_e.style.background_color != 'Springgreen')):
                                self.b_e.style.background_color = 'Gold'
                            if ((self.resp[2] == 'r') and (self.b_r.style.background_color != 'Springgreen')):
                                self.b_r.style.background_color = 'Gold'
                            if ((self.resp[2] == 't') and (self.b_t.style.background_color != 'Springgreen')):
                                self.b_t.style.background_color = 'Gold'
                            if ((self.resp[2] == 'y') and (self.b_y.style.background_color != 'Springgreen')):
                                self.b_y.style.background_color = 'Gold'
                            if ((self.resp[2] == 'u') and (self.b_u.style.background_color != 'Springgreen')):
                                self.b_u.style.background_color = 'Gold'
                            if ((self.resp[2] == 'i') and (self.b_i.style.background_color != 'Springgreen')):
                                self.b_i.style.background_color = 'Gold'
                            if ((self.resp[2] == 'o') and (self.b_o.style.background_color != 'Springgreen')):
                                self.b_o.style.background_color = 'Gold'
                            if ((self.resp[2] == 'p') and (self.b_p.style.background_color != 'Springgreen')):
                                self.b_p.style.background_color = 'Gold'
                            if ((self.resp[2] == 'a') and (self.b_a.style.background_color != 'Springgreen')):
                                self.b_a.style.background_color = 'Gold'
                            if ((self.resp[2] == 's') and (self.b_s.style.background_color != 'Springgreen')):
                                self.b_s.style.background_color = 'Gold'
                            if ((self.resp[2] == 'd') and (self.b_d.style.background_color != 'Springgreen')):
                                self.b_d.style.background_color = 'Gold'
                            if ((self.resp[2] == 'f') and (self.b_f.style.background_color != 'Springgreen')):
                                self.b_f.style.background_color = 'Gold'
                            if ((self.resp[2] == 'g') and (self.b_g.style.background_color != 'Springgreen')):
                                self.b_g.style.background_color = 'Gold'
                            if ((self.resp[2] == 'h') and (self.b_h.style.background_color != 'Springgreen')):
                                self.b_h.style.background_color = 'Gold'
                            if ((self.resp[2] == 'j') and (self.b_j.style.background_color != 'Springgreen')):
                                self.b_j.style.background_color = 'Gold'
                            if ((self.resp[2] == 'k') and (self.b_k.style.background_color != 'Springgreen')):
                                self.b_k.style.background_color = 'Gold'
                            if ((self.resp[2] == 'l') and (self.b_l.style.background_color != 'Springgreen')):
                                self.b_l.style.background_color = 'Gold'
                            if ((self.resp[2] == 'ç') and (self.b_cdl.style.background_color != 'Springgreen')):
                                self.b_cdl.style.background_color = 'Gold'
                            if ((self.resp[2] == 'z') and (self.b_z.style.background_color != 'Springgreen')):
                                self.b_z.style.background_color = 'Gold'
                            if ((self.resp[2] == 'x') and (self.b_x.style.background_color != 'Springgreen')):
                                self.b_x.style.background_color = 'Gold'
                            if ((self.resp[2] == 'c') and (self.b_c.style.background_color != 'Springgreen')):
                                self.b_c.style.background_color = 'Gold'
                            if ((self.resp[2] == 'v') and (self.b_v.style.background_color != 'Springgreen')):
                                self.b_v.style.background_color = 'Gold'
                            if ((self.resp[2] == 'b') and (self.b_b.style.background_color != 'Springgreen')):
                                self.b_b.style.background_color = 'Gold'
                            if ((self.resp[2] == 'n') and (self.b_n.style.background_color != 'Springgreen')):
                                self.b_n.style.background_color = 'Gold'
                            if ((self.resp[2] == 'm') and (self.b_m.style.background_color != 'Springgreen')):
                                self.b_m.style.background_color = 'Gold'
                        else:
                            if self.resp[2] == 'q':
                                self.b_q.style.background_color = 'Gray'
                            if self.resp[2] == 'w':
                                self.b_w.style.background_color = 'Gray'
                            if self.resp[2] == 'e':
                                self.b_e.style.background_color = 'Gray'
                            if self.resp[2] == 'r':
                                self.b_r.style.background_color = 'Gray'
                            if self.resp[2] == 't':
                                self.b_t.style.background_color = 'Gray'
                            if self.resp[2] == 'y':
                                self.b_y.style.background_color = 'Gray'
                            if self.resp[2] == 'u':
                                self.b_u.style.background_color = 'Gray'
                            if self.resp[2] == 'i':
                                self.b_i.style.background_color = 'Gray'
                            if self.resp[2] == 'o':
                                self.b_o.style.background_color = 'Gray'
                            if self.resp[2] == 'p':
                                self.b_p.style.background_color = 'Gray'
                            if self.resp[2] == 'a':
                                self.b_a.style.background_color = 'Gray'
                            if self.resp[2] == 's':
                                self.b_s.style.background_color = 'Gray'
                            if self.resp[2] == 'd':
                                self.b_d.style.background_color = 'Gray'
                            if self.resp[2] == 'f':
                                self.b_f.style.background_color = 'Gray'
                            if self.resp[2] == 'g':
                                self.b_g.style.background_color = 'Gray'
                            if self.resp[2] == 'h':
                                self.b_h.style.background_color = 'Gray'
                            if self.resp[2] == 'j':
                                self.b_j.style.background_color = 'Gray'
                            if self.resp[2] == 'k':
                                self.b_k.style.background_color = 'Gray'
                            if self.resp[2] == 'l':
                                self.b_l.style.background_color = 'Gray'
                            if self.resp[2] == 'ç':
                                self.b_cdl.style.background_color = 'Gray'
                            if self.resp[2] == 'z':
                                self.b_z.style.background_color = 'Gray'
                            if self.resp[2] == 'x':
                                self.b_x.style.background_color = 'Gray'
                            if self.resp[2] == 'c':
                                self.b_c.style.background_color = 'Gray'
                            if self.resp[2] == 'v':
                                self.b_v.style.background_color = 'Gray'
                            if self.resp[2] == 'b':
                                self.b_b.style.background_color = 'Gray'
                            if self.resp[2] == 'n':
                                self.b_n.style.background_color = 'Gray'
                            if self.resp[2] == 'm':
                                self.b_m.style.background_color = 'Gray'

                    if self.resp[3] == termo_play[3]:
                        self.output14.text = '' + termo_play_Acento[3].upper()
                        self.letra_m2.style.background_color = 'Springgreen'
                        if self.resp[3] == 'q':
                            self.b_q.style.background_color = 'Springgreen'
                        if self.resp[3] == 'w':
                            self.b_w.style.background_color = 'Springgreen'
                        if self.resp[3] == 'e':
                            self.b_e.style.background_color = 'Springgreen'
                        if self.resp[3] == 'r':
                            self.b_r.style.background_color = 'Springgreen'
                        if self.resp[3] == 't':
                            self.b_t.style.background_color = 'Springgreen'
                        if self.resp[3] == 'y':
                            self.b_y.style.background_color = 'Springgreen'
                        if self.resp[3] == 'u':
                            self.b_u.style.background_color = 'Springgreen'
                        if self.resp[3] == 'i':
                            self.b_i.style.background_color = 'Springgreen'
                        if self.resp[3] == 'o':
                            self.b_o.style.background_color = 'Springgreen'
                        if self.resp[3] == 'p':
                            self.b_p.style.background_color = 'Springgreen'
                        if self.resp[3] == 'a':
                            self.b_a.style.background_color = 'Springgreen'
                        if self.resp[3] == 's':
                            self.b_s.style.background_color = 'Springgreen'
                        if self.resp[3] == 'd':
                            self.b_d.style.background_color = 'Springgreen'
                        if self.resp[3] == 'f':
                            self.b_f.style.background_color = 'Springgreen'
                        if self.resp[3] == 'g':
                            self.b_g.style.background_color = 'Springgreen'
                        if self.resp[3] == 'h':
                            self.b_h.style.background_color = 'Springgreen'
                        if self.resp[3] == 'j':
                            self.b_j.style.background_color = 'Springgreen'
                        if self.resp[3] == 'k':
                            self.b_k.style.background_color = 'Springgreen'
                        if self.resp[3] == 'l':
                            self.b_l.style.background_color = 'Springgreen'
                        if self.resp[3] == 'ç':
                            self.b_cdl.style.background_color = 'Springgreen'
                        if self.resp[3] == 'z':
                            self.b_z.style.background_color = 'Springgreen'
                        if self.resp[3] == 'x':
                            self.b_x.style.background_color = 'Springgreen'
                        if self.resp[3] == 'c':
                            self.b_c.style.background_color = 'Springgreen'
                        if self.resp[3] == 'v':
                            self.b_v.style.background_color = 'Springgreen'
                        if self.resp[3] == 'b':
                            self.b_b.style.background_color = 'Springgreen'
                        if self.resp[3] == 'n':
                            self.b_n.style.background_color = 'Springgreen'
                        if self.resp[3] == 'm':
                            self.b_m.style.background_color = 'Springgreen'
                    else:
                        if self.resp[3] in termo_play:
                            self.letra_m2.style.background_color = 'Gold'
                            if ((self.resp[3] == 'q') and (self.b_q.style.background_color != 'Springgreen')):
                                self.b_q.style.background_color = 'Gold'
                            if ((self.resp[3] == 'w') and (self.b_w.style.background_color != 'Springgreen')):
                                self.b_w.style.background_color = 'Gold'
                            if ((self.resp[3] == 'e') and (self.b_e.style.background_color != 'Springgreen')):
                                self.b_e.style.background_color = 'Gold'
                            if ((self.resp[3] == 'r') and (self.b_r.style.background_color != 'Springgreen')):
                                self.b_r.style.background_color = 'Gold'
                            if ((self.resp[3] == 't') and (self.b_t.style.background_color != 'Springgreen')):
                                self.b_t.style.background_color = 'Gold'
                            if ((self.resp[3] == 'y') and (self.b_y.style.background_color != 'Springgreen')):
                                self.b_y.style.background_color = 'Gold'
                            if ((self.resp[3] == 'u') and (self.b_u.style.background_color != 'Springgreen')):
                                self.b_u.style.background_color = 'Gold'
                            if ((self.resp[3] == 'i') and (self.b_i.style.background_color != 'Springgreen')):
                                self.b_i.style.background_color = 'Gold'
                            if ((self.resp[3] == 'o') and (self.b_o.style.background_color != 'Springgreen')):
                                self.b_o.style.background_color = 'Gold'
                            if ((self.resp[3] == 'p') and (self.b_p.style.background_color != 'Springgreen')):
                                self.b_p.style.background_color = 'Gold'
                            if ((self.resp[3] == 'a') and (self.b_a.style.background_color != 'Springgreen')):
                                self.b_a.style.background_color = 'Gold'
                            if ((self.resp[3] == 's') and (self.b_s.style.background_color != 'Springgreen')):
                                self.b_s.style.background_color = 'Gold'
                            if ((self.resp[3] == 'd') and (self.b_d.style.background_color != 'Springgreen')):
                                self.b_d.style.background_color = 'Gold'
                            if ((self.resp[3] == 'f') and (self.b_f.style.background_color != 'Springgreen')):
                                self.b_f.style.background_color = 'Gold'
                            if ((self.resp[3] == 'g') and (self.b_g.style.background_color != 'Springgreen')):
                                self.b_g.style.background_color = 'Gold'
                            if ((self.resp[3] == 'h') and (self.b_h.style.background_color != 'Springgreen')):
                                self.b_h.style.background_color = 'Gold'
                            if ((self.resp[3] == 'j') and (self.b_j.style.background_color != 'Springgreen')):
                                self.b_j.style.background_color = 'Gold'
                            if ((self.resp[3] == 'k') and (self.b_k.style.background_color != 'Springgreen')):
                                self.b_k.style.background_color = 'Gold'
                            if ((self.resp[3] == 'l') and (self.b_l.style.background_color != 'Springgreen')):
                                self.b_l.style.background_color = 'Gold'
                            if ((self.resp[3] == 'ç') and (self.b_cdl.style.background_color != 'Springgreen')):
                                self.b_cdl.style.background_color = 'Gold'
                            if ((self.resp[3] == 'z') and (self.b_z.style.background_color != 'Springgreen')):
                                self.b_z.style.background_color = 'Gold'
                            if ((self.resp[3] == 'x') and (self.b_x.style.background_color != 'Springgreen')):
                                self.b_x.style.background_color = 'Gold'
                            if ((self.resp[3] == 'c') and (self.b_c.style.background_color != 'Springgreen')):
                                self.b_c.style.background_color = 'Gold'
                            if ((self.resp[3] == 'v') and (self.b_v.style.background_color != 'Springgreen')):
                                self.b_v.style.background_color = 'Gold'
                            if ((self.resp[3] == 'b') and (self.b_b.style.background_color != 'Springgreen')):
                                self.b_b.style.background_color = 'Gold'
                            if ((self.resp[3] == 'n') and (self.b_n.style.background_color != 'Springgreen')):
                                self.b_n.style.background_color = 'Gold'
                            if ((self.resp[3] == 'm') and (self.b_m.style.background_color != 'Springgreen')):
                                self.b_m.style.background_color = 'Gold'
                        else:
                            if self.resp[3] == 'q':
                                self.b_q.style.background_color = 'Gray'
                            if self.resp[3] == 'w':
                                self.b_w.style.background_color = 'Gray'
                            if self.resp[3] == 'e':
                                self.b_e.style.background_color = 'Gray'
                            if self.resp[3] == 'r':
                                self.b_r.style.background_color = 'Gray'
                            if self.resp[3] == 't':
                                self.b_t.style.background_color = 'Gray'
                            if self.resp[3] == 'y':
                                self.b_y.style.background_color = 'Gray'
                            if self.resp[3] == 'u':
                                self.b_u.style.background_color = 'Gray'
                            if self.resp[3] == 'i':
                                self.b_i.style.background_color = 'Gray'
                            if self.resp[3] == 'o':
                                self.b_o.style.background_color = 'Gray'
                            if self.resp[3] == 'p':
                                self.b_p.style.background_color = 'Gray'
                            if self.resp[3] == 'a':
                                self.b_a.style.background_color = 'Gray'
                            if self.resp[3] == 's':
                                self.b_s.style.background_color = 'Gray'
                            if self.resp[3] == 'd':
                                self.b_d.style.background_color = 'Gray'
                            if self.resp[3] == 'f':
                                self.b_f.style.background_color = 'Gray'
                            if self.resp[3] == 'g':
                                self.b_g.style.background_color = 'Gray'
                            if self.resp[3] == 'h':
                                self.b_h.style.background_color = 'Gray'
                            if self.resp[3] == 'j':
                                self.b_j.style.background_color = 'Gray'
                            if self.resp[3] == 'k':
                                self.b_k.style.background_color = 'Gray'
                            if self.resp[3] == 'l':
                                self.b_l.style.background_color = 'Gray'
                            if self.resp[3] == 'ç':
                                self.b_cdl.style.background_color = 'Gray'
                            if self.resp[3] == 'z':
                                self.b_z.style.background_color = 'Gray'
                            if self.resp[3] == 'x':
                                self.b_x.style.background_color = 'Gray'
                            if self.resp[3] == 'c':
                                self.b_c.style.background_color = 'Gray'
                            if self.resp[3] == 'v':
                                self.b_v.style.background_color = 'Gray'
                            if self.resp[3] == 'b':
                                self.b_b.style.background_color = 'Gray'
                            if self.resp[3] == 'n':
                                self.b_n.style.background_color = 'Gray'
                            if self.resp[3] == 'm':
                                self.b_m.style.background_color = 'Gray'

                    if self.resp[4] == termo_play[4]:
                        self.output15.text = '' + termo_play_Acento[4].upper()
                        self.letra_o2.style.background_color = 'Springgreen'
                        if self.resp[4] == 'q':
                            self.b_q.style.background_color = 'Springgreen'
                        if self.resp[4] == 'w':
                            self.b_w.style.background_color = 'Springgreen'
                        if self.resp[4] == 'e':
                            self.b_e.style.background_color = 'Springgreen'
                        if self.resp[4] == 'r':
                            self.b_r.style.background_color = 'Springgreen'
                        if self.resp[4] == 't':
                            self.b_t.style.background_color = 'Springgreen'
                        if self.resp[4] == 'y':
                            self.b_y.style.background_color = 'Springgreen'
                        if self.resp[4] == 'u':
                            self.b_u.style.background_color = 'Springgreen'
                        if self.resp[4] == 'i':
                            self.b_i.style.background_color = 'Springgreen'
                        if self.resp[4] == 'o':
                            self.b_o.style.background_color = 'Springgreen'
                        if self.resp[4] == 'p':
                            self.b_p.style.background_color = 'Springgreen'
                        if self.resp[4] == 'a':
                            self.b_a.style.background_color = 'Springgreen'
                        if self.resp[4] == 's':
                            self.b_s.style.background_color = 'Springgreen'
                        if self.resp[4] == 'd':
                            self.b_d.style.background_color = 'Springgreen'
                        if self.resp[4] == 'f':
                            self.b_f.style.background_color = 'Springgreen'
                        if self.resp[4] == 'g':
                            self.b_g.style.background_color = 'Springgreen'
                        if self.resp[4] == 'h':
                            self.b_h.style.background_color = 'Springgreen'
                        if self.resp[4] == 'j':
                            self.b_j.style.background_color = 'Springgreen'
                        if self.resp[4] == 'k':
                            self.b_k.style.background_color = 'Springgreen'
                        if self.resp[4] == 'l':
                            self.b_l.style.background_color = 'Springgreen'
                        if self.resp[4] == 'ç':
                            self.b_cdl.style.background_color = 'Springgreen'
                        if self.resp[4] == 'z':
                            self.b_z.style.background_color = 'Springgreen'
                        if self.resp[4] == 'x':
                            self.b_x.style.background_color = 'Springgreen'
                        if self.resp[4] == 'c':
                            self.b_c.style.background_color = 'Springgreen'
                        if self.resp[4] == 'v':
                            self.b_v.style.background_color = 'Springgreen'
                        if self.resp[4] == 'b':
                            self.b_b.style.background_color = 'Springgreen'
                        if self.resp[4] == 'n':
                            self.b_n.style.background_color = 'Springgreen'
                        if self.resp[4] == 'm':
                            self.b_m.style.background_color = 'Springgreen'
                    else:
                        if self.resp[4] in termo_play:
                            self.letra_o2.style.background_color = 'Gold'
                            if ((self.resp[4] == 'q') and (self.b_q.style.background_color != 'Springgreen')):
                                self.b_q.style.background_color = 'Gold'
                            if ((self.resp[4] == 'w') and (self.b_w.style.background_color != 'Springgreen')):
                                self.b_w.style.background_color = 'Gold'
                            if ((self.resp[4] == 'e') and (self.b_e.style.background_color != 'Springgreen')):
                                self.b_e.style.background_color = 'Gold'
                            if ((self.resp[4] == 'r') and (self.b_r.style.background_color != 'Springgreen')):
                                self.b_r.style.background_color = 'Gold'
                            if ((self.resp[4] == 't') and (self.b_t.style.background_color != 'Springgreen')):
                                self.b_t.style.background_color = 'Gold'
                            if ((self.resp[4] == 'y') and (self.b_y.style.background_color != 'Springgreen')):
                                self.b_y.style.background_color = 'Gold'
                            if ((self.resp[4] == 'u') and (self.b_u.style.background_color != 'Springgreen')):
                                self.b_u.style.background_color = 'Gold'
                            if ((self.resp[4] == 'i') and (self.b_i.style.background_color != 'Springgreen')):
                                self.b_i.style.background_color = 'Gold'
                            if ((self.resp[4] == 'o') and (self.b_o.style.background_color != 'Springgreen')):
                                self.b_o.style.background_color = 'Gold'
                            if ((self.resp[4] == 'p') and (self.b_p.style.background_color != 'Springgreen')):
                                self.b_p.style.background_color = 'Gold'
                            if ((self.resp[4] == 'a') and (self.b_a.style.background_color != 'Springgreen')):
                                self.b_a.style.background_color = 'Gold'
                            if ((self.resp[4] == 's') and (self.b_s.style.background_color != 'Springgreen')):
                                self.b_s.style.background_color = 'Gold'
                            if ((self.resp[4] == 'd') and (self.b_d.style.background_color != 'Springgreen')):
                                self.b_d.style.background_color = 'Gold'
                            if ((self.resp[4] == 'f') and (self.b_f.style.background_color != 'Springgreen')):
                                self.b_f.style.background_color = 'Gold'
                            if ((self.resp[4] == 'g') and (self.b_g.style.background_color != 'Springgreen')):
                                self.b_g.style.background_color = 'Gold'
                            if ((self.resp[4] == 'h') and (self.b_h.style.background_color != 'Springgreen')):
                                self.b_h.style.background_color = 'Gold'
                            if ((self.resp[4] == 'j') and (self.b_j.style.background_color != 'Springgreen')):
                                self.b_j.style.background_color = 'Gold'
                            if ((self.resp[4] == 'k') and (self.b_k.style.background_color != 'Springgreen')):
                                self.b_k.style.background_color = 'Gold'
                            if ((self.resp[4] == 'l') and (self.b_l.style.background_color != 'Springgreen')):
                                self.b_l.style.background_color = 'Gold'
                            if ((self.resp[4] == 'ç') and (self.b_cdl.style.background_color != 'Springgreen')):
                                self.b_cdl.style.background_color = 'Gold'
                            if ((self.resp[4] == 'z') and (self.b_z.style.background_color != 'Springgreen')):
                                self.b_z.style.background_color = 'Gold'
                            if ((self.resp[4] == 'x') and (self.b_x.style.background_color != 'Springgreen')):
                                self.b_x.style.background_color = 'Gold'
                            if ((self.resp[4] == 'c') and (self.b_c.style.background_color != 'Springgreen')):
                                self.b_c.style.background_color = 'Gold'
                            if ((self.resp[4] == 'v') and (self.b_v.style.background_color != 'Springgreen')):
                                self.b_v.style.background_color = 'Gold'
                            if ((self.resp[4] == 'b') and (self.b_b.style.background_color != 'Springgreen')):
                                self.b_b.style.background_color = 'Gold'
                            if ((self.resp[4] == 'n') and (self.b_n.style.background_color != 'Springgreen')):
                                self.b_n.style.background_color = 'Gold'
                            if ((self.resp[4] == 'm') and (self.b_m.style.background_color != 'Springgreen')):
                                self.b_m.style.background_color = 'Gold'
                        else:
                            if self.resp[4] == 'q':
                                self.b_q.style.background_color = 'Gray'
                            if self.resp[4] == 'w':
                                self.b_w.style.background_color = 'Gray'
                            if self.resp[4] == 'e':
                                self.b_e.style.background_color = 'Gray'
                            if self.resp[4] == 'r':
                                self.b_r.style.background_color = 'Gray'
                            if self.resp[4] == 't':
                                self.b_t.style.background_color = 'Gray'
                            if self.resp[4] == 'y':
                                self.b_y.style.background_color = 'Gray'
                            if self.resp[4] == 'u':
                                self.b_u.style.background_color = 'Gray'
                            if self.resp[4] == 'i':
                                self.b_i.style.background_color = 'Gray'
                            if self.resp[4] == 'o':
                                self.b_o.style.background_color = 'Gray'
                            if self.resp[4] == 'p':
                                self.b_p.style.background_color = 'Gray'
                            if self.resp[4] == 'a':
                                self.b_a.style.background_color = 'Gray'
                            if self.resp[4] == 's':
                                self.b_s.style.background_color = 'Gray'
                            if self.resp[4] == 'd':
                                self.b_d.style.background_color = 'Gray'
                            if self.resp[4] == 'f':
                                self.b_f.style.background_color = 'Gray'
                            if self.resp[4] == 'g':
                                self.b_g.style.background_color = 'Gray'
                            if self.resp[4] == 'h':
                                self.b_h.style.background_color = 'Gray'
                            if self.resp[4] == 'j':
                                self.b_j.style.background_color = 'Gray'
                            if self.resp[4] == 'k':
                                self.b_k.style.background_color = 'Gray'
                            if self.resp[4] == 'l':
                                self.b_l.style.background_color = 'Gray'
                            if self.resp[4] == 'ç':
                                self.b_cdl.style.background_color = 'Gray'
                            if self.resp[4] == 'z':
                                self.b_z.style.background_color = 'Gray'
                            if self.resp[4] == 'x':
                                self.b_x.style.background_color = 'Gray'
                            if self.resp[4] == 'c':
                                self.b_c.style.background_color = 'Gray'
                            if self.resp[4] == 'v':
                                self.b_v.style.background_color = 'Gray'
                            if self.resp[4] == 'b':
                                self.b_b.style.background_color = 'Gray'
                            if self.resp[4] == 'n':
                                self.b_n.style.background_color = 'Gray'
                            if self.resp[4] == 'm':
                                self.b_m.style.background_color = 'Gray'
                    self.contador = '3'
                else:
                    self.output11.text = '' + termo_play_Acento[0].upper()
                    self.letra_t2.style.background_color = 'Springgreen'
                    self.output12.text = '' + termo_play_Acento[1].upper()
                    self.letra_e2.style.background_color = 'Springgreen'
                    self.output13.text = '' + termo_play_Acento[2].upper()
                    self.letra_r2.style.background_color = 'Springgreen'
                    self.output14.text = '' + termo_play_Acento[3].upper()
                    self.letra_m2.style.background_color = 'Springgreen'
                    self.output15.text = '' + termo_play_Acento[4].upper()
                    self.letra_o2.style.background_color = 'Springgreen'
                    self.main_window.info_dialog('Você Ganhou!', f'{termo_play_Acento.upper()} era a palavra correta 🤩', )
                self.resposta = ''
                return 0
            else:
                if (self.contador == '2'):
                    self.main_window.info_dialog('Palavra inexistente!', 'A palavra digitada não é aceita 😒')
                    return 0

            if ((self.contador == '3') and (self.resposta in palavras_5char_existentes)):
                if (self.resposta != termo_play):
                    if self.resp[0] == termo_play[0]:
                        self.output16.text = '' + termo_play_Acento[0].upper()
                        self.letra_t3.style.background_color = 'Springgreen'
                        if self.resp[0] == 'q':
                            self.b_q.style.background_color = 'Springgreen'
                        if self.resp[0] == 'w':
                            self.b_w.style.background_color = 'Springgreen'
                        if self.resp[0] == 'e':
                            self.b_e.style.background_color = 'Springgreen'
                        if self.resp[0] == 'r':
                            self.b_r.style.background_color = 'Springgreen'
                        if self.resp[0] == 't':
                            self.b_t.style.background_color = 'Springgreen'
                        if self.resp[0] == 'y':
                            self.b_y.style.background_color = 'Springgreen'
                        if self.resp[0] == 'u':
                            self.b_u.style.background_color = 'Springgreen'
                        if self.resp[0] == 'i':
                            self.b_i.style.background_color = 'Springgreen'
                        if self.resp[0] == 'o':
                            self.b_o.style.background_color = 'Springgreen'
                        if self.resp[0] == 'p':
                            self.b_p.style.background_color = 'Springgreen'
                        if self.resp[0] == 'a':
                            self.b_a.style.background_color = 'Springgreen'
                        if self.resp[0] == 's':
                            self.b_s.style.background_color = 'Springgreen'
                        if self.resp[0] == 'd':
                            self.b_d.style.background_color = 'Springgreen'
                        if self.resp[0] == 'f':
                            self.b_f.style.background_color = 'Springgreen'
                        if self.resp[0] == 'g':
                            self.b_g.style.background_color = 'Springgreen'
                        if self.resp[0] == 'h':
                            self.b_h.style.background_color = 'Springgreen'
                        if self.resp[0] == 'j':
                            self.b_j.style.background_color = 'Springgreen'
                        if self.resp[0] == 'k':
                            self.b_k.style.background_color = 'Springgreen'
                        if self.resp[0] == 'l':
                            self.b_l.style.background_color = 'Springgreen'
                        if self.resp[0] == 'ç':
                            self.b_cdl.style.background_color = 'Springgreen'
                        if self.resp[0] == 'z':
                            self.b_z.style.background_color = 'Springgreen'
                        if self.resp[0] == 'x':
                            self.b_x.style.background_color = 'Springgreen'
                        if self.resp[0] == 'c':
                            self.b_c.style.background_color = 'Springgreen'
                        if self.resp[0] == 'v':
                            self.b_v.style.background_color = 'Springgreen'
                        if self.resp[0] == 'b':
                            self.b_b.style.background_color = 'Springgreen'
                        if self.resp[0] == 'n':
                            self.b_n.style.background_color = 'Springgreen'
                        if self.resp[0] == 'm':
                            self.b_m.style.background_color = 'Springgreen'
                    else:
                        if self.resp[0] in termo_play:
                            self.letra_t3.style.background_color = 'Gold'
                            if ((self.resp[0] == 'q') and (self.b_q.style.background_color != 'Springgreen')):
                                self.b_q.style.background_color = 'Gold'
                            if ((self.resp[0] == 'w') and (self.b_w.style.background_color != 'Springgreen')):
                                self.b_w.style.background_color = 'Gold'
                            if ((self.resp[0] == 'e') and (self.b_e.style.background_color != 'Springgreen')):
                                self.b_e.style.background_color = 'Gold'
                            if ((self.resp[0] == 'r') and (self.b_r.style.background_color != 'Springgreen')):
                                self.b_r.style.background_color = 'Gold'
                            if ((self.resp[0] == 't') and (self.b_t.style.background_color != 'Springgreen')):
                                self.b_t.style.background_color = 'Gold'
                            if ((self.resp[0] == 'y') and (self.b_y.style.background_color != 'Springgreen')):
                                self.b_y.style.background_color = 'Gold'
                            if ((self.resp[0] == 'u') and (self.b_u.style.background_color != 'Springgreen')):
                                self.b_u.style.background_color = 'Gold'
                            if ((self.resp[0] == 'i') and (self.b_i.style.background_color != 'Springgreen')):
                                self.b_i.style.background_color = 'Gold'
                            if ((self.resp[0] == 'o') and (self.b_o.style.background_color != 'Springgreen')):
                                self.b_o.style.background_color = 'Gold'
                            if ((self.resp[0] == 'p') and (self.b_p.style.background_color != 'Springgreen')):
                                self.b_p.style.background_color = 'Gold'
                            if ((self.resp[0] == 'a') and (self.b_a.style.background_color != 'Springgreen')):
                                self.b_a.style.background_color = 'Gold'
                            if ((self.resp[0] == 's') and (self.b_s.style.background_color != 'Springgreen')):
                                self.b_s.style.background_color = 'Gold'
                            if ((self.resp[0] == 'd') and (self.b_d.style.background_color != 'Springgreen')):
                                self.b_d.style.background_color = 'Gold'
                            if ((self.resp[0] == 'f') and (self.b_f.style.background_color != 'Springgreen')):
                                self.b_f.style.background_color = 'Gold'
                            if ((self.resp[0] == 'g') and (self.b_g.style.background_color != 'Springgreen')):
                                self.b_g.style.background_color = 'Gold'
                            if ((self.resp[0] == 'h') and (self.b_h.style.background_color != 'Springgreen')):
                                self.b_h.style.background_color = 'Gold'
                            if ((self.resp[0] == 'j') and (self.b_j.style.background_color != 'Springgreen')):
                                self.b_j.style.background_color = 'Gold'
                            if ((self.resp[0] == 'k') and (self.b_k.style.background_color != 'Springgreen')):
                                self.b_k.style.background_color = 'Gold'
                            if ((self.resp[0] == 'l') and (self.b_l.style.background_color != 'Springgreen')):
                                self.b_l.style.background_color = 'Gold'
                            if ((self.resp[0] == 'ç') and (self.b_cdl.style.background_color != 'Springgreen')):
                                self.b_cdl.style.background_color = 'Gold'
                            if ((self.resp[0] == 'z') and (self.b_z.style.background_color != 'Springgreen')):
                                self.b_z.style.background_color = 'Gold'
                            if ((self.resp[0] == 'x') and (self.b_x.style.background_color != 'Springgreen')):
                                self.b_x.style.background_color = 'Gold'
                            if ((self.resp[0] == 'c') and (self.b_c.style.background_color != 'Springgreen')):
                                self.b_c.style.background_color = 'Gold'
                            if ((self.resp[0] == 'v') and (self.b_v.style.background_color != 'Springgreen')):
                                self.b_v.style.background_color = 'Gold'
                            if ((self.resp[0] == 'b') and (self.b_b.style.background_color != 'Springgreen')):
                                self.b_b.style.background_color = 'Gold'
                            if ((self.resp[0] == 'n') and (self.b_n.style.background_color != 'Springgreen')):
                                self.b_n.style.background_color = 'Gold'
                            if ((self.resp[0] == 'm') and (self.b_m.style.background_color != 'Springgreen')):
                                self.b_m.style.background_color = 'Gold'
                        else:
                            if self.resp[0] == 'q':
                                self.b_q.style.background_color = 'Gray'
                            if self.resp[0] == 'w':
                                self.b_w.style.background_color = 'Gray'
                            if self.resp[0] == 'e':
                                self.b_e.style.background_color = 'Gray'
                            if self.resp[0] == 'r':
                                self.b_r.style.background_color = 'Gray'
                            if self.resp[0] == 't':
                                self.b_t.style.background_color = 'Gray'
                            if self.resp[0] == 'y':
                                self.b_y.style.background_color = 'Gray'
                            if self.resp[0] == 'u':
                                self.b_u.style.background_color = 'Gray'
                            if self.resp[0] == 'i':
                                self.b_i.style.background_color = 'Gray'
                            if self.resp[0] == 'o':
                                self.b_o.style.background_color = 'Gray'
                            if self.resp[0] == 'p':
                                self.b_p.style.background_color = 'Gray'
                            if self.resp[0] == 'a':
                                self.b_a.style.background_color = 'Gray'
                            if self.resp[0] == 's':
                                self.b_s.style.background_color = 'Gray'
                            if self.resp[0] == 'd':
                                self.b_d.style.background_color = 'Gray'
                            if self.resp[0] == 'f':
                                self.b_f.style.background_color = 'Gray'
                            if self.resp[0] == 'g':
                                self.b_g.style.background_color = 'Gray'
                            if self.resp[0] == 'h':
                                self.b_h.style.background_color = 'Gray'
                            if self.resp[0] == 'j':
                                self.b_j.style.background_color = 'Gray'
                            if self.resp[0] == 'k':
                                self.b_k.style.background_color = 'Gray'
                            if self.resp[0] == 'l':
                                self.b_l.style.background_color = 'Gray'
                            if self.resp[0] == 'ç':
                                self.b_cdl.style.background_color = 'Gray'
                            if self.resp[0] == 'z':
                                self.b_z.style.background_color = 'Gray'
                            if self.resp[0] == 'x':
                                self.b_x.style.background_color = 'Gray'
                            if self.resp[0] == 'c':
                                self.b_c.style.background_color = 'Gray'
                            if self.resp[0] == 'v':
                                self.b_v.style.background_color = 'Gray'
                            if self.resp[0] == 'b':
                                self.b_b.style.background_color = 'Gray'
                            if self.resp[0] == 'n':
                                self.b_n.style.background_color = 'Gray'
                            if self.resp[0] == 'm':
                                self.b_m.style.background_color = 'Gray'

                    if self.resp[1] == termo_play[1]:
                        self.output17.text = '' + termo_play_Acento[1].upper()
                        self.letra_e3.style.background_color = 'Springgreen'
                        if self.resp[1] == 'q':
                            self.b_q.style.background_color = 'Springgreen'
                        if self.resp[1] == 'w':
                            self.b_w.style.background_color = 'Springgreen'
                        if self.resp[1] == 'e':
                            self.b_e.style.background_color = 'Springgreen'
                        if self.resp[1] == 'r':
                            self.b_r.style.background_color = 'Springgreen'
                        if self.resp[1] == 't':
                            self.b_t.style.background_color = 'Springgreen'
                        if self.resp[1] == 'y':
                            self.b_y.style.background_color = 'Springgreen'
                        if self.resp[1] == 'u':
                            self.b_u.style.background_color = 'Springgreen'
                        if self.resp[1] == 'i':
                            self.b_i.style.background_color = 'Springgreen'
                        if self.resp[1] == 'o':
                            self.b_o.style.background_color = 'Springgreen'
                        if self.resp[1] == 'p':
                            self.b_p.style.background_color = 'Springgreen'
                        if self.resp[1] == 'a':
                            self.b_a.style.background_color = 'Springgreen'
                        if self.resp[1] == 's':
                            self.b_s.style.background_color = 'Springgreen'
                        if self.resp[1] == 'd':
                            self.b_d.style.background_color = 'Springgreen'
                        if self.resp[1] == 'f':
                            self.b_f.style.background_color = 'Springgreen'
                        if self.resp[1] == 'g':
                            self.b_g.style.background_color = 'Springgreen'
                        if self.resp[1] == 'h':
                            self.b_h.style.background_color = 'Springgreen'
                        if self.resp[1] == 'j':
                            self.b_j.style.background_color = 'Springgreen'
                        if self.resp[1] == 'k':
                            self.b_k.style.background_color = 'Springgreen'
                        if self.resp[1] == 'l':
                            self.b_l.style.background_color = 'Springgreen'
                        if self.resp[1] == 'ç':
                            self.b_cdl.style.background_color = 'Springgreen'
                        if self.resp[1] == 'z':
                            self.b_z.style.background_color = 'Springgreen'
                        if self.resp[1] == 'x':
                            self.b_x.style.background_color = 'Springgreen'
                        if self.resp[1] == 'c':
                            self.b_c.style.background_color = 'Springgreen'
                        if self.resp[1] == 'v':
                            self.b_v.style.background_color = 'Springgreen'
                        if self.resp[1] == 'b':
                            self.b_b.style.background_color = 'Springgreen'
                        if self.resp[1] == 'n':
                            self.b_n.style.background_color = 'Springgreen'
                        if self.resp[1] == 'm':
                            self.b_m.style.background_color = 'Springgreen'
                    else:
                        if self.resp[1] in termo_play:
                            self.letra_e3.style.background_color = 'Gold'
                            if ((self.resp[1] == 'q') and (self.b_q.style.background_color != 'Springgreen')):
                                self.b_q.style.background_color = 'Gold'
                            if ((self.resp[1] == 'w') and (self.b_w.style.background_color != 'Springgreen')):
                                self.b_w.style.background_color = 'Gold'
                            if ((self.resp[1] == 'e') and (self.b_e.style.background_color != 'Springgreen')):
                                self.b_e.style.background_color = 'Gold'
                            if ((self.resp[1] == 'r') and (self.b_r.style.background_color != 'Springgreen')):
                                self.b_r.style.background_color = 'Gold'
                            if ((self.resp[1] == 't') and (self.b_t.style.background_color != 'Springgreen')):
                                self.b_t.style.background_color = 'Gold'
                            if ((self.resp[1] == 'y') and (self.b_y.style.background_color != 'Springgreen')):
                                self.b_y.style.background_color = 'Gold'
                            if ((self.resp[1] == 'u') and (self.b_u.style.background_color != 'Springgreen')):
                                self.b_u.style.background_color = 'Gold'
                            if ((self.resp[1] == 'i') and (self.b_i.style.background_color != 'Springgreen')):
                                self.b_i.style.background_color = 'Gold'
                            if ((self.resp[1] == 'o') and (self.b_o.style.background_color != 'Springgreen')):
                                self.b_o.style.background_color = 'Gold'
                            if ((self.resp[1] == 'p') and (self.b_p.style.background_color != 'Springgreen')):
                                self.b_p.style.background_color = 'Gold'
                            if ((self.resp[1] == 'a') and (self.b_a.style.background_color != 'Springgreen')):
                                self.b_a.style.background_color = 'Gold'
                            if ((self.resp[1] == 's') and (self.b_s.style.background_color != 'Springgreen')):
                                self.b_s.style.background_color = 'Gold'
                            if ((self.resp[1] == 'd') and (self.b_d.style.background_color != 'Springgreen')):
                                self.b_d.style.background_color = 'Gold'
                            if ((self.resp[1] == 'f') and (self.b_f.style.background_color != 'Springgreen')):
                                self.b_f.style.background_color = 'Gold'
                            if ((self.resp[1] == 'g') and (self.b_g.style.background_color != 'Springgreen')):
                                self.b_g.style.background_color = 'Gold'
                            if ((self.resp[1] == 'h') and (self.b_h.style.background_color != 'Springgreen')):
                                self.b_h.style.background_color = 'Gold'
                            if ((self.resp[1] == 'j') and (self.b_j.style.background_color != 'Springgreen')):
                                self.b_j.style.background_color = 'Gold'
                            if ((self.resp[1] == 'k') and (self.b_k.style.background_color != 'Springgreen')):
                                self.b_k.style.background_color = 'Gold'
                            if ((self.resp[1] == 'l') and (self.b_l.style.background_color != 'Springgreen')):
                                self.b_l.style.background_color = 'Gold'
                            if ((self.resp[1] == 'ç') and (self.b_cdl.style.background_color != 'Springgreen')):
                                self.b_cdl.style.background_color = 'Gold'
                            if ((self.resp[1] == 'z') and (self.b_z.style.background_color != 'Springgreen')):
                                self.b_z.style.background_color = 'Gold'
                            if ((self.resp[1] == 'x') and (self.b_x.style.background_color != 'Springgreen')):
                                self.b_x.style.background_color = 'Gold'
                            if ((self.resp[1] == 'c') and (self.b_c.style.background_color != 'Springgreen')):
                                self.b_c.style.background_color = 'Gold'
                            if ((self.resp[1] == 'v') and (self.b_v.style.background_color != 'Springgreen')):
                                self.b_v.style.background_color = 'Gold'
                            if ((self.resp[1] == 'b') and (self.b_b.style.background_color != 'Springgreen')):
                                self.b_b.style.background_color = 'Gold'
                            if ((self.resp[1] == 'n') and (self.b_n.style.background_color != 'Springgreen')):
                                self.b_n.style.background_color = 'Gold'
                            if ((self.resp[1] == 'm') and (self.b_m.style.background_color != 'Springgreen')):
                                self.b_m.style.background_color = 'Gold'
                        else:
                            if self.resp[1] == 'q':
                                self.b_q.style.background_color = 'Gray'
                            if self.resp[1] == 'w':
                                self.b_w.style.background_color = 'Gray'
                            if self.resp[1] == 'e':
                                self.b_e.style.background_color = 'Gray'
                            if self.resp[1] == 'r':
                                self.b_r.style.background_color = 'Gray'
                            if self.resp[1] == 't':
                                self.b_t.style.background_color = 'Gray'
                            if self.resp[1] == 'y':
                                self.b_y.style.background_color = 'Gray'
                            if self.resp[1] == 'u':
                                self.b_u.style.background_color = 'Gray'
                            if self.resp[1] == 'i':
                                self.b_i.style.background_color = 'Gray'
                            if self.resp[1] == 'o':
                                self.b_o.style.background_color = 'Gray'
                            if self.resp[1] == 'p':
                                self.b_p.style.background_color = 'Gray'
                            if self.resp[1] == 'a':
                                self.b_a.style.background_color = 'Gray'
                            if self.resp[1] == 's':
                                self.b_s.style.background_color = 'Gray'
                            if self.resp[1] == 'd':
                                self.b_d.style.background_color = 'Gray'
                            if self.resp[1] == 'f':
                                self.b_f.style.background_color = 'Gray'
                            if self.resp[1] == 'g':
                                self.b_g.style.background_color = 'Gray'
                            if self.resp[1] == 'h':
                                self.b_h.style.background_color = 'Gray'
                            if self.resp[1] == 'j':
                                self.b_j.style.background_color = 'Gray'
                            if self.resp[1] == 'k':
                                self.b_k.style.background_color = 'Gray'
                            if self.resp[1] == 'l':
                                self.b_l.style.background_color = 'Gray'
                            if self.resp[1] == 'ç':
                                self.b_cdl.style.background_color = 'Gray'
                            if self.resp[1] == 'z':
                                self.b_z.style.background_color = 'Gray'
                            if self.resp[1] == 'x':
                                self.b_x.style.background_color = 'Gray'
                            if self.resp[1] == 'c':
                                self.b_c.style.background_color = 'Gray'
                            if self.resp[1] == 'v':
                                self.b_v.style.background_color = 'Gray'
                            if self.resp[1] == 'b':
                                self.b_b.style.background_color = 'Gray'
                            if self.resp[1] == 'n':
                                self.b_n.style.background_color = 'Gray'
                            if self.resp[1] == 'm':
                                self.b_m.style.background_color = 'Gray'

                    if self.resp[2] == termo_play[2]:
                        self.output18.text = '' + termo_play_Acento[2].upper()
                        self.letra_r3.style.background_color = 'Springgreen'
                        if self.resp[2] == 'q':
                            self.b_q.style.background_color = 'Springgreen'
                        if self.resp[2] == 'w':
                            self.b_w.style.background_color = 'Springgreen'
                        if self.resp[2] == 'e':
                            self.b_e.style.background_color = 'Springgreen'
                        if self.resp[2] == 'r':
                            self.b_r.style.background_color = 'Springgreen'
                        if self.resp[2] == 't':
                            self.b_t.style.background_color = 'Springgreen'
                        if self.resp[2] == 'y':
                            self.b_y.style.background_color = 'Springgreen'
                        if self.resp[2] == 'u':
                            self.b_u.style.background_color = 'Springgreen'
                        if self.resp[2] == 'i':
                            self.b_i.style.background_color = 'Springgreen'
                        if self.resp[2] == 'o':
                            self.b_o.style.background_color = 'Springgreen'
                        if self.resp[2] == 'p':
                            self.b_p.style.background_color = 'Springgreen'
                        if self.resp[2] == 'a':
                            self.b_a.style.background_color = 'Springgreen'
                        if self.resp[2] == 's':
                            self.b_s.style.background_color = 'Springgreen'
                        if self.resp[2] == 'd':
                            self.b_d.style.background_color = 'Springgreen'
                        if self.resp[2] == 'f':
                            self.b_f.style.background_color = 'Springgreen'
                        if self.resp[2] == 'g':
                            self.b_g.style.background_color = 'Springgreen'
                        if self.resp[2] == 'h':
                            self.b_h.style.background_color = 'Springgreen'
                        if self.resp[2] == 'j':
                            self.b_j.style.background_color = 'Springgreen'
                        if self.resp[2] == 'k':
                            self.b_k.style.background_color = 'Springgreen'
                        if self.resp[2] == 'l':
                            self.b_l.style.background_color = 'Springgreen'
                        if self.resp[2] == 'ç':
                            self.b_cdl.style.background_color = 'Springgreen'
                        if self.resp[2] == 'z':
                            self.b_z.style.background_color = 'Springgreen'
                        if self.resp[2] == 'x':
                            self.b_x.style.background_color = 'Springgreen'
                        if self.resp[2] == 'c':
                            self.b_c.style.background_color = 'Springgreen'
                        if self.resp[2] == 'v':
                            self.b_v.style.background_color = 'Springgreen'
                        if self.resp[2] == 'b':
                            self.b_b.style.background_color = 'Springgreen'
                        if self.resp[2] == 'n':
                            self.b_n.style.background_color = 'Springgreen'
                        if self.resp[2] == 'm':
                            self.b_m.style.background_color = 'Springgreen'
                    else:
                        if self.resp[2] in termo_play:
                            self.letra_r3.style.background_color = 'Gold'
                            if ((self.resp[2] == 'q') and (self.b_q.style.background_color != 'Springgreen')):
                                self.b_q.style.background_color = 'Gold'
                            if ((self.resp[2] == 'w') and (self.b_w.style.background_color != 'Springgreen')):
                                self.b_w.style.background_color = 'Gold'
                            if ((self.resp[2] == 'e') and (self.b_e.style.background_color != 'Springgreen')):
                                self.b_e.style.background_color = 'Gold'
                            if ((self.resp[2] == 'r') and (self.b_r.style.background_color != 'Springgreen')):
                                self.b_r.style.background_color = 'Gold'
                            if ((self.resp[2] == 't') and (self.b_t.style.background_color != 'Springgreen')):
                                self.b_t.style.background_color = 'Gold'
                            if ((self.resp[2] == 'y') and (self.b_y.style.background_color != 'Springgreen')):
                                self.b_y.style.background_color = 'Gold'
                            if ((self.resp[2] == 'u') and (self.b_u.style.background_color != 'Springgreen')):
                                self.b_u.style.background_color = 'Gold'
                            if ((self.resp[2] == 'i') and (self.b_i.style.background_color != 'Springgreen')):
                                self.b_i.style.background_color = 'Gold'
                            if ((self.resp[2] == 'o') and (self.b_o.style.background_color != 'Springgreen')):
                                self.b_o.style.background_color = 'Gold'
                            if ((self.resp[2] == 'p') and (self.b_p.style.background_color != 'Springgreen')):
                                self.b_p.style.background_color = 'Gold'
                            if ((self.resp[2] == 'a') and (self.b_a.style.background_color != 'Springgreen')):
                                self.b_a.style.background_color = 'Gold'
                            if ((self.resp[2] == 's') and (self.b_s.style.background_color != 'Springgreen')):
                                self.b_s.style.background_color = 'Gold'
                            if ((self.resp[2] == 'd') and (self.b_d.style.background_color != 'Springgreen')):
                                self.b_d.style.background_color = 'Gold'
                            if ((self.resp[2] == 'f') and (self.b_f.style.background_color != 'Springgreen')):
                                self.b_f.style.background_color = 'Gold'
                            if ((self.resp[2] == 'g') and (self.b_g.style.background_color != 'Springgreen')):
                                self.b_g.style.background_color = 'Gold'
                            if ((self.resp[2] == 'h') and (self.b_h.style.background_color != 'Springgreen')):
                                self.b_h.style.background_color = 'Gold'
                            if ((self.resp[2] == 'j') and (self.b_j.style.background_color != 'Springgreen')):
                                self.b_j.style.background_color = 'Gold'
                            if ((self.resp[2] == 'k') and (self.b_k.style.background_color != 'Springgreen')):
                                self.b_k.style.background_color = 'Gold'
                            if ((self.resp[2] == 'l') and (self.b_l.style.background_color != 'Springgreen')):
                                self.b_l.style.background_color = 'Gold'
                            if ((self.resp[2] == 'ç') and (self.b_cdl.style.background_color != 'Springgreen')):
                                self.b_cdl.style.background_color = 'Gold'
                            if ((self.resp[2] == 'z') and (self.b_z.style.background_color != 'Springgreen')):
                                self.b_z.style.background_color = 'Gold'
                            if ((self.resp[2] == 'x') and (self.b_x.style.background_color != 'Springgreen')):
                                self.b_x.style.background_color = 'Gold'
                            if ((self.resp[2] == 'c') and (self.b_c.style.background_color != 'Springgreen')):
                                self.b_c.style.background_color = 'Gold'
                            if ((self.resp[2] == 'v') and (self.b_v.style.background_color != 'Springgreen')):
                                self.b_v.style.background_color = 'Gold'
                            if ((self.resp[2] == 'b') and (self.b_b.style.background_color != 'Springgreen')):
                                self.b_b.style.background_color = 'Gold'
                            if ((self.resp[2] == 'n') and (self.b_n.style.background_color != 'Springgreen')):
                                self.b_n.style.background_color = 'Gold'
                            if ((self.resp[2] == 'm') and (self.b_m.style.background_color != 'Springgreen')):
                                self.b_m.style.background_color = 'Gold'
                        else:
                            if self.resp[2] == 'q':
                                self.b_q.style.background_color = 'Gray'
                            if self.resp[2] == 'w':
                                self.b_w.style.background_color = 'Gray'
                            if self.resp[2] == 'e':
                                self.b_e.style.background_color = 'Gray'
                            if self.resp[2] == 'r':
                                self.b_r.style.background_color = 'Gray'
                            if self.resp[2] == 't':
                                self.b_t.style.background_color = 'Gray'
                            if self.resp[2] == 'y':
                                self.b_y.style.background_color = 'Gray'
                            if self.resp[2] == 'u':
                                self.b_u.style.background_color = 'Gray'
                            if self.resp[2] == 'i':
                                self.b_i.style.background_color = 'Gray'
                            if self.resp[2] == 'o':
                                self.b_o.style.background_color = 'Gray'
                            if self.resp[2] == 'p':
                                self.b_p.style.background_color = 'Gray'
                            if self.resp[2] == 'a':
                                self.b_a.style.background_color = 'Gray'
                            if self.resp[2] == 's':
                                self.b_s.style.background_color = 'Gray'
                            if self.resp[2] == 'd':
                                self.b_d.style.background_color = 'Gray'
                            if self.resp[2] == 'f':
                                self.b_f.style.background_color = 'Gray'
                            if self.resp[2] == 'g':
                                self.b_g.style.background_color = 'Gray'
                            if self.resp[2] == 'h':
                                self.b_h.style.background_color = 'Gray'
                            if self.resp[2] == 'j':
                                self.b_j.style.background_color = 'Gray'
                            if self.resp[2] == 'k':
                                self.b_k.style.background_color = 'Gray'
                            if self.resp[2] == 'l':
                                self.b_l.style.background_color = 'Gray'
                            if self.resp[2] == 'ç':
                                self.b_cdl.style.background_color = 'Gray'
                            if self.resp[2] == 'z':
                                self.b_z.style.background_color = 'Gray'
                            if self.resp[2] == 'x':
                                self.b_x.style.background_color = 'Gray'
                            if self.resp[2] == 'c':
                                self.b_c.style.background_color = 'Gray'
                            if self.resp[2] == 'v':
                                self.b_v.style.background_color = 'Gray'
                            if self.resp[2] == 'b':
                                self.b_b.style.background_color = 'Gray'
                            if self.resp[2] == 'n':
                                self.b_n.style.background_color = 'Gray'
                            if self.resp[2] == 'm':
                                self.b_m.style.background_color = 'Gray'

                    if self.resp[3] == termo_play[3]:
                        self.output19.text = '' + termo_play_Acento[3].upper()
                        self.letra_m3.style.background_color = 'Springgreen'
                        if self.resp[3] == 'q':
                            self.b_q.style.background_color = 'Springgreen'
                        if self.resp[3] == 'w':
                            self.b_w.style.background_color = 'Springgreen'
                        if self.resp[3] == 'e':
                            self.b_e.style.background_color = 'Springgreen'
                        if self.resp[3] == 'r':
                            self.b_r.style.background_color = 'Springgreen'
                        if self.resp[3] == 't':
                            self.b_t.style.background_color = 'Springgreen'
                        if self.resp[3] == 'y':
                            self.b_y.style.background_color = 'Springgreen'
                        if self.resp[3] == 'u':
                            self.b_u.style.background_color = 'Springgreen'
                        if self.resp[3] == 'i':
                            self.b_i.style.background_color = 'Springgreen'
                        if self.resp[3] == 'o':
                            self.b_o.style.background_color = 'Springgreen'
                        if self.resp[3] == 'p':
                            self.b_p.style.background_color = 'Springgreen'
                        if self.resp[3] == 'a':
                            self.b_a.style.background_color = 'Springgreen'
                        if self.resp[3] == 's':
                            self.b_s.style.background_color = 'Springgreen'
                        if self.resp[3] == 'd':
                            self.b_d.style.background_color = 'Springgreen'
                        if self.resp[3] == 'f':
                            self.b_f.style.background_color = 'Springgreen'
                        if self.resp[3] == 'g':
                            self.b_g.style.background_color = 'Springgreen'
                        if self.resp[3] == 'h':
                            self.b_h.style.background_color = 'Springgreen'
                        if self.resp[3] == 'j':
                            self.b_j.style.background_color = 'Springgreen'
                        if self.resp[3] == 'k':
                            self.b_k.style.background_color = 'Springgreen'
                        if self.resp[3] == 'l':
                            self.b_l.style.background_color = 'Springgreen'
                        if self.resp[3] == 'ç':
                            self.b_cdl.style.background_color = 'Springgreen'
                        if self.resp[3] == 'z':
                            self.b_z.style.background_color = 'Springgreen'
                        if self.resp[3] == 'x':
                            self.b_x.style.background_color = 'Springgreen'
                        if self.resp[3] == 'c':
                            self.b_c.style.background_color = 'Springgreen'
                        if self.resp[3] == 'v':
                            self.b_v.style.background_color = 'Springgreen'
                        if self.resp[3] == 'b':
                            self.b_b.style.background_color = 'Springgreen'
                        if self.resp[3] == 'n':
                            self.b_n.style.background_color = 'Springgreen'
                        if self.resp[3] == 'm':
                            self.b_m.style.background_color = 'Springgreen'
                    else:
                        if self.resp[3] in termo_play:
                            self.letra_m3.style.background_color = 'Gold'
                            if ((self.resp[3] == 'q') and (self.b_q.style.background_color != 'Springgreen')):
                                self.b_q.style.background_color = 'Gold'
                            if ((self.resp[3] == 'w') and (self.b_w.style.background_color != 'Springgreen')):
                                self.b_w.style.background_color = 'Gold'
                            if ((self.resp[3] == 'e') and (self.b_e.style.background_color != 'Springgreen')):
                                self.b_e.style.background_color = 'Gold'
                            if ((self.resp[3] == 'r') and (self.b_r.style.background_color != 'Springgreen')):
                                self.b_r.style.background_color = 'Gold'
                            if ((self.resp[3] == 't') and (self.b_t.style.background_color != 'Springgreen')):
                                self.b_t.style.background_color = 'Gold'
                            if ((self.resp[3] == 'y') and (self.b_y.style.background_color != 'Springgreen')):
                                self.b_y.style.background_color = 'Gold'
                            if ((self.resp[3] == 'u') and (self.b_u.style.background_color != 'Springgreen')):
                                self.b_u.style.background_color = 'Gold'
                            if ((self.resp[3] == 'i') and (self.b_i.style.background_color != 'Springgreen')):
                                self.b_i.style.background_color = 'Gold'
                            if ((self.resp[3] == 'o') and (self.b_o.style.background_color != 'Springgreen')):
                                self.b_o.style.background_color = 'Gold'
                            if ((self.resp[3] == 'p') and (self.b_p.style.background_color != 'Springgreen')):
                                self.b_p.style.background_color = 'Gold'
                            if ((self.resp[3] == 'a') and (self.b_a.style.background_color != 'Springgreen')):
                                self.b_a.style.background_color = 'Gold'
                            if ((self.resp[3] == 's') and (self.b_s.style.background_color != 'Springgreen')):
                                self.b_s.style.background_color = 'Gold'
                            if ((self.resp[3] == 'd') and (self.b_d.style.background_color != 'Springgreen')):
                                self.b_d.style.background_color = 'Gold'
                            if ((self.resp[3] == 'f') and (self.b_f.style.background_color != 'Springgreen')):
                                self.b_f.style.background_color = 'Gold'
                            if ((self.resp[3] == 'g') and (self.b_g.style.background_color != 'Springgreen')):
                                self.b_g.style.background_color = 'Gold'
                            if ((self.resp[3] == 'h') and (self.b_h.style.background_color != 'Springgreen')):
                                self.b_h.style.background_color = 'Gold'
                            if ((self.resp[3] == 'j') and (self.b_j.style.background_color != 'Springgreen')):
                                self.b_j.style.background_color = 'Gold'
                            if ((self.resp[3] == 'k') and (self.b_k.style.background_color != 'Springgreen')):
                                self.b_k.style.background_color = 'Gold'
                            if ((self.resp[3] == 'l') and (self.b_l.style.background_color != 'Springgreen')):
                                self.b_l.style.background_color = 'Gold'
                            if ((self.resp[3] == 'ç') and (self.b_cdl.style.background_color != 'Springgreen')):
                                self.b_cdl.style.background_color = 'Gold'
                            if ((self.resp[3] == 'z') and (self.b_z.style.background_color != 'Springgreen')):
                                self.b_z.style.background_color = 'Gold'
                            if ((self.resp[3] == 'x') and (self.b_x.style.background_color != 'Springgreen')):
                                self.b_x.style.background_color = 'Gold'
                            if ((self.resp[3] == 'c') and (self.b_c.style.background_color != 'Springgreen')):
                                self.b_c.style.background_color = 'Gold'
                            if ((self.resp[3] == 'v') and (self.b_v.style.background_color != 'Springgreen')):
                                self.b_v.style.background_color = 'Gold'
                            if ((self.resp[3] == 'b') and (self.b_b.style.background_color != 'Springgreen')):
                                self.b_b.style.background_color = 'Gold'
                            if ((self.resp[3] == 'n') and (self.b_n.style.background_color != 'Springgreen')):
                                self.b_n.style.background_color = 'Gold'
                            if ((self.resp[3] == 'm') and (self.b_m.style.background_color != 'Springgreen')):
                                self.b_m.style.background_color = 'Gold'
                        else:
                            if self.resp[3] == 'q':
                                self.b_q.style.background_color = 'Gray'
                            if self.resp[3] == 'w':
                                self.b_w.style.background_color = 'Gray'
                            if self.resp[3] == 'e':
                                self.b_e.style.background_color = 'Gray'
                            if self.resp[3] == 'r':
                                self.b_r.style.background_color = 'Gray'
                            if self.resp[3] == 't':
                                self.b_t.style.background_color = 'Gray'
                            if self.resp[3] == 'y':
                                self.b_y.style.background_color = 'Gray'
                            if self.resp[3] == 'u':
                                self.b_u.style.background_color = 'Gray'
                            if self.resp[3] == 'i':
                                self.b_i.style.background_color = 'Gray'
                            if self.resp[3] == 'o':
                                self.b_o.style.background_color = 'Gray'
                            if self.resp[3] == 'p':
                                self.b_p.style.background_color = 'Gray'
                            if self.resp[3] == 'a':
                                self.b_a.style.background_color = 'Gray'
                            if self.resp[3] == 's':
                                self.b_s.style.background_color = 'Gray'
                            if self.resp[3] == 'd':
                                self.b_d.style.background_color = 'Gray'
                            if self.resp[3] == 'f':
                                self.b_f.style.background_color = 'Gray'
                            if self.resp[3] == 'g':
                                self.b_g.style.background_color = 'Gray'
                            if self.resp[3] == 'h':
                                self.b_h.style.background_color = 'Gray'
                            if self.resp[3] == 'j':
                                self.b_j.style.background_color = 'Gray'
                            if self.resp[3] == 'k':
                                self.b_k.style.background_color = 'Gray'
                            if self.resp[3] == 'l':
                                self.b_l.style.background_color = 'Gray'
                            if self.resp[3] == 'ç':
                                self.b_cdl.style.background_color = 'Gray'
                            if self.resp[3] == 'z':
                                self.b_z.style.background_color = 'Gray'
                            if self.resp[3] == 'x':
                                self.b_x.style.background_color = 'Gray'
                            if self.resp[3] == 'c':
                                self.b_c.style.background_color = 'Gray'
                            if self.resp[3] == 'v':
                                self.b_v.style.background_color = 'Gray'
                            if self.resp[3] == 'b':
                                self.b_b.style.background_color = 'Gray'
                            if self.resp[3] == 'n':
                                self.b_n.style.background_color = 'Gray'
                            if self.resp[3] == 'm':
                                self.b_m.style.background_color = 'Gray'

                    if self.resp[4] == termo_play[4]:
                        self.output20.text = '' + termo_play_Acento[4].upper()
                        self.letra_o3.style.background_color = 'Springgreen'
                        if self.resp[4] == 'q':
                            self.b_q.style.background_color = 'Springgreen'
                        if self.resp[4] == 'w':
                            self.b_w.style.background_color = 'Springgreen'
                        if self.resp[4] == 'e':
                            self.b_e.style.background_color = 'Springgreen'
                        if self.resp[4] == 'r':
                            self.b_r.style.background_color = 'Springgreen'
                        if self.resp[4] == 't':
                            self.b_t.style.background_color = 'Springgreen'
                        if self.resp[4] == 'y':
                            self.b_y.style.background_color = 'Springgreen'
                        if self.resp[4] == 'u':
                            self.b_u.style.background_color = 'Springgreen'
                        if self.resp[4] == 'i':
                            self.b_i.style.background_color = 'Springgreen'
                        if self.resp[4] == 'o':
                            self.b_o.style.background_color = 'Springgreen'
                        if self.resp[4] == 'p':
                            self.b_p.style.background_color = 'Springgreen'
                        if self.resp[4] == 'a':
                            self.b_a.style.background_color = 'Springgreen'
                        if self.resp[4] == 's':
                            self.b_s.style.background_color = 'Springgreen'
                        if self.resp[4] == 'd':
                            self.b_d.style.background_color = 'Springgreen'
                        if self.resp[4] == 'f':
                            self.b_f.style.background_color = 'Springgreen'
                        if self.resp[4] == 'g':
                            self.b_g.style.background_color = 'Springgreen'
                        if self.resp[4] == 'h':
                            self.b_h.style.background_color = 'Springgreen'
                        if self.resp[4] == 'j':
                            self.b_j.style.background_color = 'Springgreen'
                        if self.resp[4] == 'k':
                            self.b_k.style.background_color = 'Springgreen'
                        if self.resp[4] == 'l':
                            self.b_l.style.background_color = 'Springgreen'
                        if self.resp[4] == 'ç':
                            self.b_cdl.style.background_color = 'Springgreen'
                        if self.resp[4] == 'z':
                            self.b_z.style.background_color = 'Springgreen'
                        if self.resp[4] == 'x':
                            self.b_x.style.background_color = 'Springgreen'
                        if self.resp[4] == 'c':
                            self.b_c.style.background_color = 'Springgreen'
                        if self.resp[4] == 'v':
                            self.b_v.style.background_color = 'Springgreen'
                        if self.resp[4] == 'b':
                            self.b_b.style.background_color = 'Springgreen'
                        if self.resp[4] == 'n':
                            self.b_n.style.background_color = 'Springgreen'
                        if self.resp[4] == 'm':
                            self.b_m.style.background_color = 'Springgreen'
                    else:
                        if self.resp[4] in termo_play:
                            self.letra_o3.style.background_color = 'Gold'
                            if ((self.resp[4] == 'q') and (self.b_q.style.background_color != 'Springgreen')):
                                self.b_q.style.background_color = 'Gold'
                            if ((self.resp[4] == 'w') and (self.b_w.style.background_color != 'Springgreen')):
                                self.b_w.style.background_color = 'Gold'
                            if ((self.resp[4] == 'e') and (self.b_e.style.background_color != 'Springgreen')):
                                self.b_e.style.background_color = 'Gold'
                            if ((self.resp[4] == 'r') and (self.b_r.style.background_color != 'Springgreen')):
                                self.b_r.style.background_color = 'Gold'
                            if ((self.resp[4] == 't') and (self.b_t.style.background_color != 'Springgreen')):
                                self.b_t.style.background_color = 'Gold'
                            if ((self.resp[4] == 'y') and (self.b_y.style.background_color != 'Springgreen')):
                                self.b_y.style.background_color = 'Gold'
                            if ((self.resp[4] == 'u') and (self.b_u.style.background_color != 'Springgreen')):
                                self.b_u.style.background_color = 'Gold'
                            if ((self.resp[4] == 'i') and (self.b_i.style.background_color != 'Springgreen')):
                                self.b_i.style.background_color = 'Gold'
                            if ((self.resp[4] == 'o') and (self.b_o.style.background_color != 'Springgreen')):
                                self.b_o.style.background_color = 'Gold'
                            if ((self.resp[4] == 'p') and (self.b_p.style.background_color != 'Springgreen')):
                                self.b_p.style.background_color = 'Gold'
                            if ((self.resp[4] == 'a') and (self.b_a.style.background_color != 'Springgreen')):
                                self.b_a.style.background_color = 'Gold'
                            if ((self.resp[4] == 's') and (self.b_s.style.background_color != 'Springgreen')):
                                self.b_s.style.background_color = 'Gold'
                            if ((self.resp[4] == 'd') and (self.b_d.style.background_color != 'Springgreen')):
                                self.b_d.style.background_color = 'Gold'
                            if ((self.resp[4] == 'f') and (self.b_f.style.background_color != 'Springgreen')):
                                self.b_f.style.background_color = 'Gold'
                            if ((self.resp[4] == 'g') and (self.b_g.style.background_color != 'Springgreen')):
                                self.b_g.style.background_color = 'Gold'
                            if ((self.resp[4] == 'h') and (self.b_h.style.background_color != 'Springgreen')):
                                self.b_h.style.background_color = 'Gold'
                            if ((self.resp[4] == 'j') and (self.b_j.style.background_color != 'Springgreen')):
                                self.b_j.style.background_color = 'Gold'
                            if ((self.resp[4] == 'k') and (self.b_k.style.background_color != 'Springgreen')):
                                self.b_k.style.background_color = 'Gold'
                            if ((self.resp[4] == 'l') and (self.b_l.style.background_color != 'Springgreen')):
                                self.b_l.style.background_color = 'Gold'
                            if ((self.resp[4] == 'ç') and (self.b_cdl.style.background_color != 'Springgreen')):
                                self.b_cdl.style.background_color = 'Gold'
                            if ((self.resp[4] == 'z') and (self.b_z.style.background_color != 'Springgreen')):
                                self.b_z.style.background_color = 'Gold'
                            if ((self.resp[4] == 'x') and (self.b_x.style.background_color != 'Springgreen')):
                                self.b_x.style.background_color = 'Gold'
                            if ((self.resp[4] == 'c') and (self.b_c.style.background_color != 'Springgreen')):
                                self.b_c.style.background_color = 'Gold'
                            if ((self.resp[4] == 'v') and (self.b_v.style.background_color != 'Springgreen')):
                                self.b_v.style.background_color = 'Gold'
                            if ((self.resp[4] == 'b') and (self.b_b.style.background_color != 'Springgreen')):
                                self.b_b.style.background_color = 'Gold'
                            if ((self.resp[4] == 'n') and (self.b_n.style.background_color != 'Springgreen')):
                                self.b_n.style.background_color = 'Gold'
                            if ((self.resp[4] == 'm') and (self.b_m.style.background_color != 'Springgreen')):
                                self.b_m.style.background_color = 'Gold'
                        else:
                            if self.resp[4] == 'q':
                                self.b_q.style.background_color = 'Gray'
                            if self.resp[4] == 'w':
                                self.b_w.style.background_color = 'Gray'
                            if self.resp[4] == 'e':
                                self.b_e.style.background_color = 'Gray'
                            if self.resp[4] == 'r':
                                self.b_r.style.background_color = 'Gray'
                            if self.resp[4] == 't':
                                self.b_t.style.background_color = 'Gray'
                            if self.resp[4] == 'y':
                                self.b_y.style.background_color = 'Gray'
                            if self.resp[4] == 'u':
                                self.b_u.style.background_color = 'Gray'
                            if self.resp[4] == 'i':
                                self.b_i.style.background_color = 'Gray'
                            if self.resp[4] == 'o':
                                self.b_o.style.background_color = 'Gray'
                            if self.resp[4] == 'p':
                                self.b_p.style.background_color = 'Gray'
                            if self.resp[4] == 'a':
                                self.b_a.style.background_color = 'Gray'
                            if self.resp[4] == 's':
                                self.b_s.style.background_color = 'Gray'
                            if self.resp[4] == 'd':
                                self.b_d.style.background_color = 'Gray'
                            if self.resp[4] == 'f':
                                self.b_f.style.background_color = 'Gray'
                            if self.resp[4] == 'g':
                                self.b_g.style.background_color = 'Gray'
                            if self.resp[4] == 'h':
                                self.b_h.style.background_color = 'Gray'
                            if self.resp[4] == 'j':
                                self.b_j.style.background_color = 'Gray'
                            if self.resp[4] == 'k':
                                self.b_k.style.background_color = 'Gray'
                            if self.resp[4] == 'l':
                                self.b_l.style.background_color = 'Gray'
                            if self.resp[4] == 'ç':
                                self.b_cdl.style.background_color = 'Gray'
                            if self.resp[4] == 'z':
                                self.b_z.style.background_color = 'Gray'
                            if self.resp[4] == 'x':
                                self.b_x.style.background_color = 'Gray'
                            if self.resp[4] == 'c':
                                self.b_c.style.background_color = 'Gray'
                            if self.resp[4] == 'v':
                                self.b_v.style.background_color = 'Gray'
                            if self.resp[4] == 'b':
                                self.b_b.style.background_color = 'Gray'
                            if self.resp[4] == 'n':
                                self.b_n.style.background_color = 'Gray'
                            if self.resp[4] == 'm':
                                self.b_m.style.background_color = 'Gray'
                    self.contador = '4'
                else:
                    self.output16.text = '' + termo_play_Acento[0].upper()
                    self.letra_t3.style.background_color = 'Springgreen'
                    self.output17.text = '' + termo_play_Acento[1].upper()
                    self.letra_e3.style.background_color = 'Springgreen'
                    self.output18.text = '' + termo_play_Acento[2].upper()
                    self.letra_r3.style.background_color = 'Springgreen'
                    self.output19.text = '' + termo_play_Acento[3].upper()
                    self.letra_m3.style.background_color = 'Springgreen'
                    self.output20.text = '' + termo_play_Acento[4].upper()
                    self.letra_o3.style.background_color = 'Springgreen'
                    self.main_window.info_dialog('Você Ganhou!', f'{termo_play_Acento.upper()} era a palavra correta 🤩', )
                self.resposta = ''
                return 0
            else:
                if (self.contador == '3'):
                    self.main_window.info_dialog('Palavra inexistente!', 'A palavra digitada não é aceita 😒')
                    return 0

            if ((self.contador == '4') and (self.resposta in palavras_5char_existentes)):
                if (self.resposta != termo_play):
                    if self.resp[0] == termo_play[0]:
                        self.output21.text = '' + termo_play_Acento[0].upper()
                        self.letra_t4.style.background_color = 'Springgreen'
                        if self.resp[0] == 'q':
                            self.b_q.style.background_color = 'Springgreen'
                        if self.resp[0] == 'w':
                            self.b_w.style.background_color = 'Springgreen'
                        if self.resp[0] == 'e':
                            self.b_e.style.background_color = 'Springgreen'
                        if self.resp[0] == 'r':
                            self.b_r.style.background_color = 'Springgreen'
                        if self.resp[0] == 't':
                            self.b_t.style.background_color = 'Springgreen'
                        if self.resp[0] == 'y':
                            self.b_y.style.background_color = 'Springgreen'
                        if self.resp[0] == 'u':
                            self.b_u.style.background_color = 'Springgreen'
                        if self.resp[0] == 'i':
                            self.b_i.style.background_color = 'Springgreen'
                        if self.resp[0] == 'o':
                            self.b_o.style.background_color = 'Springgreen'
                        if self.resp[0] == 'p':
                            self.b_p.style.background_color = 'Springgreen'
                        if self.resp[0] == 'a':
                            self.b_a.style.background_color = 'Springgreen'
                        if self.resp[0] == 's':
                            self.b_s.style.background_color = 'Springgreen'
                        if self.resp[0] == 'd':
                            self.b_d.style.background_color = 'Springgreen'
                        if self.resp[0] == 'f':
                            self.b_f.style.background_color = 'Springgreen'
                        if self.resp[0] == 'g':
                            self.b_g.style.background_color = 'Springgreen'
                        if self.resp[0] == 'h':
                            self.b_h.style.background_color = 'Springgreen'
                        if self.resp[0] == 'j':
                            self.b_j.style.background_color = 'Springgreen'
                        if self.resp[0] == 'k':
                            self.b_k.style.background_color = 'Springgreen'
                        if self.resp[0] == 'l':
                            self.b_l.style.background_color = 'Springgreen'
                        if self.resp[0] == 'ç':
                            self.b_cdl.style.background_color = 'Springgreen'
                        if self.resp[0] == 'z':
                            self.b_z.style.background_color = 'Springgreen'
                        if self.resp[0] == 'x':
                            self.b_x.style.background_color = 'Springgreen'
                        if self.resp[0] == 'c':
                            self.b_c.style.background_color = 'Springgreen'
                        if self.resp[0] == 'v':
                            self.b_v.style.background_color = 'Springgreen'
                        if self.resp[0] == 'b':
                            self.b_b.style.background_color = 'Springgreen'
                        if self.resp[0] == 'n':
                            self.b_n.style.background_color = 'Springgreen'
                        if self.resp[0] == 'm':
                            self.b_m.style.background_color = 'Springgreen'
                    else:
                        if self.resp[0] in termo_play:
                            self.letra_t4.style.background_color = 'Gold'
                            if ((self.resp[0] == 'q') and (self.b_q.style.background_color != 'Springgreen')):
                                self.b_q.style.background_color = 'Gold'
                            if ((self.resp[0] == 'w') and (self.b_w.style.background_color != 'Springgreen')):
                                self.b_w.style.background_color = 'Gold'
                            if ((self.resp[0] == 'e') and (self.b_e.style.background_color != 'Springgreen')):
                                self.b_e.style.background_color = 'Gold'
                            if ((self.resp[0] == 'r') and (self.b_r.style.background_color != 'Springgreen')):
                                self.b_r.style.background_color = 'Gold'
                            if ((self.resp[0] == 't') and (self.b_t.style.background_color != 'Springgreen')):
                                self.b_t.style.background_color = 'Gold'
                            if ((self.resp[0] == 'y') and (self.b_y.style.background_color != 'Springgreen')):
                                self.b_y.style.background_color = 'Gold'
                            if ((self.resp[0] == 'u') and (self.b_u.style.background_color != 'Springgreen')):
                                self.b_u.style.background_color = 'Gold'
                            if ((self.resp[0] == 'i') and (self.b_i.style.background_color != 'Springgreen')):
                                self.b_i.style.background_color = 'Gold'
                            if ((self.resp[0] == 'o') and (self.b_o.style.background_color != 'Springgreen')):
                                self.b_o.style.background_color = 'Gold'
                            if ((self.resp[0] == 'p') and (self.b_p.style.background_color != 'Springgreen')):
                                self.b_p.style.background_color = 'Gold'
                            if ((self.resp[0] == 'a') and (self.b_a.style.background_color != 'Springgreen')):
                                self.b_a.style.background_color = 'Gold'
                            if ((self.resp[0] == 's') and (self.b_s.style.background_color != 'Springgreen')):
                                self.b_s.style.background_color = 'Gold'
                            if ((self.resp[0] == 'd') and (self.b_d.style.background_color != 'Springgreen')):
                                self.b_d.style.background_color = 'Gold'
                            if ((self.resp[0] == 'f') and (self.b_f.style.background_color != 'Springgreen')):
                                self.b_f.style.background_color = 'Gold'
                            if ((self.resp[0] == 'g') and (self.b_g.style.background_color != 'Springgreen')):
                                self.b_g.style.background_color = 'Gold'
                            if ((self.resp[0] == 'h') and (self.b_h.style.background_color != 'Springgreen')):
                                self.b_h.style.background_color = 'Gold'
                            if ((self.resp[0] == 'j') and (self.b_j.style.background_color != 'Springgreen')):
                                self.b_j.style.background_color = 'Gold'
                            if ((self.resp[0] == 'k') and (self.b_k.style.background_color != 'Springgreen')):
                                self.b_k.style.background_color = 'Gold'
                            if ((self.resp[0] == 'l') and (self.b_l.style.background_color != 'Springgreen')):
                                self.b_l.style.background_color = 'Gold'
                            if ((self.resp[0] == 'ç') and (self.b_cdl.style.background_color != 'Springgreen')):
                                self.b_cdl.style.background_color = 'Gold'
                            if ((self.resp[0] == 'z') and (self.b_z.style.background_color != 'Springgreen')):
                                self.b_z.style.background_color = 'Gold'
                            if ((self.resp[0] == 'x') and (self.b_x.style.background_color != 'Springgreen')):
                                self.b_x.style.background_color = 'Gold'
                            if ((self.resp[0] == 'c') and (self.b_c.style.background_color != 'Springgreen')):
                                self.b_c.style.background_color = 'Gold'
                            if ((self.resp[0] == 'v') and (self.b_v.style.background_color != 'Springgreen')):
                                self.b_v.style.background_color = 'Gold'
                            if ((self.resp[0] == 'b') and (self.b_b.style.background_color != 'Springgreen')):
                                self.b_b.style.background_color = 'Gold'
                            if ((self.resp[0] == 'n') and (self.b_n.style.background_color != 'Springgreen')):
                                self.b_n.style.background_color = 'Gold'
                            if ((self.resp[0] == 'm') and (self.b_m.style.background_color != 'Springgreen')):
                                self.b_m.style.background_color = 'Gold'
                        else:
                            if self.resp[0] == 'q':
                                self.b_q.style.background_color = 'Gray'
                            if self.resp[0] == 'w':
                                self.b_w.style.background_color = 'Gray'
                            if self.resp[0] == 'e':
                                self.b_e.style.background_color = 'Gray'
                            if self.resp[0] == 'r':
                                self.b_r.style.background_color = 'Gray'
                            if self.resp[0] == 't':
                                self.b_t.style.background_color = 'Gray'
                            if self.resp[0] == 'y':
                                self.b_y.style.background_color = 'Gray'
                            if self.resp[0] == 'u':
                                self.b_u.style.background_color = 'Gray'
                            if self.resp[0] == 'i':
                                self.b_i.style.background_color = 'Gray'
                            if self.resp[0] == 'o':
                                self.b_o.style.background_color = 'Gray'
                            if self.resp[0] == 'p':
                                self.b_p.style.background_color = 'Gray'
                            if self.resp[0] == 'a':
                                self.b_a.style.background_color = 'Gray'
                            if self.resp[0] == 's':
                                self.b_s.style.background_color = 'Gray'
                            if self.resp[0] == 'd':
                                self.b_d.style.background_color = 'Gray'
                            if self.resp[0] == 'f':
                                self.b_f.style.background_color = 'Gray'
                            if self.resp[0] == 'g':
                                self.b_g.style.background_color = 'Gray'
                            if self.resp[0] == 'h':
                                self.b_h.style.background_color = 'Gray'
                            if self.resp[0] == 'j':
                                self.b_j.style.background_color = 'Gray'
                            if self.resp[0] == 'k':
                                self.b_k.style.background_color = 'Gray'
                            if self.resp[0] == 'l':
                                self.b_l.style.background_color = 'Gray'
                            if self.resp[0] == 'ç':
                                self.b_cdl.style.background_color = 'Gray'
                            if self.resp[0] == 'z':
                                self.b_z.style.background_color = 'Gray'
                            if self.resp[0] == 'x':
                                self.b_x.style.background_color = 'Gray'
                            if self.resp[0] == 'c':
                                self.b_c.style.background_color = 'Gray'
                            if self.resp[0] == 'v':
                                self.b_v.style.background_color = 'Gray'
                            if self.resp[0] == 'b':
                                self.b_b.style.background_color = 'Gray'
                            if self.resp[0] == 'n':
                                self.b_n.style.background_color = 'Gray'
                            if self.resp[0] == 'm':
                                self.b_m.style.background_color = 'Gray'

                    if self.resp[1] == termo_play[1]:
                        self.output22.text = '' + termo_play_Acento[1].upper()
                        self.letra_e4.style.background_color = 'Springgreen'
                        if self.resp[1] == 'q':
                            self.b_q.style.background_color = 'Springgreen'
                        if self.resp[1] == 'w':
                            self.b_w.style.background_color = 'Springgreen'
                        if self.resp[1] == 'e':
                            self.b_e.style.background_color = 'Springgreen'
                        if self.resp[1] == 'r':
                            self.b_r.style.background_color = 'Springgreen'
                        if self.resp[1] == 't':
                            self.b_t.style.background_color = 'Springgreen'
                        if self.resp[1] == 'y':
                            self.b_y.style.background_color = 'Springgreen'
                        if self.resp[1] == 'u':
                            self.b_u.style.background_color = 'Springgreen'
                        if self.resp[1] == 'i':
                            self.b_i.style.background_color = 'Springgreen'
                        if self.resp[1] == 'o':
                            self.b_o.style.background_color = 'Springgreen'
                        if self.resp[1] == 'p':
                            self.b_p.style.background_color = 'Springgreen'
                        if self.resp[1] == 'a':
                            self.b_a.style.background_color = 'Springgreen'
                        if self.resp[1] == 's':
                            self.b_s.style.background_color = 'Springgreen'
                        if self.resp[1] == 'd':
                            self.b_d.style.background_color = 'Springgreen'
                        if self.resp[1] == 'f':
                            self.b_f.style.background_color = 'Springgreen'
                        if self.resp[1] == 'g':
                            self.b_g.style.background_color = 'Springgreen'
                        if self.resp[1] == 'h':
                            self.b_h.style.background_color = 'Springgreen'
                        if self.resp[1] == 'j':
                            self.b_j.style.background_color = 'Springgreen'
                        if self.resp[1] == 'k':
                            self.b_k.style.background_color = 'Springgreen'
                        if self.resp[1] == 'l':
                            self.b_l.style.background_color = 'Springgreen'
                        if self.resp[1] == 'ç':
                            self.b_cdl.style.background_color = 'Springgreen'
                        if self.resp[1] == 'z':
                            self.b_z.style.background_color = 'Springgreen'
                        if self.resp[1] == 'x':
                            self.b_x.style.background_color = 'Springgreen'
                        if self.resp[1] == 'c':
                            self.b_c.style.background_color = 'Springgreen'
                        if self.resp[1] == 'v':
                            self.b_v.style.background_color = 'Springgreen'
                        if self.resp[1] == 'b':
                            self.b_b.style.background_color = 'Springgreen'
                        if self.resp[1] == 'n':
                            self.b_n.style.background_color = 'Springgreen'
                        if self.resp[1] == 'm':
                            self.b_m.style.background_color = 'Springgreen'
                    else:
                        if self.resp[1] in termo_play:
                            self.letra_e4.style.background_color = 'Gold'
                            if ((self.resp[1] == 'q') and (self.b_q.style.background_color != 'Springgreen')):
                                self.b_q.style.background_color = 'Gold'
                            if ((self.resp[1] == 'w') and (self.b_w.style.background_color != 'Springgreen')):
                                self.b_w.style.background_color = 'Gold'
                            if ((self.resp[1] == 'e') and (self.b_e.style.background_color != 'Springgreen')):
                                self.b_e.style.background_color = 'Gold'
                            if ((self.resp[1] == 'r') and (self.b_r.style.background_color != 'Springgreen')):
                                self.b_r.style.background_color = 'Gold'
                            if ((self.resp[1] == 't') and (self.b_t.style.background_color != 'Springgreen')):
                                self.b_t.style.background_color = 'Gold'
                            if ((self.resp[1] == 'y') and (self.b_y.style.background_color != 'Springgreen')):
                                self.b_y.style.background_color = 'Gold'
                            if ((self.resp[1] == 'u') and (self.b_u.style.background_color != 'Springgreen')):
                                self.b_u.style.background_color = 'Gold'
                            if ((self.resp[1] == 'i') and (self.b_i.style.background_color != 'Springgreen')):
                                self.b_i.style.background_color = 'Gold'
                            if ((self.resp[1] == 'o') and (self.b_o.style.background_color != 'Springgreen')):
                                self.b_o.style.background_color = 'Gold'
                            if ((self.resp[1] == 'p') and (self.b_p.style.background_color != 'Springgreen')):
                                self.b_p.style.background_color = 'Gold'
                            if ((self.resp[1] == 'a') and (self.b_a.style.background_color != 'Springgreen')):
                                self.b_a.style.background_color = 'Gold'
                            if ((self.resp[1] == 's') and (self.b_s.style.background_color != 'Springgreen')):
                                self.b_s.style.background_color = 'Gold'
                            if ((self.resp[1] == 'd') and (self.b_d.style.background_color != 'Springgreen')):
                                self.b_d.style.background_color = 'Gold'
                            if ((self.resp[1] == 'f') and (self.b_f.style.background_color != 'Springgreen')):
                                self.b_f.style.background_color = 'Gold'
                            if ((self.resp[1] == 'g') and (self.b_g.style.background_color != 'Springgreen')):
                                self.b_g.style.background_color = 'Gold'
                            if ((self.resp[1] == 'h') and (self.b_h.style.background_color != 'Springgreen')):
                                self.b_h.style.background_color = 'Gold'
                            if ((self.resp[1] == 'j') and (self.b_j.style.background_color != 'Springgreen')):
                                self.b_j.style.background_color = 'Gold'
                            if ((self.resp[1] == 'k') and (self.b_k.style.background_color != 'Springgreen')):
                                self.b_k.style.background_color = 'Gold'
                            if ((self.resp[1] == 'l') and (self.b_l.style.background_color != 'Springgreen')):
                                self.b_l.style.background_color = 'Gold'
                            if ((self.resp[1] == 'ç') and (self.b_cdl.style.background_color != 'Springgreen')):
                                self.b_cdl.style.background_color = 'Gold'
                            if ((self.resp[1] == 'z') and (self.b_z.style.background_color != 'Springgreen')):
                                self.b_z.style.background_color = 'Gold'
                            if ((self.resp[1] == 'x') and (self.b_x.style.background_color != 'Springgreen')):
                                self.b_x.style.background_color = 'Gold'
                            if ((self.resp[1] == 'c') and (self.b_c.style.background_color != 'Springgreen')):
                                self.b_c.style.background_color = 'Gold'
                            if ((self.resp[1] == 'v') and (self.b_v.style.background_color != 'Springgreen')):
                                self.b_v.style.background_color = 'Gold'
                            if ((self.resp[1] == 'b') and (self.b_b.style.background_color != 'Springgreen')):
                                self.b_b.style.background_color = 'Gold'
                            if ((self.resp[1] == 'n') and (self.b_n.style.background_color != 'Springgreen')):
                                self.b_n.style.background_color = 'Gold'
                            if ((self.resp[1] == 'm') and (self.b_m.style.background_color != 'Springgreen')):
                                self.b_m.style.background_color = 'Gold'
                        else:
                            if self.resp[1] == 'q':
                                self.b_q.style.background_color = 'Gray'
                            if self.resp[1] == 'w':
                                self.b_w.style.background_color = 'Gray'
                            if self.resp[1] == 'e':
                                self.b_e.style.background_color = 'Gray'
                            if self.resp[1] == 'r':
                                self.b_r.style.background_color = 'Gray'
                            if self.resp[1] == 't':
                                self.b_t.style.background_color = 'Gray'
                            if self.resp[1] == 'y':
                                self.b_y.style.background_color = 'Gray'
                            if self.resp[1] == 'u':
                                self.b_u.style.background_color = 'Gray'
                            if self.resp[1] == 'i':
                                self.b_i.style.background_color = 'Gray'
                            if self.resp[1] == 'o':
                                self.b_o.style.background_color = 'Gray'
                            if self.resp[1] == 'p':
                                self.b_p.style.background_color = 'Gray'
                            if self.resp[1] == 'a':
                                self.b_a.style.background_color = 'Gray'
                            if self.resp[1] == 's':
                                self.b_s.style.background_color = 'Gray'
                            if self.resp[1] == 'd':
                                self.b_d.style.background_color = 'Gray'
                            if self.resp[1] == 'f':
                                self.b_f.style.background_color = 'Gray'
                            if self.resp[1] == 'g':
                                self.b_g.style.background_color = 'Gray'
                            if self.resp[1] == 'h':
                                self.b_h.style.background_color = 'Gray'
                            if self.resp[1] == 'j':
                                self.b_j.style.background_color = 'Gray'
                            if self.resp[1] == 'k':
                                self.b_k.style.background_color = 'Gray'
                            if self.resp[1] == 'l':
                                self.b_l.style.background_color = 'Gray'
                            if self.resp[1] == 'ç':
                                self.b_cdl.style.background_color = 'Gray'
                            if self.resp[1] == 'z':
                                self.b_z.style.background_color = 'Gray'
                            if self.resp[1] == 'x':
                                self.b_x.style.background_color = 'Gray'
                            if self.resp[1] == 'c':
                                self.b_c.style.background_color = 'Gray'
                            if self.resp[1] == 'v':
                                self.b_v.style.background_color = 'Gray'
                            if self.resp[1] == 'b':
                                self.b_b.style.background_color = 'Gray'
                            if self.resp[1] == 'n':
                                self.b_n.style.background_color = 'Gray'
                            if self.resp[1] == 'm':
                                self.b_m.style.background_color = 'Gray'

                    if self.resp[2] == termo_play[2]:
                        self.output23.text = '' + termo_play_Acento[2].upper()
                        self.letra_r4.style.background_color = 'Springgreen'
                        if self.resp[2] == 'q':
                            self.b_q.style.background_color = 'Springgreen'
                        if self.resp[2] == 'w':
                            self.b_w.style.background_color = 'Springgreen'
                        if self.resp[2] == 'e':
                            self.b_e.style.background_color = 'Springgreen'
                        if self.resp[2] == 'r':
                            self.b_r.style.background_color = 'Springgreen'
                        if self.resp[2] == 't':
                            self.b_t.style.background_color = 'Springgreen'
                        if self.resp[2] == 'y':
                            self.b_y.style.background_color = 'Springgreen'
                        if self.resp[2] == 'u':
                            self.b_u.style.background_color = 'Springgreen'
                        if self.resp[2] == 'i':
                            self.b_i.style.background_color = 'Springgreen'
                        if self.resp[2] == 'o':
                            self.b_o.style.background_color = 'Springgreen'
                        if self.resp[2] == 'p':
                            self.b_p.style.background_color = 'Springgreen'
                        if self.resp[2] == 'a':
                            self.b_a.style.background_color = 'Springgreen'
                        if self.resp[2] == 's':
                            self.b_s.style.background_color = 'Springgreen'
                        if self.resp[2] == 'd':
                            self.b_d.style.background_color = 'Springgreen'
                        if self.resp[2] == 'f':
                            self.b_f.style.background_color = 'Springgreen'
                        if self.resp[2] == 'g':
                            self.b_g.style.background_color = 'Springgreen'
                        if self.resp[2] == 'h':
                            self.b_h.style.background_color = 'Springgreen'
                        if self.resp[2] == 'j':
                            self.b_j.style.background_color = 'Springgreen'
                        if self.resp[2] == 'k':
                            self.b_k.style.background_color = 'Springgreen'
                        if self.resp[2] == 'l':
                            self.b_l.style.background_color = 'Springgreen'
                        if self.resp[2] == 'ç':
                            self.b_cdl.style.background_color = 'Springgreen'
                        if self.resp[2] == 'z':
                            self.b_z.style.background_color = 'Springgreen'
                        if self.resp[2] == 'x':
                            self.b_x.style.background_color = 'Springgreen'
                        if self.resp[2] == 'c':
                            self.b_c.style.background_color = 'Springgreen'
                        if self.resp[2] == 'v':
                            self.b_v.style.background_color = 'Springgreen'
                        if self.resp[2] == 'b':
                            self.b_b.style.background_color = 'Springgreen'
                        if self.resp[2] == 'n':
                            self.b_n.style.background_color = 'Springgreen'
                        if self.resp[2] == 'm':
                            self.b_m.style.background_color = 'Springgreen'
                    else:
                        if self.resp[2] in termo_play:
                            self.letra_r4.style.background_color = 'Gold'
                            if ((self.resp[2] == 'q') and (self.b_q.style.background_color != 'Springgreen')):
                                self.b_q.style.background_color = 'Gold'
                            if ((self.resp[2] == 'w') and (self.b_w.style.background_color != 'Springgreen')):
                                self.b_w.style.background_color = 'Gold'
                            if ((self.resp[2] == 'e') and (self.b_e.style.background_color != 'Springgreen')):
                                self.b_e.style.background_color = 'Gold'
                            if ((self.resp[2] == 'r') and (self.b_r.style.background_color != 'Springgreen')):
                                self.b_r.style.background_color = 'Gold'
                            if ((self.resp[2] == 't') and (self.b_t.style.background_color != 'Springgreen')):
                                self.b_t.style.background_color = 'Gold'
                            if ((self.resp[2] == 'y') and (self.b_y.style.background_color != 'Springgreen')):
                                self.b_y.style.background_color = 'Gold'
                            if ((self.resp[2] == 'u') and (self.b_u.style.background_color != 'Springgreen')):
                                self.b_u.style.background_color = 'Gold'
                            if ((self.resp[2] == 'i') and (self.b_i.style.background_color != 'Springgreen')):
                                self.b_i.style.background_color = 'Gold'
                            if ((self.resp[2] == 'o') and (self.b_o.style.background_color != 'Springgreen')):
                                self.b_o.style.background_color = 'Gold'
                            if ((self.resp[2] == 'p') and (self.b_p.style.background_color != 'Springgreen')):
                                self.b_p.style.background_color = 'Gold'
                            if ((self.resp[2] == 'a') and (self.b_a.style.background_color != 'Springgreen')):
                                self.b_a.style.background_color = 'Gold'
                            if ((self.resp[2] == 's') and (self.b_s.style.background_color != 'Springgreen')):
                                self.b_s.style.background_color = 'Gold'
                            if ((self.resp[2] == 'd') and (self.b_d.style.background_color != 'Springgreen')):
                                self.b_d.style.background_color = 'Gold'
                            if ((self.resp[2] == 'f') and (self.b_f.style.background_color != 'Springgreen')):
                                self.b_f.style.background_color = 'Gold'
                            if ((self.resp[2] == 'g') and (self.b_g.style.background_color != 'Springgreen')):
                                self.b_g.style.background_color = 'Gold'
                            if ((self.resp[2] == 'h') and (self.b_h.style.background_color != 'Springgreen')):
                                self.b_h.style.background_color = 'Gold'
                            if ((self.resp[2] == 'j') and (self.b_j.style.background_color != 'Springgreen')):
                                self.b_j.style.background_color = 'Gold'
                            if ((self.resp[2] == 'k') and (self.b_k.style.background_color != 'Springgreen')):
                                self.b_k.style.background_color = 'Gold'
                            if ((self.resp[2] == 'l') and (self.b_l.style.background_color != 'Springgreen')):
                                self.b_l.style.background_color = 'Gold'
                            if ((self.resp[2] == 'ç') and (self.b_cdl.style.background_color != 'Springgreen')):
                                self.b_cdl.style.background_color = 'Gold'
                            if ((self.resp[2] == 'z') and (self.b_z.style.background_color != 'Springgreen')):
                                self.b_z.style.background_color = 'Gold'
                            if ((self.resp[2] == 'x') and (self.b_x.style.background_color != 'Springgreen')):
                                self.b_x.style.background_color = 'Gold'
                            if ((self.resp[2] == 'c') and (self.b_c.style.background_color != 'Springgreen')):
                                self.b_c.style.background_color = 'Gold'
                            if ((self.resp[2] == 'v') and (self.b_v.style.background_color != 'Springgreen')):
                                self.b_v.style.background_color = 'Gold'
                            if ((self.resp[2] == 'b') and (self.b_b.style.background_color != 'Springgreen')):
                                self.b_b.style.background_color = 'Gold'
                            if ((self.resp[2] == 'n') and (self.b_n.style.background_color != 'Springgreen')):
                                self.b_n.style.background_color = 'Gold'
                            if ((self.resp[2] == 'm') and (self.b_m.style.background_color != 'Springgreen')):
                                self.b_m.style.background_color = 'Gold'
                        else:
                            if self.resp[2] == 'q':
                                self.b_q.style.background_color = 'Gray'
                            if self.resp[2] == 'w':
                                self.b_w.style.background_color = 'Gray'
                            if self.resp[2] == 'e':
                                self.b_e.style.background_color = 'Gray'
                            if self.resp[2] == 'r':
                                self.b_r.style.background_color = 'Gray'
                            if self.resp[2] == 't':
                                self.b_t.style.background_color = 'Gray'
                            if self.resp[2] == 'y':
                                self.b_y.style.background_color = 'Gray'
                            if self.resp[2] == 'u':
                                self.b_u.style.background_color = 'Gray'
                            if self.resp[2] == 'i':
                                self.b_i.style.background_color = 'Gray'
                            if self.resp[2] == 'o':
                                self.b_o.style.background_color = 'Gray'
                            if self.resp[2] == 'p':
                                self.b_p.style.background_color = 'Gray'
                            if self.resp[2] == 'a':
                                self.b_a.style.background_color = 'Gray'
                            if self.resp[2] == 's':
                                self.b_s.style.background_color = 'Gray'
                            if self.resp[2] == 'd':
                                self.b_d.style.background_color = 'Gray'
                            if self.resp[2] == 'f':
                                self.b_f.style.background_color = 'Gray'
                            if self.resp[2] == 'g':
                                self.b_g.style.background_color = 'Gray'
                            if self.resp[2] == 'h':
                                self.b_h.style.background_color = 'Gray'
                            if self.resp[2] == 'j':
                                self.b_j.style.background_color = 'Gray'
                            if self.resp[2] == 'k':
                                self.b_k.style.background_color = 'Gray'
                            if self.resp[2] == 'l':
                                self.b_l.style.background_color = 'Gray'
                            if self.resp[2] == 'ç':
                                self.b_cdl.style.background_color = 'Gray'
                            if self.resp[2] == 'z':
                                self.b_z.style.background_color = 'Gray'
                            if self.resp[2] == 'x':
                                self.b_x.style.background_color = 'Gray'
                            if self.resp[2] == 'c':
                                self.b_c.style.background_color = 'Gray'
                            if self.resp[2] == 'v':
                                self.b_v.style.background_color = 'Gray'
                            if self.resp[2] == 'b':
                                self.b_b.style.background_color = 'Gray'
                            if self.resp[2] == 'n':
                                self.b_n.style.background_color = 'Gray'
                            if self.resp[2] == 'm':
                                self.b_m.style.background_color = 'Gray'

                    if self.resp[3] == termo_play[3]:
                        self.output24.text = '' + termo_play_Acento[3].upper()
                        self.letra_m4.style.background_color = 'Springgreen'
                        if self.resp[3] == 'q':
                            self.b_q.style.background_color = 'Springgreen'
                        if self.resp[3] == 'w':
                            self.b_w.style.background_color = 'Springgreen'
                        if self.resp[3] == 'e':
                            self.b_e.style.background_color = 'Springgreen'
                        if self.resp[3] == 'r':
                            self.b_r.style.background_color = 'Springgreen'
                        if self.resp[3] == 't':
                            self.b_t.style.background_color = 'Springgreen'
                        if self.resp[3] == 'y':
                            self.b_y.style.background_color = 'Springgreen'
                        if self.resp[3] == 'u':
                            self.b_u.style.background_color = 'Springgreen'
                        if self.resp[3] == 'i':
                            self.b_i.style.background_color = 'Springgreen'
                        if self.resp[3] == 'o':
                            self.b_o.style.background_color = 'Springgreen'
                        if self.resp[3] == 'p':
                            self.b_p.style.background_color = 'Springgreen'
                        if self.resp[3] == 'a':
                            self.b_a.style.background_color = 'Springgreen'
                        if self.resp[3] == 's':
                            self.b_s.style.background_color = 'Springgreen'
                        if self.resp[3] == 'd':
                            self.b_d.style.background_color = 'Springgreen'
                        if self.resp[3] == 'f':
                            self.b_f.style.background_color = 'Springgreen'
                        if self.resp[3] == 'g':
                            self.b_g.style.background_color = 'Springgreen'
                        if self.resp[3] == 'h':
                            self.b_h.style.background_color = 'Springgreen'
                        if self.resp[3] == 'j':
                            self.b_j.style.background_color = 'Springgreen'
                        if self.resp[3] == 'k':
                            self.b_k.style.background_color = 'Springgreen'
                        if self.resp[3] == 'l':
                            self.b_l.style.background_color = 'Springgreen'
                        if self.resp[3] == 'ç':
                            self.b_cdl.style.background_color = 'Springgreen'
                        if self.resp[3] == 'z':
                            self.b_z.style.background_color = 'Springgreen'
                        if self.resp[3] == 'x':
                            self.b_x.style.background_color = 'Springgreen'
                        if self.resp[3] == 'c':
                            self.b_c.style.background_color = 'Springgreen'
                        if self.resp[3] == 'v':
                            self.b_v.style.background_color = 'Springgreen'
                        if self.resp[3] == 'b':
                            self.b_b.style.background_color = 'Springgreen'
                        if self.resp[3] == 'n':
                            self.b_n.style.background_color = 'Springgreen'
                        if self.resp[3] == 'm':
                            self.b_m.style.background_color = 'Springgreen'
                    else:
                        if self.resp[3] in termo_play:
                            self.letra_m4.style.background_color = 'Gold'
                            if ((self.resp[3] == 'q') and (self.b_q.style.background_color != 'Springgreen')):
                                self.b_q.style.background_color = 'Gold'
                            if ((self.resp[3] == 'w') and (self.b_w.style.background_color != 'Springgreen')):
                                self.b_w.style.background_color = 'Gold'
                            if ((self.resp[3] == 'e') and (self.b_e.style.background_color != 'Springgreen')):
                                self.b_e.style.background_color = 'Gold'
                            if ((self.resp[3] == 'r') and (self.b_r.style.background_color != 'Springgreen')):
                                self.b_r.style.background_color = 'Gold'
                            if ((self.resp[3] == 't') and (self.b_t.style.background_color != 'Springgreen')):
                                self.b_t.style.background_color = 'Gold'
                            if ((self.resp[3] == 'y') and (self.b_y.style.background_color != 'Springgreen')):
                                self.b_y.style.background_color = 'Gold'
                            if ((self.resp[3] == 'u') and (self.b_u.style.background_color != 'Springgreen')):
                                self.b_u.style.background_color = 'Gold'
                            if ((self.resp[3] == 'i') and (self.b_i.style.background_color != 'Springgreen')):
                                self.b_i.style.background_color = 'Gold'
                            if ((self.resp[3] == 'o') and (self.b_o.style.background_color != 'Springgreen')):
                                self.b_o.style.background_color = 'Gold'
                            if ((self.resp[3] == 'p') and (self.b_p.style.background_color != 'Springgreen')):
                                self.b_p.style.background_color = 'Gold'
                            if ((self.resp[3] == 'a') and (self.b_a.style.background_color != 'Springgreen')):
                                self.b_a.style.background_color = 'Gold'
                            if ((self.resp[3] == 's') and (self.b_s.style.background_color != 'Springgreen')):
                                self.b_s.style.background_color = 'Gold'
                            if ((self.resp[3] == 'd') and (self.b_d.style.background_color != 'Springgreen')):
                                self.b_d.style.background_color = 'Gold'
                            if ((self.resp[3] == 'f') and (self.b_f.style.background_color != 'Springgreen')):
                                self.b_f.style.background_color = 'Gold'
                            if ((self.resp[3] == 'g') and (self.b_g.style.background_color != 'Springgreen')):
                                self.b_g.style.background_color = 'Gold'
                            if ((self.resp[3] == 'h') and (self.b_h.style.background_color != 'Springgreen')):
                                self.b_h.style.background_color = 'Gold'
                            if ((self.resp[3] == 'j') and (self.b_j.style.background_color != 'Springgreen')):
                                self.b_j.style.background_color = 'Gold'
                            if ((self.resp[3] == 'k') and (self.b_k.style.background_color != 'Springgreen')):
                                self.b_k.style.background_color = 'Gold'
                            if ((self.resp[3] == 'l') and (self.b_l.style.background_color != 'Springgreen')):
                                self.b_l.style.background_color = 'Gold'
                            if ((self.resp[3] == 'ç') and (self.b_cdl.style.background_color != 'Springgreen')):
                                self.b_cdl.style.background_color = 'Gold'
                            if ((self.resp[3] == 'z') and (self.b_z.style.background_color != 'Springgreen')):
                                self.b_z.style.background_color = 'Gold'
                            if ((self.resp[3] == 'x') and (self.b_x.style.background_color != 'Springgreen')):
                                self.b_x.style.background_color = 'Gold'
                            if ((self.resp[3] == 'c') and (self.b_c.style.background_color != 'Springgreen')):
                                self.b_c.style.background_color = 'Gold'
                            if ((self.resp[3] == 'v') and (self.b_v.style.background_color != 'Springgreen')):
                                self.b_v.style.background_color = 'Gold'
                            if ((self.resp[3] == 'b') and (self.b_b.style.background_color != 'Springgreen')):
                                self.b_b.style.background_color = 'Gold'
                            if ((self.resp[3] == 'n') and (self.b_n.style.background_color != 'Springgreen')):
                                self.b_n.style.background_color = 'Gold'
                            if ((self.resp[3] == 'm') and (self.b_m.style.background_color != 'Springgreen')):
                                self.b_m.style.background_color = 'Gold'
                        else:
                            if self.resp[3] == 'q':
                                self.b_q.style.background_color = 'Gray'
                            if self.resp[3] == 'w':
                                self.b_w.style.background_color = 'Gray'
                            if self.resp[3] == 'e':
                                self.b_e.style.background_color = 'Gray'
                            if self.resp[3] == 'r':
                                self.b_r.style.background_color = 'Gray'
                            if self.resp[3] == 't':
                                self.b_t.style.background_color = 'Gray'
                            if self.resp[3] == 'y':
                                self.b_y.style.background_color = 'Gray'
                            if self.resp[3] == 'u':
                                self.b_u.style.background_color = 'Gray'
                            if self.resp[3] == 'i':
                                self.b_i.style.background_color = 'Gray'
                            if self.resp[3] == 'o':
                                self.b_o.style.background_color = 'Gray'
                            if self.resp[3] == 'p':
                                self.b_p.style.background_color = 'Gray'
                            if self.resp[3] == 'a':
                                self.b_a.style.background_color = 'Gray'
                            if self.resp[3] == 's':
                                self.b_s.style.background_color = 'Gray'
                            if self.resp[3] == 'd':
                                self.b_d.style.background_color = 'Gray'
                            if self.resp[3] == 'f':
                                self.b_f.style.background_color = 'Gray'
                            if self.resp[3] == 'g':
                                self.b_g.style.background_color = 'Gray'
                            if self.resp[3] == 'h':
                                self.b_h.style.background_color = 'Gray'
                            if self.resp[3] == 'j':
                                self.b_j.style.background_color = 'Gray'
                            if self.resp[3] == 'k':
                                self.b_k.style.background_color = 'Gray'
                            if self.resp[3] == 'l':
                                self.b_l.style.background_color = 'Gray'
                            if self.resp[3] == 'ç':
                                self.b_cdl.style.background_color = 'Gray'
                            if self.resp[3] == 'z':
                                self.b_z.style.background_color = 'Gray'
                            if self.resp[3] == 'x':
                                self.b_x.style.background_color = 'Gray'
                            if self.resp[3] == 'c':
                                self.b_c.style.background_color = 'Gray'
                            if self.resp[3] == 'v':
                                self.b_v.style.background_color = 'Gray'
                            if self.resp[3] == 'b':
                                self.b_b.style.background_color = 'Gray'
                            if self.resp[3] == 'n':
                                self.b_n.style.background_color = 'Gray'
                            if self.resp[3] == 'm':
                                self.b_m.style.background_color = 'Gray'

                    if self.resp[4] == termo_play[4]:
                        self.output25.text = '' + termo_play_Acento[4].upper()
                        self.letra_o4.style.background_color = 'Springgreen'
                        if self.resp[4] == 'q':
                            self.b_q.style.background_color = 'Springgreen'
                        if self.resp[4] == 'w':
                            self.b_w.style.background_color = 'Springgreen'
                        if self.resp[4] == 'e':
                            self.b_e.style.background_color = 'Springgreen'
                        if self.resp[4] == 'r':
                            self.b_r.style.background_color = 'Springgreen'
                        if self.resp[4] == 't':
                            self.b_t.style.background_color = 'Springgreen'
                        if self.resp[4] == 'y':
                            self.b_y.style.background_color = 'Springgreen'
                        if self.resp[4] == 'u':
                            self.b_u.style.background_color = 'Springgreen'
                        if self.resp[4] == 'i':
                            self.b_i.style.background_color = 'Springgreen'
                        if self.resp[4] == 'o':
                            self.b_o.style.background_color = 'Springgreen'
                        if self.resp[4] == 'p':
                            self.b_p.style.background_color = 'Springgreen'
                        if self.resp[4] == 'a':
                            self.b_a.style.background_color = 'Springgreen'
                        if self.resp[4] == 's':
                            self.b_s.style.background_color = 'Springgreen'
                        if self.resp[4] == 'd':
                            self.b_d.style.background_color = 'Springgreen'
                        if self.resp[4] == 'f':
                            self.b_f.style.background_color = 'Springgreen'
                        if self.resp[4] == 'g':
                            self.b_g.style.background_color = 'Springgreen'
                        if self.resp[4] == 'h':
                            self.b_h.style.background_color = 'Springgreen'
                        if self.resp[4] == 'j':
                            self.b_j.style.background_color = 'Springgreen'
                        if self.resp[4] == 'k':
                            self.b_k.style.background_color = 'Springgreen'
                        if self.resp[4] == 'l':
                            self.b_l.style.background_color = 'Springgreen'
                        if self.resp[4] == 'ç':
                            self.b_cdl.style.background_color = 'Springgreen'
                        if self.resp[4] == 'z':
                            self.b_z.style.background_color = 'Springgreen'
                        if self.resp[4] == 'x':
                            self.b_x.style.background_color = 'Springgreen'
                        if self.resp[4] == 'c':
                            self.b_c.style.background_color = 'Springgreen'
                        if self.resp[4] == 'v':
                            self.b_v.style.background_color = 'Springgreen'
                        if self.resp[4] == 'b':
                            self.b_b.style.background_color = 'Springgreen'
                        if self.resp[4] == 'n':
                            self.b_n.style.background_color = 'Springgreen'
                        if self.resp[4] == 'm':
                            self.b_m.style.background_color = 'Springgreen'
                    else:
                        if self.resp[4] in termo_play:
                            self.letra_o4.style.background_color = 'Gold'
                            if ((self.resp[4] == 'q') and (self.b_q.style.background_color != 'Springgreen')):
                                self.b_q.style.background_color = 'Gold'
                            if ((self.resp[4] == 'w') and (self.b_w.style.background_color != 'Springgreen')):
                                self.b_w.style.background_color = 'Gold'
                            if ((self.resp[4] == 'e') and (self.b_e.style.background_color != 'Springgreen')):
                                self.b_e.style.background_color = 'Gold'
                            if ((self.resp[4] == 'r') and (self.b_r.style.background_color != 'Springgreen')):
                                self.b_r.style.background_color = 'Gold'
                            if ((self.resp[4] == 't') and (self.b_t.style.background_color != 'Springgreen')):
                                self.b_t.style.background_color = 'Gold'
                            if ((self.resp[4] == 'y') and (self.b_y.style.background_color != 'Springgreen')):
                                self.b_y.style.background_color = 'Gold'
                            if ((self.resp[4] == 'u') and (self.b_u.style.background_color != 'Springgreen')):
                                self.b_u.style.background_color = 'Gold'
                            if ((self.resp[4] == 'i') and (self.b_i.style.background_color != 'Springgreen')):
                                self.b_i.style.background_color = 'Gold'
                            if ((self.resp[4] == 'o') and (self.b_o.style.background_color != 'Springgreen')):
                                self.b_o.style.background_color = 'Gold'
                            if ((self.resp[4] == 'p') and (self.b_p.style.background_color != 'Springgreen')):
                                self.b_p.style.background_color = 'Gold'
                            if ((self.resp[4] == 'a') and (self.b_a.style.background_color != 'Springgreen')):
                                self.b_a.style.background_color = 'Gold'
                            if ((self.resp[4] == 's') and (self.b_s.style.background_color != 'Springgreen')):
                                self.b_s.style.background_color = 'Gold'
                            if ((self.resp[4] == 'd') and (self.b_d.style.background_color != 'Springgreen')):
                                self.b_d.style.background_color = 'Gold'
                            if ((self.resp[4] == 'f') and (self.b_f.style.background_color != 'Springgreen')):
                                self.b_f.style.background_color = 'Gold'
                            if ((self.resp[4] == 'g') and (self.b_g.style.background_color != 'Springgreen')):
                                self.b_g.style.background_color = 'Gold'
                            if ((self.resp[4] == 'h') and (self.b_h.style.background_color != 'Springgreen')):
                                self.b_h.style.background_color = 'Gold'
                            if ((self.resp[4] == 'j') and (self.b_j.style.background_color != 'Springgreen')):
                                self.b_j.style.background_color = 'Gold'
                            if ((self.resp[4] == 'k') and (self.b_k.style.background_color != 'Springgreen')):
                                self.b_k.style.background_color = 'Gold'
                            if ((self.resp[4] == 'l') and (self.b_l.style.background_color != 'Springgreen')):
                                self.b_l.style.background_color = 'Gold'
                            if ((self.resp[4] == 'ç') and (self.b_cdl.style.background_color != 'Springgreen')):
                                self.b_cdl.style.background_color = 'Gold'
                            if ((self.resp[4] == 'z') and (self.b_z.style.background_color != 'Springgreen')):
                                self.b_z.style.background_color = 'Gold'
                            if ((self.resp[4] == 'x') and (self.b_x.style.background_color != 'Springgreen')):
                                self.b_x.style.background_color = 'Gold'
                            if ((self.resp[4] == 'c') and (self.b_c.style.background_color != 'Springgreen')):
                                self.b_c.style.background_color = 'Gold'
                            if ((self.resp[4] == 'v') and (self.b_v.style.background_color != 'Springgreen')):
                                self.b_v.style.background_color = 'Gold'
                            if ((self.resp[4] == 'b') and (self.b_b.style.background_color != 'Springgreen')):
                                self.b_b.style.background_color = 'Gold'
                            if ((self.resp[4] == 'n') and (self.b_n.style.background_color != 'Springgreen')):
                                self.b_n.style.background_color = 'Gold'
                            if ((self.resp[4] == 'm') and (self.b_m.style.background_color != 'Springgreen')):
                                self.b_m.style.background_color = 'Gold'
                        else:
                            if self.resp[4] == 'q':
                                self.b_q.style.background_color = 'Gray'
                            if self.resp[4] == 'w':
                                self.b_w.style.background_color = 'Gray'
                            if self.resp[4] == 'e':
                                self.b_e.style.background_color = 'Gray'
                            if self.resp[4] == 'r':
                                self.b_r.style.background_color = 'Gray'
                            if self.resp[4] == 't':
                                self.b_t.style.background_color = 'Gray'
                            if self.resp[4] == 'y':
                                self.b_y.style.background_color = 'Gray'
                            if self.resp[4] == 'u':
                                self.b_u.style.background_color = 'Gray'
                            if self.resp[4] == 'i':
                                self.b_i.style.background_color = 'Gray'
                            if self.resp[4] == 'o':
                                self.b_o.style.background_color = 'Gray'
                            if self.resp[4] == 'p':
                                self.b_p.style.background_color = 'Gray'
                            if self.resp[4] == 'a':
                                self.b_a.style.background_color = 'Gray'
                            if self.resp[4] == 's':
                                self.b_s.style.background_color = 'Gray'
                            if self.resp[4] == 'd':
                                self.b_d.style.background_color = 'Gray'
                            if self.resp[4] == 'f':
                                self.b_f.style.background_color = 'Gray'
                            if self.resp[4] == 'g':
                                self.b_g.style.background_color = 'Gray'
                            if self.resp[4] == 'h':
                                self.b_h.style.background_color = 'Gray'
                            if self.resp[4] == 'j':
                                self.b_j.style.background_color = 'Gray'
                            if self.resp[4] == 'k':
                                self.b_k.style.background_color = 'Gray'
                            if self.resp[4] == 'l':
                                self.b_l.style.background_color = 'Gray'
                            if self.resp[4] == 'ç':
                                self.b_cdl.style.background_color = 'Gray'
                            if self.resp[4] == 'z':
                                self.b_z.style.background_color = 'Gray'
                            if self.resp[4] == 'x':
                                self.b_x.style.background_color = 'Gray'
                            if self.resp[4] == 'c':
                                self.b_c.style.background_color = 'Gray'
                            if self.resp[4] == 'v':
                                self.b_v.style.background_color = 'Gray'
                            if self.resp[4] == 'b':
                                self.b_b.style.background_color = 'Gray'
                            if self.resp[4] == 'n':
                                self.b_n.style.background_color = 'Gray'
                            if self.resp[4] == 'm':
                                self.b_m.style.background_color = 'Gray'
                    self.contador = '5'
                else:
                    self.output21.text = '' + termo_play_Acento[0].upper()
                    self.letra_t4.style.background_color = 'Springgreen'
                    self.output22.text = '' + termo_play_Acento[1].upper()
                    self.letra_e4.style.background_color = 'Springgreen'
                    self.output23.text = '' + termo_play_Acento[2].upper()
                    self.letra_r4.style.background_color = 'Springgreen'
                    self.output24.text = '' + termo_play_Acento[3].upper()
                    self.letra_m4.style.background_color = 'Springgreen'
                    self.output25.text = '' + termo_play_Acento[4].upper()
                    self.letra_o4.style.background_color = 'Springgreen'
                    self.main_window.info_dialog('Você Ganhou!', f'{termo_play_Acento.upper()} era a palavra correta 🤩', )
                self.resposta = ''
                return 0
            else:
                if (self.contador == '4'):
                    self.main_window.info_dialog('Palavra inexistente!', 'A palavra digitada não é aceita 😒')
                    return 0

            if ((self.contador == '5') and (self.resposta in palavras_5char_existentes)):
                if (self.resposta != termo_play):
                    if self.resp[0] == termo_play[0]:
                        self.output26.text = '' + termo_play_Acento[0].upper()
                        self.letra_t5.style.background_color = 'Springgreen'
                        if self.resp[0] == 'q':
                            self.b_q.style.background_color = 'Springgreen'
                        if self.resp[0] == 'w':
                            self.b_w.style.background_color = 'Springgreen'
                        if self.resp[0] == 'e':
                            self.b_e.style.background_color = 'Springgreen'
                        if self.resp[0] == 'r':
                            self.b_r.style.background_color = 'Springgreen'
                        if self.resp[0] == 't':
                            self.b_t.style.background_color = 'Springgreen'
                        if self.resp[0] == 'y':
                            self.b_y.style.background_color = 'Springgreen'
                        if self.resp[0] == 'u':
                            self.b_u.style.background_color = 'Springgreen'
                        if self.resp[0] == 'i':
                            self.b_i.style.background_color = 'Springgreen'
                        if self.resp[0] == 'o':
                            self.b_o.style.background_color = 'Springgreen'
                        if self.resp[0] == 'p':
                            self.b_p.style.background_color = 'Springgreen'
                        if self.resp[0] == 'a':
                            self.b_a.style.background_color = 'Springgreen'
                        if self.resp[0] == 's':
                            self.b_s.style.background_color = 'Springgreen'
                        if self.resp[0] == 'd':
                            self.b_d.style.background_color = 'Springgreen'
                        if self.resp[0] == 'f':
                            self.b_f.style.background_color = 'Springgreen'
                        if self.resp[0] == 'g':
                            self.b_g.style.background_color = 'Springgreen'
                        if self.resp[0] == 'h':
                            self.b_h.style.background_color = 'Springgreen'
                        if self.resp[0] == 'j':
                            self.b_j.style.background_color = 'Springgreen'
                        if self.resp[0] == 'k':
                            self.b_k.style.background_color = 'Springgreen'
                        if self.resp[0] == 'l':
                            self.b_l.style.background_color = 'Springgreen'
                        if self.resp[0] == 'ç':
                            self.b_cdl.style.background_color = 'Springgreen'
                        if self.resp[0] == 'z':
                            self.b_z.style.background_color = 'Springgreen'
                        if self.resp[0] == 'x':
                            self.b_x.style.background_color = 'Springgreen'
                        if self.resp[0] == 'c':
                            self.b_c.style.background_color = 'Springgreen'
                        if self.resp[0] == 'v':
                            self.b_v.style.background_color = 'Springgreen'
                        if self.resp[0] == 'b':
                            self.b_b.style.background_color = 'Springgreen'
                        if self.resp[0] == 'n':
                            self.b_n.style.background_color = 'Springgreen'
                        if self.resp[0] == 'm':
                            self.b_m.style.background_color = 'Springgreen'
                    else:
                        if self.resp[0] in termo_play:
                            self.letra_t5.style.background_color = 'Gold'
                            if ((self.resp[0] == 'q') and (self.b_q.style.background_color != 'Springgreen')):
                                self.b_q.style.background_color = 'Gold'
                            if ((self.resp[0] == 'w') and (self.b_w.style.background_color != 'Springgreen')):
                                self.b_w.style.background_color = 'Gold'
                            if ((self.resp[0] == 'e') and (self.b_e.style.background_color != 'Springgreen')):
                                self.b_e.style.background_color = 'Gold'
                            if ((self.resp[0] == 'r') and (self.b_r.style.background_color != 'Springgreen')):
                                self.b_r.style.background_color = 'Gold'
                            if ((self.resp[0] == 't') and (self.b_t.style.background_color != 'Springgreen')):
                                self.b_t.style.background_color = 'Gold'
                            if ((self.resp[0] == 'y') and (self.b_y.style.background_color != 'Springgreen')):
                                self.b_y.style.background_color = 'Gold'
                            if ((self.resp[0] == 'u') and (self.b_u.style.background_color != 'Springgreen')):
                                self.b_u.style.background_color = 'Gold'
                            if ((self.resp[0] == 'i') and (self.b_i.style.background_color != 'Springgreen')):
                                self.b_i.style.background_color = 'Gold'
                            if ((self.resp[0] == 'o') and (self.b_o.style.background_color != 'Springgreen')):
                                self.b_o.style.background_color = 'Gold'
                            if ((self.resp[0] == 'p') and (self.b_p.style.background_color != 'Springgreen')):
                                self.b_p.style.background_color = 'Gold'
                            if ((self.resp[0] == 'a') and (self.b_a.style.background_color != 'Springgreen')):
                                self.b_a.style.background_color = 'Gold'
                            if ((self.resp[0] == 's') and (self.b_s.style.background_color != 'Springgreen')):
                                self.b_s.style.background_color = 'Gold'
                            if ((self.resp[0] == 'd') and (self.b_d.style.background_color != 'Springgreen')):
                                self.b_d.style.background_color = 'Gold'
                            if ((self.resp[0] == 'f') and (self.b_f.style.background_color != 'Springgreen')):
                                self.b_f.style.background_color = 'Gold'
                            if ((self.resp[0] == 'g') and (self.b_g.style.background_color != 'Springgreen')):
                                self.b_g.style.background_color = 'Gold'
                            if ((self.resp[0] == 'h') and (self.b_h.style.background_color != 'Springgreen')):
                                self.b_h.style.background_color = 'Gold'
                            if ((self.resp[0] == 'j') and (self.b_j.style.background_color != 'Springgreen')):
                                self.b_j.style.background_color = 'Gold'
                            if ((self.resp[0] == 'k') and (self.b_k.style.background_color != 'Springgreen')):
                                self.b_k.style.background_color = 'Gold'
                            if ((self.resp[0] == 'l') and (self.b_l.style.background_color != 'Springgreen')):
                                self.b_l.style.background_color = 'Gold'
                            if ((self.resp[0] == 'ç') and (self.b_cdl.style.background_color != 'Springgreen')):
                                self.b_cdl.style.background_color = 'Gold'
                            if ((self.resp[0] == 'z') and (self.b_z.style.background_color != 'Springgreen')):
                                self.b_z.style.background_color = 'Gold'
                            if ((self.resp[0] == 'x') and (self.b_x.style.background_color != 'Springgreen')):
                                self.b_x.style.background_color = 'Gold'
                            if ((self.resp[0] == 'c') and (self.b_c.style.background_color != 'Springgreen')):
                                self.b_c.style.background_color = 'Gold'
                            if ((self.resp[0] == 'v') and (self.b_v.style.background_color != 'Springgreen')):
                                self.b_v.style.background_color = 'Gold'
                            if ((self.resp[0] == 'b') and (self.b_b.style.background_color != 'Springgreen')):
                                self.b_b.style.background_color = 'Gold'
                            if ((self.resp[0] == 'n') and (self.b_n.style.background_color != 'Springgreen')):
                                self.b_n.style.background_color = 'Gold'
                            if ((self.resp[0] == 'm') and (self.b_m.style.background_color != 'Springgreen')):
                                self.b_m.style.background_color = 'Gold'
                        else:
                            if self.resp[0] == 'q':
                                self.b_q.style.background_color = 'Gray'
                            if self.resp[0] == 'w':
                                self.b_w.style.background_color = 'Gray'
                            if self.resp[0] == 'e':
                                self.b_e.style.background_color = 'Gray'
                            if self.resp[0] == 'r':
                                self.b_r.style.background_color = 'Gray'
                            if self.resp[0] == 't':
                                self.b_t.style.background_color = 'Gray'
                            if self.resp[0] == 'y':
                                self.b_y.style.background_color = 'Gray'
                            if self.resp[0] == 'u':
                                self.b_u.style.background_color = 'Gray'
                            if self.resp[0] == 'i':
                                self.b_i.style.background_color = 'Gray'
                            if self.resp[0] == 'o':
                                self.b_o.style.background_color = 'Gray'
                            if self.resp[0] == 'p':
                                self.b_p.style.background_color = 'Gray'
                            if self.resp[0] == 'a':
                                self.b_a.style.background_color = 'Gray'
                            if self.resp[0] == 's':
                                self.b_s.style.background_color = 'Gray'
                            if self.resp[0] == 'd':
                                self.b_d.style.background_color = 'Gray'
                            if self.resp[0] == 'f':
                                self.b_f.style.background_color = 'Gray'
                            if self.resp[0] == 'g':
                                self.b_g.style.background_color = 'Gray'
                            if self.resp[0] == 'h':
                                self.b_h.style.background_color = 'Gray'
                            if self.resp[0] == 'j':
                                self.b_j.style.background_color = 'Gray'
                            if self.resp[0] == 'k':
                                self.b_k.style.background_color = 'Gray'
                            if self.resp[0] == 'l':
                                self.b_l.style.background_color = 'Gray'
                            if self.resp[0] == 'ç':
                                self.b_cdl.style.background_color = 'Gray'
                            if self.resp[0] == 'z':
                                self.b_z.style.background_color = 'Gray'
                            if self.resp[0] == 'x':
                                self.b_x.style.background_color = 'Gray'
                            if self.resp[0] == 'c':
                                self.b_c.style.background_color = 'Gray'
                            if self.resp[0] == 'v':
                                self.b_v.style.background_color = 'Gray'
                            if self.resp[0] == 'b':
                                self.b_b.style.background_color = 'Gray'
                            if self.resp[0] == 'n':
                                self.b_n.style.background_color = 'Gray'
                            if self.resp[0] == 'm':
                                self.b_m.style.background_color = 'Gray'

                    if self.resp[1] == termo_play[1]:
                        self.output27.text = '' + termo_play_Acento[1].upper()
                        self.letra_e5.style.background_color = 'Springgreen'
                        if self.resp[1] == 'q':
                            self.b_q.style.background_color = 'Springgreen'
                        if self.resp[1] == 'w':
                            self.b_w.style.background_color = 'Springgreen'
                        if self.resp[1] == 'e':
                            self.b_e.style.background_color = 'Springgreen'
                        if self.resp[1] == 'r':
                            self.b_r.style.background_color = 'Springgreen'
                        if self.resp[1] == 't':
                            self.b_t.style.background_color = 'Springgreen'
                        if self.resp[1] == 'y':
                            self.b_y.style.background_color = 'Springgreen'
                        if self.resp[1] == 'u':
                            self.b_u.style.background_color = 'Springgreen'
                        if self.resp[1] == 'i':
                            self.b_i.style.background_color = 'Springgreen'
                        if self.resp[1] == 'o':
                            self.b_o.style.background_color = 'Springgreen'
                        if self.resp[1] == 'p':
                            self.b_p.style.background_color = 'Springgreen'
                        if self.resp[1] == 'a':
                            self.b_a.style.background_color = 'Springgreen'
                        if self.resp[1] == 's':
                            self.b_s.style.background_color = 'Springgreen'
                        if self.resp[1] == 'd':
                            self.b_d.style.background_color = 'Springgreen'
                        if self.resp[1] == 'f':
                            self.b_f.style.background_color = 'Springgreen'
                        if self.resp[1] == 'g':
                            self.b_g.style.background_color = 'Springgreen'
                        if self.resp[1] == 'h':
                            self.b_h.style.background_color = 'Springgreen'
                        if self.resp[1] == 'j':
                            self.b_j.style.background_color = 'Springgreen'
                        if self.resp[1] == 'k':
                            self.b_k.style.background_color = 'Springgreen'
                        if self.resp[1] == 'l':
                            self.b_l.style.background_color = 'Springgreen'
                        if self.resp[1] == 'ç':
                            self.b_cdl.style.background_color = 'Springgreen'
                        if self.resp[1] == 'z':
                            self.b_z.style.background_color = 'Springgreen'
                        if self.resp[1] == 'x':
                            self.b_x.style.background_color = 'Springgreen'
                        if self.resp[1] == 'c':
                            self.b_c.style.background_color = 'Springgreen'
                        if self.resp[1] == 'v':
                            self.b_v.style.background_color = 'Springgreen'
                        if self.resp[1] == 'b':
                            self.b_b.style.background_color = 'Springgreen'
                        if self.resp[1] == 'n':
                            self.b_n.style.background_color = 'Springgreen'
                        if self.resp[1] == 'm':
                            self.b_m.style.background_color = 'Springgreen'
                    else:
                        if self.resp[1] in termo_play:
                            self.letra_e5.style.background_color = 'Gold'
                            if ((self.resp[1] == 'q') and (self.b_q.style.background_color != 'Springgreen')):
                                self.b_q.style.background_color = 'Gold'
                            if ((self.resp[1] == 'w') and (self.b_w.style.background_color != 'Springgreen')):
                                self.b_w.style.background_color = 'Gold'
                            if ((self.resp[1] == 'e') and (self.b_e.style.background_color != 'Springgreen')):
                                self.b_e.style.background_color = 'Gold'
                            if ((self.resp[1] == 'r') and (self.b_r.style.background_color != 'Springgreen')):
                                self.b_r.style.background_color = 'Gold'
                            if ((self.resp[1] == 't') and (self.b_t.style.background_color != 'Springgreen')):
                                self.b_t.style.background_color = 'Gold'
                            if ((self.resp[1] == 'y') and (self.b_y.style.background_color != 'Springgreen')):
                                self.b_y.style.background_color = 'Gold'
                            if ((self.resp[1] == 'u') and (self.b_u.style.background_color != 'Springgreen')):
                                self.b_u.style.background_color = 'Gold'
                            if ((self.resp[1] == 'i') and (self.b_i.style.background_color != 'Springgreen')):
                                self.b_i.style.background_color = 'Gold'
                            if ((self.resp[1] == 'o') and (self.b_o.style.background_color != 'Springgreen')):
                                self.b_o.style.background_color = 'Gold'
                            if ((self.resp[1] == 'p') and (self.b_p.style.background_color != 'Springgreen')):
                                self.b_p.style.background_color = 'Gold'
                            if ((self.resp[1] == 'a') and (self.b_a.style.background_color != 'Springgreen')):
                                self.b_a.style.background_color = 'Gold'
                            if ((self.resp[1] == 's') and (self.b_s.style.background_color != 'Springgreen')):
                                self.b_s.style.background_color = 'Gold'
                            if ((self.resp[1] == 'd') and (self.b_d.style.background_color != 'Springgreen')):
                                self.b_d.style.background_color = 'Gold'
                            if ((self.resp[1] == 'f') and (self.b_f.style.background_color != 'Springgreen')):
                                self.b_f.style.background_color = 'Gold'
                            if ((self.resp[1] == 'g') and (self.b_g.style.background_color != 'Springgreen')):
                                self.b_g.style.background_color = 'Gold'
                            if ((self.resp[1] == 'h') and (self.b_h.style.background_color != 'Springgreen')):
                                self.b_h.style.background_color = 'Gold'
                            if ((self.resp[1] == 'j') and (self.b_j.style.background_color != 'Springgreen')):
                                self.b_j.style.background_color = 'Gold'
                            if ((self.resp[1] == 'k') and (self.b_k.style.background_color != 'Springgreen')):
                                self.b_k.style.background_color = 'Gold'
                            if ((self.resp[1] == 'l') and (self.b_l.style.background_color != 'Springgreen')):
                                self.b_l.style.background_color = 'Gold'
                            if ((self.resp[1] == 'ç') and (self.b_cdl.style.background_color != 'Springgreen')):
                                self.b_cdl.style.background_color = 'Gold'
                            if ((self.resp[1] == 'z') and (self.b_z.style.background_color != 'Springgreen')):
                                self.b_z.style.background_color = 'Gold'
                            if ((self.resp[1] == 'x') and (self.b_x.style.background_color != 'Springgreen')):
                                self.b_x.style.background_color = 'Gold'
                            if ((self.resp[1] == 'c') and (self.b_c.style.background_color != 'Springgreen')):
                                self.b_c.style.background_color = 'Gold'
                            if ((self.resp[1] == 'v') and (self.b_v.style.background_color != 'Springgreen')):
                                self.b_v.style.background_color = 'Gold'
                            if ((self.resp[1] == 'b') and (self.b_b.style.background_color != 'Springgreen')):
                                self.b_b.style.background_color = 'Gold'
                            if ((self.resp[1] == 'n') and (self.b_n.style.background_color != 'Springgreen')):
                                self.b_n.style.background_color = 'Gold'
                            if ((self.resp[1] == 'm') and (self.b_m.style.background_color != 'Springgreen')):
                                self.b_m.style.background_color = 'Gold'
                        else:
                            if self.resp[1] == 'q':
                                self.b_q.style.background_color = 'Gray'
                            if self.resp[1] == 'w':
                                self.b_w.style.background_color = 'Gray'
                            if self.resp[1] == 'e':
                                self.b_e.style.background_color = 'Gray'
                            if self.resp[1] == 'r':
                                self.b_r.style.background_color = 'Gray'
                            if self.resp[1] == 't':
                                self.b_t.style.background_color = 'Gray'
                            if self.resp[1] == 'y':
                                self.b_y.style.background_color = 'Gray'
                            if self.resp[1] == 'u':
                                self.b_u.style.background_color = 'Gray'
                            if self.resp[1] == 'i':
                                self.b_i.style.background_color = 'Gray'
                            if self.resp[1] == 'o':
                                self.b_o.style.background_color = 'Gray'
                            if self.resp[1] == 'p':
                                self.b_p.style.background_color = 'Gray'
                            if self.resp[1] == 'a':
                                self.b_a.style.background_color = 'Gray'
                            if self.resp[1] == 's':
                                self.b_s.style.background_color = 'Gray'
                            if self.resp[1] == 'd':
                                self.b_d.style.background_color = 'Gray'
                            if self.resp[1] == 'f':
                                self.b_f.style.background_color = 'Gray'
                            if self.resp[1] == 'g':
                                self.b_g.style.background_color = 'Gray'
                            if self.resp[1] == 'h':
                                self.b_h.style.background_color = 'Gray'
                            if self.resp[1] == 'j':
                                self.b_j.style.background_color = 'Gray'
                            if self.resp[1] == 'k':
                                self.b_k.style.background_color = 'Gray'
                            if self.resp[1] == 'l':
                                self.b_l.style.background_color = 'Gray'
                            if self.resp[1] == 'ç':
                                self.b_cdl.style.background_color = 'Gray'
                            if self.resp[1] == 'z':
                                self.b_z.style.background_color = 'Gray'
                            if self.resp[1] == 'x':
                                self.b_x.style.background_color = 'Gray'
                            if self.resp[1] == 'c':
                                self.b_c.style.background_color = 'Gray'
                            if self.resp[1] == 'v':
                                self.b_v.style.background_color = 'Gray'
                            if self.resp[1] == 'b':
                                self.b_b.style.background_color = 'Gray'
                            if self.resp[1] == 'n':
                                self.b_n.style.background_color = 'Gray'
                            if self.resp[1] == 'm':
                                self.b_m.style.background_color = 'Gray'

                    if self.resp[2] == termo_play[2]:
                        self.output28.text = '' + termo_play_Acento[2].upper()
                        self.letra_r5.style.background_color = 'Springgreen'
                        if self.resp[2] == 'q':
                            self.b_q.style.background_color = 'Springgreen'
                        if self.resp[2] == 'w':
                            self.b_w.style.background_color = 'Springgreen'
                        if self.resp[2] == 'e':
                            self.b_e.style.background_color = 'Springgreen'
                        if self.resp[2] == 'r':
                            self.b_r.style.background_color = 'Springgreen'
                        if self.resp[2] == 't':
                            self.b_t.style.background_color = 'Springgreen'
                        if self.resp[2] == 'y':
                            self.b_y.style.background_color = 'Springgreen'
                        if self.resp[2] == 'u':
                            self.b_u.style.background_color = 'Springgreen'
                        if self.resp[2] == 'i':
                            self.b_i.style.background_color = 'Springgreen'
                        if self.resp[2] == 'o':
                            self.b_o.style.background_color = 'Springgreen'
                        if self.resp[2] == 'p':
                            self.b_p.style.background_color = 'Springgreen'
                        if self.resp[2] == 'a':
                            self.b_a.style.background_color = 'Springgreen'
                        if self.resp[2] == 's':
                            self.b_s.style.background_color = 'Springgreen'
                        if self.resp[2] == 'd':
                            self.b_d.style.background_color = 'Springgreen'
                        if self.resp[2] == 'f':
                            self.b_f.style.background_color = 'Springgreen'
                        if self.resp[2] == 'g':
                            self.b_g.style.background_color = 'Springgreen'
                        if self.resp[2] == 'h':
                            self.b_h.style.background_color = 'Springgreen'
                        if self.resp[2] == 'j':
                            self.b_j.style.background_color = 'Springgreen'
                        if self.resp[2] == 'k':
                            self.b_k.style.background_color = 'Springgreen'
                        if self.resp[2] == 'l':
                            self.b_l.style.background_color = 'Springgreen'
                        if self.resp[2] == 'ç':
                            self.b_cdl.style.background_color = 'Springgreen'
                        if self.resp[2] == 'z':
                            self.b_z.style.background_color = 'Springgreen'
                        if self.resp[2] == 'x':
                            self.b_x.style.background_color = 'Springgreen'
                        if self.resp[2] == 'c':
                            self.b_c.style.background_color = 'Springgreen'
                        if self.resp[2] == 'v':
                            self.b_v.style.background_color = 'Springgreen'
                        if self.resp[2] == 'b':
                            self.b_b.style.background_color = 'Springgreen'
                        if self.resp[2] == 'n':
                            self.b_n.style.background_color = 'Springgreen'
                        if self.resp[2] == 'm':
                            self.b_m.style.background_color = 'Springgreen'
                    else:
                        if self.resp[2] in termo_play:
                            self.letra_r5.style.background_color = 'Gold'
                            if ((self.resp[2] == 'q') and (self.b_q.style.background_color != 'Springgreen')):
                                self.b_q.style.background_color = 'Gold'
                            if ((self.resp[2] == 'w') and (self.b_w.style.background_color != 'Springgreen')):
                                self.b_w.style.background_color = 'Gold'
                            if ((self.resp[2] == 'e') and (self.b_e.style.background_color != 'Springgreen')):
                                self.b_e.style.background_color = 'Gold'
                            if ((self.resp[2] == 'r') and (self.b_r.style.background_color != 'Springgreen')):
                                self.b_r.style.background_color = 'Gold'
                            if ((self.resp[2] == 't') and (self.b_t.style.background_color != 'Springgreen')):
                                self.b_t.style.background_color = 'Gold'
                            if ((self.resp[2] == 'y') and (self.b_y.style.background_color != 'Springgreen')):
                                self.b_y.style.background_color = 'Gold'
                            if ((self.resp[2] == 'u') and (self.b_u.style.background_color != 'Springgreen')):
                                self.b_u.style.background_color = 'Gold'
                            if ((self.resp[2] == 'i') and (self.b_i.style.background_color != 'Springgreen')):
                                self.b_i.style.background_color = 'Gold'
                            if ((self.resp[2] == 'o') and (self.b_o.style.background_color != 'Springgreen')):
                                self.b_o.style.background_color = 'Gold'
                            if ((self.resp[2] == 'p') and (self.b_p.style.background_color != 'Springgreen')):
                                self.b_p.style.background_color = 'Gold'
                            if ((self.resp[2] == 'a') and (self.b_a.style.background_color != 'Springgreen')):
                                self.b_a.style.background_color = 'Gold'
                            if ((self.resp[2] == 's') and (self.b_s.style.background_color != 'Springgreen')):
                                self.b_s.style.background_color = 'Gold'
                            if ((self.resp[2] == 'd') and (self.b_d.style.background_color != 'Springgreen')):
                                self.b_d.style.background_color = 'Gold'
                            if ((self.resp[2] == 'f') and (self.b_f.style.background_color != 'Springgreen')):
                                self.b_f.style.background_color = 'Gold'
                            if ((self.resp[2] == 'g') and (self.b_g.style.background_color != 'Springgreen')):
                                self.b_g.style.background_color = 'Gold'
                            if ((self.resp[2] == 'h') and (self.b_h.style.background_color != 'Springgreen')):
                                self.b_h.style.background_color = 'Gold'
                            if ((self.resp[2] == 'j') and (self.b_j.style.background_color != 'Springgreen')):
                                self.b_j.style.background_color = 'Gold'
                            if ((self.resp[2] == 'k') and (self.b_k.style.background_color != 'Springgreen')):
                                self.b_k.style.background_color = 'Gold'
                            if ((self.resp[2] == 'l') and (self.b_l.style.background_color != 'Springgreen')):
                                self.b_l.style.background_color = 'Gold'
                            if ((self.resp[2] == 'ç') and (self.b_cdl.style.background_color != 'Springgreen')):
                                self.b_cdl.style.background_color = 'Gold'
                            if ((self.resp[2] == 'z') and (self.b_z.style.background_color != 'Springgreen')):
                                self.b_z.style.background_color = 'Gold'
                            if ((self.resp[2] == 'x') and (self.b_x.style.background_color != 'Springgreen')):
                                self.b_x.style.background_color = 'Gold'
                            if ((self.resp[2] == 'c') and (self.b_c.style.background_color != 'Springgreen')):
                                self.b_c.style.background_color = 'Gold'
                            if ((self.resp[2] == 'v') and (self.b_v.style.background_color != 'Springgreen')):
                                self.b_v.style.background_color = 'Gold'
                            if ((self.resp[2] == 'b') and (self.b_b.style.background_color != 'Springgreen')):
                                self.b_b.style.background_color = 'Gold'
                            if ((self.resp[2] == 'n') and (self.b_n.style.background_color != 'Springgreen')):
                                self.b_n.style.background_color = 'Gold'
                            if ((self.resp[2] == 'm') and (self.b_m.style.background_color != 'Springgreen')):
                                self.b_m.style.background_color = 'Gold'
                        else:
                            if self.resp[2] == 'q':
                                self.b_q.style.background_color = 'Gray'
                            if self.resp[2] == 'w':
                                self.b_w.style.background_color = 'Gray'
                            if self.resp[2] == 'e':
                                self.b_e.style.background_color = 'Gray'
                            if self.resp[2] == 'r':
                                self.b_r.style.background_color = 'Gray'
                            if self.resp[2] == 't':
                                self.b_t.style.background_color = 'Gray'
                            if self.resp[2] == 'y':
                                self.b_y.style.background_color = 'Gray'
                            if self.resp[2] == 'u':
                                self.b_u.style.background_color = 'Gray'
                            if self.resp[2] == 'i':
                                self.b_i.style.background_color = 'Gray'
                            if self.resp[2] == 'o':
                                self.b_o.style.background_color = 'Gray'
                            if self.resp[2] == 'p':
                                self.b_p.style.background_color = 'Gray'
                            if self.resp[2] == 'a':
                                self.b_a.style.background_color = 'Gray'
                            if self.resp[2] == 's':
                                self.b_s.style.background_color = 'Gray'
                            if self.resp[2] == 'd':
                                self.b_d.style.background_color = 'Gray'
                            if self.resp[2] == 'f':
                                self.b_f.style.background_color = 'Gray'
                            if self.resp[2] == 'g':
                                self.b_g.style.background_color = 'Gray'
                            if self.resp[2] == 'h':
                                self.b_h.style.background_color = 'Gray'
                            if self.resp[2] == 'j':
                                self.b_j.style.background_color = 'Gray'
                            if self.resp[2] == 'k':
                                self.b_k.style.background_color = 'Gray'
                            if self.resp[2] == 'l':
                                self.b_l.style.background_color = 'Gray'
                            if self.resp[2] == 'ç':
                                self.b_cdl.style.background_color = 'Gray'
                            if self.resp[2] == 'z':
                                self.b_z.style.background_color = 'Gray'
                            if self.resp[2] == 'x':
                                self.b_x.style.background_color = 'Gray'
                            if self.resp[2] == 'c':
                                self.b_c.style.background_color = 'Gray'
                            if self.resp[2] == 'v':
                                self.b_v.style.background_color = 'Gray'
                            if self.resp[2] == 'b':
                                self.b_b.style.background_color = 'Gray'
                            if self.resp[2] == 'n':
                                self.b_n.style.background_color = 'Gray'
                            if self.resp[2] == 'm':
                                self.b_m.style.background_color = 'Gray'

                    if self.resp[3] == termo_play[3]:
                        self.output29.text = '' + termo_play_Acento[3].upper()
                        self.letra_m5.style.background_color = 'Springgreen'
                        if self.resp[3] == 'q':
                            self.b_q.style.background_color = 'Springgreen'
                        if self.resp[3] == 'w':
                            self.b_w.style.background_color = 'Springgreen'
                        if self.resp[3] == 'e':
                            self.b_e.style.background_color = 'Springgreen'
                        if self.resp[3] == 'r':
                            self.b_r.style.background_color = 'Springgreen'
                        if self.resp[3] == 't':
                            self.b_t.style.background_color = 'Springgreen'
                        if self.resp[3] == 'y':
                            self.b_y.style.background_color = 'Springgreen'
                        if self.resp[3] == 'u':
                            self.b_u.style.background_color = 'Springgreen'
                        if self.resp[3] == 'i':
                            self.b_i.style.background_color = 'Springgreen'
                        if self.resp[3] == 'o':
                            self.b_o.style.background_color = 'Springgreen'
                        if self.resp[3] == 'p':
                            self.b_p.style.background_color = 'Springgreen'
                        if self.resp[3] == 'a':
                            self.b_a.style.background_color = 'Springgreen'
                        if self.resp[3] == 's':
                            self.b_s.style.background_color = 'Springgreen'
                        if self.resp[3] == 'd':
                            self.b_d.style.background_color = 'Springgreen'
                        if self.resp[3] == 'f':
                            self.b_f.style.background_color = 'Springgreen'
                        if self.resp[3] == 'g':
                            self.b_g.style.background_color = 'Springgreen'
                        if self.resp[3] == 'h':
                            self.b_h.style.background_color = 'Springgreen'
                        if self.resp[3] == 'j':
                            self.b_j.style.background_color = 'Springgreen'
                        if self.resp[3] == 'k':
                            self.b_k.style.background_color = 'Springgreen'
                        if self.resp[3] == 'l':
                            self.b_l.style.background_color = 'Springgreen'
                        if self.resp[3] == 'ç':
                            self.b_cdl.style.background_color = 'Springgreen'
                        if self.resp[3] == 'z':
                            self.b_z.style.background_color = 'Springgreen'
                        if self.resp[3] == 'x':
                            self.b_x.style.background_color = 'Springgreen'
                        if self.resp[3] == 'c':
                            self.b_c.style.background_color = 'Springgreen'
                        if self.resp[3] == 'v':
                            self.b_v.style.background_color = 'Springgreen'
                        if self.resp[3] == 'b':
                            self.b_b.style.background_color = 'Springgreen'
                        if self.resp[3] == 'n':
                            self.b_n.style.background_color = 'Springgreen'
                        if self.resp[3] == 'm':
                            self.b_m.style.background_color = 'Springgreen'
                    else:
                        if self.resp[3] in termo_play:
                            self.letra_m5.style.background_color = 'Gold'
                            if ((self.resp[3] == 'q') and (self.b_q.style.background_color != 'Springgreen')):
                                self.b_q.style.background_color = 'Gold'
                            if ((self.resp[3] == 'w') and (self.b_w.style.background_color != 'Springgreen')):
                                self.b_w.style.background_color = 'Gold'
                            if ((self.resp[3] == 'e') and (self.b_e.style.background_color != 'Springgreen')):
                                self.b_e.style.background_color = 'Gold'
                            if ((self.resp[3] == 'r') and (self.b_r.style.background_color != 'Springgreen')):
                                self.b_r.style.background_color = 'Gold'
                            if ((self.resp[3] == 't') and (self.b_t.style.background_color != 'Springgreen')):
                                self.b_t.style.background_color = 'Gold'
                            if ((self.resp[3] == 'y') and (self.b_y.style.background_color != 'Springgreen')):
                                self.b_y.style.background_color = 'Gold'
                            if ((self.resp[3] == 'u') and (self.b_u.style.background_color != 'Springgreen')):
                                self.b_u.style.background_color = 'Gold'
                            if ((self.resp[3] == 'i') and (self.b_i.style.background_color != 'Springgreen')):
                                self.b_i.style.background_color = 'Gold'
                            if ((self.resp[3] == 'o') and (self.b_o.style.background_color != 'Springgreen')):
                                self.b_o.style.background_color = 'Gold'
                            if ((self.resp[3] == 'p') and (self.b_p.style.background_color != 'Springgreen')):
                                self.b_p.style.background_color = 'Gold'
                            if ((self.resp[3] == 'a') and (self.b_a.style.background_color != 'Springgreen')):
                                self.b_a.style.background_color = 'Gold'
                            if ((self.resp[3] == 's') and (self.b_s.style.background_color != 'Springgreen')):
                                self.b_s.style.background_color = 'Gold'
                            if ((self.resp[3] == 'd') and (self.b_d.style.background_color != 'Springgreen')):
                                self.b_d.style.background_color = 'Gold'
                            if ((self.resp[3] == 'f') and (self.b_f.style.background_color != 'Springgreen')):
                                self.b_f.style.background_color = 'Gold'
                            if ((self.resp[3] == 'g') and (self.b_g.style.background_color != 'Springgreen')):
                                self.b_g.style.background_color = 'Gold'
                            if ((self.resp[3] == 'h') and (self.b_h.style.background_color != 'Springgreen')):
                                self.b_h.style.background_color = 'Gold'
                            if ((self.resp[3] == 'j') and (self.b_j.style.background_color != 'Springgreen')):
                                self.b_j.style.background_color = 'Gold'
                            if ((self.resp[3] == 'k') and (self.b_k.style.background_color != 'Springgreen')):
                                self.b_k.style.background_color = 'Gold'
                            if ((self.resp[3] == 'l') and (self.b_l.style.background_color != 'Springgreen')):
                                self.b_l.style.background_color = 'Gold'
                            if ((self.resp[3] == 'ç') and (self.b_cdl.style.background_color != 'Springgreen')):
                                self.b_cdl.style.background_color = 'Gold'
                            if ((self.resp[3] == 'z') and (self.b_z.style.background_color != 'Springgreen')):
                                self.b_z.style.background_color = 'Gold'
                            if ((self.resp[3] == 'x') and (self.b_x.style.background_color != 'Springgreen')):
                                self.b_x.style.background_color = 'Gold'
                            if ((self.resp[3] == 'c') and (self.b_c.style.background_color != 'Springgreen')):
                                self.b_c.style.background_color = 'Gold'
                            if ((self.resp[3] == 'v') and (self.b_v.style.background_color != 'Springgreen')):
                                self.b_v.style.background_color = 'Gold'
                            if ((self.resp[3] == 'b') and (self.b_b.style.background_color != 'Springgreen')):
                                self.b_b.style.background_color = 'Gold'
                            if ((self.resp[3] == 'n') and (self.b_n.style.background_color != 'Springgreen')):
                                self.b_n.style.background_color = 'Gold'
                            if ((self.resp[3] == 'm') and (self.b_m.style.background_color != 'Springgreen')):
                                self.b_m.style.background_color = 'Gold'
                        else:
                            if self.resp[3] == 'q':
                                self.b_q.style.background_color = 'Gray'
                            if self.resp[3] == 'w':
                                self.b_w.style.background_color = 'Gray'
                            if self.resp[3] == 'e':
                                self.b_e.style.background_color = 'Gray'
                            if self.resp[3] == 'r':
                                self.b_r.style.background_color = 'Gray'
                            if self.resp[3] == 't':
                                self.b_t.style.background_color = 'Gray'
                            if self.resp[3] == 'y':
                                self.b_y.style.background_color = 'Gray'
                            if self.resp[3] == 'u':
                                self.b_u.style.background_color = 'Gray'
                            if self.resp[3] == 'i':
                                self.b_i.style.background_color = 'Gray'
                            if self.resp[3] == 'o':
                                self.b_o.style.background_color = 'Gray'
                            if self.resp[3] == 'p':
                                self.b_p.style.background_color = 'Gray'
                            if self.resp[3] == 'a':
                                self.b_a.style.background_color = 'Gray'
                            if self.resp[3] == 's':
                                self.b_s.style.background_color = 'Gray'
                            if self.resp[3] == 'd':
                                self.b_d.style.background_color = 'Gray'
                            if self.resp[3] == 'f':
                                self.b_f.style.background_color = 'Gray'
                            if self.resp[3] == 'g':
                                self.b_g.style.background_color = 'Gray'
                            if self.resp[3] == 'h':
                                self.b_h.style.background_color = 'Gray'
                            if self.resp[3] == 'j':
                                self.b_j.style.background_color = 'Gray'
                            if self.resp[3] == 'k':
                                self.b_k.style.background_color = 'Gray'
                            if self.resp[3] == 'l':
                                self.b_l.style.background_color = 'Gray'
                            if self.resp[3] == 'ç':
                                self.b_cdl.style.background_color = 'Gray'
                            if self.resp[3] == 'z':
                                self.b_z.style.background_color = 'Gray'
                            if self.resp[3] == 'x':
                                self.b_x.style.background_color = 'Gray'
                            if self.resp[3] == 'c':
                                self.b_c.style.background_color = 'Gray'
                            if self.resp[3] == 'v':
                                self.b_v.style.background_color = 'Gray'
                            if self.resp[3] == 'b':
                                self.b_b.style.background_color = 'Gray'
                            if self.resp[3] == 'n':
                                self.b_n.style.background_color = 'Gray'
                            if self.resp[3] == 'm':
                                self.b_m.style.background_color = 'Gray'

                    if self.resp[4] == termo_play[4]:
                        self.output30.text = '' + termo_play_Acento[4].upper()
                        self.letra_o5.style.background_color = 'Springgreen'
                        if self.resp[4] == 'q':
                            self.b_q.style.background_color = 'Springgreen'
                        if self.resp[4] == 'w':
                            self.b_w.style.background_color = 'Springgreen'
                        if self.resp[4] == 'e':
                            self.b_e.style.background_color = 'Springgreen'
                        if self.resp[4] == 'r':
                            self.b_r.style.background_color = 'Springgreen'
                        if self.resp[4] == 't':
                            self.b_t.style.background_color = 'Springgreen'
                        if self.resp[4] == 'y':
                            self.b_y.style.background_color = 'Springgreen'
                        if self.resp[4] == 'u':
                            self.b_u.style.background_color = 'Springgreen'
                        if self.resp[4] == 'i':
                            self.b_i.style.background_color = 'Springgreen'
                        if self.resp[4] == 'o':
                            self.b_o.style.background_color = 'Springgreen'
                        if self.resp[4] == 'p':
                            self.b_p.style.background_color = 'Springgreen'
                        if self.resp[4] == 'a':
                            self.b_a.style.background_color = 'Springgreen'
                        if self.resp[4] == 's':
                            self.b_s.style.background_color = 'Springgreen'
                        if self.resp[4] == 'd':
                            self.b_d.style.background_color = 'Springgreen'
                        if self.resp[4] == 'f':
                            self.b_f.style.background_color = 'Springgreen'
                        if self.resp[4] == 'g':
                            self.b_g.style.background_color = 'Springgreen'
                        if self.resp[4] == 'h':
                            self.b_h.style.background_color = 'Springgreen'
                        if self.resp[4] == 'j':
                            self.b_j.style.background_color = 'Springgreen'
                        if self.resp[4] == 'k':
                            self.b_k.style.background_color = 'Springgreen'
                        if self.resp[4] == 'l':
                            self.b_l.style.background_color = 'Springgreen'
                        if self.resp[4] == 'ç':
                            self.b_cdl.style.background_color = 'Springgreen'
                        if self.resp[4] == 'z':
                            self.b_z.style.background_color = 'Springgreen'
                        if self.resp[4] == 'x':
                            self.b_x.style.background_color = 'Springgreen'
                        if self.resp[4] == 'c':
                            self.b_c.style.background_color = 'Springgreen'
                        if self.resp[4] == 'v':
                            self.b_v.style.background_color = 'Springgreen'
                        if self.resp[4] == 'b':
                            self.b_b.style.background_color = 'Springgreen'
                        if self.resp[4] == 'n':
                            self.b_n.style.background_color = 'Springgreen'
                        if self.resp[4] == 'm':
                            self.b_m.style.background_color = 'Springgreen'
                    else:
                        if self.resp[4] in termo_play:
                            self.letra_o5.style.background_color = 'Gold'
                            if ((self.resp[4] == 'q') and (self.b_q.style.background_color != 'Springgreen')):
                                self.b_q.style.background_color = 'Gold'
                            if ((self.resp[4] == 'w') and (self.b_w.style.background_color != 'Springgreen')):
                                self.b_w.style.background_color = 'Gold'
                            if ((self.resp[4] == 'e') and (self.b_e.style.background_color != 'Springgreen')):
                                self.b_e.style.background_color = 'Gold'
                            if ((self.resp[4] == 'r') and (self.b_r.style.background_color != 'Springgreen')):
                                self.b_r.style.background_color = 'Gold'
                            if ((self.resp[4] == 't') and (self.b_t.style.background_color != 'Springgreen')):
                                self.b_t.style.background_color = 'Gold'
                            if ((self.resp[4] == 'y') and (self.b_y.style.background_color != 'Springgreen')):
                                self.b_y.style.background_color = 'Gold'
                            if ((self.resp[4] == 'u') and (self.b_u.style.background_color != 'Springgreen')):
                                self.b_u.style.background_color = 'Gold'
                            if ((self.resp[4] == 'i') and (self.b_i.style.background_color != 'Springgreen')):
                                self.b_i.style.background_color = 'Gold'
                            if ((self.resp[4] == 'o') and (self.b_o.style.background_color != 'Springgreen')):
                                self.b_o.style.background_color = 'Gold'
                            if ((self.resp[4] == 'p') and (self.b_p.style.background_color != 'Springgreen')):
                                self.b_p.style.background_color = 'Gold'
                            if ((self.resp[4] == 'a') and (self.b_a.style.background_color != 'Springgreen')):
                                self.b_a.style.background_color = 'Gold'
                            if ((self.resp[4] == 's') and (self.b_s.style.background_color != 'Springgreen')):
                                self.b_s.style.background_color = 'Gold'
                            if ((self.resp[4] == 'd') and (self.b_d.style.background_color != 'Springgreen')):
                                self.b_d.style.background_color = 'Gold'
                            if ((self.resp[4] == 'f') and (self.b_f.style.background_color != 'Springgreen')):
                                self.b_f.style.background_color = 'Gold'
                            if ((self.resp[4] == 'g') and (self.b_g.style.background_color != 'Springgreen')):
                                self.b_g.style.background_color = 'Gold'
                            if ((self.resp[4] == 'h') and (self.b_h.style.background_color != 'Springgreen')):
                                self.b_h.style.background_color = 'Gold'
                            if ((self.resp[4] == 'j') and (self.b_j.style.background_color != 'Springgreen')):
                                self.b_j.style.background_color = 'Gold'
                            if ((self.resp[4] == 'k') and (self.b_k.style.background_color != 'Springgreen')):
                                self.b_k.style.background_color = 'Gold'
                            if ((self.resp[4] == 'l') and (self.b_l.style.background_color != 'Springgreen')):
                                self.b_l.style.background_color = 'Gold'
                            if ((self.resp[4] == 'ç') and (self.b_cdl.style.background_color != 'Springgreen')):
                                self.b_cdl.style.background_color = 'Gold'
                            if ((self.resp[4] == 'z') and (self.b_z.style.background_color != 'Springgreen')):
                                self.b_z.style.background_color = 'Gold'
                            if ((self.resp[4] == 'x') and (self.b_x.style.background_color != 'Springgreen')):
                                self.b_x.style.background_color = 'Gold'
                            if ((self.resp[4] == 'c') and (self.b_c.style.background_color != 'Springgreen')):
                                self.b_c.style.background_color = 'Gold'
                            if ((self.resp[4] == 'v') and (self.b_v.style.background_color != 'Springgreen')):
                                self.b_v.style.background_color = 'Gold'
                            if ((self.resp[4] == 'b') and (self.b_b.style.background_color != 'Springgreen')):
                                self.b_b.style.background_color = 'Gold'
                            if ((self.resp[4] == 'n') and (self.b_n.style.background_color != 'Springgreen')):
                                self.b_n.style.background_color = 'Gold'
                            if ((self.resp[4] == 'm') and (self.b_m.style.background_color != 'Springgreen')):
                                self.b_m.style.background_color = 'Gold'
                        else:
                            if self.resp[4] == 'q':
                                self.b_q.style.background_color = 'Gray'
                            if self.resp[4] == 'w':
                                self.b_w.style.background_color = 'Gray'
                            if self.resp[4] == 'e':
                                self.b_e.style.background_color = 'Gray'
                            if self.resp[4] == 'r':
                                self.b_r.style.background_color = 'Gray'
                            if self.resp[4] == 't':
                                self.b_t.style.background_color = 'Gray'
                            if self.resp[4] == 'y':
                                self.b_y.style.background_color = 'Gray'
                            if self.resp[4] == 'u':
                                self.b_u.style.background_color = 'Gray'
                            if self.resp[4] == 'i':
                                self.b_i.style.background_color = 'Gray'
                            if self.resp[4] == 'o':
                                self.b_o.style.background_color = 'Gray'
                            if self.resp[4] == 'p':
                                self.b_p.style.background_color = 'Gray'
                            if self.resp[4] == 'a':
                                self.b_a.style.background_color = 'Gray'
                            if self.resp[4] == 's':
                                self.b_s.style.background_color = 'Gray'
                            if self.resp[4] == 'd':
                                self.b_d.style.background_color = 'Gray'
                            if self.resp[4] == 'f':
                                self.b_f.style.background_color = 'Gray'
                            if self.resp[4] == 'g':
                                self.b_g.style.background_color = 'Gray'
                            if self.resp[4] == 'h':
                                self.b_h.style.background_color = 'Gray'
                            if self.resp[4] == 'j':
                                self.b_j.style.background_color = 'Gray'
                            if self.resp[4] == 'k':
                                self.b_k.style.background_color = 'Gray'
                            if self.resp[4] == 'l':
                                self.b_l.style.background_color = 'Gray'
                            if self.resp[4] == 'ç':
                                self.b_cdl.style.background_color = 'Gray'
                            if self.resp[4] == 'z':
                                self.b_z.style.background_color = 'Gray'
                            if self.resp[4] == 'x':
                                self.b_x.style.background_color = 'Gray'
                            if self.resp[4] == 'c':
                                self.b_c.style.background_color = 'Gray'
                            if self.resp[4] == 'v':
                                self.b_v.style.background_color = 'Gray'
                            if self.resp[4] == 'b':
                                self.b_b.style.background_color = 'Gray'
                            if self.resp[4] == 'n':
                                self.b_n.style.background_color = 'Gray'
                            if self.resp[4] == 'm':
                                self.b_m.style.background_color = 'Gray'
                    self.main_window.info_dialog('Você Perdeu!', f'{termo_play.upper()} era a palavra correta 😢')
                else:
                    self.output26.text = '' + termo_play_Acento[0].upper()
                    self.letra_t5.style.background_color = 'Springgreen'
                    self.output27.text = '' + termo_play_Acento[1].upper()
                    self.letra_e5.style.background_color = 'Springgreen'
                    self.output28.text = '' + termo_play_Acento[2].upper()
                    self.letra_r5.style.background_color = 'Springgreen'
                    self.output29.text = '' + termo_play_Acento[3].upper()
                    self.letra_m5.style.background_color = 'Springgreen'
                    self.output30.text = '' + termo_play_Acento[4].upper()
                    self.letra_o5.style.background_color = 'Springgreen'
                    self.main_window.info_dialog('Você Ganhou!', f'{termo_play_Acento.upper()} era a palavra correta 🤩', )
                self.resposta = ''
                return 0
            else:
                if (self.contador == '5'):
                    self.main_window.info_dialog('Palavra inexistente!', 'A palavra digitada não é aceita 😒')
                    return 0
        else:
            self.main_window.info_dialog('Tá faltando letra!', 'A palavra digitada não tem 5 letras 😐')
            return 0


    def teclado(self, widget, letra):
        if self.contador == '0':
            if letra == 'del':
                if self.output5.text != '_':
                    self.output5.text = '_'
                    self.resp[4] = ''
                    self.resposta = '' + self.resposta[:4]
                    return 0
                if self.output4.text != '_':
                    self.output4.text = '_'
                    self.resp[3] = ''
                    self.resposta = '' + self.resposta[:3]
                    return 0
                if self.output3.text != '_':
                    self.output3.text = '_'
                    self.resp[2] = ''
                    self.resposta = '' + self.resposta[:2]
                    return 0
                if self.output2.text != '_':
                    self.output2.text = '_'
                    self.resp[1] = ''
                    self.resposta = '' + self.resposta[:1]
                    return 0
                if self.output1.text != '_':
                    self.output1.text = '_'
                    self.resp[0] = ''
                    self.resposta = ''
                    return 0

            if ((self.output1.text == '_') and (letra!='del')):
                self.output1.text = '' + letra.upper()
                self.resp[0] = '' + letra
                self.resposta = self.resposta + letra
                return 0
            if ((self.output2.text == '_') and (letra!='del')):
                self.output2.text = '' + letra.upper()
                self.resp[1] = '' + letra
                self.resposta = self.resposta + letra
                return 0
            if ((self.output3.text == '_') and (letra!='del')):
                self.output3.text = '' + letra.upper()
                self.resp[2] = '' + letra
                self.resposta = self.resposta + letra
                return 0
            if ((self.output4.text == '_') and (letra!='del')):
                self.output4.text = '' + letra.upper()
                self.resp[3] = '' + letra
                self.resposta = self.resposta + letra
                return 0
            if ((self.output5.text == '_') and (letra!='del')):
                self.output5.text = '' + letra.upper()
                self.resp[4] = '' + letra
                self.resposta = self.resposta + letra
                return 0

        if self.contador == '1':
            if letra == 'del':
                if self.output10.text != '_':
                    self.output10.text = '_'
                    self.resp[4] = ''
                    self.resposta = '' + self.resposta[:4]
                    return 0
                if self.output9.text != '_':
                    self.output9.text = '_'
                    self.resp[3] = ''
                    self.resposta = '' + self.resposta[:3]
                    return 0
                if self.output8.text != '_':
                    self.output8.text = '_'
                    self.resp[2] = ''
                    self.resposta = '' + self.resposta[:2]
                    return 0
                if self.output7.text != '_':
                    self.output7.text = '_'
                    self.resp[1] = ''
                    self.resposta = '' + self.resposta[:1]
                    return 0
                if self.output6.text != '_':
                    self.output6.text = '_'
                    self.resp[0] = ''
                    self.resposta = ''
                    return 0

            if ((self.output6.text == '_') and (letra!='del')):
                self.output6.text = '' + letra.upper()
                self.resp[0] = '' + letra
                self.resposta = self.resposta + letra
                return 0
            if ((self.output7.text == '_') and (letra!='del')):
                self.output7.text = '' + letra.upper()
                self.resp[1] = '' + letra
                self.resposta = self.resposta + letra
                return 0
            if ((self.output8.text == '_') and (letra!='del')):
                self.output8.text = '' + letra.upper()
                self.resp[2] = '' + letra
                self.resposta = self.resposta + letra
                return 0
            if ((self.output9.text == '_') and (letra!='del')):
                self.output9.text = '' + letra.upper()
                self.resp[3] = '' + letra
                self.resposta = self.resposta + letra
                return 0
            if ((self.output10.text == '_') and (letra!='del')):
                self.output10.text = '' + letra.upper()
                self.resp[4] = '' + letra
                self.resposta = self.resposta + letra
                return 0

        if self.contador == '2':
            if letra == 'del':
                if self.output15.text != '_':
                    self.output15.text = '_'
                    self.resp[4] = ''
                    self.resposta = '' + self.resposta[:4]
                    return 0
                if self.output14.text != '_':
                    self.output14.text = '_'
                    self.resp[3] = ''
                    self.resposta = '' + self.resposta[:3]
                    return 0
                if self.output13.text != '_':
                    self.output13.text = '_'
                    self.resp[2] = ''
                    self.resposta = '' + self.resposta[:2]
                    return 0
                if self.output12.text != '_':
                    self.output12.text = '_'
                    self.resp[1] = ''
                    self.resposta = '' + self.resposta[:1]
                    return 0
                if self.output11.text != '_':
                    self.output11.text = '_'
                    self.resp[0] = ''
                    self.resposta = ''
                    return 0

            if ((self.output11.text == '_') and (letra!='del')):
                self.output11.text = '' + letra.upper()
                self.resp[0] = '' + letra
                self.resposta = self.resposta + letra
                return 0
            if ((self.output12.text == '_') and (letra!='del')):
                self.output12.text = '' + letra.upper()
                self.resp[1] = '' + letra
                self.resposta = self.resposta + letra
                return 0
            if ((self.output13.text == '_') and (letra!='del')):
                self.output13.text = '' + letra.upper()
                self.resp[2] = '' + letra
                self.resposta = self.resposta + letra
                return 0
            if ((self.output14.text == '_') and (letra!='del')):
                self.output14.text = '' + letra.upper()
                self.resp[3] = '' + letra
                self.resposta = self.resposta + letra
                return 0
            if ((self.output15.text == '_') and (letra!='del')):
                self.output15.text = '' + letra.upper()
                self.resp[4] = '' + letra
                self.resposta = self.resposta + letra
                return 0

        if self.contador == '3':
            if letra == 'del':
                if self.output20.text != '_':
                    self.output20.text = '_'
                    self.resp[4] = ''
                    self.resposta = '' + self.resposta[:4]
                    return 0
                if self.output19.text != '_':
                    self.output19.text = '_'
                    self.resp[3] = ''
                    self.resposta = '' + self.resposta[:3]
                    return 0
                if self.output18.text != '_':
                    self.output18.text = '_'
                    self.resp[2] = ''
                    self.resposta = '' + self.resposta[:2]
                    return 0
                if self.output17.text != '_':
                    self.output17.text = '_'
                    self.resp[1] = ''
                    self.resposta = '' + self.resposta[:1]
                    return 0
                if self.output16.text != '_':
                    self.output16.text = '_'
                    self.resp[0] = ''
                    self.resposta = ''
                    return 0

            if ((self.output16.text == '_') and (letra!='del')):
                self.output16.text = '' + letra.upper()
                self.resp[0] = '' + letra
                self.resposta = self.resposta + letra
                return 0
            if ((self.output17.text == '_') and (letra!='del')):
                self.output17.text = '' + letra.upper()
                self.resp[1] = '' + letra
                self.resposta = self.resposta + letra
                return 0
            if ((self.output18.text == '_') and (letra!='del')):
                self.output18.text = '' + letra.upper()
                self.resp[2] = '' + letra
                self.resposta = self.resposta + letra
                return 0
            if ((self.output19.text == '_') and (letra!='del')):
                self.output19.text = '' + letra.upper()
                self.resp[3] = '' + letra
                self.resposta = self.resposta + letra
                return 0
            if ((self.output20.text == '_') and (letra!='del')):
                self.output20.text = '' + letra.upper()
                self.resp[4] = '' + letra
                self.resposta = self.resposta + letra
                return 0

        if self.contador == '4':
            if letra == 'del':
                if self.output25.text != '_':
                    self.output25.text = '_'
                    self.resp[4] = ''
                    self.resposta = '' + self.resposta[:4]
                    return 0
                if self.output24.text != '_':
                    self.output24.text = '_'
                    self.resp[3] = ''
                    self.resposta = '' + self.resposta[:3]
                    return 0
                if self.output23.text != '_':
                    self.output23.text = '_'
                    self.resp[2] = ''
                    self.resposta = '' + self.resposta[:2]
                    return 0
                if self.output22.text != '_':
                    self.output22.text = '_'
                    self.resp[1] = ''
                    self.resposta = '' + self.resposta[:1]
                    return 0
                if self.output21.text != '_':
                    self.output21.text = '_'
                    self.resp[0] = ''
                    self.resposta = ''
                    return 0

            if ((self.output21.text == '_') and (letra!='del')):
                self.output21.text = '' + letra.upper()
                self.resp[0] = '' + letra
                self.resposta = self.resposta + letra
                return 0
            if ((self.output22.text == '_') and (letra!='del')):
                self.output22.text = '' + letra.upper()
                self.resp[1] = '' + letra
                self.resposta = self.resposta + letra
                return 0
            if ((self.output23.text == '_') and (letra!='del')):
                self.output23.text = '' + letra.upper()
                self.resp[2] = '' + letra
                self.resposta = self.resposta + letra
                return 0
            if ((self.output24.text == '_') and (letra!='del')):
                self.output24.text = '' + letra.upper()
                self.resp[3] = '' + letra
                self.resposta = self.resposta + letra
                return 0
            if ((self.output25.text == '_') and (letra!='del')):
                self.output25.text = '' + letra.upper()
                self.resp[4] = '' + letra
                self.resposta = self.resposta + letra
                return 0

        if self.contador == '5':
            if letra == 'del':
                if self.output30.text != '_':
                    self.output30.text = '_'
                    self.resp[4] = ''
                    self.resposta = '' + self.resposta[:4]
                    return 0
                if self.output29.text != '_':
                    self.output29.text = '_'
                    self.resp[3] = ''
                    self.resposta = '' + self.resposta[:3]
                    return 0
                if self.output28.text != '_':
                    self.output28.text = '_'
                    self.resp[2] = ''
                    self.resposta = '' + self.resposta[:2]
                    return 0
                if self.output27.text != '_':
                    self.output27.text = '_'
                    self.resp[1] = ''
                    self.resposta = '' + self.resposta[:1]
                    return 0
                if self.output26.text != '_':
                    self.output26.text = '_'
                    self.resp[0] = ''
                    self.resposta = ''
                    return 0

            if ((self.output26.text == '_') and (letra!='del')):
                self.output26.text = '' + letra.upper()
                self.resp[0] = '' + letra
                self.resposta = self.resposta + letra
                return 0
            if ((self.output27.text == '_') and (letra!='del')):
                self.output27.text = '' + letra.upper()
                self.resp[1] = '' + letra
                self.resposta = self.resposta + letra
                return 0
            if ((self.output28.text == '_') and (letra!='del')):
                self.output28.text = '' + letra.upper()
                self.resp[2] = '' + letra
                self.resposta = self.resposta + letra
                return 0
            if ((self.output29.text == '_') and (letra!='del')):
                self.output29.text = '' + letra.upper()
                self.resp[3] = '' + letra
                self.resposta = self.resposta + letra
                return 0
            if ((self.output30.text == '_') and (letra!='del')):
                self.output30.text = '' + letra.upper()
                self.resp[4] = '' + letra
                self.resposta = self.resposta + letra
                return 0

def main():

    return Palavra_App()

# briefcase run android -d RX8NB09JBYN -u

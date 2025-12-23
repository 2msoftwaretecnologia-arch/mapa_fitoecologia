from database.text_infos import Text_infos
from buildkite.interfaces.simple_interface import simple_choices

def get_techinal_note_text():
    kind = Text_infos.kind_mapa
    nome = Text_infos.nome_propriedade

    # Mapa de configurações para cada tipo de mapa
    configs = {
        'Fitoecologia': {
            'prompt': "Qual a fitofisionomia predominante da propriedade?",
            'attr': 'strongest_fifisionomia',
            'interface': simple_choices,
            'items_attr': 'current_items',
            'template': (
                "O mapa de Fitofisionomias da propriedade {nome} detalha as formações vegetais da área, "
                "com destaque para a {{{attr}}}."
            )
        },
        'Geologia': {
            'prompt': "Qual a Geologia predominante da propriedade?",
            'attr': 'strongest_geology',
            'interface': lambda **kw: simple_choices(text="Geologia Predominante", **kw),
            'items_attr': 'itens_atuais',
            'template': (
                "O mapa geológico da propriedade {nome} detalha as formações litológicas presentes na área, "
                "com destaque para a {{{attr}}}."
            )
        },
        'Pedologia': {
            'prompt': "Qual a Pedologia predominante da propriedade?",
            'attr': 'tipo_dominante_pedologia',
            'interface': lambda **kw: simple_choices(text="Pedologia Predominante", **kw),
            'items_attr': 'itens_atuais',
            'template': (
                "O mapa pedológico da propriedade {nome} detalha as formações solares presentes na área, "
                "com destaque para a {{{attr}}}."
            )
        },
        'Regioes_climaticas': {
            'prompt': "Qual a Região Climática predominante da propriedade?",
            'attr': 'tipo_dominante_regiao_climatica',
            'interface': lambda **kw: simple_choices(text="Região Climática Predominante", **kw),
            'items_attr': 'itens_atuais',
            'template': (
                "O mapa de Regiões Climáticas da propriedade {nome} detalha as regiões climáticas predominantes na área, "
                "com destaque para a {{{attr}}}."
            )
        },
        'Declividade': {
            'prompt': "Qual a Declividade predominante da propriedade?",
            'attr': 'tipo_dominante_declividade',
            'interface': lambda **kw: simple_choices(text="Declividade Predominante", **kw),
            'items_attr': 'itens_atuais',
            'template': (
                "O mapa de Declividade da propriedade {nome} detalha as declividades predominantes na área, "
                "com destaque para a {{{attr}}}."
            )
        },
        'Erodibilidade': {
            'prompt': "Qual a Erodibilidade predominante da propriedade?",
            'attr': 'tipo_dominante_erodibilidade',
            'interface': lambda **kw: simple_choices(text="Erodibilidade Predominante", **kw),
            'items_attr': 'itens_atuais',
            'template': (
                "O mapa de Erodibilidade da propriedade {nome} detalha as erodibilidades predominantes na área, "
                "com destaque para a {{{attr}}}."
            )
        }
    }

    if kind not in configs:
        return ""

    cfg = configs[kind]
    items = getattr(Text_infos, cfg['items_attr'])
    escolha = cfg['interface'](text=cfg['prompt'], buttons=items)
    setattr(Text_infos, cfg['attr'], escolha)

    corpo = cfg['template'].format(nome=nome, attr=cfg['attr'])
    return f"""Nota Técnica

{corpo}
Esses dados são fundamentais para o planejamento ambiental, regularização fundiária e ações de conservação. Os direitos autorais e a propriedade intelectual deste mapeamento pertencem à ENVIMAP. Qualquer uso, reprodução ou distribuição deste registro técnico deve ser devidamente referenciado e autorizado."""

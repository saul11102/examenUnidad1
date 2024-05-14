save_escultura = {
    'type' : 'object',
    'propierties' : {
        'nombre': {'type' : 'string'},
        'autor': {'type' : 'string'},
        'latitud': {'type' : 'float'},
        'longitud' : {'type': 'float'}
    },
    'required' : ['nombre','autor','latitud', 'longitud']
}

modify_state = {
    'type' : 'object',
    'propierties' : {
        'nombre': {'type' : 'string'}
    },
    'required' : ['nombre']
}


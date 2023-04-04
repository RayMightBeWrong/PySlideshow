def get_attr_value(attrs, key):
    value = None
    for attr in attrs:
        if attr[0] == key:
            value = attr[1]
            break
    return value

def validate_config(attrs):
    keys = [attr[0] for attr in attrs]
    if len(attrs) == 2:
        if ('height' in keys) and ('width' in keys):
            if get_attr_value(attrs, 'width') > 0 and get_attr_value(attrs, 'height') > 0:
                res = {'width': get_attr_value(attrs, 'width'), 'heigth': get_attr_value(attrs, 'height')}
                return (True, res)
    elif len(attrs) == 1:
        if 'height' in keys:
            if get_attr_value(attrs, 'height') > 0:
                height = get_attr_value(attrs, 'height')
                width = height 
                res = {'heigth': height, 'width': width}
                return (True, res)
        elif 'width' in keys:
            if get_attr_value(attrs, 'width') > 0:
                width = get_attr_value(attrs, 'width') 
                height = width 
                res = {'heigth': height, 'width': width}
                return (True, res)
    elif len(attrs) == 0:
        res = {'width': 500, 'heigth': 500}
        return (True, res)
    return (False, [])

def validate_durationtag(attrs):
    if len(attrs) == 1:
        if attrs[0][0] == 'time' and (isinstance(attrs[0][1], float) and attrs[0][1] > 0):
            return (True, attrs)

    return (False, [])

def validate_imgtag_attrs(keys, attrs):
    if not isinstance(get_attr_value(attrs, 'center'), bool):
        return False
    elif not isinstance(get_attr_value(attrs, 'cont'), str):
        return False
    elif 'query' in keys and not isinstance(get_attr_value(attrs, 'query'), str):
        return False
    elif 'src' in keys and not isinstance(get_attr_value(attrs, 'src'), str):
        return False
    else:
        return True

def validate_imgtag(attrs):
    keys = [attr[0] for attr in attrs]
    if len(attrs) == 2:
        if ('cont' in keys) and ('src' in keys or 'query' in keys):
            attrs.append(('center', False))
            return (validate_imgtag_attrs(keys, attrs), attrs)
    elif len(attrs) == 3:
        if ('center' in keys) and ('cont' in keys) and ('src' in keys or 'query' in keys):
            return (validate_imgtag_attrs(keys, attrs), attrs)
    return (False, [])


def validate_texttag_attrs(keys, attrs):
    if not isinstance(get_attr_value(attrs, 'center'), bool):
        return False
    elif not isinstance(get_attr_value(attrs, 'cont'), str):
        return False
    elif not isinstance(get_attr_value(attrs, 'text'), str):
        return False
    elif not isinstance(get_attr_value(attrs, 'font'), str):
        return False

    if isinstance(get_attr_value(attrs, 'color'), str) or isinstance(get_attr_value(attrs, 'color'), tuple):
        color = get_attr_value(attrs, 'color')
        if isinstance(color, tuple):
            if len(color) != 3:
                return False
            for value in color:
                if value < 0 or value > 255:
                    return False
    else:
        return False

    if isinstance(get_attr_value(attrs, 'size'), float):
        if get_attr_value(attrs, 'size') < 0:
            return False

    return True

def validate_texttag(attrs):
    keys = [attr[0] for attr in attrs]
    attrs_keys = ['cont', 'text', 'font', 'size', 'color']
    if len(attrs) == 5 or len(attrs) == 6:
        all_present = True
        for attr_key in attrs_keys:
            if not attr_key in keys:
                all_present = False
                break

        if len(attrs) == 6:
            if 'center' not in keys:
                all_present = False
        else:
            attrs.append(('center', False))

        if all_present:
            return (validate_texttag_attrs(keys, attrs), attrs)

    return (False, [])

def validate_tag(tag, attrs):
    if tag == 'duration':
        return validate_durationtag(attrs)
    elif tag == 'img':
        return validate_imgtag(attrs)
    elif tag == 'text':
        return validate_texttag(attrs)
    else:
        return (False, [])


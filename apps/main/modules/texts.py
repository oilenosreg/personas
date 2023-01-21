class TextCreate():
    def title(model):
        text = f'Crear {model._meta.verbose_name.lower()}'
        return text

    def unique(model, field):
        model = model._meta
        model_name = model.verbose_name.title()
        field = model.get_field(field)
        field_name = field.verbose_name
        text = f'{field_name} ya existe.'
        return text

    def required(model, field):
        model = model._meta
        model_name = model.verbose_name.title()
        field = model.get_field(field)
        field_name = field.verbose_name
        text = f'{field_name} es obligatorio.'
        return text    

    def success(model, field):
        model = model._meta
        model_name = model.verbose_name.title()
        text = f'{model_name} {field} creado con éxito'
        return text

    def error():
        text = f'No fue posible guardar los datos; por favor, verifique la información ingresada.'
        return text

class TextList():
    def title(model):
        text = f'Listado de {model._meta.verbose_name_plural.lower()}'
        return text


class TextUpdate():
    def title(model, field):
        model = model._meta
        model_name = model.verbose_name.title()        
        text = f'Actualizar {model_name.lower()}: {field.upper()}'
        return text

    def success(model, field):
        model = model._meta
        model_name = model.verbose_name.title()
        text = f'{model_name} {field} actualizado con éxito'
        return text     

    def error():
        return TextCreate.error()


class TextDetails():
    def title(model, field):
        model = model._meta
        model_name = model.verbose_name.title()        
        text = f'Detalle {model_name.lower()}: {field.upper()}'
        return text


class TextDelete():
    def title(model):
        text = f'Anular {model._meta.verbose_name.title()}'
        return text
    
    def confirm(model, field):
        model = model._meta
        model_name = model.verbose_name.title()
        # field = model.get_field(field)
        # field_name = field.verbose_name
        text = f'¿Desea anular {model_name.lower()} {field.upper()}?'
        return text

    def success(model, field):
        model = model._meta
        model_name = model.verbose_name.title()
        text = f'{model_name} {field} anulado con éxito'
        return text

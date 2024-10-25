from django import template
from babel.numbers import format_currency
register = template.Library()

@register.filter
def local_currency(value, currency='PYG'):
    try:
        value = float(value)
        return format_currency(value, currency, locale='es_PY', format=u'#,##0.00')
    
    except (ValueError, TypeError):
        return value
    # try:
        
    #     print(salario)
    #     return format_currency(salario, currency, locale='en_US')
    # except (ValueError, TypeError):
    #     return value.replace(',')
import markdown
from lxml.html.clean import Cleaner 
from django.template.defaultfilters import register, stringfilter
from django import template

register = template.Library()

@register.filter(name='convert_markdown')
@stringfilter
def convert_markdown(value):
    cleaner = Cleaner(scripts=True, javascript=True) #as we are rendering html we need cleaner to clean javascript to prevent XSS
    return cleaner.clean_html(markdown.markdown(value)) #this will remove all script tags, and embbeded javascript events
from transformer.registry import register
from transformer.transforms.base import BaseTransform

class StringLowercaseTransform(BaseTransform):

    category = 'string'
    name = 'lowercase'
    label = 'String / Uppercase'
    help_text = 'Convert all characters in a string to lowercase'

    def transform(self, str_input, **kwargs):
        return str_input.lower() if str_input else ''

register(StringLowercaseTransform())

from rest_framework.schemas.openapi import AutoSchema
from rest_framework.utils import formatting
from django.utils.encoding import force_text, smart_text
import re
from rest_framework.compat import coreapi, coreschema, uritemplate
from rest_framework.settings import api_settings

header_regex = re.compile('^[a-zA-Z][0-9A-Za-z_]*:')

class MakeSchema(AutoSchema):
    """ 生成swagger yaml文档, 比官方版本多了注释 """
    def get_operation(self, path, method):

        operation = {}

        operation['operationId'] = self._get_operation_id(path, method)
        operation['description'] = self.get_description(path, method)

        parameters = []
        parameters += self._get_path_parameters(path, method)
        parameters += self._get_pagination_parameters(path, method)
        parameters += self._get_filter_parameters(path, method)
        operation['parameters'] = parameters

        request_body = self._get_request_body(path, method)
        if request_body:
            operation['requestBody'] = request_body
        operation['responses'] = self._get_responses(path, method)

        return operation

    def get_description(self, path, method):
        """
        Determine a link description.

        This will be based on the method docstring if one exists,
        or else the class docstring.
        """
        view = self.view

        method_name = getattr(view, 'action', method.lower())
        method_docstring = getattr(view, method_name, None).__doc__
        if method_docstring:
            # An explicit docstring on the method or action.
            return self._get_description_section(view, method.lower(), formatting.dedent(smart_text(method_docstring)))
        else:
            return self._get_description_section(view, getattr(view, 'action', method.lower()), view.get_view_description())

    def _get_description_section(self, view, header, description):
        lines = [line for line in description.splitlines()]
        current_section = ''
        sections = {'': ''}

        for line in lines:
            if header_regex.match(line):
                current_section, seperator, lead = line.partition(':')
                sections[current_section] = lead.strip()
            else:
                sections[current_section] += '\n' + line

        # TODO: SCHEMA_COERCE_METHOD_NAMES appears here and in `SchemaGenerator.get_keys`
        coerce_method_names = api_settings.SCHEMA_COERCE_METHOD_NAMES
        if header in sections:
            return sections[header].strip()
        if header in coerce_method_names:
            if coerce_method_names[header] in sections:
                return sections[coerce_method_names[header]].strip()
        return sections[''].strip()
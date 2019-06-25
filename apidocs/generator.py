from rest_framework.schemas.openapi import SchemaGenerator

class ApiDocsGenerator(SchemaGenerator):
    def get_paths(self, request=None):
        result = {}

        paths, view_endpoints = self._get_paths_and_endpoints(request)

        # Only generate the path prefix for paths that will be included
        if not paths:
            return None
        prefix = self.determine_path_prefix(paths)
        if prefix == '/':  # no prefix
            prefix = ''

        for path, method, view in view_endpoints:
            if not self.has_view_permissions(path, method, view):
                continue
            operation = view.schema.get_operation(path, method)
            # subpath = path[len(prefix):]
            fullPath = self.url + path[1:]
            result.setdefault(fullPath, {})
            result[fullPath][method.lower()] = operation

        return result
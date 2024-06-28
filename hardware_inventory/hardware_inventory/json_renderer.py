from rest_framework.renderers import JSONRenderer

class CustomJSONRenderer(JSONRenderer):
    def render(self, data, accepted_media_type=None, renderer_context=None):
        if isinstance(data, list):
            return super().render({'items': data}, accepted_media_type, renderer_context)
        return super().render(data, accepted_media_type, renderer_context)

from django.template import Context, Template
from django.test import TestCase, override_settings


class TestMinifiedTemplateTag(TestCase):
    @override_settings(DEBUG=False)
    def test_basic_example_with_debug_off(self):
        base_string = '<a href="url/to/static/file.min.js"</a>'
        self._test_debug_dependent_output(base_string)

    @override_settings(DEBUG=True)
    def test_basic_example_with_debug_on(self):
        base_string = '<a href="url/to/static/file.js"</a>'
        self._test_debug_dependent_output(base_string)

    def _test_debug_dependent_output(self, expected):
        template = '{% load utils %}<a href="{{ "url/to/static/file"|minified:"js" }}"</a>'
        rendered = Template(template_string=template).render(context=Context({}))
        self.assertEqual(rendered, expected)

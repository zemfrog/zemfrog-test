"""
Unit Testing For (API {{ name }})
"""

from flask import current_app
from hypothesis import given
from schemathesis import from_wsgi
from schemathesis.models import Case

schema = from_wsgi("{{openapi}}", current_app)

{%- for spec in specs %}
{{spec["func"]}}_strategy = schema["{{spec['url']}}"]["{{ spec['method'] | upper}}"].as_strategy()

@given(case={{spec["func"]}}_strategy)
def test_{{spec["func"]}}(case: Case):
    response = case.call_wsgi()
    case.validate_response(response)
{% endfor %}

{% for entry in entries %}
{% if entry.abbreviation %}
## **{{ entry.abbreviation }}**
*({{ entry.title }})*
{% else %}
## **{{ entry.title }}**
{% endif %}
* {{ entry.description }}
{% for link in entry.links %}
* <{{ link }}>
{% endfor %}
{% if entry.tags %}* Tags: {{ entry.tags|join(', ') }}{% endif %}
{% endfor %}

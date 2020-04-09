{% if output_type=='mkdocs' and lexicon %}---
title: {{ lexicon['title'] }}
summary: {{ lexicon['description'] }}
authors: {% for author in lexicon['authors'] %}
  - {{ author }}
{% endfor %}
---
{% elif output_type=='readme' and lexicon %}# {{ lexicon['title'] }}{% endif %}
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
{% if output_type=='readme' %}
</br>
</br>
</br>

[Lexicon Repository](https://github.com/technopreneurG/lexicon)
{% endif %}

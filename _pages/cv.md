---
layout: career
title: CV
description: Professional experience, education, technical skills, and selected publications.
permalink: /cv/
redirect_from:
  - /resume
  - /resume/
---

# Curriculum Vitae

**Jintao Li**  
Data Science Manager · Singapore  
[Email](mailto:{{ site.author.email }}) · [LinkedIn](https://www.linkedin.com/in/{{ site.author.linkedin }})

## Professional Summary

Data science manager with a Ph.D. background and experience in applied machine learning, forecasting, optimization, and decision-support systems. I lead six data scientists at Ocean Network Express and remain hands-on in analytical design, validation, and production delivery on Google Cloud.

## Professional Experience

{% for job in site.data.profile.experience %}
### {{ job.role }}

**{{ job.company }}** · {{ job.location }}  
*{{ job.start | date: '%b %Y' }} to {% if job.end %}{{ job.end | date: '%b %Y' }}{% else %}Present{% endif %}*

{{ job.summary }}

{% for detail in job.details %}
- {{ detail }}
{% endfor %}

{% endfor %}

## Selected Work

{% for area in site.data.profile.focus %}
- **{{ area.title }}:** {{ area.description }}
{% endfor %}

[Read more about selected projects]({{ '/work/' | relative_url }}).

## Technical Expertise

- **Data science:** Time series forecasting, regression, optimization, simulation, scenario analysis, model validation.
- **Programming and machine learning:** Python, C++, SQL, Pandas, NumPy, scikit-learn, PyTorch, TensorFlow.
- **Cloud and engineering:** Google Cloud, BigQuery, Cloud Run, AWS, Git, Linux, production workflows.
- **Leadership:** Technical strategy, code and model review, mentoring, delivery planning, stakeholder alignment.

## Education

{% for item in site.data.profile.education %}
### {{ item.degree }}
**{{ item.institution }}** · {{ item.period }}  
{{ item.detail }}
{% endfor %}

**Visiting Researcher, University of Tokyo** · Jul 2021 to Sep 2021  
Research on non-equilibrium statistical physics and pattern formation.

## Selected Publications

- Li, J. et al. [Competition between Cell Types under Cell Cycle Regulation with Apoptosis](https://doi.org/10.1103/PhysRevResearch.4.033156). *Physical Review Research*, 2022.
- Li, J. et al. [Role of the Cell Cycle in Collective Cell Dynamics](https://doi.org/10.1103/PhysRevX.11.031025). *Physical Review X*, 2021.
- Wang, J., Li, J. et al. Ion-specific electrolyte thermodynamic modeling. *Fluid Phase Equilibria*, 2020.

[More research and publications]({{ '/research/' | relative_url }}).

## Languages

{% for language in site.data.profile.languages %}
- {{ language }}
{% endfor %}

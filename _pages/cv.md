---
layout: career
title: Experience & Leadership
description: Experience in applied machine learning, forecasting, optimization, production systems, and data science team leadership.
permalink: /cv/
resume: true
redirect_from:
  - /resume
  - /resume/
---
<div class="page-shell resume-shell">
  <header class="page-heading resume-heading">
    <div><p class="eyebrow">Experience & leadership</p><h1>Jintao Li<span class="heading-dot">.</span></h1><p class="page-lede">Forecasting & Optimization · Production Data Science · Technical Leadership</p><p class="resume-contact">Singapore <span aria-hidden="true">·</span> <a href="mailto:{{ site.author.email }}">{{ site.author.email }}</a> <span aria-hidden="true">·</span> <a href="https://www.linkedin.com/in/{{ site.author.linkedin }}">LinkedIn {% include icon-arrow.html %}</a></p></div>
  </header>
  <div class="resume-summary"><p class="eyebrow">Professional summary</p><p>Data science manager working on forecasting, optimization, and production decision-support systems for global shipping operations. I lead six data scientists, combining hands-on modeling and end-to-end GCP deployment with analytical strategy and collaboration across business and engineering teams.</p></div>
  <section class="cv-outcomes" aria-labelledby="outcomes-heading"><h2 id="outcomes-heading">Selected delivery outcomes</h2><ul>{% for area in site.data.profile.focus %}<li>{{ area.description }}</li>{% endfor %}</ul></section>
  <nav class="page-jumps" aria-label="Experience sections"><a href="#outcomes-heading">Impact</a><a href="#experience">Experience</a><a href="#capabilities">Capabilities</a><a href="#education">Education</a><a href="#publications">Publications</a></nav>

  <section class="resume-section" aria-labelledby="experience"><h2 id="experience">Professional experience</h2>{% include experience.html %}</section>

  <section class="resume-section" aria-labelledby="capabilities"><h2 id="capabilities">Core capabilities</h2><div class="capability-grid">
    <div><h3>Modeling & decision science</h3><p>Forecasting, time series, optimization, simulation, scenario analysis, model validation, and KPI design.</p></div>
    <div><h3>Technology & systems</h3><p>Python, Pandas, NumPy, scikit-learn, PyTorch, TensorFlow, C++, BigQuery, GCP, AWS, Git, and Linux.</p></div>
    <div><h3>Technical leadership</h3><p>Analytical strategy, project prioritization, mentoring, technical review, delivery ownership, and stakeholder alignment.</p></div>
    <div><h3>Production analytics</h3><p>Data pipelines, recurring forecasting workflows, monitoring, validation, and maintainable analytical systems.</p></div>
  </div></section>

  <section class="resume-section" aria-labelledby="education"><h2 id="education">Education & scientific background</h2>
    {% for item in site.data.profile.education %}<article class="education-item"><div><h3>{{ item.degree }}</h3><p class="education-institution">{{ item.institution }}</p><p>{{ item.detail }}</p></div><span>{{ item.period }}</span></article>{% endfor %}
    <article class="education-item"><div><h3>Visiting Researcher</h3><p class="education-institution">University of Tokyo</p><p>Non-equilibrium statistical physics and pattern formation with Prof. Kazumasa Takeuchi.</p></div><span>Jul 2021 – Sep 2021</span></article>
  </section>

  <section class="resume-section" aria-labelledby="publications"><div class="inline-heading"><h2 id="publications">Selected publications</h2><a class="text-link" href="{{ '/research/' | relative_url }}">Research background {% include icon-arrow.html direction="right" %}</a></div><ul class="publication-summary">
    <li><a href="https://doi.org/10.1103/PhysRevResearch.4.033156">Competition between Cell Types under Cell Cycle Regulation with Apoptosis</a><span>Physical Review Research · 2022</span></li>
    <li><a href="https://doi.org/10.1103/PhysRevX.11.031025">Role of the Cell Cycle in Collective Cell Dynamics</a><span>Physical Review X · 2021</span></li>
    <li>Ion-specific electrolyte thermodynamic modeling<span>Fluid Phase Equilibria · 2020</span></li>
  </ul></section>

  <section class="resume-section" aria-labelledby="additional"><h2 id="additional">Additional information</h2><div class="capability-grid"><div><h3>Languages</h3><ul class="plain-list">{% for language in site.data.profile.languages %}<li>{{ language }}</li>{% endfor %}</ul></div><div><h3>Location & career focus</h3><p>Based in Singapore. Interested in senior applied data science and technical leadership roles in supply chain and industrial AI.</p></div></div>
  <details class="professional-development"><summary>Professional development</summary><ul><li>PyTorch for Deep Learning — Zero To Mastery Academy, 2022</li><li>DeepLearning.AI TensorFlow Developer Specialization — Coursera, 2021</li><li>Deep Learning Specialization — Coursera, 2020</li><li>Professional Certificate in Computer Science for Artificial Intelligence — edX, 2020</li></ul></details></section>
</div>

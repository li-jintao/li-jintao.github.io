---
layout: career
title: Applied Data Science Expertise
description: Applied machine learning, optimization, production data science, cloud analytics, and technical leadership.
permalink: /skills/
redirect_from:
  - /skills
---
<div class="page-shell">
  <header class="page-heading"><p class="eyebrow">Expertise</p><h1>Forecasting, optimization,<br>and production systems<span class="heading-dot">.</span></h1><p class="page-lede">Modeling and engineering capabilities for industry roles in applied data science, decision systems, and technical leadership.</p></header>
  <div class="expertise-grid">{% for area in site.data.profile.expertise %}<section class="expertise-card"><span class="card-number">0{{ forloop.index }}</span><h2>{{ area.title }}</h2><p>{{ area.description }}</p><ul class="tags" aria-label="Tools and practices">{% for tool in area.tools %}<li>{{ tool }}</li>{% endfor %}</ul></section>{% endfor %}</div>
  <section class="working-style section" aria-labelledby="approach-heading"><p class="eyebrow">How I work</p><h2 id="approach-heading">Start with the decision.</h2><div class="approach-grid"><article><span>01 / Frame</span><h3>Make the problem precise.</h3><p>Identify the decision, the operational constraints, and how success will be assessed before choosing a model.</p></article><article><span>02 / Validate</span><h3>Test the assumptions.</h3><p>Use baselines, scenarios, and validation to understand when an approach works and where its limits matter.</p></article><article><span>03 / Deliver</span><h3>Build for everyday use.</h3><p>Work with engineering and business teams on repeatable workflows, monitoring, and outputs people can trust.</p></article></div></section>
  <section class="language-section"><div><p class="eyebrow">Across teams & regions</p><h2>Communication matters.</h2></div><ul class="plain-list">{% for language in site.data.profile.languages %}<li>{{ language }}</li>{% endfor %}</ul></section>
</div>
{% include contact-card.html %}

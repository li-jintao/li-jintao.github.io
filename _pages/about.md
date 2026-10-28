---
layout: career
permalink: /
title: Applied Data Science for Forecasting & Optimization
description: Jintao Li is a Singapore-based data science manager building forecasting, optimization, and production decision-support systems. Senior data science, applied science, and technical leadership.
redirect_from:
  - /about/
  - /about.html
---
<section class="hero" aria-labelledby="hero-heading">
  <div class="hero-copy">
    <p class="eyebrow">Jintao Li · Singapore</p>
    <h1 id="hero-heading">Forecasting.<br><span>Optimization.<br>Production ML.</span></h1>
    <p class="hero-description">{{ site.data.profile.summary }}</p>
    <div class="button-group">
      <a class="button button-primary" href="{{ '/work/' | relative_url }}">Explore selected work {% include icon-arrow.html %}</a>
      <a class="button button-secondary" href="{{ '/cv/' | relative_url }}">Read my experience {% include icon-arrow.html direction="right" %}</a>
    </div>
    <p class="hero-footnote">Applied modeling <span aria-hidden="true">/</span> Operational decisions <span aria-hidden="true">/</span> End-to-end delivery</p>
  </div>
  <aside class="profile-card" aria-label="Current role">
    <div class="portrait-wrap"><img src="{{ '/images/profile_pic_2025dec.jpg' | relative_url }}" width="1600" height="1600" alt="Portrait of Jintao Li" fetchpriority="high"></div>
    <div class="profile-caption"><span class="caption-label">Current role</span><h2>Data Science Manager</h2><p>Digital Solution Unit Leader<br>Ocean Network Express<br>Leading six data scientists</p><div class="profile-location"><span class="location-dot" aria-hidden="true"></span> Singapore · Global headquarters</div></div>
  </aside>
</section>

<div class="credentials-strip" aria-label="Industry experience">
  <span>Industry experience.<br><strong>Hands-on technical delivery.</strong></span>
  <p>Ocean Network Express <small>Forecasting & operational planning</small></p>
  <p>Google Cloud <small>Internal tools deployed end to end</small></p>
  <p>6 data scientists <small>Technical direction & mentoring</small></p>
</div>

<section class="section" aria-labelledby="focus-heading">
  <div class="section-heading"><div><p class="eyebrow">Selected work & impact</p><h2 id="focus-heading">Models that support<br>operational decisions.</h2></div><p>Forecast accuracy, operating costs, and tools delivered to internal users.</p></div>
  <div class="focus-grid">
    {% for area in site.data.profile.focus %}
    <article class="focus-card"><span class="card-number">{{ area.number }}</span><h3><a href="{{ '/work/' | relative_url }}#{{ area.id }}">{{ area.title }}</a></h3><p>{{ area.description }}</p><ul class="tags" aria-label="Related expertise">{% for tag in area.tags %}<li>{{ tag }}</li>{% endfor %}</ul></article>
    {% endfor %}
  </div>
</section>

<section class="leadership-section section" aria-labelledby="leadership-heading">
  <div class="leadership-intro"><p class="eyebrow">Career focus</p><h2 id="leadership-heading">Hands-on science.<br>Technical ownership.</h2><p>{{ site.data.profile.career_focus }}</p><a class="text-link" href="{{ '/skills/' | relative_url }}">Explore my expertise {% include icon-arrow.html direction="right" %}</a></div>
  <div class="leadership-pillars">
    <article><span class="pillar-label">Modeling & production</span><h3>Forecasting, optimization,<br>and applied ML.</h3><p>Developing models and analytical workflows around real planning constraints, validation needs, and operational decisions.</p></article>
    <article><span class="pillar-label">Technical leadership</span><h3>Direction, review,<br>and delivery.</h3><p>Guiding six data scientists, reviewing analytical approaches, and working with operations and engineering teams to deliver internal tools.</p></article>
  </div>
</section>

<section class="section" aria-labelledby="experience-heading">
  <div class="section-heading"><div><p class="eyebrow">Industry experience</p><h2 id="experience-heading">From data science<br>to technical leadership.</h2></div><a class="text-link" href="{{ '/cv/' | relative_url }}">Read my full experience {% include icon-arrow.html direction="right" %}</a></div>
  {% include experience.html compact=true %}
</section>
{% include contact-card.html %}

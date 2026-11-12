# Jintao Li | Personal Website

Source for [li-jintao.github.io](https://li-jintao.github.io), a compact personal site focused on **forward-deployed engineering, cloud delivery, applied ML, and supply chain management**.

## Pages and content

| Page | Source |
| --- | --- |
| About | `_pages/about.md` |
| Selected Work | `_pages/work.html` |
| CV | `_pages/cv.md` |
| Skills | `_pages/skills.md` |
| Research & illustrations | `_pages/research.md` |

Shared experience and education data are in `_data/profile.yml`. Navigation is in `_data/navigation.yml`.

Design is intentionally text-first. The sole stylesheet is `assets/css/career.css`. Shared layout files live in `_layouts/` and `_includes/`.

## Images

- `images/profile.png`: profile photograph shared by the site and SEO metadata.
- `images/research-overview.png`: research illustration shown directly on the research page.
- `images/research-overview.pdf`: full-resolution research illustration.
- `assets/images/monogram.svg`: favicon.

Change the profile picture once in `images/profile.png`; the sidebar and metadata reference this same file. Research illustrations should remain directly visible.

## Local development

This repository uses Ruby `4.0.9`, Jekyll `4.4.1`, and Bundler, with versions tracked in `.ruby-version` and `Gemfile.lock`.

```sh
gem install bundler --version 4.0.23
bundle install
bundle exec jekyll serve --config _config.yml,_config.dev.yml
```

Validate the production build before publishing:

```sh
JEKYLL_ENV=production bundle exec jekyll build --trace
python3 script/check_site.py _site
```

Pushes to `master` trigger the GitHub Actions workflow at `.github/workflows/pages.yml` to build, validate, and deploy GitHub Pages. Pull requests build and validate without deploying.

## Maintenance and legacy sources

The repository started from Academic Pages, itself derived from Minimal Mistakes. The active website now uses a small custom layout and does not load those templates' JavaScript, Sass, or demo pages. The unused source files were removed from the live branch after archiving the pre-cleanup state in `archive/pre-cleanup-2026-11-12`. Git history also preserves them.

Keep job titles and technical accomplishments accurate. Avoid internal metrics, confidential operational rules, and unsupported quantitative claims.

## Attribution

Originally based on [Academic Pages](https://github.com/academicpages/academicpages.github.io) and [Minimal Mistakes](https://github.com/mmistakes/minimal-mistakes). See [LICENSE](LICENSE) for inherited license terms.

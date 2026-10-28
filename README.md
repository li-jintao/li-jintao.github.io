# Jintao Li — Data Science & Technical Leadership

A personal site for applied data science, decision systems, and technical leadership. The overview, selected work, experience, and expertise pages lead with industry outcomes and technical ownership. Publications are available as supporting background from the footer. Experience, results, skills, and qualifications are readable directly on the website.

## Development

The site uses **Ruby 4.0.9**, **Jekyll 4.4.1**, and **Bundler 4.0.23**. Ruby is pinned in `.ruby-version`; gem versions and checksums are recorded in `Gemfile.lock`.

With Ruby 4.0.9 installed:

```sh
gem install bundler --version 4.0.23
bundle install
bundle exec jekyll serve --config _config.yml,_config.dev.yml
```

The server rebuilds when content changes. Restart it after changing configuration.

Build and check the production output:

```sh
JEKYLL_ENV=production bundle exec jekyll build --trace
python3 script/check_site.py _site
```

The check covers the four industry pages and the supporting publications page, navigation, SEO descriptions and canonical URLs, local links and anchors, legacy redirects, XML feeds, and the 404 page. Python 3 is needed only for this check.

No Node.js build or JavaScript is needed for the career pages. Their content is rendered as HTML with responsive CSS. The old theme's npm scripts and assets remain available for reference.

### Codex cloud environment

The prepared cloud environment retains its runtime and gems outside this checkout. Initialize a shell with:

```sh
source /workspace/.cloud-setup/modern/env.sh
cd /workspace/li-jintao.github.io
bundle exec jekyll serve --config _config.yml,_config.dev.yml --destination /workspace/.cloud-setup/modern/_site --host 127.0.0.1 --port 4000
```

Use the existing checkout; cloud tasks are already isolated. Do not create a Git worktree unless explicitly requested. The environment settings contain the reusable install and startup instructions.

## Positioning

The site is aimed at senior data scientist, applied scientist, and technical-lead opportunities in supply chain forecasting, optimization, and industrial AI. Technically focused data science manager roles are also relevant. Target-role interests are separate from the actual job titles in the experience section.

## Updating content

- `_data/profile.yml`: experience, role descriptions, expertise, education, and languages. Experience is reused on the overview and CV.
- `_pages/about.md`: homepage narrative and structure.
- `_pages/work.html`: problem, contribution, and outcome summaries, using the work entries in `_data/profile.yml`.
- `_pages/cv.md`: professional experience, capabilities, education, and selected publications.
- `_pages/skills.md`: expertise and working approach.
- `_pages/research.md`: research background, publications, and talks.
- `_config.yml`: identity, contact details, canonical site URL, and metadata.
- `assets/css/career.css`: responsive design and print styles.

Keep claims grounded in actual work. Add business impact, team size, deployment scale, and project outcomes only when verified and suitable for public disclosure. Qualitative cost and forecasting results, GCP deployment, and leadership of six data scientists were confirmed by the site owner; no percentage improvements are assumed.

Legacy blog posts, template portfolio and teaching entries, archive pages, and the old talk map are excluded from the published career site in `_config.yml`. Their source files are retained. Selected research talks and publications remain on `/research/`. The old `/about/`, `/resume`, and `/Research/` URLs redirect to the appropriate current page.

## Publishing to GitHub Pages

Jekyll 4 is built with **GitHub Actions**, rather than GitHub Pages' older built-in Jekyll stack.

1. In the repository's **Settings → Pages**, set **Build and deployment → Source** to **GitHub Actions**.
2. Push or merge the changes to `master`. The workflow builds, checks, uploads, and deploys the site.
3. Check the **Build and deploy Jekyll site** run in the Actions tab.

Pull requests run the same build and checks without deploying. The workflow uses GitHub's provided token; no personal access token is needed. The canonical site is configured for `https://li-jintao.github.io`.

## Attribution

Originally based on [Academic Pages](https://github.com/academicpages/academicpages.github.io) and Michael Rose's [Minimal Mistakes](https://github.com/mmistakes/minimal-mistakes). Inherited assets retain their original licensing. See [LICENSE](LICENSE).

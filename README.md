```
smartsync_crawler/
├── app/
│   ├── __init__.py
│   ├── utils/
│   ├── spiders/
│   └── templates/
├── crawler/
│   ├── settings.py
│   ├── items.py
│   └── pipelines.py
├── data/
│   ├── raw/
│   └── processed/
├── tests/
├── pyproject.toml
└── run.py
``


```bash
poetry init --no-interaction --python=^3.11
poetry add flask scrapy pillow python-dotenv

```
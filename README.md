# Wiki_RAG_LLM_App

Project structure:
Wiki_RAG_LLM_App/
├── backend/
│   ├── app/
│   │   ├── __init__.py
│   │   ├── main.py              # FastAPI app initialization
│   │   ├── config/
│   │   │   ├── __init__.py
│   │   │   └── settings.py      # Pydantic settings
│   │   ├── database/
│   │   │   ├── __init__.py
│   │   │   └── session.py       # Database connection setup
│   │   ├── models/
│   │   │   ├── __init__.py
│   │   │   ├── base.py          # SQLModel base models
│   │   │   └── query_history.py # Query history table model
│   │   ├── routers/
│   │   │   ├── __init__.py
│   │   │   ├── api_v1.py        # Main API endpoints
│   │   │   └── wikipedia.py     # Wikipedia-specific endpoints
│   │   ├── schemas/
│   │   │   ├── __init__.py
│   │   │   └── requests.py      # Pydantic request models
│   │   ├── services/
│   │   │   ├── __init__.py
│   │   │   ├── rag.py           # RAG pipeline implementation
│   │   │   ├── wikipedia.py     # Wikipedia API wrapper
│   │   │   └── hf_client.py     # Hugging Face client wrapper
│   │   ├── utils/
│   │   │   ├── __init__.py
│   │   │   ├── logger.py        # Logging configuration
│   │   │   └── text_processing.py # Chunking/cleaning utils
│   │   └── worker.py            # Background task processor
│   ├── alembic/                # Database migrations
│   │   └── versions/
│   ├── requirements/
│   │   ├── base.txt
│   │   ├── dev.txt
│   │   └── prod.txt
│   ├── tests/
│   │   ├── __init__.py
│   │   ├── conftest.py
│   │   ├── test_api.py
│   │   └── test_rag.py
│   ├── Dockerfile
│   └── alembic.ini
│
├── frontend/
│   ├── src/
│   │   ├── __init__.py
│   │   ├── main.py              # Streamlit main app
│   │   ├── components/          # Reusable Streamlit components
│   │   │   ├── __init__.py
│   │   │   ├── chat.py
│   │   │   └── history.py
│   │   └── assets/              # CSS/images
│   ├── requirements.txt
│   └── Dockerfile
│
├── infrastructure/
│   ├── docker-compose.yml       # Postgres/Redis etc
│   └── nginx/
│       └── nginx.conf
│
├── scripts/
│   ├── setup_db.py
│   └── load_test_data.py
│
├── .env.example
├── .gitignore
├── README.md
├── pyproject.toml
└── Makefile

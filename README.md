[![Celery](https://img.shields.io/badge/Celery-37814A?style=for-the-badge&logo=celery&logoColor=white)](https://docs.celeryq.dev/)
[![Python](https://img.shields.io/badge/Python-3.10+-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://www.python.org/)
[![Status](https://img.shields.io/badge/Status-Active-success?style=for-the-badge)]()

The heavy-lifting background worker designed to process search and game-related logic asynchronously. It consumes tasks produced by the `search_game_endpoint` API to ensure high performance and non-blocking operations.

---

## 🏗️ Architecture Overview

This service acts as the backend consumer in the system architecture.

┌────────────────────────┐      Job Queue      ┌────────────────────────┐
│  search_game_endpoint  │ ──────────────────> │  search_game_handler   │
│   (API Entry Point)    │                     │   (Background Worker)  │
└────────────────────────┘                     └────────────────────────┘
│
│ Processes
▼
[Game Logic & Analytics]



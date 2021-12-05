# Sharecipe Backend Server

This repository is the final project submission for 'CSE42101: Database System' in UNIST.

Sharecipe is a web services that offers recipes customized to users' tastes and environments.

Users can post their recipes and tag ingredients, cooking methods, and themes of recipes for search by other users.

Each recipe can be evaluated by users so that the other users can reference those reviews.

# How to Start

## Prerequisites

- Docker
- 'Make' command

## Process

1. Clone this repository to your local machine.

   ```shell
   git clone https://github.com/kmlee78/sharecipe.git;
   cd sharecipe
   ```

2. Run docker compose scripts.
   ```shell
   make dev-up
   ```
3. Run container bash shell.
   ```shell
   make dev-shell
   ```
4. Create base objects for testing.(inside the shell)
   ```shell
   python src/manage.py shell
   ```
   ```python
   from dummy_data import refresh_data()
   refresh_data()
   ```
5. Open signup page with browser.

   - URL: **localhost:8000/users/signup**

# ER Modeling information

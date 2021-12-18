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
3. Open signup page with browser.

   - URL: **localhost:8000/docs**

4. Create base objects by requesting via endpoint named "/create-base-objects".

# ER Modeling information

![KakaoTalk_Image_2021-12-05-19-20-08](https://user-images.githubusercontent.com/41867381/144742587-e7db36a0-9514-42ac-a3fc-3b06d07559b3.jpeg)

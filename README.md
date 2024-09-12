# Preparation
1. `python -m venv .venv` to create virtual environment.
2. `./.venv/Scripts/activate` to activate virtual environment.
3. `python -m pip install -r requirement.txt` to install packages.
4. Install `redis`. `redis` for windows: https://github.com/microsoftarchive/redis/releases (You can use docker if you want)

# Server
1. `./scripts/windows/run.bat` to run django server.
2. `./scripts/windows/run-celery.bat` to run celery in another terminal. (Make sure redis is online)

# Celery test
1. `POST` http://localhost:8000/clip_video. Body example:
  ``` json
    {
      "video_file": "test_video.mp4",
      "clip_name": "clipped.mp4",
      "start_time": "00:00:00",
      "end_time": "00:00:10"
    }
   ```
2. This example function will find a file in `temp` folder.
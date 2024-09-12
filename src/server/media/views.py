from django.shortcuts import render
from django.conf import settings
import os
import math

# Create your views here.
from rest_framework.response import Response
from rest_framework.views import APIView
from .tasks import clip_video


class Clip_Video_API(APIView):

    def get(self, request):
        return Response("GET Clip Video API")

    def post(self, request):

        try:
            data = request.data
            print(data)
            media_dir = os.path.abspath(
                os.path.join(settings.BASE_DIR, "..", "..", "temp")
            )

            print(f"Media: {media_dir}")
            video_file_path = os.path.join(media_dir, data["video_file"])
            clip_path = os.path.join(media_dir, data["clip_name"])

            clip_video.delay(video_file_path, data, clip_path)

            data, st, msg = clip_path, 200, "Video clipped successfully"
        except Exception as error:
            print(error)
            data, st, msg = "", 500, "Error while clipping the video"
        resp_json = {"data": data, "st": st, "msg": msg}
        return Response(resp_json)

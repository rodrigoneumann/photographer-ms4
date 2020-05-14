from django.contrib.auth import views as auth_views
from django.urls import include, path
from .views import (
    all_photos,
    music_view,
    studio_view,
    food_view,
    weeding_view,
    drone_view,
    fineArt_view,
    portfolio,
    all_videos,
    institutional_videos_view,
    shows_videos_view,
    events_videos_view,
    drone_videos_view
)

urlpatterns = [
    path("", portfolio, name="portfolio"),
    path("photos/", all_photos, name="photos"),
    path("photos/music", music_view, name="music"),
    path("photos/studio", studio_view, name="studio"),
    path("photos/food", food_view, name="food"),
    path("photos/weeding", weeding_view, name="weeding"),
    path("photos/drone", drone_view, name="photo_drone"),
    path("photos/fineart", fineArt_view, name="fineart"),
    path("videos/", all_videos, name="videos"),
    path("videos/institutional", institutional_videos_view, name="institutional"),
    path("videos/events", events_videos_view, name="events"),
    path("videos/music", shows_videos_view, name="video_music"),
    path("videos/drone", drone_videos_view, name="drone"),
]

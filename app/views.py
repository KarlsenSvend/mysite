from django.shortcuts import render
from django.views.generic import View, TemplateView
from mysite.views import JsonResponseMixin
from app.models import Song

# Create your views here.
class Songs(JsonResponseMixin, TemplateView):
    http_method_names = ['GET']

    def dispatch(self, request, *args, **kwargs):
        super(Songs, self).dispatch(request, *args, **kwargs)

        str_title = request.REQUEST.get('title')
        sort_by = request.REQUEST.get('sort_by')
        order_by = request.REQUEST.get('order')

        if str_title is None:
            songs = Song.objects.all()
        else:
            if sort_by is not None:
                if order_by is not None:
                    if order_by=="desc":
                        songs = Song.objects.filter(title=str_title).order_by("-{sort_by}".format(sort_by=sort_by))
                    else:
                        songs = Song.objects.filter(title=str_title).order_by("{sort_by}".format(sort_by=sort_by))
                else:
                    songs = Song.objects.filter(title=str_title)
            else:
                songs = Song.objects.filter(title=str_title)


        list_of_songs = list()
        for song in songs:
            list_of_songs.append({"id": song.id, "artist": song.artist, "title": song.title})

        return self.server_only_result({"songs": list_of_songs})

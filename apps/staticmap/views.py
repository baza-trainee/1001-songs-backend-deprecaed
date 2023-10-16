from django.db.models import Count, Q
from rest_framework.generics import GenericAPIView
from rest_framework.response import Response
from rest_framework import status

from apps.songs.models import Song
from apps.songs.serializers import SongSerializer


class MapListView(GenericAPIView):
    """
    List of songs by regions
    """
    @staticmethod
    def get(*args, **kwargs):
        # не работает на версии джанго под рендер
        # result_count = Song.objects.all().values('location__region').annotate(count=Count('location__region'))
        count_region = Song.objects.all().aggregate(
            Рівне=Count('id', filter=Q(location__region='Рівне')),
            Кіровоград=Count('id', filter=Q(location__region='Кіровоград')),
            Полтава=Count('id', filter=Q(location__region='Полтава')),
            Вінниця=Count('id', filter=Q(location__region='Вінниця')),
            Луцьк=Count('id', filter=Q(location__region='Луцьк')),
            Дніпро=Count('id', filter=Q(location__region='Дніпро')),
            Донецк=Count('id', filter=Q(location__region='Донецк')),
            Житомир=Count('id', filter=Q(location__region='Житомир')),
            Ужгород=Count('id', filter=Q(location__region='Ужгород')),
            Запоріжжя=Count('id', filter=Q(location__region='Запоріжжя')),
            Івано_Франківськ=Count('id', filter=Q(location__region='Івано_Франківськ')),
            Київ=Count('id', filter=Q(location__region='Київ')),
            Луганськ=Count('id', filter=Q(location__region='Луганськ')),
            Львів=Count('id', filter=Q(location__region='Львів')),
            Миколаїв=Count('id', filter=Q(location__region='Миколаїв')),
            Одеса=Count('id', filter=Q(location__region='Одеса')),
            Суми=Count('id', filter=Q(location__region='Суми')),
            Тернопіль=Count('id', filter=Q(location__region='Тернопіль')),
            Харьків=Count('id', filter=Q(location__region='Харьків')),
            Херсон=Count('id', filter=Q(location__region='Херсон')),
            Хмельницький=Count('id', filter=Q(location__region='Хмельницький')),
            Черкаси=Count('id', filter=Q(location__region='Черкаси')),
            Чернівці=Count('id', filter=Q(location__region='Чернівці')),
            Чернігів=Count('id', filter=Q(location__region='Чернігів')),
            Крим=Count('id', filter=Q(location__region='Крим')),
        )
        return Response(count_region)


class MapRegionListView(GenericAPIView):
    """
    List of songs in the selected region
    """
    queryset = Song.objects.all()

    def get(self, *args, **kwargs):
        params = self.request.query_params.dict()
        print(params)
        if params:
            songs_region = Song.objects.filter(location__region=params['region'])
            serializer = SongSerializer(instance=songs_region, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response('Specify the search region', status=status.HTTP_404_NOT_FOUND)


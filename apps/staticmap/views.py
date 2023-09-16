from django.db.models import Count, Q
from rest_framework.generics import GenericAPIView
from rest_framework.response import Response
from rest_framework import status

from apps.songs.models import Song
from apps.songs.serializers import SongSerializer


class MapListView(GenericAPIView):
    @staticmethod
    def get(*args, **kwargs):
        # не работает на версии джанго под рендер
        # result_count = Song.objects.all().values('location__region').annotate(count=Count('location__region'))
        count_region = Song.objects.all().aggregate(
            Rivne=Count('id', filter=Q(location__region='Рівне')),
            Kirivograd=Count('id', filter=Q(location__region='Кіровоград')),
            Poltava=Count('id', filter=Q(location__region='Полтава')),
            Vinnitsa=Count('id', filter=Q(location__region='Вінниця')),
            Lutsk=Count('id', filter=Q(location__region='Луцьк')),
            Dnipro=Count('id', filter=Q(location__region='Дніпро')),
            Donetsk=Count('id', filter=Q(location__region='Донецк')),
            Zhytomyr=Count('id', filter=Q(location__region='Житомир')),
            Uzhhorod=Count('id', filter=Q(location__region='Ужгород')),
            Zaporizhia=Count('id', filter=Q(location__region='Запоріжжя')),
            Ivano_Frankivsk=Count('id', filter=Q(location__region='Івано-Франківськ')),
            Kyiv=Count('id', filter=Q(location__region='Київ')),
            Luhansk=Count('id', filter=Q(location__region='Луганськ')),
            Lviv=Count('id', filter=Q(location__region='Львів')),
            Mykolaiv=Count('id', filter=Q(location__region='Миколаїв')),
            Odesa=Count('id', filter=Q(location__region='Одеса')),
            Sumy=Count('id', filter=Q(location__region='Суми')),
            Ternopil=Count('id', filter=Q(location__region='Тернопіль')),
            Kharkiv=Count('id', filter=Q(location__region='Харьків')),
            Kherson=Count('id', filter=Q(location__region='Херсон')),
            Khmelnytskyi=Count('id', filter=Q(location__region='Хмельницький')),
            Cherkasy=Count('id', filter=Q(location__region='Черкаси')),
            Chernivtsi=Count('id', filter=Q(location__region='Чернівці')),
            Chernihiv=Count('id', filter=Q(location__region='Чернігів')),
            Crimea=Count('id', filter=Q(location__region='Крим')),
        )
        return Response(count_region)


class MapRegionListView(GenericAPIView):
    queryset = Song.objects.all()

    def get(self, *args, **kwargs):
        params = self.request.query_params.dict()
        if params:
            songs_region = Song.objects.filter(location__region=params['region'])
            serializer = SongSerializer(instance=songs_region, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response('Specify the search region', status=status.HTTP_404_NOT_FOUND)


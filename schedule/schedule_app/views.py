
from django.shortcuts import render
from .models import Group, Event , Weekday, Schedule
from .forms import GroupForm


def index(request):
    form = GroupForm()
    if request.method == 'POST':
        form = GroupForm(request.POST)
        if form.is_valid():
            selected_group = form.cleaned_data['name']
            schedules = Schedule.objects.filter(group__name=selected_group)
            return render(request, 'schedule_list/schedule_list.html', {'schedules': schedules, 'selected_group': selected_group})
    return render(request, 'index/index.html', {'form': form})

def group_schedule(request, group_id):
    group = Group.objects.get(id=group_id)
    events = group.event_set.all()
    return render(request, 'schedule_app/schedule.html', {'group': group, 'events': events})

def schedule_for_day(request, weekday):
    # Получаем все расписания для заданного дня недели
    schedules = Schedule.objects.filter(weekday__name=weekday)

    # Передаем расписания в шаблон
    return render(request, 'schedule_list/schedule_list.html', {'schedules': schedules})

# from rest_framework.views import APIView
# from rest_framework.response import Response
# from rest_framework import status
# from .models import Group, Event, Weekday, Schedule
# from .serializers import EventSerializer

# class EventList(APIView):
#     def get(self, request):
#         events = Event.objects.all()
#         serializer = EventSerializer(events, many=True)
#         return Response(serializer.data)
# class EventDetail(APIView):
#     def get(self, request, pk):
#         try:
#             event = Event.objects.get(pk=pk)
#         except Event.DoesNotExist:
#             return Response(status=status.HTTP_404_NOT_FOUND)
#         serializer = EventSerializer(event)
#         return Response(serializer.data)

#     def put(self, request, pk): 
#         try:
#             event = Event.objects.get(pk=pk)
#         except Event.DoesNotExist:
#             return Response(status=status.HTTP_404_NOT_FOUND)
#         serializer = EventSerializer(event, data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
#     def delete(self, request, pk):
#         try:
#             event = Event.objects.get(pk=pk)
#         except Event.DoesNotExist:
#             return Response(status=status.HTTP_404_NOT_FOUND)
#         event.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)

# from rest_framework.generics import GenericAPIView
# from rest_framework.mixins import ListModelMixin, CreateModelMixin, RetrieveModelMixin, UpdateModelMixin, DestroyModelMixin
# from .serializers import EventSerializer

# class EventList(GenericAPIView, ListModelMixin, CreateModelMixin):
#     queryset = Event.objects.all()
#     serializer_class = EventSerializer

#     def get(self, request, *args, **kwargs):    
#         return self.list(request, *args, **kwargs)

#     def post(self, request, *args, **kwargs):
#         return self.create(request, *args, **kwargs)

# class EventDetail(GenericAPIView, RetrieveModelMixin, UpdateModelMixin, DestroyModelMixin):
#     queryset = Event.objects.all()
#     serializer_class = EventSerializer

#     def get(self, request, *args, **kwargs):
#         return self.retrieve(request, *args, **kwargs)

#     def put(self, request, *args, **kwargs):
#         return self.update(request, *args, **kwargs)

#     def delete(self, request, *args, **kwargs):
#         return self.destroy(request, *args, **kwargs)

from rest_framework.generics import get_object_or_404
from rest_framework.response import Response
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework import status
from .serializers import EventSerializer

class EventList(ListCreateAPIView):
    queryset = Event.objects.all()
    serializer_class = EventSerializer

    def preform_create(self, serializer):
        group_id = self.kwargs.get('group_id')
        group = get_object_or_404(Group, id=group_id)
        serializer.save(group=group)

        return Response(serializer.data, status=status.HTTP_201_CREATED)

class EventDetail(RetrieveUpdateDestroyAPIView):
    queryset = Event.objects.all()  
    serializer_class = EventSerializer
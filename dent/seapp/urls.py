from django.urls import path
from .views import current_user, UserList

from rest_framework.routers import DefaultRouter
from .views import HistoryViewSet,PatientViewSet,WorkTimesViewSet,VisitViewSet , ReservationView , makeReservation
from django.conf.urls import url

router = DefaultRouter()
router.register('history',HistoryViewSet)
router.register('patient',PatientViewSet)
router.register('worktimes',WorkTimesViewSet)
router.register('visit',VisitViewSet)

urlpatterns = [
    url(r'^reserve/', ReservationView.as_view() ),
    url(r'^make-reserve/', makeReservation.as_view() ),
    path('current_user/', current_user),
    path('users/', UserList.as_view())
]
urlpatterns+=router.urls

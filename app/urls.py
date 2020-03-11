from django.urls import path
from . import views

app_name = 'app'
#    path('', views.MonthCalendar.as_view(), name='month'),
urlpatterns = [
    path('', views.index, name='index'),
    path('month/', views.MonthCalendar.as_view(), name='month'),
    path('month/<int:year>/<int:month>/', views.MonthCalendar.as_view(), name='month'),
    path('week/', views.WeekCalendar.as_view(), name='week'),
    path('week/<int:year>/<int:month>/<int:day>/', views.WeekCalendar.as_view(), name='week'),
    path('week_with_schedule/', views.WeekWithScheduleCalendar.as_view(), name='week_with_schedule'),
    path(
        'week_with_schedule/<int:year>/<int:month>/<int:day>/',
        views.WeekWithScheduleCalendar.as_view(),
        name='week_with_schedule'
    ),
    path(
        'month_with_schedule/',
        views.MonthWithScheduleCalendar.as_view(), name='month_with_schedule'
    ),
    path(
        'month_with_schedule/<int:year>/<int:month>/',
        views.MonthWithScheduleCalendar.as_view(), name='month_with_schedule'
    ),
    path('mycalendar/', views.MyCalendar.as_view(), name='mycalendar'),
    path(
        'mycalendar/<int:year>/<int:month>/<int:day>/', views.MyCalendar.as_view(), name='mycalendar'
    ),
    path(
        'month_with_forms/',
        views.MonthWithFormsCalendar.as_view(), name='month_with_forms'
    ),
    path(
        'month_with_forms/<int:year>/<int:month>/',
        views.MonthWithFormsCalendar.as_view(), name='month_with_forms'
    ),
    path('schedule_delete/<int:schedule_id>', views.scheduleDelete, name='schedule_delete'),
    path('memo/', views.memo, name='memo'),
    path('memo_detail/<int:memo_id>', views.memoDetail, name='memo_detail'),
    path('memo_create/', views.memoCreate, name='memo_create'),
    path('memo_delete/<int:memo_id>', views.memoDelete, name='memo_delete'),
    path('memo_edit/<int:memo_id>', views.memoEdit, name='memo_edit'),
]

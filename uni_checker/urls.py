from django.urls import path
from .views import(
    ItemUpdateView,
    IndexView,
    ItemCreateView,
    ItemDestructView,
    RowBoolChangeView,
    ExamView,
    RowDeleteView,
    ItemReadQuestionIncrease,
    ItemReadQuestionDecrease,
)

app_name = 'uni_checker'

urlpatterns = [
    path('', IndexView.as_view(), name='main_editor'),
    path('<int:pk>/', ItemUpdateView.as_view(), name='item_update'),
    path('new/', ItemCreateView.as_view(), name='new_item'),
    path('delete_item/<int:pk>/', ItemDestructView.as_view(), name='item_delete'),
    path('change_row_bool/<int:pk>/', RowBoolChangeView.as_view(), name='row_bool_change'),
    path('read_question_increase/<int:pk>/', ItemReadQuestionIncrease.as_view(), name='read_question_increase'),
    path('read_question_decrease/<int:pk>/', ItemReadQuestionDecrease.as_view(), name='read_question_decrease'),
    path('exam_mode/', ExamView.as_view(), name='exam_mode'),

    # isn't complete
    path('row_delete/<int:pk>/', RowDeleteView.as_view(), name='row_delete'),
]
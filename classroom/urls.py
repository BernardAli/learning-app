from django.urls import path
from .views import index, categories, category_courses, new_course, edit_course, \
    delete_course, enroll, my_courses, course_details
from module.views import new_module, course_modules
from page.views import new_page_module, page_detail
from quiz.views import new_quiz, new_question, quiz_detail, take_quiz, \
    submit_attempt, attempt_detail

urlpatterns = [
    # Course - Classroom views
    path('newcourse/', new_course, name='newcourse'),
    path('mycourses/', my_courses, name='my-courses'),
    path('categories/ ', categories, name='categories'),
    path('categories/<category_slug>/', category_courses, name='category-courses'),
    path('<course_id>/', course_details, name='course'),
    path('<course_id>/enroll/', enroll, name='enroll'),
    path('<course_id>/edit/', edit_course, name='edit-course'),
    path('<course_id>/delete/', delete_course, name='delete-course'),

    # Modules
    path('<course_id>/modules/', course_modules, name='modules'),
    path('<course_id>/modules/newmodule', new_module, name='new-module'),

    # Pages
    path('<course_id>/modules/<module_id>/pages/new_page/', new_page_module, name='new-page'),
    path('<course_id>/modules/<module_id>/pages/<page_id>/', page_detail, name='page-detail'),

    # Quiz
    path('<course_id>/modules/<module_id>/quiz/newquiz/', new_quiz, name='new-quiz'),
    path('<course_id>/modules/<module_id>/quiz/<quiz_id>/newquestion', new_question, name='new-question'),
    path('<course_id>/modules/<module_id>/quiz/<quiz_id>/', quiz_detail, name='quiz-detail'),
    path('<course_id>/modules/<module_id>/quiz/<quiz_id>/take', take_quiz, name='take-quiz'),
    path('<course_id>/modules/<module_id>/quiz/<quiz_id>/take/submit', submit_attempt, name='submit-quiz'),
    path('<course_id>/modules/<module_id>/quiz/<quiz_id>/<attempt_id>/result', attempt_detail, name='attempt-detail'),
]
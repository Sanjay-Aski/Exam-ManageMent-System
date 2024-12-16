from django.urls import path
from universities import views as university_view

urlpatterns = [
    path(
        "manage-university-ins",
        university_view.manage_university_ins_fn,
        name="manage_university_ins",
    ),
    path(
        "manage-university-upd/<int:university_id>",
        university_view.manage_university_upd_fn,
        name="manage_university_upd",
    ),
    path(
        "manage-university-del/<int:uni_id>",
        university_view.manage_university_del_fn,
        name="manage_university_del",
    ),
    path(
        "manage-university-sel",
        university_view.manage_university_sel_fn,
        name="manage_university_sel",
    ),
]

from django.urls import path
from institutes import views as institute_view

urlpatterns = [
    # Institute_with_Inst_Type
    path(
        "manage-inst-with-inst-type-ins",
        institute_view.manage_inst_with_inst_type_ins_fn,
        name="manage_inst_with_inst_type_ins_fn",
    ),
    path(
        "manage-inst-with-inst-type-del/<int:inst_with_inst_type_id>",
        institute_view.manage_inst_with_inst_type_del_fn,
        name="manage_inst_with_inst_type_del_fn",
    ),

    # Institute_detail
    path(
        "manage-inst-ins",
        institute_view.manage_inst_ins_fn,
        name="manage_inst_ins",
    ),
    path(
        "manage-inst-upd/<int:inst_id>",
        institute_view.manage_inst_upd_fn,
        name="manage_inst_upd",
    ),
    path(
        "manage-inst-del/<int:inst_id>",
        institute_view.manage_inst_del_fn,
        name="manage_inst_del",
    ),
    path(
        "manage-ra-ins",
        institute_view.manage_ra_ins_fn,
        name="manage_ra_ins",
    ),
    path(
        "manage-ra-upd/<int:ra_id>",
        institute_view.manage_ra_upd_fn,
        name="manage_ra_upd",
    ),
    path(
        "manage-ra-del/<int:ra_id>",
        institute_view.manage_ra_del_fn,
        name="manage_ra_del",
    ),
    path(
        "manage-ra-view",
        institute_view.manage_ra_view_fn,
        name="manage_ra_view",
    ),
]

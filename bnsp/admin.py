from django.contrib import admin, messages
from django.http.response import HttpResponseRedirect
from django.utils.translation import ngettext

from francedata.services.django_admin import (
    TimeStampModelAdmin,
    view_reverse_changelink,
)

from bnsp import models


@admin.register(models.Query)
class QueryAdmin(TimeStampModelAdmin):
    change_form_template = "bnsp/admin/query_changeform.html"

    search_fields = ("name", "query")
    list_display = (
        "__str__",
        "last_polled",
        "view_documents_link",
    )
    list_filter = ("source",)

    readonly_fields = [
        "id",
        "created_at",
        "updated_at",
        "view_documents_link",
    ]

    fieldsets = [
        (
            None,
            {
                "fields": [
                    "name",
                    ("query", "is_active"),
                    "source",
                    "view_documents_link",
                ]
            },
        ),
        (
            "Ajout de métadonnées",
            {
                "fields": [
                    "identify_regions",
                    "identify_departements",
                    "identify_metropoles",
                    "identify_main_cities",
                ]
            },
        ),
        (
            "Exécution",
            {
                "fields": [
                    "last_polled",
                    "last_success",
                    "last_change",
                ]
            },
        ),
        ("Métadonnées", {"fields": ["id", "created_at", "updated_at"]}),
    ]

    actions = ["force_run_queries"]

    def view_documents_link(self, obj):
        return view_reverse_changelink(obj, "core", "bnsp_query", "document")

    view_documents_link.short_description = "Documents"

    # Force immediate execution of query on the admin detail view
    def response_change(self, request, obj):
        if "_force_run_query" in request.POST:
            obj.run()
            return HttpResponseRedirect(".")  # stay on the same detail page
        return super().response_change(request, obj)

    # Force immediate execution of queries on the admin list view
    @admin.action(description="Lancer les requêtes maintenant")
    def force_run_queries(self, request, queryset):
        for q in queryset:
            q.run()

        updated = len(queryset)

        self.message_user(
            request,
            ngettext(
                "%d requête a été exécutée avec succès.",
                "%d requêtes ont été exécutées avec succès.",
                updated,
            )
            % updated,
            messages.SUCCESS,
        )

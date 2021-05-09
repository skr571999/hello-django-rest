from django.contrib import admin

from .models import User, Company, Country


class UserAdmin(admin.ModelAdmin):
    list_display = ('name', "is_seller", "email", "mobile_no")

    # def active(self, obj):
    #     return obj.is_active == 1

    # active.boolean = True

    # def make_active(modeladmin, request, queryset):
    #     queryset.update(is_active=1)
    #     messages.success(
    #         request, "Selected Record(s) Marked as Active Successfully !!")

    # def make_inactive(modeladmin, request, queryset):
    #     queryset.update(is_active=0)
    #     messages.success(
    #         request, "Selected Record(s) Marked as Inactive Successfully !!")

    # admin.site.add_action(make_active, "Make Active")
    # admin.site.add_action(make_inactive, "Make Inactive")

    # To Remove the Add User Button
    def has_add_permission(self, request):
        return False


admin.site.register(User, UserAdmin)
admin.site.register(Company)
admin.site.register(Country)

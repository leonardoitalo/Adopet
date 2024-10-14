from rest_framework import permissions


class ShelterPermissions(permissions.BasePermission):
    """
    Custom permission to allow only shelters to exclude adoptions.
    """

    def has_permission(self, request, view):
        # Allow all users access to view adoptions
        if request.method in permissions.SAFE_METHODS:  # GET, HEAD, OPTIONS
            return True

        # The user needs to be authenticated and be a shelter
        return (
            request.user.is_authenticated
            and request.user.groups.filter(name="Shelter").exists()
        )

    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:  # GET, HEAD, OPTIONS
            return True

        return (
            request.method in ["DELETE", "PUT"]
            and request.user.groups.filter(name="Shelter").exists()
        )


class AllowAnyForCreateOtherwiseAuthenticated(permissions.BasePermission):
    """
    Custom permission to allow any user to create but requires authentication for other actions.
    """

    def has_permission(self, request, view):
        # Allow any user to create (POST)
        if request.method == "POST":
            return True

        # For other methods, require the user to be authenticated
        return request.user.is_authenticated

from rest_framework import permissions


class ShelterPermissions(permissions.BasePermission):
    """
    Permissão personalizada para permitir que apenas abrigos excluam adoções.
    """

    def has_permission(self, request, view):
        # Permitir que todos os usuários tenham acesso para visualizar as adoções
        if request.method in permissions.SAFE_METHODS:  # GET, HEAD, OPTIONS
            return True

        # O usuário precisa estar autenticado e ser um abrigo
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
    Permissão personalizada para permitir que
    qualquer usuário tenha permissão do método POST, mas requer autenticação para outras ações.
    """

    def has_permission(self, request, view):
        # Allow any user to create (POST)
        if request.method == "POST":
            return True

        # For other methods, require the user to be authenticated
        return request.user.is_authenticated

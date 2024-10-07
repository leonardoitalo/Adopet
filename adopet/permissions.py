from rest_framework import permissions

class IsShelterAndCanDeleteAdoption(permissions.BasePermission):
    """
    Custom permission to allow only shelters to exclude adoptions.
    """

    def has_permission(self, request, view):
        # Allow all users access to view adoptions 
        if request.method in permissions.SAFE_METHODS:  # GET, HEAD, OPTIONS
            return True
        
        # Allow all users to create an adoption(POST)
        if request.method == 'POST':
            return True
        
        # The user needs to be authenticated and be a shelter
        return request.user.is_authenticated and request.user.groups.filter(name='Shelter').exists()

    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:  # GET, HEAD, OPTIONS
            return True
        
        return request.method == 'DELETE' and request.user.groups.filter(name='Shelter').exists()
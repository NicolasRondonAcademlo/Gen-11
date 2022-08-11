from rest_framework.permissions import BasePermission, IsAuthenticated, SAFE_METHODS

#
# class IsLibraryUser(BasePermission):
#     """
#     Allows access only to admin users.
#     """
#
#     def has_permission(self, request, view):
#         return bool(request.user and request.user.is_staff)

class IsLibraryUser(BasePermission):
    """
    The request is authenticated as a user, or is a read-only request.
    """

    def has_permission(self, request, view):
        if request.user.is_staff:
            return True
        else:
            return bool(
                request.method in SAFE_METHODS or
                request.user and
                request.user.is_authenticated
            )

class IsRentForAnother(BasePermission):

    def has_object_permission(self,  request, view, obj):

        if obj.is_rent:
            if request.user.is_staff:
                return True
            elif request.user == obj.member:
                return True
            else:
                return False
        else:
            if request.user.is_staff:
                return True
            else:
                return False


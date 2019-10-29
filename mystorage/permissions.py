from rest_framework import permissions

class IsAuthorOrReadonly(permissions.BasePermission):

    def has_permission(self, request, view):
        
        return request.user.is_authenticated # 인증된(관리자,유저) 유저만 볼수있게

    def has_object_permission(self, request, view, obj):

        if request.method in permissions.SAFE_METHODS:
            return True

        # DELETE 요청에 대해 관리자일 경우에만 삭제 가능
        if request.method == 'DELETE':  
            return request.user.is_superuser
           #return request.user.is_staff

        # PUT 요청에 대해 작성자일 경우에만 요청 허용
        if request.method == 'PUT':
            return obj.author == request.user
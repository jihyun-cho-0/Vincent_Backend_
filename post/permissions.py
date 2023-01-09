from rest_framework import permissions 

class IsAuthorOrReadonly(permissions.BasePermission): 

    def has_permission(self, request, view): # 인증된 사용자에 한하여 목록조회/포스트 등록 가능
        return request.user and request.user.is_authenticated

    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS: # GET, OPTION, HEAD 요청일 때는 그냥 허용
            return True
        return obj.author == request.user # DELETE, PATCH 일 때는 현재 사용자와 객체가 참조 중인 사용자가 일치할 때마다 허용
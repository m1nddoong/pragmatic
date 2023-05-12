from django.contrib.auth.models import User
from django.http import HttpResponseForbidden

def account_ownership_required(func): # decorator 정의 (이 계정의 소유권이 필요하다는 이름)
    def decorated(request, *args, **kwargs): # request 를 받아
        # 우리가 원하는 작업 - 본인인지 확인하는 작업
        # get, post 등의 요청을 받으면서 pk 로 받은 값을 가지고 있는 User 객체가 user 가 되는 것
        user = User.objects.get(pk=kwargs['pk'])
        # pk 를 확인해서 그 User 객체가 실제로 request 를 보낸 user 와 같은지 아닌지 확인
        if not user == request.user: # 유저가 아니라면
            return HttpResponseForbidden()
        return func(request, *args, **kwargs) # 아닌 경우는 그냉 보내주기
    return decorated
    # account_ownership_required 라는 decorator 를 만들었으니까 views.py 에 적용하기
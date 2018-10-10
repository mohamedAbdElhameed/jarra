from rest_framework import viewsets
from .models import MyUser, OrderSchema
from .serializers import MyUserSerializer
from rest_framework.response import Response
# Create your views here.


class MyUserView(viewsets.ModelViewSet):
    def create(self, request, *args, **kwargs):
        my_user = MyUser.objects.filter(processor_id=request.data['processor_id'])
        if len(my_user) == 0:
            mutable = request.POST._mutable
            request.POST._mutable = True
            order = OrderSchema.objects.all()[0]
            order.order_id += 1
            order.save()
            request.data['order_id'] = str(order.order_id)
            request.POST._mutable = mutable
            serializer = self.get_serializer(data=request.data)
            if serializer.is_valid():
                self.perform_create(serializer)
                return Response({
                    'status': 'ok',
                    'msg': 'تم التسجيل بنجاح',
                    'order': order.order_id
                })
            else:
                return Response({
                    'status': 'fail',
                    'msg': 'تسجيلك خاطئ',
                    'order': '00000'
                })
        else:
            return Response({
                    'status': 'fail',
                    'msg': 'لقد قمت بالتسجيل من قبل',
                    'order': '00000'
                })

    queryset = MyUser.objects.all()
    serializer_class = MyUserSerializer

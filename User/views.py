from rest_framework.viewsets import ModelViewSet
from .serializers import InfoSerializer #Dòng này import TodoSerializer từ module serializers cùng thư mục. 
from User.models import Info #import model Todo từ module models trong ứng dụng TodoList. Model Todo đại diện cho một bảng trong cơ sở dữ liệu, với các trường và phương thức tương ứng

class InfoViewSet(ModelViewSet):
    queryset = Info.objects.all()  #Todo.objects.all() lấy tất cả các đối tượng Todo từ cơ sở dữ liệu.
    serializer_class = InfoSerializer #serializer_class xác định lớp serializer sẽ được sử dụng để chuyển đổi giữa các đối tượng Todo và định dạng JSON.
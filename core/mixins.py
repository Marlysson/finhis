
from .serializers import UserSerializer, ProfileSerializer, CategorySerializer, RequestCategorySerializer
from .models import Profile, Category, RequestCategory

class CategoryDataRepeated:
	queryset = Category.objects.all()
	serializer_class = CategorySerializer

class RequestCategoryDataRepeated:
	queryset = RequestCategory.objects.all()
	serializer_class = RequestCategory
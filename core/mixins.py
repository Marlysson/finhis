
from .serializers import UserSerializer, ProfileSerializer, CategorySerializer, RequestCategorySerializer
from .models import Profile, Category, RequestCategory


class ProfileDataRepeated:
	serializer_class = ProfileSerializer
	queryset = Profile.objects.all()

class CategoryDataRepeated:
	serializer_class = CategorySerializer
	queryset = Category.objects.all()

class RequestCategoryDataRepeated:
	serializer_class = RequestCategory
	queryset = RequestCategory.objects.all()
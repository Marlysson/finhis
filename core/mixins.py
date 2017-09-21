
from .serializers import UserSerializer, ProfileSerializer, CategorySerializer, RequestCategorySerializer, MovementSerializer
from .models import Profile, Category, RequestCategory, Movement

class ProfileDataRepeated:
	queryset = Profile.objects.all()
	serializer_class = ProfileSerializer

class MovementDataRepeated:
	queryset = Movement.objects.all()
	serializer_class = MovementSerializer

class CategoryDataRepeated:
	queryset = Category.objects.all()
	serializer_class = CategorySerializer

class RequestCategoryDataRepeated:
	queryset = RequestCategory.objects.all()
	serializer_class = RequestCategory
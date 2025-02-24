from drf_spectacular.utils import (
    extend_schema_view,
    extend_schema,
    OpenApiParameter,
    OpenApiTypes,
)

from rest_framework import (
    viewsets,
    mixins,
    status,
)
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from django.utils.translation import gettext as _
from django.utils.translation import activate
from core.models import Product
from product import serializers

class ProductViewSet(viewsets.ModelViewSet):
    """View for manage recipe APIs."""
    serializer_class = serializers.ProductSerializer
    queryset = Product.objects.all()
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]
    

    def get_serializer_class(self):
        """Return the serializer class for request."""
        if self.action == 'list':
            return serializers.ProductSerializer
        return self.serializer_class

    def perform_create(self, serializer):
        """Create a new product."""
        serializer.save(user=self.request.user)


class BaseProductAttrViewSet(mixins.DestroyModelMixin,
                            mixins.UpdateModelMixin,
                            mixins.ListModelMixin,
                            viewsets.GenericViewSet):
    """Base viewset for product  attributes."""
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

class ChangeLanguageView(APIView):
    def post(self, request):
        language = request.data.get("language")
        if language:
            activate(language)
            return Response({"message": _("Language changed successfully.")})
        return Response({"error": _("Language not provided.")}, status=400)

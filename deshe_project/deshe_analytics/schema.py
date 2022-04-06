import graphene
from graphene_django import DjangoObjectType
from .models import Stock

class StockType(DjangoObjectType):
    class Meta:
        model = Stock
        fields = '__all__'

class Query(graphene.ObjectType):
    get_all_stock = graphene.List(StockType)
    def resolve_get_all_stock(root, info):
        return Stock.objects.all()

schema = graphene.Schema(query=Query)

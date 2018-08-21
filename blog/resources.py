from import_export import resources
from .models import Ymon
from .models import Person

class YmonResource(resources.ModelResource):
    class Meta:
        model = Ymon
        

class PersonResource(resources.ModelResource):
    class Meta:
        model = Person
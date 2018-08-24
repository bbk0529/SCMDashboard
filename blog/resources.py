from import_export import resources
from .models import Ymon


class YmonResource(resources.ModelResource):
    class Meta:
        model = Ymon
        

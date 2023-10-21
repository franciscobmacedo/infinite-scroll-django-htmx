from django.views.generic import ListView
from core.models import Product

class HomeView(ListView):
    model = Product
    template_name = "core/index.html"
    context_object_name = "products"
    paginate_by = 10
    ordering = "pk"

    def get_template_names(self, *args, **kwargs):
        if self.request.htmx:
            return "core/product-list.html"
        else:
            return self.template_name

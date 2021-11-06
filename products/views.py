from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, DeleteView, UpdateView
from products.models import Product, Category
from products.forms import ProductCreateForm, CategoryCreateForm
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from django.http import Http404, HttpResponse
from django.shortcuts import redirect


@method_decorator(login_required(login_url='/user/login/'), name='dispatch')
class ProductListView(ListView):
    template_name = 'product/dashboard.html'
    queryset = Product.objects.all().order_by('-updated_at')


@method_decorator(login_required(login_url='/user/login/'), name='dispatch')
class ProductDetailView(DetailView):
    template_name = 'product/detail_product.html'
    queryset = Product.objects.all().order_by('-updated_at')


@method_decorator(login_required(login_url='/user/login/'), name='dispatch')
class ProductCreateView(CreateView):
    template_name = 'product/new_product.html'
    form_class = ProductCreateForm
    success_url = '/dashboard/'
    queryset = Product.objects.all()

    def get_initial(self):
        initial = super(ProductCreateView, self).get_initial()
        initial.update({'seller': self.request.user})
        return initial

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.seller = self.request.user
        self.object.save()

        return super(ProductCreateView, self).form_valid(form)


@method_decorator(login_required(login_url='/user/login/'), name='dispatch')
class CategoryCreateView(CreateView):
    template_name = 'product/new_category.html'
    form_class = CategoryCreateForm
    success_url = '/dashboard/'
    queryset = Category.objects.all()


@method_decorator(login_required(login_url='/user/login/'), name='dispatch')
class ProductDeleteView(DeleteView):
    template_name = 'product/delete_product.html'
    success_url = '/dashboard/'
    queryset = Product.objects.all()

    def dispatch(self, request, *args, **kwargs):
        obj = self.get_object()
        if obj.seller.id != self.request.user.id:
            raise Http404('You\'re not allowed to delete this product!')
        return super(ProductDeleteView, self).dispatch(request, *args, **kwargs)


@method_decorator(login_required(login_url='/user/login/'), name='dispatch')
class ProductUpdateView(UpdateView):
    template_name = 'product/edit_product.html'
    form_class = ProductCreateForm
    success_url = '/dashboard/'
    queryset = Product.objects.all()

    def dispatch(self, request, *args, **kwargs):
        obj = self.get_object()
        if obj.seller.id != self.request.user.id:
            raise Http404('You\'re not allowed to edit this product!')
        return super(ProductUpdateView, self).dispatch(request, *args, **kwargs)

    def get_initial(self):
        initial = super(ProductUpdateView, self).get_initial()
        initial.update({'seller': self.request.user})
        return initial

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.seller = self.request.user
        self.object.save()

        return super(ProductUpdateView, self).form_valid(form)


def search_view(request):
    query = request.GET.get('q', None)
    user = None
    context = {'query': query}
    if request.user.is_authenticated:
        user = request.user
    if query.strip():
        products = Product.objects.filter(name__contains=query).order_by('-updated_at')
        context['object_list'] = products
        return render(request, 'product/dashboard.html', context)
    else:
        response = redirect('/dashboard/')
        return response

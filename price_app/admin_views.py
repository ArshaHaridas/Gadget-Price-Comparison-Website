

from django.shortcuts import  render
from django.views.generic import TemplateView

from price_app.models import Comments


def IndexView(request):
    return render(request, 'admin/admin_index.html', {})

class View_Comment(TemplateView):
    template_name='admin/comments.html'
    def get_context_data(self, **kwargs):
        context = super(View_Comment,self).get_context_data(**kwargs)

        commen = Comments.objects.all()

        context['commen'] = commen
        return context
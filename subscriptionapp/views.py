from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404

# Create your views here.
from django.urls import reverse
from django.utils.decorators import method_decorator
from django.views.generic import RedirectView, ListView

from articleapp.models import Article
from projectapp.models import Project
from subscriptionapp.models import Subscription

@method_decorator(login_required, 'get')
# 폼 같은 요청을 받을 부분 없이 처리하므로 RedirectView 사용
class SubscriptionView(RedirectView):
    def get_redirect_url(self, *args, **kwargs):
        return reverse('projectapp:detail', kwargs={'pk': self.request.GET.get('project_pk')})

    def get(self, request, *args, **kwargs):
        # project가 없으면 404 페이지 이동
        project = get_object_or_404(Project, pk=request.GET.get('project_pk'))
        user = self.request.user

        subscription = Subscription.objects.filter(project=project, user=user)

        if subscription.exists():
            subscription.delete()
        else:
            Subscription(user=user, project=project).save()

        return super(SubscriptionView, self).get(request, *args, **kwargs)

@method_decorator(login_required, 'get')
class SubscriptionListView(ListView):
    model = Article
    template_name = 'subscriptionapp/list.html'
    context_object_name = 'article_list'
    paginate_by = 5

    def get_queryset(self):
        projects = Subscription.objects.filter(user=self.request.user).values_list('project')
        print(projects)
        article_list = Article.objects.filter(project__in=projects)
        print(article_list)
        return article_list
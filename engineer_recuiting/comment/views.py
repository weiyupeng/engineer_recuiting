from django.views.generic import UpdateView
from django.core.urlresolvers import reverse_lazy
from django.http import HttpResponseRedirect

from engineer_recuiting.comment.models import Comment,DepartmentComment,EngieerComment
# Create your views here.

class EngineerAutherMinix(object):
    '''only the engineer who finished this transaction can put her/his comment '''
    def dispatch(self, request, *args, **kwargs):
        comment=Comment.objects.get(id=int(self.kwargs['pk']))
        if self.request.user.id != comment.application.applier.id:
            return HttpResponseRedirect('/not leagall')

        return super(EngineerAutherMinix,self).dispatch(request, *args, **kwargs)

class EngineerCommentView(EngineerAutherMinix,UpdateView):

    form_class = EngieerComment
    model = Comment
    template_name = 'create_comment.html'
    success_url = reverse_lazy('view_history')


class DepartmentAutherMinix(object):
    '''only the department who finished this transaction can put her/his comment '''
    def dispatch(self, request, *args, **kwargs):
        comment=Comment.objects.get(id=int(self.kwargs['pk']))
        if self.request.user.id != comment.application.recruitment.department.id:
            return HttpResponseRedirect('not leagal')

        return super(DepartmentAutherMinix, self).dispatch(request, *args, **kwargs)

class DepartmentCommentView(DepartmentAutherMinix,UpdateView):

    form_class = DepartmentComment
    template_name = 'create_comment.html'
    model = Comment
    success_url = reverse_lazy('view_history')

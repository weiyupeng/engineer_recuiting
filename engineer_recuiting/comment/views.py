from django.shortcuts import render
from django.views.generic import UpdateView
from django.core.urlresolvers import reverse_lazy

from engineer_recuiting.comment.models import Comment,DepartmentComment,EngieerComment
# Create your views here.
class EngineerCommentView(UpdateView):

    form_class = EngieerComment
    model = Comment
    template_name = 'create_comment.html'
    success_url = reverse_lazy('view_history')


class DepartmentCommentView(UpdateView):

    form_class = DepartmentComment
    template_name = 'create_comment.html'
    model = Comment
    success_url = reverse_lazy('view_history')

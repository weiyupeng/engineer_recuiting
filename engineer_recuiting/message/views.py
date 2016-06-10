from django.shortcuts import render
from django.db.models import Q
from django.core.urlresolvers import reverse_lazy
from django.views.generic import FormView,TemplateView
from django.contrib.auth.models import User

from engineer_recuiting.message.models import MessageForm,Message
# Create your views here.
class SendMessageView(FormView):

    form_class = MessageForm
    template_name = 'conversation.html'
    # success_url = reverse_lazy('',
    #                            {self.args})
    def get_success_url(self):

        return  reverse_lazy('sending_message',kwargs={'id':self.kwargs['id']})

    # def get_context_data(self, **kwargs):
    #
    #     context=super(SendMessageView,self).get_context_data(**kwargs)
    #     user1=User.objects.get(id=self.request.user.id)
    #     user2=User.objects.get(id=int(self.kwargs['id']))
    #     context['conversations']=get_conversations(user1,user2)
    #     return context
    def get(self, request, *args, **kwargs):
        context={}
        user1=User.objects.get(id=self.request.user.id)
        user2=User.objects.get(id=int(self.kwargs['id']))
        context['conversations']=get_conversations(user1,user2)
        context['form']=self.form_class()
        return render(self.request,'conversation.html',context)

    def form_valid(self, form):
        context={}
        user1=User.objects.get(id=self.request.user.id)
        user2=User.objects.get(id=int(self.kwargs['id']))
        form=self.form_class(self.request.POST)
        instance=form.save(commit=False)
        instance.from_user=User.objects.get(id=self.request.user.id)
        instance.to_user=User.objects.get(id=int(self.kwargs['id']))
        instance.save()

        context['conversations']=get_conversations(user1,user2)
        context['form']=self.form_class()
        return render(self.request,'conversation.html',context)

class MessageBoxView(TemplateView):

    template_name ='message_box.html'

    def get_context_data(self, **kwargs):

        context=super(MessageBoxView,self).get_context_data(**kwargs)
        user=User.objects.get(id=self.request.user.id)

        context['reminder']=reminder(user)
        context['unread_message']=get_unread_messages(user)
        context['recently_contactor']=get_recently_contactor(user)

        return context

def get_conversations(user1,user2):
    conversations=Message.objects.filter((Q(from_user=user1)&Q(to_user=user2))|
                                        (Q(from_user=user2)&Q(to_user=user1))).order_by('time')
    for each in conversations:
        each.is_read=True
        each.save()
    return conversations

def get_unread_messages(user1):
    unread_messages=Message.objects.filter(to_user=user1,is_read=False)
    return unread_messages

def reminder(user):
    return Message.objects.filter(to_user=user,is_read=False).count()

def get_recently_contactor(user):
    rencently_messages=Message.objects.filter(Q(from_user=user))
    to_user_ids=rencently_messages.values_list('to_user').distinct()
    users=User.objects.filter(id__in=to_user_ids)
    return users

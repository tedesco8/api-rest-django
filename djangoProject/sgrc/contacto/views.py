
from rest_framework import viewsets,status
from django.core.mail import send_mail
from django.http import HttpResponse
from rest_framework.decorators import action
from django.views.decorators.csrf import csrf_protect

#debugger
import pdb

pdb.set_trace()

class sendemailViewSet(viewsets.ModelViewSet):
    authentication_classes = ()
    permission_classes = ()

    @csrf_protect
    @action(detail=True,methods=['POST'])
    def sendmail(self, request):
        pdb.set_trace()

        subject = request.POST.get('subject', '')
        message = request.POST.get('message', '')
        from_email = request.POST.get('from_email', '')
        
        if subject and message and from_email:
            try:
                pdb.set_trace()
                send_mail(
                    subject,
                    message,
                    from_email,
                    ['contacto@outboxdev.net'],
                    fail_silently=False,
                )
                return HttpResponse('Mail successfully send')
            except BadHeaderError:
                pdb.set_trace()
                return HttpResponse('Invalid header found.')
        else:
            pdb.set_trace()
            return HttpResponse('Make sure all fields are entered and valid.')
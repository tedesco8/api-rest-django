
from rest_framework import viewsets,status
from django.core.mail import send_mail
from django.http import HttpResponse
from rest_framework.decorators import action



class send_email(viewsets.ModelViewSet):

    @action(detail=True,methods=['POST',])
    def sendmail(request):

        subject = request.POST.get('subject', '')
        message = request.POST.get('message', '')
        from_email = request.POST.get('from_email', '')
        if subject and message and from_email:
            try:
                send_mail(
                    subject,
                    message,
                    from_email,
                    ['contacto@outboxdev.net'],
                    fail_silently=False,
                )
                return HttpResponse('Mail successfully send')
            except BadHeaderError:
                return HttpResponse('Invalid header found.')
        else:
            return HttpResponse('Make sure all fields are entered and valid.')
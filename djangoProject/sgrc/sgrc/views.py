
from rest_framework import viewsets,status
from django.core.mail import send_mail
from django.http import HttpResponse



class send_email(viewsets.ModelViewSet):
    def sendmail(request):
    
        send_mail(
            'Subject',
            'Email message',
            'from@example.com',
            ['to@example.com'],
            fail_silently=False,
        )

        return HttpResponse('Mail successfully send')
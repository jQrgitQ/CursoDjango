from unittest import loader

from django.http import HttpResponse

from members.modelos.teacher.models import Teacher

"""
def get_teachers(request):
  #template = loader.get_template('myfirst.html')
  #return HttpResponse(template.render())

  teachers = Teacher.objects.all().values()
  template = loader.get_template('teachers.html.html')
  context = {
    'teachers': teachers,
  }
  return HttpResponse(template.render(context, request))
  
"""
#import Member
from cProfile import Profile

from django.contrib import admin
from members.models import Member
#from members.modelos.teacher.models import Teacher

# Register your models here.
admin.site.register(Member)
#admin.site.register(Teacher)
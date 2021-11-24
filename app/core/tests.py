import sys, os
myDir = os.getcwd()
sys.path.append(myDir)

from app.wsgi import *

from django.test import TestCase
from core.models import Type

#listar

# query = Type.objects.all()
# print (query)

# Insertar

# type = Type()
# type.name = 'Encargado'
# type.save()

# Edición

# type = Type.objects.get(id=1)
# type.name = "Presidente"
# type.save()

# Eliminar

# type = Type.objects.get(id=4)
# type.delete()

# Listar ***
#obj = Type.objects.filter(name__icontains='pre')
obj = Type.objects.filter(name__startswith='E')
print(obj)



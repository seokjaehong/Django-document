from django.db import models

# Create your models here.
from django.db.models import Manager


class CustomManager(Manager):
    def get_queryset(self):
        print('Custom manager get_queryset!')
        return super().get_queryset()


class OtherManger(Manager):
    def get_queryset(self):
        print('Other manager get_queryset!')
        return super().get_queryset()


class AbstractBase(models.Model):
    objects = CustomManager()

    class Meta:
        abstract = True


class ChildA(AbstractBase):
    pass


class ChildB(AbstractBase):
    default_manager = OtherManger()


class ExtraManagerModel(models.Model):
    extra_manager = OtherManger()

    class Meta:
        abstract = True


class ChildC(AbstractBase, ExtraManagerModel):
    pass


class ChildD(ExtraManagerModel):
    pass

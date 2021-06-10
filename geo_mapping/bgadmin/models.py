from django.db import models


class Oblast(models.Model):
    uid = models.CharField(max_length=16, help_text='')
    oblast = models.CharField(max_length=16)
    ekatte = models.CharField(max_length=8)
    obl_name = models.CharField(max_length=32)
    region = models.CharField(max_length=8)
    document = models.CharField(max_length=8)
    abc = models.CharField(max_length=8)


class Ekatte(models.Model):
    uid = models.CharField(max_length=16)
    ekatte = models.CharField(max_length=8)
    tvm = models.CharField(max_length=8)
    ekatte_name = models.CharField(max_length=32)
    oblast = models.CharField(max_length=16)
    obstina = models.CharField(max_length=16)
    kmetstvo = models.CharField(max_length=16)
    kind = models.CharField(max_length=16)
    category = models.CharField(max_length=16)
    altitude = models.CharField(max_length=16)
    document = models.CharField(max_length=24)
    tsb = models.CharField(max_length=16)
    abc = models.CharField(max_length=16)


class Ekdoc(models.Model):
    uid = models.CharField(max_length=16)
    document = models.CharField(max_length=8)
    doc_kind = models.CharField(max_length=32)
    doc_name = models.CharField(max_length=256)
    doc_inst = models.CharField(max_length=512)
    doc_num = models.CharField(max_length=32)
    doc_date = models.DateField()
    doc_act = models.DateField()
    dv_danni = models.CharField(null=True, blank=True, max_length=16)
    dv_date = models.DateField(null=True, blank=True)


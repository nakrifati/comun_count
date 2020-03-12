from django.db import models


class Com(models.Model):
    electric = models.CharField(max_length=256, default='')
    water_h = models.CharField(max_length=256, default='')
    water_c = models.CharField(max_length=256, default='')
    waste = models.CharField(max_length=256, default='')
    date = models.DateField()

    def __str__(self):
        return "%s %s %s %s %s" % (self.electric, self.water_h, self.water_c, self.waste, self.date)


class ComCost(models.Model):
    electric_cost = models.CharField(max_length=256, default='')
    water_h_cost = models.CharField(max_length=256, default='')
    water_c_cost = models.CharField(max_length=256, default='')
    waste_cost = models.CharField(max_length=256, default='')

    def __str__(self):
        return "%s %s %s %s" % (self.electric_cost, self.water_h_cost, self.water_c_cost, self.waste_cost)




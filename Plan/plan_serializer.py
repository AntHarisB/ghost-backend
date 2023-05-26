from rest_framework import serializers
from PerformanceTab.models import ProjectInformation
from django.db.models import Sum

class PlanSerializer(serializers.Serializer):

    dev_total = serializers.SerializerMethodField()
    design_total =serializers.SerializerMethodField()
    other_total = serializers.SerializerMethodField()
    total_rev_total = serializers.SerializerMethodField()
    neto =  serializers.SerializerMethodField()

    direct_total= serializers.SerializerMethodField()
    indirect_total = serializers.SerializerMethodField()
    marketing_total = serializers.SerializerMethodField()
    HRcost_total = serializers.SerializerMethodField()
    officeCost_total = serializers.SerializerMethodField()
    salesCosts_total = serializers.SerializerMethodField()
    otherCosts_total = serializers.SerializerMethodField()
    expenses = serializers.SerializerMethodField()

    def get_dev_total(self, obj):
        year = self.context['year']
        project = ProjectInformation.objects.filter(year=year).aggregate(dev_total=Sum('development'))
        return round(project['dev_total'], 2)
    
    def get_design_total(self, obj):
        year = self.context['year']
        project = ProjectInformation.objects.filter(year=year).aggregate(design_total=Sum('design'))
        return round(project['design_total'], 2)
    
    def get_other_total(self, obj):
        year = self.context['year']
        project = ProjectInformation.objects.filter(year=year).aggregate(other_total=Sum('other'))
        return round(project['other_total'], 2)

    def get_total_rev_total(self, obj):
        year = self.context['year']
        project = ProjectInformation.objects.filter(year=year).aggregate(total_rev_total=Sum('total_revenue'))
        return round(project['total_rev_total'], 2)
    
    def get_neto(self, obj):
        dev_total = self.get_dev_total(obj)
        design_total = self.get_design_total(obj)
        other_total = self.get_other_total(obj)
        total_rev_total = self.get_total_rev_total(obj)
        neto = dev_total + design_total + other_total + total_rev_total
        return round(neto, 2)
    
    def get_direct_total(self, obj):
        year = self.context['year']
        project = ProjectInformation.objects.filter(year=year).aggregate(direct_total=Sum('direct'))
        return round(project['direct_total'], 2)
    
    def get_indirect_total(self, obj):
        year = self.context['year']
        project = ProjectInformation.objects.filter(year=year).aggregate(indirect_total=Sum('indirect'))
        return round(project['indirect_total'], 2)

    def get_marketing_total(self, obj):
        year = self.context['year']
        project = ProjectInformation.objects.filter(year=year).aggregate(marketing_total=Sum('marketing'))
        return round(project['marketing_total'], 2)
    
    def get_HRcost_total(self, obj):
        year = self.context['year']
        project = ProjectInformation.objects.filter(year=year).aggregate(HRcost_total=Sum('HRcost'))
        return round(project['HRcost_total'], 2)
    
    def get_officeCost_total(self, obj):
        year = self.context['year']
        project = ProjectInformation.objects.filter(year=year).aggregate(officeCost_total=Sum('officeCost'))
        return round(project['officeCost_total'], 2)
    
    def get_salesCosts_total(self, obj):
        year = self.context['year']
        project = ProjectInformation.objects.filter(year=year).aggregate(salesCosts_total=Sum('salesCosts'))
        return round(project['salesCosts_total'], 2)
    
    def get_otherCosts_total(self, obj):
        year = self.context['year']
        project = ProjectInformation.objects.filter(year=year).aggregate(otherCosts_total=Sum('otherCosts'))
        return round(project['otherCosts_total'], 2)
    
    def get_expenses(self, obj):
        direct_total = self.get_direct_total(obj)
        indirect_total = self.get_indirect_total(obj)
        marketing_total = self.get_marketing_total(obj)
        HRcost_total = self.get_HRcost_total(obj)
        salesCosts_total = self.get_salesCosts_total(obj)
        officeCost_total = self.get_officeCost_total(obj)
        otherCosts_total = self.get_otherCosts_total(obj)
        neto = direct_total + indirect_total + marketing_total + HRcost_total + salesCosts_total + otherCosts_total + officeCost_total
        return round(neto, 2)

    class Meta:
        model = ProjectInformation
        fields = ['dev_total', 'design_total', 'other_total', 'total_rev_total', 'neto',
                  'direct_total', 'indirect_total', 'marketing_total', 'HRcost_total', 'officeCost_total', 'salesCosts_total', 'otherCosts_total', 'expenses']
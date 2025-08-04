from rest_framework import serializers
from .models import IPO


class IPOSerializer(serializers.ModelSerializer):
    listing_gain = serializers.ReadOnlyField()
    current_return = serializers.ReadOnlyField()
    status_display = serializers.CharField(source='get_status_display', read_only=True)
    issue_type_display = serializers.CharField(source='get_issue_type_display', read_only=True)
    logo_url = serializers.SerializerMethodField()
    rhp_pdf_url = serializers.SerializerMethodField()
    drhp_pdf_url = serializers.SerializerMethodField()
    
    class Meta:
        model = IPO
        fields = [
            'id', 'company_name', 'logo', 'logo_url', 'price_band', 
            'open_date', 'close_date', 'issue_size', 'issue_type', 
            'issue_type_display', 'listing_date', 'status', 'status_display',
            'ipo_price', 'listing_price', 'current_market_price', 
            'rhp_pdf', 'rhp_pdf_url', 'drhp_pdf', 'drhp_pdf_url',
            'listing_gain', 'current_return', 'created_at', 'updated_at'
        ]
        read_only_fields = ['id', 'created_at', 'updated_at']
    
    def get_logo_url(self, obj):
        if obj.logo:
            request = self.context.get('request')
            if request:
                return request.build_absolute_uri(obj.logo.url)
            return obj.logo.url
        return None
    
    def get_rhp_pdf_url(self, obj):
        if obj.rhp_pdf:
            request = self.context.get('request')
            if request:
                return request.build_absolute_uri(obj.rhp_pdf.url)
            return obj.rhp_pdf.url
        return None
    
    def get_drhp_pdf_url(self, obj):
        if obj.drhp_pdf:
            request = self.context.get('request')
            if request:
                return request.build_absolute_uri(obj.drhp_pdf.url)
            return obj.drhp_pdf.url
        return None


class IPOListSerializer(serializers.ModelSerializer):
    listing_gain = serializers.ReadOnlyField()
    current_return = serializers.ReadOnlyField()
    status_display = serializers.CharField(source='get_status_display', read_only=True)
    logo_url = serializers.SerializerMethodField()
    
    class Meta:
        model = IPO
        fields = [
            'id', 'company_name', 'logo_url', 'price_band', 
            'open_date', 'close_date', 'issue_size', 'status', 
            'status_display', 'ipo_price', 'listing_gain', 'current_return'
        ]
    
    def get_logo_url(self, obj):
        if obj.logo:
            request = self.context.get('request')
            if request:
                return request.build_absolute_uri(obj.logo.url)
            return obj.logo.url
        return None 
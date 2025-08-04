from django.contrib import admin
from django.utils.html import format_html
from django.urls import reverse
from django.utils.safestring import mark_safe
from .models import IPO


@admin.register(IPO)
class IPOAdmin(admin.ModelAdmin):
    list_display = [
        'company_name', 
        'status', 
        'price_band', 
        'open_date', 
        'close_date', 
        'issue_size', 
        'ipo_price',
        'listing_gain_display',
        'current_return_display',
        'logo_preview'
    ]
    
    list_filter = [
        'status', 
        'issue_type', 
        'open_date', 
        'close_date', 
        'listing_date'
    ]
    
    search_fields = [
        'company_name', 
        'price_band'
    ]
    
    readonly_fields = [
        'listing_gain_display', 
        'current_return_display', 
        'logo_preview',
        'created_at', 
        'updated_at'
    ]
    
    fieldsets = (
        ('Basic Information', {
            'fields': ('company_name', 'logo', 'status', 'issue_type')
        }),
        ('Pricing Information', {
            'fields': ('price_band', 'ipo_price', 'listing_price', 'current_market_price')
        }),
        ('Issue Details', {
            'fields': ('issue_size', 'open_date', 'close_date', 'listing_date')
        }),
        ('Documents', {
            'fields': ('rhp_pdf', 'drhp_pdf'),
            'classes': ('collapse',)
        }),
        ('Calculated Fields', {
            'fields': ('listing_gain_display', 'current_return_display'),
            'classes': ('collapse',)
        }),
        ('Timestamps', {
            'fields': ('created_at', 'updated_at'),
            'classes': ('collapse',)
        }),
    )
    
    date_hierarchy = 'open_date'
    
    actions = ['mark_as_upcoming', 'mark_as_ongoing', 'mark_as_listed']
    
    def logo_preview(self, obj):
        if obj.logo:
            return format_html(
                '<img src="{}" style="max-height: 50px; max-width: 50px;" />',
                obj.logo.url
            )
        return "No logo"
    logo_preview.short_description = 'Logo'
    
    def listing_gain_display(self, obj):
        gain = obj.listing_gain
        if gain is not None:
            color = 'green' if gain >= 0 else 'red'
            return format_html(
                '<span style="color: {};">{:.2f}%</span>',
                color, gain
            )
        return "N/A"
    listing_gain_display.short_description = 'Listing Gain'
    
    def current_return_display(self, obj):
        return_val = obj.current_return
        if return_val is not None:
            color = 'green' if return_val >= 0 else 'red'
            return format_html(
                '<span style="color: {};">{:.2f}%</span>',
                color, return_val
            )
        return "N/A"
    current_return_display.short_description = 'Current Return'
    
    def mark_as_upcoming(self, request, queryset):
        updated = queryset.update(status='upcoming')
        self.message_user(request, f'{updated} IPOs marked as upcoming.')
    mark_as_upcoming.short_description = "Mark selected IPOs as upcoming"
    
    def mark_as_ongoing(self, request, queryset):
        updated = queryset.update(status='ongoing')
        self.message_user(request, f'{updated} IPOs marked as ongoing.')
    mark_as_ongoing.short_description = "Mark selected IPOs as ongoing"
    
    def mark_as_listed(self, request, queryset):
        updated = queryset.update(status='listed')
        self.message_user(request, f'{updated} IPOs marked as listed.')
    mark_as_listed.short_description = "Mark selected IPOs as listed"
    
    class Media:
        css = {
            'all': ('admin/css/ipo_admin.css',)
        }

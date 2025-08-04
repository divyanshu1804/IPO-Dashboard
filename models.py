from django.db import models
from django.core.validators import MinValueValidator
from decimal import Decimal


class IPO(models.Model):
    STATUS_CHOICES = [
        ('upcoming', 'Upcoming'),
        ('ongoing', 'Ongoing'),
        ('listed', 'Listed'),
    ]
    
    ISSUE_TYPE_CHOICES = [
        ('book_building', 'Book Building'),
        ('fixed_price', 'Fixed Price'),
        ('offer_for_sale', 'Offer for Sale'),
    ]
    
    company_name = models.CharField(max_length=200, unique=True)
    logo = models.ImageField(upload_to='ipo_logos/', blank=True, null=True)
    price_band = models.CharField(max_length=100, help_text="e.g., ₹1000-1100")
    open_date = models.DateField()
    close_date = models.DateField()
    issue_size = models.DecimalField(
        max_digits=15, 
        decimal_places=2, 
        validators=[MinValueValidator(Decimal('0.01'))],
        help_text="Issue size in crores"
    )
    issue_type = models.CharField(max_length=20, choices=ISSUE_TYPE_CHOICES, default='book_building')
    listing_date = models.DateField(blank=True, null=True)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='upcoming')
    ipo_price = models.DecimalField(
        max_digits=10, 
        decimal_places=2, 
        blank=True, 
        null=True,
        validators=[MinValueValidator(Decimal('0.01'))],
        help_text="Final IPO price"
    )
    listing_price = models.DecimalField(
        max_digits=10, 
        decimal_places=2, 
        blank=True, 
        null=True,
        validators=[MinValueValidator(Decimal('0.01'))],
        help_text="Listing price"
    )
    current_market_price = models.DecimalField(
        max_digits=10, 
        decimal_places=2, 
        blank=True, 
        null=True,
        validators=[MinValueValidator(Decimal('0.01'))],
        help_text="Current market price"
    )
    rhp_pdf = models.FileField(
        upload_to='ipo_documents/rhp/', 
        blank=True, 
        null=True,
        help_text="Red Herring Prospectus"
    )
    drhp_pdf = models.FileField(
        upload_to='ipo_documents/drhp/', 
        blank=True, 
        null=True,
        help_text="Draft Red Herring Prospectus"
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        ordering = ['-open_date']
        verbose_name = 'IPO'
        verbose_name_plural = 'IPOs'
    
    def __str__(self):
        return self.company_name
    
    @property
    def listing_gain(self):
        """Calculate listing gain as percentage"""
        if self.ipo_price and self.listing_price and self.ipo_price > 0:
            gain = ((self.listing_price - self.ipo_price) / self.ipo_price) * 100
            return round(gain, 2)
        return None
    
    @property
    def current_return(self):
        """Calculate current return as percentage from IPO price"""
        if self.ipo_price and self.current_market_price and self.ipo_price > 0:
            return_val = ((self.current_market_price - self.ipo_price) / self.ipo_price) * 100
            return round(return_val, 2)
        return None
    
    def get_status_display_class(self):
        """Get Bootstrap CSS class for status"""
        status_classes = {
            'upcoming': 'badge bg-warning',
            'ongoing': 'badge bg-primary',
            'listed': 'badge bg-success',
        }
        return status_classes.get(self.status, 'badge bg-secondary')

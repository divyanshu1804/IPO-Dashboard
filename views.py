from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse
from django.db.models import Q
from rest_framework import viewsets, filters
from rest_framework.decorators import action
from rest_framework.response import Response
from django_filters.rest_framework import DjangoFilterBackend
from .models import IPO
from .serializers import IPOSerializer, IPOListSerializer


class IPOViewSet(viewsets.ModelViewSet):
    """
    ViewSet for IPO model with full CRUD operations
    """
    queryset = IPO.objects.all()
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    filterset_fields = ['status', 'issue_type']
    search_fields = ['company_name', 'price_band']
    ordering_fields = ['open_date', 'close_date', 'issue_size', 'ipo_price', 'listing_price']
    ordering = ['-open_date']
    
    def get_serializer_class(self):
        if self.action == 'list':
            return IPOListSerializer
        return IPOSerializer
    
    @action(detail=False, methods=['get'])
    def upcoming(self, request):
        """Get upcoming IPOs"""
        upcoming_ipos = IPO.objects.filter(status='upcoming')
        serializer = self.get_serializer(upcoming_ipos, many=True)
        return Response(serializer.data)
    
    @action(detail=False, methods=['get'])
    def ongoing(self, request):
        """Get ongoing IPOs"""
        ongoing_ipos = IPO.objects.filter(status='ongoing')
        serializer = self.get_serializer(ongoing_ipos, many=True)
        return Response(serializer.data)
    
    @action(detail=False, methods=['get'])
    def listed(self, request):
        """Get listed IPOs"""
        listed_ipos = IPO.objects.filter(status='listed')
        serializer = self.get_serializer(listed_ipos, many=True)
        return Response(serializer.data)
    
    @action(detail=True, methods=['get'])
    def performance(self, request, pk=None):
        """Get IPO performance metrics"""
        ipo = self.get_object()
        data = {
            'listing_gain': ipo.listing_gain,
            'current_return': ipo.current_return,
            'ipo_price': ipo.ipo_price,
            'listing_price': ipo.listing_price,
            'current_market_price': ipo.current_market_price,
        }
        return Response(data)


def home(request):
    """Home page view with categorized IPOs"""
    search_query = request.GET.get('search', '')
    status_filter = request.GET.get('status', '')
    
    # Base queryset
    ipos = IPO.objects.all()
    
    # Apply search filter
    if search_query:
        ipos = ipos.filter(
            Q(company_name__icontains=search_query) |
            Q(price_band__icontains=search_query)
        )
    
    # Apply status filter
    if status_filter:
        ipos = ipos.filter(status=status_filter)
    
    # Categorize IPOs
    upcoming_ipos = ipos.filter(status='upcoming')[:6]
    ongoing_ipos = ipos.filter(status='ongoing')[:6]
    listed_ipos = ipos.filter(status='listed')[:6]
    
    context = {
        'upcoming_ipos': upcoming_ipos,
        'ongoing_ipos': ongoing_ipos,
        'listed_ipos': listed_ipos,
        'search_query': search_query,
        'status_filter': status_filter,
        'total_upcoming': IPO.objects.filter(status='upcoming').count(),
        'total_ongoing': IPO.objects.filter(status='ongoing').count(),
        'total_listed': IPO.objects.filter(status='listed').count(),
    }
    
    return render(request, 'ipo_app/home.html', context)


def ipo_detail(request, ipo_id):
    """IPO detail page view"""
    ipo = get_object_or_404(IPO, id=ipo_id)
    
    # Get related IPOs (same status)
    related_ipos = IPO.objects.filter(status=ipo.status).exclude(id=ipo.id)[:4]
    
    context = {
        'ipo': ipo,
        'related_ipos': related_ipos,
    }
    
    return render(request, 'ipo_app/detail.html', context)


def ipo_list(request):
    """Full IPO list page with advanced filtering"""
    search_query = request.GET.get('search', '')
    status_filter = request.GET.get('status', '')
    issue_type_filter = request.GET.get('issue_type', '')
    sort_by = request.GET.get('sort', '-open_date')
    
    ipos = IPO.objects.all()
    
    # Apply filters
    if search_query:
        ipos = ipos.filter(
            Q(company_name__icontains=search_query) |
            Q(price_band__icontains=search_query)
        )
    
    if status_filter:
        ipos = ipos.filter(status=status_filter)
    
    if issue_type_filter:
        ipos = ipos.filter(issue_type=issue_type_filter)
    
    # Apply sorting
    if sort_by in ['open_date', '-open_date', 'close_date', '-close_date', 
                   'issue_size', '-issue_size', 'ipo_price', '-ipo_price']:
        ipos = ipos.order_by(sort_by)
    
    context = {
        'ipos': ipos,
        'search_query': search_query,
        'status_filter': status_filter,
        'issue_type_filter': issue_type_filter,
        'sort_by': sort_by,
        'status_choices': IPO.STATUS_CHOICES,
        'issue_type_choices': IPO.ISSUE_TYPE_CHOICES,
    }
    
    return render(request, 'ipo_app/list.html', context)


def api_docs(request):
    """API documentation page"""
    return render(request, 'ipo_app/api_docs.html')

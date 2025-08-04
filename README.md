# IPO Tracker - Django Web Application

A comprehensive Django-based web application for tracking Initial Public Offerings (IPOs) with a modern, responsive interface and RESTful API.

## 🚀 Features

### Backend Features
- **Django 5.0.6** with Python 3.12+
- **PostgreSQL** database for robust data storage
- **Django REST Framework** for API endpoints
- **Comprehensive IPO Model** with all required fields
- **Property Methods** for calculated fields (listing_gain, current_return)
- **Admin Interface** with advanced filtering and actions
- **File Upload** support for logos and PDF documents
- **Search & Filter** capabilities

### Frontend Features
- **Bootstrap 5** responsive design
- **Modern UI/UX** with hover effects and animations
- **Search & Filter** functionality
- **Table & Card** view options
- **Performance Metrics** display
- **Document Download** links
- **Mobile Responsive** design

### API Features
- **RESTful API** with full CRUD operations
- **Pagination** support
- **Search & Filter** endpoints
- **Status-specific** endpoints
- **Performance metrics** endpoint
- **Comprehensive documentation**

## 📋 Prerequisites

- Python 3.12 or higher
- PostgreSQL database
- pip (Python package manager)

## 🛠️ Installation

### 1. Clone the Repository
```bash
git clone <repository-url>
cd ipo-website
```

### 2. Create Virtual Environment
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

### 3. Install Dependencies
```bash
pip install -r requirements.txt
```

### 4. Database Setup

#### PostgreSQL Configuration
1. Create a PostgreSQL database:
```sql
CREATE DATABASE ipo_database;
CREATE USER ipo_user WITH PASSWORD 'your_password';
GRANT ALL PRIVILEGES ON DATABASE ipo_database TO ipo_user;
```

2. Update database settings in `ipo_project/settings.py`:
```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'ipo_database',
        'USER': 'ipo_user',
        'PASSWORD': 'your_password',
        'HOST': 'localhost',
        'PORT': '5432',
    }
}
```

### 5. Django Setup
```bash
# Create database tables
python manage.py makemigrations
python manage.py migrate

# Create superuser for admin access
python manage.py createsuperuser

# Collect static files
python manage.py collectstatic

# Run development server
python manage.py runserver
```

## 🏗️ Project Structure

```
ipo-website/
├── ipo_project/          # Main Django project
│   ├── settings.py       # Project settings
│   ├── urls.py          # Main URL configuration
│   └── wsgi.py          # WSGI configuration
├── ipo_app/             # IPO application
│   ├── models.py        # IPO model definition
│   ├── views.py         # Views and API endpoints
│   ├── serializers.py   # DRF serializers
│   ├── admin.py         # Django admin configuration
│   └── urls.py          # App URL configuration
├── templates/           # HTML templates
│   ├── base.html        # Base template
│   └── ipo_app/         # App-specific templates
│       ├── home.html    # Home page
│       ├── detail.html  # IPO detail page
│       ├── list.html    # IPO list page
│       ├── api_docs.html # API documentation
│       └── partials/    # Reusable template parts
├── static/              # Static files
│   ├── css/            # CSS stylesheets
│   ├── js/             # JavaScript files
│   └── images/         # Images and assets
├── media/              # User-uploaded files
├── requirements.txt    # Python dependencies
└── README.md          # This file
```

## 🎯 Usage

### Web Interface

1. **Home Page** (`/`): View categorized IPOs (upcoming, ongoing, listed)
2. **IPO List** (`/list/`): Browse all IPOs with advanced filtering
3. **IPO Detail** (`/detail/<id>/`): View detailed IPO information
4. **API Docs** (`/api-docs/`): API documentation

### Admin Interface

1. Access admin at `/admin/`
2. Login with superuser credentials
3. Manage IPO entries with full CRUD operations
4. Upload logos and PDF documents
5. Use bulk actions for status updates

### API Endpoints

#### List IPOs
```bash
GET /api/ipo/
```

#### Get IPO Details
```bash
GET /api/ipo/{id}/
```

#### Filter IPOs
```bash
GET /api/ipo/?status=upcoming&issue_type=book_building
```

#### Search IPOs
```bash
GET /api/ipo/?search=company_name
```

#### Sort IPOs
```bash
GET /api/ipo/?ordering=-open_date
```

#### Status-Specific Endpoints
```bash
GET /api/ipo/upcoming/
GET /api/ipo/ongoing/
GET /api/ipo/listed/
```

#### Performance Metrics
```bash
GET /api/ipo/{id}/performance/
```

## 📊 IPO Model Fields

| Field | Type | Description |
|-------|------|-------------|
| company_name | CharField | Company name (unique) |
| logo | ImageField | Company logo |
| price_band | CharField | Price band (e.g., ₹1000-1100) |
| open_date | DateField | IPO open date |
| close_date | DateField | IPO close date |
| issue_size | DecimalField | Issue size in crores |
| issue_type | CharField | Type of issue |
| listing_date | DateField | Listing date |
| status | CharField | IPO status (upcoming/ongoing/listed) |
| ipo_price | DecimalField | Final IPO price |
| listing_price | DecimalField | Listing price |
| current_market_price | DecimalField | Current market price |
| rhp_pdf | FileField | Red Herring Prospectus |
| drhp_pdf | FileField | Draft Red Herring Prospectus |

### Calculated Properties

- **listing_gain**: Percentage gain from IPO price to listing price
- **current_return**: Percentage return from IPO price to current market price

## 🔧 Configuration

### Environment Variables
Create a `.env` file for sensitive settings:
```env
SECRET_KEY=your-secret-key-here
DEBUG=True
DATABASE_URL=postgresql://user:password@localhost:5432/ipo_database
```

### Static and Media Files
- Static files are served from `static/` directory
- Media files (uploads) are stored in `media/` directory
- Configure your web server to serve these directories in production

## 🧪 Testing

### API Testing with Postman
1. Import the provided Postman collection
2. Set the base URL variable
3. Test all endpoints

### Manual Testing
1. Create test IPO entries via admin
2. Test search and filter functionality
3. Verify calculated properties
4. Test file uploads

## 🚀 Deployment

### Production Settings
1. Set `DEBUG = False`
2. Configure production database
3. Set up static file serving
4. Configure media file storage
5. Set up HTTPS
6. Configure logging

### Recommended Stack
- **Web Server**: Nginx
- **Application Server**: Gunicorn
- **Database**: PostgreSQL
- **File Storage**: AWS S3 (for media files)
- **CDN**: CloudFront (for static files)

## 📈 Performance Optimization

1. **Database Indexing**: Add indexes on frequently queried fields
2. **Caching**: Implement Redis for caching
3. **CDN**: Use CDN for static and media files
4. **Database Optimization**: Regular maintenance and query optimization
5. **Image Optimization**: Compress uploaded images

## 🔒 Security

1. **CSRF Protection**: Enabled by default
2. **SQL Injection**: Protected by Django ORM
3. **File Upload Security**: Validate file types and sizes
4. **Admin Security**: Use strong passwords and 2FA
5. **HTTPS**: Enable in production

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Add tests
5. Submit a pull request

## 📝 License

This project is licensed under the MIT License - see the LICENSE file for details.

## 🆘 Support

For support and questions:
- Create an issue in the repository
- Contact the development team
- Check the API documentation

## 🔄 Updates

### Version History
- **v1.0.0**: Initial release with basic IPO tracking
- **v1.1.0**: Added API endpoints and advanced filtering
- **v1.2.0**: Enhanced UI/UX and performance metrics

### Future Enhancements
- Real-time price updates
- Email notifications
- Advanced analytics
- Mobile app
- Social features
- Integration with stock exchanges

---

**Built with ❤️ using Django and Bootstrap** 
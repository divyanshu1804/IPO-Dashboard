# IPO Tracker - Quick Setup Guide

## Quick Start (5 minutes)

### 1. Install Dependencies
```bash
pip install -r requirements.txt
```

### 2. Database Setup (Choose One)

#### Option A: Use SQLite (Quick Start)
Update `ipo_project/settings.py`:
```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}
```

#### Option B: Use PostgreSQL (Production Ready)
1. Install PostgreSQL
2. Create database: `CREATE DATABASE ipo_database;`
3. Update settings with your credentials

### 3. Initialize Database
```bash
python manage.py makemigrations
python manage.py migrate
```

### 4. Create Admin User
```bash
python manage.py createsuperuser
```

### 5. Add Sample Data
```bash
python manage.py populate_sample_data
```

### 6. Run the Application
```bash
python manage.py runserver
```

## Access Points

- **Home Page**: http://localhost:8000/
- **Admin Panel**: http://localhost:8000/admin/
- **API Endpoints**: http://localhost:8000/api/ipo/
- **API Documentation**: http://localhost:8000/api-docs/

## Features Available

### Web Interface
- Home page with categorized IPOs
- IPO list with advanced filtering
- IPO detail pages with performance metrics
- Search functionality
- Responsive design

### Admin Interface
- Create, edit, delete IPOs
- Upload logos and PDFs
- Bulk status updates
- Advanced filtering and search

### API Endpoints
- List all IPOs: `GET /api/ipo/`
- Get IPO details: `GET /api/ipo/{id}/`
- Filter by status: `GET /api/ipo/?status=upcoming`
- Search IPOs: `GET /api/ipo/?search=company_name`
- Sort IPOs: `GET /api/ipo/?ordering=-open_date`
- Status endpoints: `/api/ipo/upcoming/`, `/api/ipo/ongoing/`, `/api/ipo/listed/`
- Performance metrics: `GET /api/ipo/{id}/performance/`

## Testing

### Test the Web Interface
1. Visit http://localhost:8000/
2. Browse different IPO categories
3. Use search and filter options
4. Click on IPO cards to view details

### Test the API
1. Import `IPO_Tracker_API.postman_collection.json` into Postman
2. Set base URL to `http://localhost:8000`
3. Test all endpoints

### Test Admin Interface
1. Go to http://localhost:8000/admin/
2. Login with superuser credentials
3. Create, edit, and delete IPO entries
4. Upload test files

## Sample Data Included

The `populate_sample_data` command creates:
- 2 Upcoming IPOs
- 2 Ongoing IPOs  
- 4 Listed IPOs with performance data

## Production Deployment

1. Set `DEBUG = False`
2. Configure production database
3. Set up static file serving
4. Configure media file storage
5. Set up HTTPS
6. Use Gunicorn + Nginx

---

**Ready to track IPOs!** 
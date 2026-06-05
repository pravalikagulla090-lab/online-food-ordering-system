========================================================================
🍽️           ONLINE FOOD ORDERING & MANAGEMENT SYSTEM
========================================================================

A full-stack web application built using Python, Django, and Django 
REST Framework (DRF). This project connects a clean, traditional web 
frontend with a secure API engine backend to manage food menus, active 
shopping carts, user checkout pipelines, and order histories.

------------------------------------------------------------------------
✨ KEY FEATURES
------------------------------------------------------------------------

* Restaurant & Menu Explorer: Browse partner restaurants and view 
  available dish catalogs pulled dynamically from database records.
* Active Database Cart: Add or remove items from your basket seamlessly 
  with dynamic quantity and subtotal cost tracking.
* Order Lifecycle Control: Track ongoing receipts from a personalized 
  dashboard and cancel pending orders with an automated state update.
* Custom Security Bridge: Includes a specialized backend authentication 
  handler to resolve traditional "403 Forbidden" API errors, allowing 
  standard web browser sessions to update API states safely.

------------------------------------------------------------------------
📂 PROJECT ARCHITECTURE
------------------------------------------------------------------------

food_ordering_system/
│
├── foodproject/          # Main Project Core Configuration
│   ├── settings.py       # Global app properties & framework rules
│   └── urls.py           # Master URL routing table
│
├── cart/                 # Shopping Basket Module
│   ├── models.py         # Database schemas for Cart & CartItem rows
│   └── views.py          # View controller handling item allocation
│
├── menu/                 # Restaurant Menu Catalog Module
│   └── models.py         # Schemas defining food items & categories
│
├── orders/               # Checkout & Lifecycle Tracking Module
│   ├── views.py          # Handles order confirmation and cancellation
│   └── urls.py           # Explicit endpoint patterns for order states
│
└── templates/            # Web Frontend Layouts
    ├── menu.html         # Interactive food menu choice board
    └── cart_list.html    # Invoice checkout summary dashboard

------------------------------------------------------------------------
🛠️ TECH STACK
------------------------------------------------------------------------

* Backend Core: Python & Django
* API Layer: Django REST Framework (DRF)
* Database Engine: SQLite3
* Frontend Viewports: HTML5, JavaScript (Fetch API), and Inline CSS

------------------------------------------------------------------------
⚙️ HOW TO SETUP AND RUN LOCALLY
------------------------------------------------------------------------

Follow these straightforward steps to run the application on your computer:

1. INITIALIZE VIRTUAL ENVIRONMENT
   Open your terminal/PowerShell inside the root folder and run:
   
   python -m venv venv
   .\venv\Scripts\activate

2. APPLY DATABASE TABLES MIGRATIONS
   Generate the database layout using Django's built-in migration engine:
   
   python manage.py makemigrations
   python manage.py migrate

3. SETUP ADMINISTRATOR ACCOUNT
   Create a superuser profile to access Django's backend admin panel:
   
   python manage.py createsuperuser

4. START THE LIVE DEVELOPMENT SERVER
   Fire up the system engine:
   
   python manage.py runserver

   Now open your browser and head to the application's local link:
   👉 http://127.0.0.1:8000/

------------------------------------------------------------------------
🔒 CUSTOM ARCHITECTURE FIX INSIDE THIS PROJECT
------------------------------------------------------------------------

When building mixed application stacks, standard frontend views often run 
into "Authentication details not provided" or "CSRF token missing" errors 
when trying to cancel orders or alter cart tables.

This project overrides that security roadblock by implementing a custom 
authentication validator inside 'orders/views.py':

class CsrfExemptSessionAuthentication(SessionAuthentication):
    def enforce_csrf(self, request):
        return  # Bypasses checking for explicit API tokens

By combining this custom class with standard TokenAuthentication, the 
system successfully enables your normal logged-in web browser profile 
to complete order updates cleanly without getting blocked by the API router!

========================================================================
Thank you for exploring this project! Feel free to modify, expand, or 
fork the code for your own development needs.
========================================================================

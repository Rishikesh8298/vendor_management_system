# vendor_management_system
Step 1: Prequisites python 3.9.0 or greater version is available. AND postman for api testing.
Step 2: pip install -r requirement.txt
Step 3: python manage.py makemigrations
Step 4: python manage.py migrate
Step 5: python manage.py runserver

There are following endpoints for creating users or Login.
Step 1: POST /register/ for creating users and sample data.
{
    "username": "test",
    "email": "test@example.com",
    "password": "test1@123"
    "re_password": "test1@123"
}
Step 2: POST /login/ for login users and sample data
{
    "username": "test",
    "password": "test1@123"
}

API Endpoints for Vendor:

● POST /api/vendors/: Create a new vendor.
● GET /api/vendors/: List all vendors.
● GET /api/vendors/{vendor_id}/: Retrieve a specific vendor's details.
● PUT /api/vendors/{vendor_id}/: Update a vendor's details.
● DELETE /api/vendors/{vendor_id}/: Delete a vendor.

API Endpoints for PurchaseOrder:
● POST /api/purchase_orders/: Create a purchase order.
● GET /api/purchase_orders/: List all purchase orders with an option to filter by
vendor.
● GET /api/purchase_orders/{po_id}/: Retrieve details of a specific purchase order.
● PUT /api/purchase_orders/{po_id}/: Update a purchase order.
● DELETE /api/purchase_orders/{po_id}/: Delete a purchase order.

API Endpoints for HistoricalPerformance:
● GET /api/vendors/{vendor_id}/performance:

Documentations for whole api
swagger/
re-doc/
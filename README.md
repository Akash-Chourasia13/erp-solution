# Django ERP MVP for Inventory and Billing Management

This is an MVP (Minimum Viable Product) ERP system built using Django for managing inventory and billing in a retail environment, specifically designed for a mall. The system focuses on three core functionalities:

## Key Features:
1. **Inventory Management with Barcode Scanner:**
   - Easily manage products using a barcode scanner for quick updates and tracking.
   - Keep track of stock levels in real-time as products are scanned, added, or sold.

2. **Customer and Business Management (B2B & B2C):**
   - Add and manage customers and businesses before generating bills, supporting both B2B and B2C transactions.
   - Maintain customer information for recurring transactions and better service.

3. **Billing and Transaction History:**
   - Generate invoices and receipts with detailed breakdowns.
   - Store transaction history, allowing for viewing and downloading past bills at any time.

## Tech Stack:
- **Backend**: Django & Django REST Framework
- **Database**: SQLite (can be easily switched to PostgreSQL, MySQL, etc.)
- **Frontend**: HTML, CSS, JavaScript (Django templates)
- **Barcode Scanning**: Supports integration with both traditional barcode scanners and mobile devices as scanners.

## How It Works:
This system streamlines retail operations by enabling barcode scanning for inventory management, easy customer data input, and automated bill generation. It is ideal for small to medium-sized businesses looking to digitize their operations with a scalable solution.

## Future Enhancements:
- Adding advanced reporting and analytics.
- Integration with payment gateways for seamless billing.
- Expanding functionalities to include more modules like employee management, supplier tracking, etc.

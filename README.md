# Farm_Fresh_India

A web application for connecting local farmers with consumers looking for fresh produce.

## Features

- Browse local farm products
- Search by category and location
- User accounts for farmers and consumers
- Online ordering system
- Delivery scheduling

## Technology Stack

- Django backend with REST API
- Frontend built with React/Next.js
- PostgreSQL database
- Responsive mobile-first design

## Installation

1. Clone the repository
   ```
   git clone https://github.com/yourusername/farm-fresh.git
   cd farm-fresh
   ```

2. Set up virtual environment
   ```
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. Install dependencies
   ```
   pip install -r requirements.txt
   ```

4. Set up environment variables
   ```
   cp .env.example .env
   # Edit .env with your configuration
   ```

5. Run migrations
   ```
   python manage.py migrate
   ```

6. Start the development server
   ```
   python manage.py runserver
   ```

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## License

This project is licensed under the MIT License - see the LICENSE file for details.

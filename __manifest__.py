{
    'name': 'Book Store',
    'version': '1.0',
    'category': 'Sales',
    'summary': 'Manage books in a bookstore',
    'description': 'A simple custom Odoo module for managing books.',
    'depends': ['base'],
    'data': ['security/ir.model.access.csv','views/book_views.xml',],
    'installable': True,
    'application': True,
}
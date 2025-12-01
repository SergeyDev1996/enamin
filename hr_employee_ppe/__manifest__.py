{
    "name": "HR Employee PPE",
    "summary": "Track personal protective equipment assigned to employees.",
    "version": "17.0.1.0.0",
    "category": "Human Resources",
    "website": "https://github.com/OCA/hr",
    "author": "Odoo Community Association (OCA)",
    "license": "LGPL-3",
    "depends": ["hr", "stock"],
    "data": [
        "security/ir.model.access.csv",
        "views/hr_employee_ppe_views.xml",
        "views/hr_employee_views.xml",
        "data/product_data.xml",
    ],
    "installable": True,
}

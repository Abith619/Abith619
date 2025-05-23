{
    "name": "Chat-GPT Generation",
    "version": "1.0",
    "currency": 'INR',
    "summary": "Chat-GPT Generation",
    "category": "Requirement",
    "description": """
            Chat-GPT Model Generation
        """,
    "depends": ["base","contacts","web",'account'],
    "data": [
        'security/ir.model.access.csv',
        'views/chat_gpt.xml',
        'views/mind_map.xml',
        'views/intent.xml',
        'views/prompt.xml',
        'wizards/bot_gen.xml',
            ],
    'demo': [
    ],
    'css': [],
    "author": "Abith",
    "website": "",
    "installable": True,
    "application": True,
    "auto_install": False,
    "images": [],
    'license': 'LGPL-3',
}

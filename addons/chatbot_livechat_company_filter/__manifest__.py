{
    'name': 'Livechat y Chatbots - Multiempresa',
    'version': '1.0',
    'category': 'Customization',
    'depends': ['base', 'im_livechat', 'mail'],
    'author': 'ChatGPT',
    'description': 'Agrega soporte multiempresa a canales de chat en vivo y scripts de chatbot.',
    'data': [
        'views/im_livechat_channel_views.xml',
        'views/chatbot_script_views.xml',
    ],
    'installable': True,
    'application': False,
}
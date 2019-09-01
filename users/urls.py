from django.urls import path, include
from users.views import *

urlpatterns = [
    path('', homepage, name = 'homepage'),
    path('dashboard', dashboard, name = 'dashboard'),
    path('signin', signin, name = 'signin'),
    path('signup', signup, name = 'signup'),
    path('signout', signout, name = 'signout'),

    path('resetpass', resetpass, name = 'resetpass'),
    path('resetpass/verify', verify, name = 'resetpassverify'),
	path('resetpass/newpassword', newpassword, name = 'newpassword'),

	path('active', account_active, name = 'account_active'),
	path('resendmail', send_activation_mail_again, name = 'send_activation_mail_again'),

	path('decks/add', deck_add, name = 'deck_add'),
	path('decks/<slug:slug>', deck_detail, name = 'deck_detail'),
	path('decks/delete/<slug:slug>', deck_delete, name = 'deck_delete'),

	path('card/add', card_add, name = 'card_add'),
]
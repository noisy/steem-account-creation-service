from django.db import models
from django.utils.translation import ugettext_lazy as _


class Account(models.Model):

    name = models.CharField(_('Account Name'), max_length=32)
    public_owner_key = models.CharField(_('Public Owner Key'), max_length=128)
    public_active_key = models.CharField(_('Public Active Key'), max_length=128)
    public_posting_key = models.CharField(_('Public Posting Key'), max_length=128)
    public_memo_key = models.CharField(_('Public Memo Key'), max_length=128)

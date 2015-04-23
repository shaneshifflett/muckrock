"""
Models for the crowdfund application
"""

from django.contrib.auth.models import User, AnonymousUser
from django.db import models

from datetime import date
from decimal import Decimal
import logging

from muckrock.foia.models import FOIARequest

class CrowdfundABC(models.Model):
    """Abstract base class for crowdfunding objects"""
    # pylint: disable=R0903, model-missing-unicode
    payment_required = models.DecimalField(
        max_digits=8,
        decimal_places=2,
        default='0.00'
    )
    payment_received = models.DecimalField(
        max_digits=8,
        decimal_places=2,
        default='0.00'
    )
    date_due = models.DateField()

    def expired(self):
        """Has this crowdfuning run out of time?"""
        return date.today() >= self.date_due

    class Meta:
        abstract = True

class CrowdfundPaymentABC(models.Model):
    """Abstract base class for crowdfunding objects"""
    # pylint: disable=R0903, model-missing-unicode
    user = models.ForeignKey(User, blank=True, null=True)
    name = models.CharField(max_length=255, blank=True)
    amount = models.DecimalField(max_digits=8, decimal_places=2)
    date = models.DateTimeField(auto_now_add=True)
    show = models.BooleanField(default=False)

    class Meta:
        abstract = True

class CrowdfundRequest(CrowdfundABC):
    """Keep track of crowdfunding for a request"""
    name = models.CharField(max_length=255, default='Crowdfund this request')
    description = models.TextField(blank=True)
    foia = models.OneToOneField(FOIARequest, related_name='crowdfund')

    def __unicode__(self):
        # pylint: disable=E1101
        return 'Crowdfunding for %s' % self.foia.title

    @models.permalink
    def get_absolute_url(self):
        """The url for this object"""
        return ('crowdfund-request', [], {'pk': self.pk})

    def update_payment_received(self):
        """Combine the amounts of all the payments"""
        total_amount = Decimal()
        payments = self.payments.all()
        for payment in payments:
            logging.debug(payment)
            total_amount += payment.amount
        self.payment_received = total_amount
        self.save()

    def contributors(self):
        """Return a list of all the contributors to a crowdfund"""
        contributors = []
        payments = self.payments.all()
        for payment in payments:
            if payment.show and payment.user:
                contributors.append(payment.user)
            else:
                contributors.append(AnonymousUser())
        return contributors

class CrowdfundRequestPayment(CrowdfundPaymentABC):
    """M2M intermediate model"""
    crowdfund = models.ForeignKey(CrowdfundRequest, related_name='payments')

    def __unicode__(self):
        # pylint: disable=E1101
        return 'Payment of $%.2f by %s on %s for %s' % \
            (self.amount, self.user, self.date.date(), self.crowdfund.foia)

class Project(models.Model):
    """A project involving multiple FOIA Requests"""
    name = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255)
    description = models.TextField(blank=True)
    foias = models.ManyToManyField(
        'foia.FOIARequest',
        related_name='foias',
        blank=True,
        null=True
    )

    def __unicode__(self):
        return self.name

class CrowdfundProject(CrowdfundABC):
    """Keep track of crowdfunding for a project"""
    project = models.OneToOneField(Project, related_name='crowdfund')
    payments = models.ManyToManyField(User, through='CrowdfundProjectPayment')

    def __unicode__(self):
        return self.project.name

class CrowdfundProjectPayment(CrowdfundPaymentABC):
    """M2M intermediate model"""
    # pylint: disable=model-missing-unicode
    crowdfund = models.ForeignKey(CrowdfundProject)

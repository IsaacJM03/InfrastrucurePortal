from django.db import models
import json
from django.utils import timezone

class HardwareItem(models.Model):
    name = models.CharField(max_length=100)
    model = models.CharField(max_length=255)
    serial_number = models.CharField(max_length=50)
    location = models.CharField(max_length=100)
    
    CATEGORY_CHOICES = [
        ('computers', 'Computers'),
        ('servers', 'Servers'),
        ('networking equipment', 'Networking Equipment'),
    ]
    category = models.CharField(max_length=100, choices=CATEGORY_CHOICES)
    
    status_choices = [
        ('in_use', 'In Use'),
        ('in_storage', 'In Storage'),
        ('under_maintenance', 'Under Maintenance'),
    ]
    status = models.CharField(max_length=20, choices=status_choices, default='in_storage')
    status_history = models.TextField(blank=True, null=True)
    
    def __str__(self):
        return self.name

    class Meta:
        db_table = 'hardware_items'

    # Methods
    def save(self,*args, **kwargs):
        if self.pk:
            old_status = HardwareItem.objects.get(pk=self.pk).status
            if old_status != self.status:
                self.log_status_change(old_status, self.status)
        super().save(*args, **kwargs)
    
    def log_status_change(self,old_status,new_status):
        timestamp = timezone.now().isoformat()
        change_entry = {
            'timestamp': timestamp,
            'old_status': old_status,
            'new_status': new_status
        }
        if not self.status_history:
            self.status_history = json.dumps([change_entry])
        else:
            history = json.loads(self.status_history)
            history.append(change_entry)
            self.status_history = json.dumps(history)

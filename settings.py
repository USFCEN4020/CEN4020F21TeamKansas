class Settings:
    def __init__(self, user, email_notifications, sms_notifications, targeted_ads, language_set):
        self.user = user
        self.email_notifications = email_notifications
        self.sms_notifications = sms_notifications
        self.targeted_ads = targeted_ads
        self.language_set = language_set

    def get_user(self):
        return self.user

    def get_email_notif(self):
        return self.email_notifications

    def get_sms_notif(self):
        return self.sms_notifications

    def get_targeted_ads(self):
        return self.targeted_ads

    def get_language(self):
        return self.language_set

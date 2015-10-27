# -*- coding: utf-8 -*-

from __future__ import unicode_literals

from django.views import generic


class View(generic.TemplateView):
    template_name = 'user.html'

    def get_context_data(self, **context):
        context['user'] = self.request.user
        return context


user = View.as_view(template_name = 'user.html')

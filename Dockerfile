FROM python:2-onbuild

COPY build/start.sh /start.sh
RUN chmod +x /start.sh
ENV DJANGO_SETTINGS_MODULE buurman.settings.production
EXPOSE 8000

CMD ["/start.sh"]
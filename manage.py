#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""
import os
import sys


def main():
    """Run administrative tasks."""
    # 환경 변수를 사용하여 설정 파일 선택
    env = os.environ.get('DJANGO_ENV', 'development')

    if env == 'development':
        os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'review_spot_backend.settings.base_settings')
    elif env == 'production':
        os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'review_spot_backend.settings.product_settings')
    else:
        os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'review_spot_backend.settings.base_settings')
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    execute_from_command_line(sys.argv)


if __name__ == '__main__':
    main()

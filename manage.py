#!/usr/bin/env python
import os
import sys

from project_module import PROJECT_MODULE

# Edit this if necessary or override the variable in your environment.
os.environ.setdefault('DJANGO_SETTINGS_MODULE', '%s.settings' % PROJECT_MODULE)

try:
    # For local development in a virtualenv:
    from funfactory import manage
except ImportError:
    # Production:
    # Add a temporary path so that we can import the funfactory
    tmp_path = os.path.join(os.path.dirname(os.path.abspath(__file__)),
                            'vendor', 'src', 'funfactory')
    sys.path.append(tmp_path)

    from funfactory import manage

    # Let the path magic happen in setup_environ() !
    sys.path.remove(tmp_path)


manage.setup_environ(__file__, more_pythonic=True)

if __name__ == "__main__":
    manage.main()

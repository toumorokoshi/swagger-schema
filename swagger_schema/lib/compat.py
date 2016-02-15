import sys

is_py3 = sys.version_info[0] >= 3

if is_py3:
    string_type = str
else:
    string_type = basestring

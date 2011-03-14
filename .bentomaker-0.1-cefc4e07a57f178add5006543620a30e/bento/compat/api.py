import os

if os.name == "posix":
    from posix_path \
        import \
            relpath
elif os.name == "nt":
    from nt_path \
        import \
            relpath
else:
    raise ImportError("relpath implementation for os %s not included" \
                      % os.name)

try:
    from subprocess \
        import \
            check_call, CalledProcessError
except ImportError:
    from bento.compat._subprocess \
        import \
            check_call, CalledProcessError

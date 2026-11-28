import os
from config import MAX_CHARS


def get_file_content(working_directory: str, file_path: str) -> str:
    try:
        working_dir_abs = os.path.abspath(working_directory)
        file_path_abs = os.path.normpath(os.path.join(working_dir_abs, file_path))
        is_path_valid = (os.path.commonpath([working_dir_abs, file_path_abs]) == working_dir_abs)
        if not is_path_valid:
            return f'Error: Cannot list "{file_path}" as it is outside the permitted working directory'

        if not os.path.isfile(file_path_abs):
            return f'Error: File not found or is not a regular file: "{file_path}"'

        with open(file_path_abs, "r") as f:
            file_contents = f.read(MAX_CHARS)
            if f.read(1):
                file_contents += (f'[...File "{file_path}" truncated at {MAX_CHARS} characters]')

        return file_contents
    except Exception as e:
        raise RuntimeError(f"Error: {e}")

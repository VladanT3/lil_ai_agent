import os

def get_files_info(working_directory: str, directory: str = ".") -> str:
    try:
        working_dir_abs = os.path.abspath(working_directory)
        target_dir_abs = os.path.normpath(os.path.join(working_dir_abs, directory))
        if not os.path.isdir(target_dir_abs):
            print(f'Error: "{directory}" is not a directory')
            return ""

        is_path_valid = os.path.commonpath([working_dir_abs, target_dir_abs]) == working_dir_abs
        if not is_path_valid:
            print(f'Error: Cannot list "{directory}" as it is outside the permitted working directory')
            return ""
        else:
            print(f'Success: "{directory}" is within the working directory')

        file_list = ""
        for file in os.listdir(target_dir_abs):
            name = file
            file_size = os.path.getsize(target_dir_abs + f"/{file}")
            is_dir = os.path.isdir(target_dir_abs + f"/{file}")

            file_list += f"- {name}: file_size={file_size}, is_dir={is_dir}\n"
            
        return file_list
    except Exception as e:
        raise RuntimeError(f"Error: {e}")

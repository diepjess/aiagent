import os


def get_files_info(working_directory, directory=None):
    abs_working_dir = os.path.abspath(working_directory)
    if directory is None:
        directory = working_directory
    if directory:
        join_path = os.path.join(abs_working_dir, directory)
        target_dir_abs = os.path.abspath(join_path)
        if not target_dir_abs.startswith(abs_working_dir):
            return f'Error: Cannot list "{directory}" as it is outside the permitted working directory'
        if not os.path.isdir(target_dir_abs):
            return f'Error: "{directory}" is not a directory'
    try:
        files = []
        contents = os.listdir(target_dir_abs)
        for filename in contents:
            filepath = os.path.join(target_dir_abs, filename)
            is_dir = os.path.isdir(filepath)
            file_size = 0
            file_size = os.path.getsize(filepath)
            file_info = f"- {filename}: file_size={file_size}, is_dir={is_dir}"
            files.append(file_info)
        return "\n".join(files)
    except Exception as e:
        return f"Error listing files: {e}"
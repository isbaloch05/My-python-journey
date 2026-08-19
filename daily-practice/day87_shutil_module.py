import shutil 
"""
shutil — High-level file operations module (Python Standard Library)
======================================================================

FILE OPERATIONS
----------------
shutil.copy(src, dst)
    Copies a single file's content and permissions to dst.
    dst can be a filename or a directory.

shutil.copy2(src, dst)
    Same as copy(), but also preserves metadata (timestamps, etc).

shutil.copyfile(src, dst)
    Copies file content only (no permissions/metadata). dst must be a filename.

shutil.copymode(src, dst)
    Copies permission bits only, not content.

shutil.copystat(src, dst)
    Copies metadata (timestamps, permissions) only, not content.

FOLDER OPERATIONS
------------------
shutil.copytree(src, dst, dirs_exist_ok=False)
    Recursively copies an entire directory tree from src to dst.
    dst must NOT already exist unless dirs_exist_ok=True.

shutil.rmtree(path)
    Recursively deletes a directory and everything inside it.

shutil.move(src, dst)
    Moves a file or folder to a new location (works like cut-paste).

DISK USAGE
-----------
shutil.disk_usage(path)
    Returns (total, used, free) space in bytes for the given path.

ARCHIVES
---------
shutil.make_archive(base_name, format, root_dir)
    Creates a compressed archive (zip, tar, etc) from a folder.

shutil.unpack_archive(filename, extract_dir)
    Extracts an archive to a directory.

MISC
-----
shutil.which(cmd)
    Finds the full path of an executable (like the 'which' command).

shutil.get_terminal_size()
    Returns the size of the terminal window (columns, lines).
"""



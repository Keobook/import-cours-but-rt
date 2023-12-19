from sys import argv

def absolute_path(relative_path: str) -> str:
  """A simple utility function to transform relative to absolute path.

  Args:
      relative_path (str): The relative path we're trying to get.

  Returns:
      str: The absolute path of our target.
  """

  current_file_path = argv[0].replace("\\", "/") ### In case, we're on Windows, return the path in POSIX
  absolute_local_path = "/".join(current_file_path.strip().split("/")[:-1]) + "/"

  ### We're going to clean the relative path, to simplify the URI
  if relative_path.startswith("./"):
    relative_path = relative_path[2:]

  return absolute_local_path + relative_path

def get_absolute_current_path() -> str:
  current_file_path = argv[0].replace("\\", "/") ### In case, we're on Windows, return the path in POSIX
  absolute_local_path = "/".join(current_file_path.strip().split("/")[:-1]) + "/"

  return absolute_local_path

if __name__ == "__main__":
  print(absolute_path("./src/test.png"))
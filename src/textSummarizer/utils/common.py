import os
from box.exceptions import BoxValueError
import yaml
from textSummarizer.logging import logger
from ensure import ensure_annotations #this will help in raising error if wrong type of argument is passed to the function than the expected one, without this it will not raise any error and will run the code with wrong type of argument. Ex: if we pass int instead of str to a function which expects str, it will raise error if @ensure_annotations is used above the function.

from box import ConfigBox #this will help in accessing values in yaml file as if they are attributes of a class Ex: config.model_name otherwise we have to use config['model_name'] like we do with dictionaries.
from pathlib import Path
from typing import Any



@ensure_annotations
def read_yaml(path_to_yaml: Path) -> ConfigBox: 
    #Description of function:
    """reads yaml file and returns content in ConfigBox type

    Args:
        path_to_yaml (str): path like input

    Raises:
        ValueError: if yaml file is empty
        e: empty file

    Returns:
        ConfigBox: ConfigBox type
    """
    try:
        with open(path_to_yaml) as yaml_file:
            content = yaml.safe_load(yaml_file)
            logger.info(f"yaml file: {path_to_yaml} loaded successfully")
            return ConfigBox(content)
    except BoxValueError:
        raise ValueError("yaml file is empty")
    except Exception as e:
        raise e
    


@ensure_annotations
def create_directories(path_to_directories: list, verbose=True):
    """creates list of directories

    Args:
        path_to_directories (list): list of path of directories
        ignore_log (bool, optional): ignore if multiple dirs is to be created. Defaults to False.
    """
    for path in path_to_directories:
        os.makedirs(path, exist_ok=True)
        if verbose:
            logger.info(f"created directory at: {path}")



@ensure_annotations
def get_size(path: Path) -> str:
    """get size in KB

    Args:
        path (Path): path of the file

    Returns:
        str: size in KB
    """
    size_in_kb = round(os.path.getsize(path)/1024)
    return f"~ {size_in_kb} KB"

    
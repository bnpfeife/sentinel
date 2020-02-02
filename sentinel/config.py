from schema import And
from schema import Optional
from schema import Schema
from schema import Use
import re
import typing
import yaml


def load(path:str) -> typing.Dict[str, typing.Any]:
    '''
    '''
    with open(path) as data:
        return Schema({
          'targets': [{
            'src': And(str, len),  # source path
            'dst': And(str, len),  # destination path
            # command takes a list of strings. The list is passed into calli().
            # Each element within the list can optionally specify format
            # variables to reference parts of the source and destination
            # file paths.
            'commands': [[ And(str, len) ]],
            # include_regex and exclude_regex take a list of regex strings.
            # Each element is pre-compiled to save processing power while
            # analyzing the file paths.
            'include_regex':                       [ Use(lambda s: re.compile(s)) ],
            Optional('exclude_regex', default=[]): [ Use(lambda s: re.compile(s)) ],
            }],
          'interval': int
        }).validate(yaml.safe_load(data))


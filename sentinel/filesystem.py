import typing
import re
import os
import os.path


def get_matching(
    target: str,
    re_includes: typing.List[re.Pattern]=[],
    re_excludes: typing.List[re.Pattern]=[]) -> typing.List[str]:
    '''
    '''
    return [ _path for _path in
        # Iterate through each object within the target directory. Construct
        # a flattened list of paths to each object relative to the target
        # directory. All objects that are NOT files are ignored.
        [ os.path.relpath(os.path.join(_root, _file), start=target)
            for (_root, _dirs, _files) in os.walk(target) for _file in _files ]
            # Determine if each relative path matches at least ONE regex
            # within re_includes and matches NONE within re_excludes.
            if not any([ regex.match(_path) for regex in re_excludes ]) and
                   any([ regex.match(_path) for regex in re_includes ]) ]


def get_modified_times(
    target: str,
    objects: typing.List[str]) -> typing.List[typing.Tuple[str, float]]:
    '''
    '''
    # Iterate through each object within the object list. Construct a list
    # of tuples containing the relative path and last modified time.
    return [ (_object, os.stat(os.path.join(target, _object)).st_mtime)
        for _object in objects ]

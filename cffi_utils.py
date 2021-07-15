import os
import numpy as np
from cffi import FFI

def ensure_folder_or_file(fileURI):
    if not os.path.isdir(fileURI) and not os.path.isfile(fileURI):
        raise OSError("Target does not exist.\nSearched for: " + fileURI + "\n")

def extract_function_def(headerFileURI):
    funDef = ''
    with open(headerFileURI) as headerFile:
        hf = headerFile.read()
        idxLo = hf.find(r'extern "C" {')
        idxHi = hf.find('} //end extern "C"')
        while (idxLo>0 and idxHi>0):
            tmp = hf[idxLo+12:idxHi]
            if "#" not in tmp:
                funDef += tmp
            hf = hf[idxHi+18:]
            idxLo = hf.find(r'extern "C" {')
            idxHi = hf.find('} //end extern "C"')
    return funDef

def ensure_np_type(arr, target_type):
    if arr.dtype is not np.dtype(target_type):
        return arr.astype(np.float64)
    else:
        return arr

def get_pointer_to_np_arr(arr, ctype, ffi):
    return ffi.cast(ctype, arr.ctypes.data)

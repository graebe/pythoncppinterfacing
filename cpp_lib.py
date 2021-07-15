# Imports
import os
import numpy as np
from cffi import FFI

# Import Utils
from cffi_utils import ensure_folder_or_file, ensure_np_type
from cffi_utils import extract_function_def
from cffi_utils import get_pointer_to_np_arr

# Global DLL Load Function
CWD = __file__.replace('\\', '/')
CWD = CWD[:CWD.rfind('/')]

# Libs
sharedLibFolderURI = CWD + "/build"
headerFileURI = CWD + "/cpp_lib.h"
dllURI = CWD + "/build/libcpp_lib.dll"

# Preparations
ensure_folder_or_file(sharedLibFolderURI)
ensure_folder_or_file(headerFileURI)
ensure_folder_or_file(dllURI)
functionDefinitions = extract_function_def(headerFileURI)

# Add Lib to Windows PATH
os.environ['PATH'] = sharedLibFolderURI + os.pathsep + os.environ['PATH']

# Instantiate FFI
ffi = FFI()
cpp_lib = ffi.dlopen(dllURI)
ffi.cdef(functionDefinitions)

# Wrapper Class myProcessor
class myProcessor():

    def __init__(self, exp, size):
        self.id = cpp_lib.myProcessorInit(exp, size)

    def process(self, data, size):
        data = ensure_np_type(data, 'float64')
        pointer_to_data = get_pointer_to_np_arr(data, "double*", ffi)
        ret = cpp_lib.myProcessorProcess(self.id, pointer_to_data, size)
        if ret<0:
            raise ValueError("Sth bad happened in c++ code")
        else:
            return data

if __name__ == "__main__":
    exp = 2
    size = 10
    data = np.array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])
    mpInst = myProcessor(exp, size)
    data = mpInst.process(data, size)
    print(data)
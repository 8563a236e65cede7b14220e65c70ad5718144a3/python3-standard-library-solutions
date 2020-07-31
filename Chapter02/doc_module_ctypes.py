"""
ctypes - A foreign function library for Python

ctypes is a foreign function library for Python. It provides C compatible
data types and allows calling functions in DLLs or shared libraries. It
can be used to wrap these libraries in pure Python


Loading dynamic link libraries
    On Linux it is required to specify the filename including the
    extension to load a library, so attribute access can not be used to
    load libraries. Either the LoadLibrary() method of the dll loaders
    should be used, or you should load the library by creating an
    instance of CDLL by calling the constructor
"""
import ctypes

ctypes.cdll.LoadLibrary("libc.so.6")
libc = ctypes.CDLL("libc.so.6")
libc

"""
Accessing functions from loaded calls
    Functions are accessed as attributes of dll objects
    Sometimes dlls export functions with names which aren't valid
    Python identifiers, like "??2@YAPAXI@Z". In this case, you have to
    use getattr() to retrieve the function
"""
libc.printf
#getattr(ctypes.cdll.msvcrt, "??2@YAPAXI@Z")

"""
Calling functions
    You can call these functions like any other Python callable. This
    example uses the time() function, which returns system time in
    seconds since the Unix epoch
    To find out the correct calling convention you have to look into
    the C header file or the documentation for the function you want to
    call
    The faulthandler module can be helpful in debugging crashes
    (e.g. from segmentation faults produced by erroneous C library
    calls)
    None, integers, bytes objects and (unicode) strings are the only
    native Python objects that can be directly used as parameters in
    these function calls. None is passed as a C NULL pointer, bytes
    objects and strings are passed as pointer to the memory block
    that contains their data (char * or wchar_t *). Python integers
    are passed as the platforms default C int type, their value is
    masked to fit into the C type    
"""
print(libc.time(None))

"""
Fundamental data types
    ctypes type     C type                  Python type
    _bool           _Bool                   bool(1)
    c_char          char                    1-character bytes object
    c_wchar         wchar_t                 1-character string
    c_byte          char                    int
    c_ubyte         unsigned char           int
    c_short         short                   int
    c_ushort        unsigned short          int
    c_int           int                     int
    c_uint          unsigned int            int
    c_long          long                    int
    c_ulong         unsigned long           int
    c_longlong      long long               int
    c_ulonglong     unsigned long log       int
    c_size_t        size_t                  int
    c_ssize_t       ssize_t                 int
    c_float         float                   float
    c_double        double                  float
    c_longdouble    long_double             float
    c_char_p        char* (NUL terminated)  bytes object or None
    c_wchar_p       wchar_t*(NUL terminated)string or None
    c_void_p        void*                   int or None
    
    All of these types can be created by calling them with an optional
    initializer of the correct type and value:
"""
ctypes.c_int()
ctypes.c_wchar_p("Hello, World")
ctypes.c_ushort(-3)

"""
    Since these types are mutable, their value can also be changed 
    afterwards
"""

i = ctypes.c_int(42)
print(i)
print(i.value)
i.value = -99
print(i.value)

"""
    Assigning a new value to instances of the point types c_char_p,
    c_wchar_p and c_void_p changes the memory location they point
    to, not the contents of the memory block 
"""
s = "Hello, World"
c_s = ctypes.c_wchar_p(s)
print(c_s)
print(c_s.value)
c_s.value = "Hi, there"
print(c_s)  # the memory location has changed
print(c_s.value)
print(s)    # first object is unchanged

"""
    ***Be careful not to pass them to functions expecting pointers
    to mutable memory. If you need mutable memory blocks, ctype
    has a create_string_buffer() function which creates these in
    various ways. The current memory block contents can be accessed
    (or changed) with the raw proprerty; if you want to access
    it as NUL terminated string, use the value property
"""
# create a 3 byte buffer, initialized to NUL bytes
p = ctypes.create_string_buffer(3)
print(ctypes.sizeof(p), repr(p.raw))
# create a buffer containing a NUL terminated string
p = ctypes.create_string_buffer(b"Hello")
print(ctypes.sizeof(p), repr(p.raw))
print(repr(p.value))
#create a 10 byte buffer
p = ctypes.create_string_buffer(b"Hello", 10)
print(ctypes.sizeof(p), repr(p.raw))
p.value = b"Hi"
print(ctypes.sizeof(p), repr(p.raw))

"""
    The create_string_buffer function replaces the c_buffer() function
    as well as the c_string() function from earlier ctypes releases. To
    create a mutable memory block containing unicode characters of the
    C type wchar_t use the create_unicode_buffer() function.
    
    Note that printf prints to the real standard output channel, not
    to sys.stdout, so these examples will only work at the 
    console prompt.
"""
printf = libc.printf
printf(b"Hello, %s\n", b"World!")
printf(b"Hello, %S\n", "World!")
printf(b"%d bottles of beer\n", 42)
printf(b"%f bottles of beer\n", ctypes.c_double(42.5))

"""
    All Python types except integers, strings, and bytes objects have
    to be wrapped in their corresponding ctype so that they can be
    converted to the required C data type.
"""
printf(b"An int %d, a double %f\n", 1245, ctypes.c_double(3.14))

"""
Calling functions with your own custom data types
    You can also customize ctypes argument conversion to allow instances
    of your own classes to be used as function arguments. ctypes looks
    for an _as_parameter_ attribute and uses this as the function
    argument. It must be one of integer, string or bytes
    
    If you don't want to store the instance's data in the _as_parameter_
    instance variable, you could define a property which makes the
    attribute available on request.

"""


class Bottles:

    def __init__(self, number):
        self._as_parameter_ = number

bottles = Bottles(42)
printf(b"%d bottles of beer\n", bottles)

"""
Specifying the required argument types (function prototypes)
    It is possible to specify the required argument types of
    functions exported from DLLs by setting the argtype attribute.
    
    argtypes must be a sequence of C data types
"""
printf.argtypes = [ctypes.c_char_p, ctypes.c_char_p, ctypes.c_int,
                   ctypes.c_double]
printf(b"String '%s', Int %d, Double %f\n", b"Hi", 10, 2.2)

"""
    Specifying a format protects against incompatible argument types
    (just as a prototype for a C function), and tries to conver the
    arguments to valid types
"""
try:
    printf(b"%d %d %d", 1, 2, 3)
except ctypes.ArgumentError:
    print("Wrong Type")

"""
    If you have defined your own classes which you pass to function calls,
    you have to implement a from_param() class method for them to be able
    to use them in the argtypes sequence. The from_param() class method
    receives the Python object passed to the function call, it should
    do a type check or whatever is needed to make sure this object is
    acceptable, and then return the object itself, its _as_parameter_
    attribute, or whatever you want to pass as the C function argument
    in this case. The result should be an integer, string, bytes, a
    ctypes instance or an object with an _as_parameter_ attribute.
    
Return types
    By default functions are assumed to return the C int type. Other
    return types can be specified by setting the restype attribute of
    the function object.
"""
strchr = libc.strchr
print(strchr(b"abcdef", ord("d")))
strchr.restype = ctypes.c_char_p
print(strchr(b"abcdef", ord("d")))
print(strchr(b"abcdef", ord("x")))

strchr.argtypes = [ctypes.c_char_p, ctypes.c_char]
print(strchr(b"abcdef", b"d"))
try:
    print(strchr(b"abcdef", b"def"))
except ctypes.ArgumentError as err:
    print(err)
print(strchr(b"abcdef", b"d"))

"""
    You can also use a callable Python object (a function or a class
    for example) as the restype attribute, if the foreign function
    returns an integer. The callable will be called with the integer
    the C function returns, and the result of this call will be used
    as the result of your function call. This is useful to check for
    error return values and automatically raise an exception
    
    Note errcheck attribute provides a more powerful error checking
    mechanism

Passing pointers
    Sometimes a C api expects a pointer to a data type as parameter,
    probably to write into the corresponding location, or if the data
    is too large to be passed by value.
    
    ctypes exports the byref() function which is used to pass parameters
    by reference. The same effect can be achieved with the pointer()
    function, although pointer() does a lot more work since it 
    constructs a real pointer object, so it is faster to use byref()
    if you don't need the pointer object in Python itself.
"""
i = ctypes.c_int()
f = ctypes.c_float()
s = ctypes.create_string_buffer(b"\000" * 32)
print(i.value, f.value, repr(s.value))
libc.sscanf(b"1 3.14 Hello", b"%d %f %s",
            ctypes.byref(i), ctypes.byref(f), s)
print(i.value, f.value, repr(s.value))

"""
Structures and unions
    Structures and unions must derive from the Structure and Union
    base classes which are defined in the ctypes module. Each subclass
    must define a _fields_ attribute. _fields_ must be a list of
    2-tuples containing a field name and a field type.
    
    The field type must be a ctypes type like c_int, or any other
    derived ctypes type: structure, union, array, pointer
"""


class POINT(ctypes.Structure):
    _fields_ = [
        ("x", ctypes.c_int),
        ("y", ctypes.c_int)
    ]


point = POINT(10, 20)
print(point.x, point.y)
point = POINT(y=5)
print(point.x, point.y)
try:
    POINT(1, 2, 3)
except TypeError as err:
    print(err)

"""
    You can, however, build much more complicated structures. A structure
    can itself contain other structures by using a structure as a field
    type.
"""


class RECT(ctypes.Structure):
    _fields_ = [
        ("upperleft", POINT),
        ("lowerright", POINT)
    ]

    def __str__(self):
        return f"({self.upperleft.x}, {self.upperleft.y}), " \
               f"({self.lowerright.x}, {self.lowerright.y})"


rc = RECT(point)
print(rc.upperleft.x, rc.upperleft.y)
print(rc.lowerright.x, rc.lowerright.y)

"""
    Nested structures can also be initialized in the constructor in
    sever ways
"""
r = RECT(POINT(1, 2), POINT(3, 4))
print(r)
r = RECT((1, 2), (3, 4))
print(r)

"""
Field descriptors can be retrieved from the class, they are useful
for debugging because they can provide useful information
"""
print(POINT.x)
print(POINT.y)

"""
Structure/union alignment and byte order
    BY default, structure and union fields are aligned in the same
    way the C compiler does it. It is possible to override this
    behaviour by specifying a _pack_ class attribute
    in the subclass definition. This must be set to a positive integer
    and specifies the maximum alignment for the fields.
    
    ctypes uses the native byte order for Structures and Unions. To
    build structures with non-native byte order, you can use one of the
    BigEndianStructure, LittleEndianStructure, BigEndianUnion and
    LittleEndianUnion base classes. These classes cannot contain
    pointer fields.
    
Bit fields in structures and unions
    It is possible to create structures and unions containing bit fields.
    Bit fields are only possible for integer fields, the bit width is 
    specified as in the third item in the _fields_ tuples
"""


class Int(ctypes.Structure):
    _fields_ = [
        ("first_16", ctypes.c_int, 16),
        ("second_16", ctypes.c_int, 16)
    ]


print(Int.first_16)
print(Int.second_16)

"""
Arrays
    Arrays are sequences containing a fixed number of instances of the
    same type.
    
    The recommended way to create array types is by multiplying a data
    type with a positive integer
"""
TenPointsArrayType = POINT * 10


class MyStruct(ctypes.Structure):
    _fields_ = [
        ("a", ctypes.c_int),
        ("b", ctypes.c_float),
        ("point_array", POINT * 4)
    ]


print(len(MyStruct().point_array))

"""
    Instances are created in the usual way, by calling the class
"""
arr = TenPointsArrayType()
for pt in arr:
    print(pt.x, pt.y)

TenIntegers = ctypes.c_int * 10
ii = TenIntegers(1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
print(ii)
for i in ii:
    print(i, end=" ")
print()

"""
Pointers
    Pointer instances are created by calling the pointer() function
    on a ctypes type
"""
i = ctypes.c_int(42)
pi = ctypes.pointer(i)

"""
    Pointer instances have a contents attribute which returns the
    object to which the pointer points
"""
print(pi.contents)

"""
    Note that ctypes does not have original object return, it constructs
    a new, equivalent object each time you retrieve an attribute
"""
print(pi.contents is i)
print(pi.contents is pi.contents)

"""
    Assigning another c_int instance to the pointer's contents attribute
    would cause the pointer to point to the memory locations where this
    is stored
"""
i = ctypes.c_int(99)
pi.contents = i
print(pi.contents)

"""
    Pointer instances can also be indexed with integers:
"""
print(pi[0])

"""
    Assigning to an integer index changes the pointed to value:
"""
print(i)
pi[0] = 22
print(i)

"""
    It is also possible to use indexes different from 0, but you must
    know what you're doing, just as in C. You can access or change
    arbitrary memory locations. Generally, you only use this feature
    if you receive a pointer from a C function, and you know that
    the pointer actually points to an array instead of a single item
    
    Behind the scenes, the pointer() function does more than simply
    create pointer instances, it has to create pointer types first. This
    is done with the POINTER() function, which accepts any ctypes and
    returns a new type
"""
PI = ctypes.POINTER(ctypes.c_int)
print(PI)
try:
    PI(42)
except TypeError as err:
    print(err)
print(PI(ctypes.c_int(42)))

"""
    Calling the pointer type without an argument creates a NULL pointer.
    NULL pointers have a FALSE boolean value
"""
null_ptr = ctypes.POINTER(ctypes.c_int)()
print(bool(null_ptr))

"""
    ctypes checks for NULL when dereferencing pointers (but 
    dereferencing invalid non-NULL pointers would crash Python)
"""
try:
    null_ptr[0]
except ValueError as err:
    print(err)
try:
    null_ptr[0] = 1234
except ValueError as err:
    print(err)

"""
Type conversions
    Usually ctypes does strict type checking. This means, if you have
    POINTER(c_int) in the argtypes list of a function or as the type of
    a member field in a structure definition, only instances of exactly
    the same type are accepted. There are some exceptions to this rule,
    where ctypes accepts other objects e.g. compatible array instances.
"""


class Bar(ctypes.Structure):
    _fields_ = [
        ("count", ctypes.c_int),
        ("values", ctypes.POINTER(ctypes.c_int))
    ]


bar = Bar()
bar.values = (ctypes.c_int * 3)(1, 2, 3)
bar.count = 3
for i in range(bar.count):
    print(bar.values[i])

"""
    In addition, if a function argument is explicitly declared to be a
    pointer type (such as POINTER(c_int)) in argtypes, an object of the
    pointed type (c_int in this case) can be passed to the function.
    ctypes will apply the required byref() conversion in this case
    automatically.
    
    To set a POINTER type field to NULL, you can assign None
"""
bar.values = None

"""
    Sometimes you have instances of incompatible types. In C, you 
    can cast one type into another type. ctypes provides a cast()
    function which can be used in the same way. The Bar structure
    defined above accepts POINTER(c_int) pointers or c_int arrays
    for its values field, but not instances of other types
"""
try:
    bar.values = (ctypes.c_byte * 4)()
except TypeError as err:
    print(err)

"""
    For these cases, the cast function is handy.
    
    The cast() function can be used to cast a ctypes instance into a
    pointer to a different ctypes data type. cast() takes two parameters,
    a ctypes object that is or can be converted to a pointer of some
    kind, and a ctypes pointer type. It returns an instance of the 
    second argument, which references the same memory block as the first
    argument
"""
a = (ctypes.c_byte * 4)()
print(ctypes.cast(a, ctypes.POINTER(ctypes.c_int)))
bar = Bar()
bar.values = ctypes.cast((ctypes.c_byte * 4)(),
                         ctypes.POINTER(ctypes.c_int))
print(bar.values[0])

"""
Incomplete Types
    Incomplete Types are structures, unions or arrays whose members
    are not yet specified. In C, they are specified by forward
    declarations which are defined later
    
    struct cell;    /* forward declaration */
    
    struct cell {
        char* name
        struct cell* next;
    };
    
    The straight forward translations into ctypes code would be    
"""
try:
    class cell(ctypes.Structure):
        _fields_ = [
            ("name", ctypes.c_char_p),
            ("next", ctypes.POINTER(cell))
        ]
except NameError as err:
    print(err)
"""
    but this does not work as the new class cell is not available in
    the class statement itself. In ctypes, we define the cell class and
    set the _fields_ attribute later, after the class statement
"""


class cell(ctypes.Structure):
    pass


cell._fields_ = [
    ("name", ctypes.c_wchar_p),
    ("next", ctypes.POINTER(cell))
]

c1 = cell()
c1.name = "foo"
c2 = cell()
c2.name = "bar"
c1.next = ctypes.pointer(c2)
c2.next = ctypes.pointer(c1)
p = c1

for i in range(8):
    print(p.name, end=" ")
    p = p.next[0]
print()

"""
Callback functions
    ctypes allows creating C callable function pointers from Python
    callables. These are sometimes called callback functions.
    
    First, you must create a class for the callback function. The
    class knows the calling convention, the return type, and the
    types of arguments this function will receive.
    
    The CFUNCTYPE() factory creates types for callback functions using
    the cdecl calling convention. On Windows, the WINFUNCTYPE().
    
    Both of these factory functions are called with the result type
    as the first argument, and the callback functions expected
    arguments as the remaining arguments.
"""
IntArray5 = ctypes.c_int * 5
ia = IntArray5(5, 1, 7, 33, 99)
qsort = libc.qsort
qsort.restype = None

"""
    qsort() must be called with a pointer to the data to sort, the number
    of items in the data array, the size of one item, and a pointer to the
    comparison function, the callback. The callback will then be called with
    two pointers to items, and it must return a negative integer if the
    first item is smaller than the second, a zero if they are equal and
    a positive integer otherwise
"""
CMPFUNC = ctypes.CFUNCTYPE(ctypes.c_int,
                           ctypes.POINTER(ctypes.c_int),
                           ctypes.POINTER(ctypes.c_int))


def py_cmp_func(a, b):
    print("py_cmp_func", a[0], b[0])
    return 0


cmp_func = CMPFUNC(py_cmp_func)

qsort(ia, len(ia), ctypes.sizeof(ctypes.c_int), cmp_func)


def py_cmp_func(a, b):
    print("py_cmp_func", a[0], b[0])
    return a[0] - b[0]


qsort(ia, len(ia), ctypes.sizeof(ctypes.c_int),
      CMPFUNC(py_cmp_func))

for i in ia:
    print(i, end=" ")
print()

"""
    The function factories can be used as decorator factories, so we
    may as well write
"""


@ctypes.CFUNCTYPE(ctypes.c_int,
                  ctypes.POINTER(ctypes.c_int),
                  ctypes.POINTER(ctypes.c_int))
def py_cmp_func(a, b):
    print("py_cmp_func", a[0], b[0])
    return a[0] - b[0]


qsort(ia, len(ia), ctypes.sizeof(ctypes.c_int), py_cmp_func)

"""
    Make sure you keep references to CFUNCTYPE() objects as long as 
    they are used from C code. ctypes doesn't, and if you don't, they
    may be garbage collected, crashing your program when a callback
    is made

Accessing values exported from dlls
    Some shared libraries not only export functions, they also export
    variables. An example in the Python library itself is the
    Py_OptimizeFlag, an integer set to 0, 1 or 2, depending on the
    -O or -OO flag given on startup
    
    ctypes can access values like this with the in_dll() class methods
    of the type. pythonapi is a predefined symbol giving access to the
    Python C api
"""
opt_flag = ctypes.c_int.in_dll(ctypes.pythonapi, "Py_OptimizeFlag")
print(opt_flag)

"""
    An extended example which also demonstrates the use of pointers
    accesses the PyImport_FrozenModules pointer exported by Python
"""


class struct_frozen(ctypes.Structure):
    _fields_ = [
        ("name", ctypes.c_char_p),
        ("code", ctypes.POINTER(ctypes.c_ubyte)),
        ("size", ctypes.c_int)
    ]


FrozenTable = ctypes.POINTER(struct_frozen)
table = FrozenTable.in_dll(ctypes.pythonapi, "PyImport_FrozenModules")

"""
    Since table is a pointer to the array of struct_frozen records, we
    can iterate over it, but we just have to make sure that out loop
    terminates, because pointers have no size. Sooner or later it would 
    probably crash with an access violation, so it's better to break out
    of the loop when we hit the NULL entry
"""
for item in table:
    if item.name is None:
        break
    print(item.name.decode("ascii"), item.size)

"""
    The fact that standard Python has a frozen module and a frozen
    package (indicated by the negative size member) is not well know,
    it is only used for testing

Surprises
    There are some edges in ctypes where you might expect something
    other than what actually happens
    
    Consider the following example
"""


class POINT(ctypes.Structure):
    _fields_ = [
        ("x", ctypes.c_int),
        ("y", ctypes.c_int)
    ]


class RECT(ctypes.Structure):
    _fields_ = [
        ("a", POINT),
        ("b", POINT)
    ]


p1 = POINT(1, 2)
p2 = POINT(3, 4)
rc = RECT(p1, p2)

print(rc.a.x, rc.a.y, rc.b.x, rc.b.y)
# Swap the two points around
rc.a, rc.b = rc.b, rc.a
print(rc.a.x, rc.a.y, rc.b.x, rc.b.y)

"""
    temp0, temp1 = rc.b, rc.a
    rc.a = temp0
    rc.b = temp1
    
    Note that temp0 and temp1 are objects still using the internal
    buffer of the rc object above. So executing rc.a = temp0 copies
    the buffer contents of temp0 into rc's buffer. This, in turn,
    changes the contents of temp1 so that the last assignment 
    rc.b = temp1 doesn't have the expected effect
    
    Keep in mind that retrieving the sub-objects from Structures,
    Unions and Arrays doesn't copy the sub-object, instead it
    retrieves a wrapper object accessing the root-object's underlying
    buffer.
"""
s = ctypes.c_char_p()
s.value = b"abc def ghi"
print(s.value)
print(s.value is s.value)

"""
    ctypes instances are objects containing a memory block plus some
    descriptors accessing the contents of the memory. Storing a Python
    object in the memory block does not store the object itself, instead
    the contents of the object is stored. Accessing the contents again
    constructs a new Python object each time

Variable-sized data types
    ctypes provides some support for variable-sized arrays and
    structures.
    
    The resize() function can be used to resize the memory buffer
    of an existing ctypes object. The function takes the object as
    first argument, and the requested size in bytes as the second
    argument. The memory block cannot be made smaller than the natural
    memory block specified by the objects type, a ValueError is
    raised if this is tried
"""
short_array = (ctypes.c_short * 4)()
print(ctypes.sizeof(short_array))
try:
    ctypes.resize(short_array, 4)
except ValueError as err:
    print(err)
ctypes.resize(short_array, 32)
print(ctypes.sizeof(short_array))
print(ctypes.sizeof(type(short_array)))

# How would we access the additional elements?
print(short_array[:])
try:
    short_array[7]
except IndexError as err:
    print(err)

"""
    Another way to use variable-sized data types with ctypes is to use
    the dynamic nature of Python and (re-)define the data types after
    the required size is already known, on a case by case basis


ctypes reference

Finding shared libraries
    When programming in a compiled language, shared libraries are
    accessed when compiling/linking a program, and when the program
    is run.
    
    The purpose of the find_library() function is to locate a library
    in a way similar to what the compiler or runtime loader does (on
    platforms with several versions of a shared library the most recent
    should be loaded), while the ctypes library loaders act like when
    a program is run, and call the runtime loader directly.
    
    The ctypes.util module provides a function which can help to
    determine the library to load
    
    ctypes.util.find_library(name)
        Try to find a library and return a pathname. name is the library
        name without any prefix like lib, suffix like .so or .dylib or
        version number. If no library can be found, returns None
"""
import ctypes.util

print(ctypes.util.find_library("m"))
print(ctypes.util.find_library("c"))
print(ctypes.util.find_library("bz2"))

"""
    Loading shared libraries
    There are several ways to load shared libraries into the Python
    process. One way is to instantiate one of the following classes
    
    class ctypes.CDLL(name, mode=DEFAULT_MODE, handle=None,
        use_errno=False, use_last_error=False, winmode=0)
        Instances of this class represent loaded shared libraries. 
        Functions in these libraries use the standard C calling 
        convention and are assumed to return int
        
    The Python global interpreter lock is released before calling
    any function exported by these libraries, and reacquired afterwards
    
    class ctypes.PyDLL(name, mode=DEFAULT_MODE, handle=None)
        Instances of this class behave like CDLL instances, except
        that the Python GIL is not released during the function call,
        and after the function execution the Python error flag is checked.
        If the error flag is set, a Python exception is raised. This is
        only useful to call Python C api functions directly
        
    All of these classes can be instantiated by calling them with at least
    one argument, the pathname of the shared library. If you have an existing
    handle to an already loaded shared library, it can be passed as the
    handle named parameter, otherwise, the underlying platforms dlopen
    or LoadLibrary function is used to load the library into the process
    and to get a handle to it
    
    The mode parameter can be used to specify how the library is loaded.
    Consult dlopen(3) manpage
    
    The use_errno parameter, when set to true, enables a ctypes 
    mechanism that allows accessing the system errno error number in a
    sage way. ctypes maintains a thread-local copy of the systems errno
    variable. If you call foreign functions created with use_errno=True
    then the errno value before the function call is swapped with ctypes
    private copy, the same happens immediately after the function call.
    
    The function ctypes.get_errno() returns the value of the ctypes
    private copy and the function ctypes.set_errno() changes the ctypes
    private copy to a new value, and returns the former value
    
    The use_last_error parameter, when set to true, enables the same
    mechanism for the Windows error code. Winmode is used on windows.
    
    ctypes.RTLD_GLOBAL
        Flag to use as mode parameter
    ctypes.RTLD_LOCAL
        Flag to use as mode parameter
    ctypes.DEFAULT_MODE
        The default mode which is used to load shared libraries
    
    Instances of these classes have no public methods. Functions
    exported by the shared library can be accessed by attributes or
    by index. Note, accessing the function through an attribute caches
    the result and therefore accessing it repeatedly returns the same
    object each time. On the other hand, accessing it through an
    index returns a new object each time
"""
print("libc.time == libc.time", libc.time == libc.time)
print("libc[\"time\"] == libc[\"time\"]", libc["time"] == libc["time"])

"""
    The following public attributes are available, their name starts
    with an underscore to not clash with exported function names
    
    PyDLL._handle
        The system handle used to access the library
    PyDLL._name
        The name of the library passed in the constructor
    
    Shared libraries can also be loaded by using one of the prefabricated
    objects, which are instances of the LibraryLoader class, either by
    calling the LoadLibrary() method, or by retrieving the library
    as attribtue of the loader instances
    
    class ctypes.LibraryLoader(dlltype)
        dlltype should be one of CDLL, PyDLL, WinDLL or OleDLL
        
        __getattr__() has special behaviour. It allows loading a shared
        library by accessing it as attribute of a library loader instance.
        The result is cached, so repeated attribute accesses return the
        same library each time.
        
        LoadLibrary(name)
            Load a shared library into the process and return it. This
            method always returns a new instance of the library
    
    These prefabricated library loaders are available:
    
    ctypes.cdll
        Creates CDLL instances
    ctypes.windll
        Creates WinDLL instances. Windows Only
    ctypes.oledll
        Creates OleDLL instances. Windows Only
    ctypes.pydll
        Creates PyDLL instances
        
    For accessing the C python api directly, a ready-to-use Python
    shared library object is available:
    
    ctypes.pythonapi
        An instance of PyDLL that exposes Python C API functions as 
        attributes. Note that all these functions are assumed to return
        C int, which is of course not always the truth, so you have to
        assign the correct restype attribute to use these functions
    
    Loading a library through any of these objects raises an auditing
    event ctypes.dlopen with string argument name, the name used to load
    the library
    
    Accessing a function on a loaded library raises an auditing event
    ctypes.dlsym with arguments library (the library object) and name 
    (the symbol's name as a string or integer)
    
    In cases when only the library handle is available rather than the
    object, accessing a function raises an auditing event 
    ctypes.dlsym/handle with arguments handle (the raw library handle)
    and name
    
Foreign Functions
    Foreign functions can be accessed as attributes of loaded
    shared libraries. The function objects created in this way by
    default accept any number of arguments, accept any ctypes data
    instances as arguments, and return the default result type by the 
    library loader. They are instances of a private class
    
    class ctypes._FuncPtr
        Base class for C callable foreign functions
        
        Instances of foreign functions are also C compatible data types;
        they represent C function pointers.
        
        This behaviour can be customized by assigning to special 
        attributes of the foreign function object.
        
        restype
            Assign a ctypes type to specify the result type of the
            foreign function. Use None for void, a function not returning
            anything
            
            It is possible to assign a callable Python object that is not
            a ctypes type, in this case the function is assumed to return
            a C int, and the callable will be called with this integer,
            allowing further processing or error checking. Using this is
            deprecated, rather assign callable to errcheck attribute
        
        argtypes
            Assign a tuple of ctypes types to specify the argument types
            that the function accepts. Functions using the stdcall
            calling convention can only be called with the same number of
            arguments as the length of this tuple; functions using the
            C calling convention accept additional, unspecified arguments
            as well.
            
            When a foreign function is called, each actual argument is 
            passed to the from_param() class method of the items in the
            argtypes tuple, this method allows adapting the actual argument
            to an object that the foreign function accepts. e.g.
            c_char_p item in the argtypes tuple will convert a string passed
            as argument into a bytes object using ctypes conversion rules.
            
            It is now possible to put items in argtypes which are not
            ctypes, but each item must have a from_param() method which 
            returns a value usable as argument (integer, string, ctypes
            instance). This allows defining adapters that can adapt custom
            objects as function parameters.
        
        errcheck
            Assign a Python function or another callable to this attribute.
            The callable will be called with three or more arguments
                callable(result, func, arguments)
                    result is what the foreign function returns, as 
                    specified by the restype attribute
                    
                    func is the foreign function object itself, this allows
                    reusing the same callable object to check or post 
                    process the results of several functions.
                    
                    arguments is a tuple containing the parameters 
                    originally passed to the function call, this allows
                    specializing the behaviour on the arguments used
            
            The object that this function returns will be returned from
            the foreign function call, but it can also check the result
            value and raise an exception if the foreign function call
            failed.
            
    exception ctypes.ArgumentError
        This exception is raised when a foreign function call cannot
        convert one of the passed arguments.

Function prototypes
    Foreign functions can also be created by instantiating function
    prototypes. Function prototypes are similar to function prototypes
    in C, they describe a function (return type, argument types,
    calling convention) without defining an implementation. The
    factory functions must be called with the desired result type
    and argument types of the function, and can be used as decorator
    factories, and as such, be applied to functions through the
    @wrapper syntax
    
    ctypes.CFUNCTYPE(restype, *argtypes, use_errno=False,
    use_last_error=False)
        The returned function prototype creates functions that use the
        standard C calling convention. The function will release the
        GIL during the call. If use_errno is set to try, the ctypes
        private copy of the system errno variable is exchanged with
        the real errno value before and after the call
    
    ctypes.PYFUNCTYPE(restype, *argtypes)
        The returned function prototype creates functions that use
        the Python calling convention. The function will not release
        the GIL during the call
        
    Function prototypes created by these factory functions can be 
    instantiated in different ways, depending on the type and number
    of the parameters in the call
        
        prototype(address)
            Returns a foreign function at the specified address
            which must be an integer
            
        prototype(callable)
            Creates a C callable function (a callback function) from
            a Python callable
        
        prototype(func_spec[,paramflags])
            Return a foreign function exported by a shared library.
            func_spec must be a 2-tuple (name_or_ordinal, library).
            The first item is the name of the exported function as
            string, or the ordinal of the exported function as small
            integer. The second item is the shared library instance
        
        prototype(vtbl_index, name[,paramflags[,iid]]_
            Returns a foreign function that will call a COM method.
            vtbl_index is the index into the virtual function table,
            a small non-negative integer. name is the name of the 
            COM method. iid is an optional pointer to the interface
            identifier which is used in extended error reporting
            
        The optional paramflags parameter creates foreign function
        wrappers with much more functionality than the features
        described above.
        
        paramflags must be a tuple of the same length as argtypes
        
        Each item in this tuple contains further information about
        a parameter, it must be a tuple containing one, two or three
        items.
            First item
                1 - Specifies an input parameter to the function
                2 - Output parameter. The foreign function fills in a
                    value
                4 - Input parameter which defaults to the integer zero
        
        The optional second item is the parameter name as string. If
        this is specified, the foreign function can be called with
        named parameters
        
        The optional third item is the default value for this parameter
        
        Functions with output parameters will automatically return
        the output parameter value if there is a single one, or a
        tuple containing the output parameter values when there are
        more than one.
        
        Output parameters can be combined with the errcheck protocol
        to do further output processing and error checking. If the 
        errcheck function returns the argument tuple it receives
        unchanged, ctypes continues the normal processing it does on
        the output parameters.
        
Utility functions
    
    ctypes.addressof(obj)
        Returns the address of the memory buffer as integer. obj
        must be an instance of a ctypes type
        Raises an auditing event ctypes.addressof with argument obj
    
    ctypes.alignment(obj_or_type)
        Returns the alignment requirements of a ctypes type. 
        obj_or_type must be a ctypes type or instance
    
    ctypes.byref(obj[,offeset])
        Returns a light-weight pointer to obj, which must be an
        instance of a ctypes type. offset defaults to zero, and must
        be an integer that will be added to the internal pointer
        value
        
        byref(obj, offset) corresponds to
        (((char* )&obj) + offset)
        
        The returned object can only be used as a foreign function
        call parameter. It behaves similar to pointer(obj) but the
        construction is a lot faster
        
    ctypes.cast(obj, type)
        This function is similar to the cast operator in C. It
        returns a new instance of type which points to the same 
        memory block as obj. type must be a pointer type, and
        obj must be an object that can be interpreted as a pointer
    
    ctypes.create_string_buffer(init_or_size, size=None)
        This function creates a mutable character buffer. The
        returned object is a ctypes array of c_char
        
        init_or_size must be an integer which specifies the size of
        the array, or a bytes object which will be used to initialize
        the array items
        
        If a bytes object is specified as the first argument, the
        buffer is made one item larger than its length so that the last
        element in the array is a NUL termination character. An 
        integer can be passed as second argument which allows specifying
        the size of the array if the length of the bytes should not
        be used
        
    ctypes.create_unicode_buffer(init_or_size, size=None)
        This function creates a mutable unicode character buffer. The
        returned object is a ctypes array of c_wchar
        
        init_or_size must be an integer which specifies the size of
        the array, or a string object which will be used to initialize
        the array items
        
        If a string is specified as the first argument, the
        buffer is made one item larger than its length so that the last
        element in the array is a NUL termination character. An 
        integer can be passed as second argument which allows specifying
        the size of the array if the length of the string should not
        be used
    
    ctypes.util.find_library(name)
        Try to find a library and return a pathname. name is the 
        library name without any prefix like lib, suffix like .so or
        version number. If no library can be found, returns None
        
    ctypes.get_errno()
        Returns the current value of the ctypes-private copy of the
        system errno variable in the calling thread.
        
    ctypes.memmove(dst, src, count)
        Same as the standard C memmove library function: copies
        count bytes from src to dst. dst and src must be integers or
        ctypes instances that can be converted to pointers
    
    ctypes.memset(dst, c, count)
        Same as the standard C memset library function: fills the
        memory block at address dst with count bytes of value c. dst
        must be an integer specifying an address or a ctypes instance
        
    ctypes.POINTER(type)
        This factory function creates and returns a new ctypes
        pointer type. Pointer types are cached and reused internally,
        so calling this function repeatedly is cheap. type must be
        a ctypes type.
    
    ctypes.pointer(obj)
        This function creates a new pointer instance, pointing to
        obj. The returned object is of type POINTER(type(obj))
        
    ctypes.resize(obj, size)
        This function resizes the internal memory buffer of obj, which
        must be an instance of a ctypes type. It is not possible to 
        make the buffer smaller than the native size of the objects
        type, as given by sizeof(type(obj)), but it is possible to
        enlarge the buffer
    
    ctypes.set_errno(value)
        Set the current value of the ctypes-private copy of the system
        errno variable in the calling thread to value and return the
        previous value
    
    ctypes.sizeof(obj_or_type)
        Returns the size in bytes of a ctypes type or instance memory
        buffer. Does the same as the C sizeof operator
    
    ctypes.string_at(address, size=-1)
        This function returns the C string starting at memory address
        address as a bytes object. If size is specified, it is used as
        size, otherwise the string is assumed to be zero-terminated

    ctypes.wstring_at(address, size=-1)
        This function returns the wide charater string starting at 
        memory address address as a string. If size is specified, it is
        used as the number of characters of the string, otherwise 
        the string is assumed to be zero-terminated

Data types
    
    class ctypes._CData
        This non-public class is the common base class of all ctypes
        data types. Among other things, all ctypes instances contain
        a memory block that hold C compatible data. The address of the
        memory block is returned by the addressof() helper function. 
        Another instance variable is exposed as _objects; this contains
        other Python objects that need to be kept alive in case
        the memory block contains pointers.
        
        Common methods of ctypes data types, these are all class
        methods (to be exact, they are methods of the metaclass)
        
        from_buffer(source[,offset])
            This method returns a ctypes instance that shares the 
            buffer of the source object. The source object must support
            the writeable buffer interface. The optional offset
            parameter specifies an offset into the source buffer in
            bytes; the default is zero. If the source buffer is not
            large enough a ValueError is raised
        
        from_buffer_copy(source[,offset])
            This method creates a ctypes instance, copying the buffer
            from the source object buffer, which must be readable. The
            optional offset parameter specifies an offset into the 
            source buffer in bytes; the default is zero. If the source
            buffer is not large enough, a ValueError is raised.
            
        from_address(address)
            This method returns a ctypes type instance using the
            memory specified by address which must be an integer
            
        from_param(obj)
            This method adapts obj to a ctypes type. It is called with
            the actual object used in the foreign function call when 
            the type is present in the foreign function's argtypes
            tuple; it must return an object that can be used as a
            function call parameter
            
            All ctypes data types have a default implementation of this
            classmethod that normally returns obj if that is an instance
            of the type. Some types accept other objects as well.
        
        in_dll(library, name)
            This method returns a ctypes type instance exported by a
            shared library. name is the name of the symbol that exports
            the data, library is the loaded shared library.
            
        Common instance variables of ctypes data types:
        _b_base_
            Sometimes ctypes data instances do not own the memory block
            they contain, instead they share part of the memory block
            of a base object. The _b_base_ read-only member is the root
            ctypes object that owns the memory block
        
        _b_needsfree_
            The read-only variable is true when the ctypes data instance
            has allocated the memory block itself, false otherwise.
        
        _objects
            This member is either None or a dictionary containing 
            Python objects that need to be kept alive so that the 
            memory block contents is kept valid. This object is only
            exposed for debugging; never modify the contents of this
            dictionary

Fundamental data types
    
    class ctypes._SimpleCData
        This non-public class is the base class of all fundamental
        ctypes data types. It is mentioned here because it contains
        the common attributes of the fundamental ctypes data types.
        _SimpleCData is a subclass of _CData, so it inherits their
        methods and attributes. ctypes data types that are not and
        do not contain pointers can now be pickled.
    
    Instances have a single attribute:
    
    value
        This attribute contains the actual value of the instance. For
        integer and pointer types, it is an integer, for character
        types, it is a single character bytes object or string, for
        character pointer types it is a Python bytes object or string
        
        When the value attribute is retrieved from a ctypes instance,
        usually a new object is returned each time. ctypes does not
        implement original object return, always a new object is
        constructed. The same is true for all other ctypes object
        instances
    
    Fundamental data types, when returned as foreign function call 
    results, or, for example, by retrieving structure field members
    or array items, are transparently converted to native Python
    types. In other words, if a foreign function has a restype of
    c_char_p, you will always receive a Python bytes object, not
    a c_char_p instance.
    
    Subclasses of fundamental data types do not inherit this behaviour.
    So if a foreign functions restype is a subclass of c_void_p, you
    will receive an instance of this subclass from the function call.
    Of course, you can get the value of the pointer by accessing the
    value attribute
    
    c_byte          C signed char
    c_char          C char
    c_char_p        C char*
    c_double        C double
    c_longdouble    C long double
    c_float         C float
    c_int           C signed int
    c_int8          C 8-bit signed int
    c_int16         C 16-bit signed int
    c_int32         C 32-bit signed int
    c_int64         C 64-bit signed int
    c_long          C signed long
    c_longlong      C signed long long
    c_short         C signed short
    c_size_t        C size_t
    c_ssize_t       C ssize_t
    c_ubyte         C unsigned char
    c_uint          C unsigned int
    c_uint8         C 8-bit unsigned int
    c_uint16        C 16-bit unsigned int
    c_uint32        C 32-bit unsigned int
    c_uint64        C 64-bit unsigned int
    c_ulong         C unsigned long
    c_ulonglong     C unsigned long long
    c_ushort        C unsigned short
    c_void_p        C void*
    c_wchar         C wchar_t
    c_wchar_p       C wchar_t*
    c_bool          C _Bool from C99
    py_object       C PyObject* 

Structured Data Types
    
    class ctypes.Union(*args, **kw)
        Abstract base class for unions in native byte order
    
    class ctypes.BigEndianStructure(*args, **kw)
        Abstract base class for structures in big endian byte order
        
    class ctypes.LittleEndianStructure(*args, **kw)
        Abstract base class for structures in little endian byte order
    
    Structures with non-native byte order cannot contain pointer type
    fields, or any other data types containing pointer type fields.
    
    class ctypes.Structure(*args, **kw)
        Abstract base class for structures in native byte order.
        
        Concrete structure and union types must be created by 
        subclassing one of these types, and at least define a _fields_
        class variable. ctypes will create descriptors which allow reading
        and writing the fields by direct attribute accesses. These are the
        
        _fields_
            A sequence defining the structure fields. The items must be
            2-tuples or 3-tuples. The first item is the name of the field,
            the second item specifies the type of the field; it can be
            any ctypes data type
            
            For integer type fields like c_int, a third optional item can
            be given. It must be a small positive integer defining the
            bit width of the field
            
            Field names must be unique within one structure or union. This
            is not checked, only one field can be accessed when names are
            repeated
            
            It is possible to define the _fields_ class variable after the
            class statement that defines the Structure subclass, this allows
            creating data types that directly or indirectly reference 
            themselves
"""


class List(ctypes.Structure):
    pass


List._fields_ = [("pnext", ctypes.POINTER(List))]

"""
            The _fields_ class variable must, however, be defined
            before the type is first used (an instance is created,
            sizeof() is called on it, and so on). Later assignments
            to the _fields_ class variable will raise an AttributeError
            
            It is possible to define sub-subclasses of structure 
            types, they inherit the fields of the base class plus the
            _fields_ defined in the sub_subclass, if any
            
        _pack_
            An optional small integer that allows overriding the
            alignment of structure fields in the instance. _pack_
            must already be defined when _fields_ is assigned, 
            otherwise it will have no effect
        
        _anonymous_
            An optional sequence that lists the names of unnamed
            (anonymous) fields. _anonymous_ must already be defined
            when _fields_ is assigned, otherwise it will have no effect
            
            The fields listed in this variable must be structure or
            union type fields. ctypes will create descriptors in the
            structure type that allows accessing the nested fields
            directly, without the need to create the structure or 
            union fields.
    
    It is possible to define sub-subclasses of structures, they
    inherit the fields of the base class. If the subclass definition
    has a separate _fields_ variable, the fields specified in this are
    appended to the fields of the base class
    
    Structure and union constructors accept both positional and
    keyword arguments. Positional arguments are used to initialize
    member fields in the same order as they appear in _fields_.
    Keyword arguments in the constructor are interpreted as attribute
    assignments, so they will initialize _fields_ with the same name, or
    create new attributes for names not present in _fields_
    
Arrays and pointers
    
    class ctypes.Array(*args)
        Abstract base class for arrays
        
        The recommended way to create concrete array types is by
        multiplying any ctypes data type with a positive integer. 
        Alternatively, you can subclass this type and define
        _length_ and _type_ class variables. Array elements can be
        read and written using the standard subscript and slice
        accesses; for slice reads, the resulting object is not
        itself an Array
        
        _length_
            A positive integer specifying the number of elements in
            the array. Out-of-range subscripts result in an IndexError
            Will be returned by len()
        _type_
        Specifies the type of each element in the array
        
        Array subclass constructors accept positional arguments, used
        to initialize the elements in order
    
    class ctypes._Pointer
        Private, abstract base class for pointers.
        
        Concrete pointer types are created by calling POINTER() with
        the type that will be pointed to; this is done automatically
        by pointer()
        
        If a pointer points to an array, its elements can be read and
        written using standard subscript and slice accesses. Pointer
        objects have no size, so len() will raise a TypeError. 
        Negative subscripts will read from the memory before the
        pointer (as in C) and out-of-range subscripts will probably
        crash with an access violation
            _type_
                Specifies the type pointed to
            contents
                Returns the object to which the pointer points. 
                Assigning to this attribute changes the pointer to point
                to the assigned object
"""
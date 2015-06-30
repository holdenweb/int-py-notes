"""This is a simple module to demonstrate the import mechanism.
It contains a function definition and a print statement that will
cause output to appear when the module's code is executed.

This version has been modified to use stars not minus signs."""

def f_simple(s):
    line = "*"*len(s)
    return "\n".join([line, s, line])

print(f_simple("This is a test string"))
"""
Modules & packages, exception handling overview
"""


# PyPI is a repository for open-source third-party Python packages
# similar to NuGet in .net world or NPM for Node.js

# use pip install to install packages , --proxy='' may be required when behind a FW
# e.g. pip install colorama (coloring console output)

# internal modules and packages
# modules are just .py scripts that are called from another .py script
# packages are a colloction of modules; it requires a __init__.py script

# sample in ./modules_packages/

# if __name__ == '__main__":
# it also allows to see if something was imported or run directly
# also used as a 'main' function handler so that everything can be aligned as python doesn't really have a main
# by default everything is run from top to bottom, this helps to have a clean startup function

# exception handling: the same as try-catch-finally
# try: except: finally:  e.g.

def test(path):
    try:
        f = open(path, 'w')
        f.write('test ')
    except TypeError:
        print('Type error')
    except OSError:
        print('OS error')
    except:
        print('Generic error')
    finally:
        print('I always run')

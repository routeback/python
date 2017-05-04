#!/usr/bin/python3

# Provides a list of locally installed python modules and their version

import pip
installed_packages = pip.get_installed_distributions()
installed_packages_list = sorted(["%s==%s" % (i.key, i.version)
     for i in installed_packages])
print ("\n".join(installed_packages_list))


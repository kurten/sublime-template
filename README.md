=============================
 Simple Sublime templates plugin
=============================
:Author: Kurten Chan <chinkurten@gmail.com>

This is a simple plugin for sublime text 2 that will allow you to have a set of
templates for certain file types. It is useful to add boilerplate code
like guards in C/C++ headers, or license disclaimers.


Installation
============

1. ``cd Sublime Text 2/Packages/``

2. ``git clone git://github.com/kurten/sublime-template.git``


Updating
========


1. ``cd Sublime Text 2/Packages/sublime-template``

2. ``git pull``


Setting
=============

In your Preferences.sublime-settings you can put:

* ``sublime_template_template : "template"`` to define your own template(in Sublime Text 2/Packages/sublime-template/templates/ folder).

* ``sublime_template_user : "Kurten Chan" `` to define who create file.

* ``sublime_template_email : "chinkurten@gmail.com" `` to define creator's email.

* ``sublime_template_guard : "guard"`` to define a string with alphanumeric characters and underscores.


Usage
=====

use Command Palette and select ``Sublime Template: New File With Template``


Variables in templates
----------------------

The following variables will be expanded in templates:

``%DAY%``, ``%YEAR%``, ``%MONTH%``
    Numerical day of the month, year and month.
``%DATE%``
    Date in ``YYYY-mm-dd`` format
``%TIME%``
    Time in ``HH:MM`` format
``%FDATE``
    Full date (date + time), in ``YYYY-mm-dd HH:MM`` format.
``%FILE%``
    File name, without extension.
``%FFILE%``
    File name, with extension.
``%MAIL%``
    Current user's e-mail address. May be overriden by defining ``g:email``.
``%USER%``
    Current logged-in user name. May be overriden by defining ``g:username``.
``%HOST%``
    Host name.
``%GUARD%``
    A string with alphanumeric characters and underscores, suitable for use
    in proprocessor guards for C/C++/Objective-C header files.
``%HERE%``
    Expands to nothing, but ensures that the cursor will be placed in its
    position after expanding the template.


Thanks to [aperezdc](https://github.com/aperezdc/vim-template/)，I use his vim-template projects template files.

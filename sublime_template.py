#
# sublime_template.py
# Copyright (C) 2014 Kurten Chan <chinkurten@gmail.com>
# 
# Distributed under terms of the BSD license.
# 
# coding=utf-8
#
import os
import sublime
import sublime_plugin
import datetime
import sys
import os

def get_time(format):
    return datetime.datetime.now().strftime(format)


# New File With Template Command
class SublimeTemplateCommand(sublime_plugin.WindowCommand):
    def run(self):
        self.window.show_input_panel("File name with ext:", "",
                                         self.on_done, None, None)
    #after input done callback
    def on_done(self, text, edit=None):
        if text == "":
            return

        file_name, ext = os.path.splitext(text)
        view = self.window.new_file()
        view.set_name(text)
        content, here = self.get_content(file_name, ext)
        view.run_command("insert_snippet", { "contents": "%s" %  content })  #insert content
        try:
            syntax_file = sublime.packages_path() + '/sublime-template/template_syntax_map.json'
            file = open(syntax_file)
            import json
            data = json.load(file);
            if ext in data:
                syntax = data.get(ext)
                view.set_syntax_file(syntax)
            file.close()
        except IOError as e:
            print(e.strerror)
        view.sel().clear()  #clear all region
        view.sel().add(sublime.Region(here, here))  #set cursor to here
    
    #get template content from template file
    def get_content(self, file_name, ext):
        settings = sublime.load_settings("Preferences.sublime-settings")
        template = sublime.packages_path() + "/sublime-template/templates/"
        template = template + settings.get('sublime_template_template', 'template') + ext
        try:
            if os.path.exists(template) == False:
                return "", 0
            file = open(template)
            lines = file.readlines()
            file.close()
            user = settings.get('sublime_template_user', os.getlogin())
            email = settings.get('sublime_template_email', "example@example.com")
            guard = settings.get('sublime_template_guard', (file_name + '_h'))
            content = "".join(lines)
            content = content.replace('%FFILE%', (file_name + ext))
            content = content.replace('%FILE%', file_name)
            content = content.replace('%YEAR%', get_time('%Y'))
            content = content.replace('%DAY%', get_time('%d'))
            content = content.replace('%MONTH%', get_time('%m'))
            content = content.replace('%DATE%', get_time("%Y-%m-%d"))
            content = content.replace('%TIME%', get_time("%H:%M"))
            content = content.replace('%FDATE%', get_time("%Y-%m-%d %H:%M"))
            content = content.replace('%USER%', user)
            content = content.replace('%MAIL%', email)
            content = content.replace('%GUARD%', guard)
            here = content.find('%HERE%')
            content = content.replace('%HERE%', '')
            return content, here

        except IOError as e:
            print("file not found:" + e.strerror)
        return "", 0

        
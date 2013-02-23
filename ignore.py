from os import path

import sublime
from git import GitTextCommand, GitWindowCommand, plugin_file

class GitIgnoreCommand(GitTextCommand):
    def run(self, edit):
        command = ['git', 'status', '-s', '--ignored', self.get_file_name()]
        self.run_command(command, self.ignore_done);

    def ignore_done(self, result):
        # check index status.
        print result
        if result.startswith('\?'):
            return
        command = ['git', 'rev-parse', '--show-toplevel'];
        self.run_command(command, self.show_toplevel_done)

    def show_toplevel_done(self, result):
        ignorefile = result.strip() + '/.gitignore'
        ignorepath = path.relpath(path.abspath(self.get_file_name()), result.strip());
        with open(ignorefile, 'a') as f:
            f.write('\n' + ignorepath)



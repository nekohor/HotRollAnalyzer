import subprocess
import os


class Exporter:

    def __init__(self, ctx):
        self.ctx = ctx

    def export(self, tag):
        if tag == "pond":
            print("pond export")
            self.pond_export()
        print("end export")

    def pond_export(self):
        print('Run Pond task ({})...'.format(os.getpid()))
        print(self.ctx.dir.pond_dir)
        print(self.ctx.dir.root_dir)
        commond = " ".join(
            [self.ctx.dir.program_dir + "/" + "exporter.exe",
             self.ctx.dir.pond_dir,
             self.ctx.dir.root_dir])
        print(commond)
        input("hehe")
        p = subprocess.Popen(
            commond,
            shell=True,
            stdout=subprocess.PIPE,
            stderr=subprocess.STDOUT)

        while p.poll() is None:
            info = p.stdout.readline().strip()
            if info:
                print('Subprogram output: {}'.format(info))
        if p.returncode == 0:
            print('Subprogram success')
        else:
            print(p.returncode)
            print('Subprogram failed')

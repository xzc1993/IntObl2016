import subprocess

for idx in range(0, 400, 4):
    process = subprocess.Popen([
        'qsub',
        '-l', 'nodes=1:ppn=12',
        '-A', 'intob2016',
        '-l', 'walltime=2:00:00',
        '-F', '"{0} {1}"'.format(str(idx), str(idx+4)),
        '/people/plgkzieba/IntObl2016/main.sh'])

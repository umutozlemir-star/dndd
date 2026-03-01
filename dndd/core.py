import subprocess
def pypck(name,version):
  n=name+"/"+name
  subprocess.run(["mkdir",n])
  init=f"""from {name} from test,dndd
  __version__={version}"""
  core=f"""def test():
    print("test comlete")
  def dndd()
    print("{name} {version} dndd")"""
print("comlete")

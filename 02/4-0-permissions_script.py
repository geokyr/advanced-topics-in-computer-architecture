import os

path = "/home/george/adv-ca/advcomparch-22-ex2-helpcode"

top = path + "/spec_execs_train_inputs/"
for folder in os.listdir(top):
    for file in os.listdir(top + folder):
        if file.endswith(("nn", "static")):
            exe = top+folder+"/"+file
            os.system(f"sudo chmod u+x {exe}")
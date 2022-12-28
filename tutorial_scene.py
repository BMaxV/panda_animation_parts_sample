from math import pi, sin, cos

from direct.showbase.ShowBase import ShowBase
from direct.task import Task
from direct.actor.Actor import Actor

class Wrapper:
    def __init__(self):

        # this is required for this demo
        self.b = ShowBase()

        # this is sort of optional allows for easily building and deleting
        # elements
        self.setup()

    def setup(self):

        # Load the environment model.
        # Reparent the model to render.
        scene = self.b.loader.loadModel("models/environment")
        scene.reparentTo(self.b.render)
        
        # Apply scale and position transforms on the model.
        scene.setScale(0.25, 0.25, 0.25)
        scene.setPos(-2, 42, 0)


        # Add the spinCameraTask procedure to the task manager.
        self.b.taskMgr.add(self.spinCameraTask, "SpinCameraTask")
        
        filename="./BlendFile.gltf"
        
        my_actor=Actor(filename)
        
        my_actor.reparentTo(self.b.render)
        
        my_actor.make_subpart("y_plus",["Yplus"])
        my_actor.make_subpart("y_neg",["Ynegative"])
        
        ob = self.b.loader.loadModel(filename)
        ob.reparentTo(self.b.render)
           

    def spinCameraTask(self, task):
        d=100
        angleDegrees = task.time * 6.0
        angleRadians = angleDegrees * (pi / 180.0)
        self.b.camera.setPos(d * sin(angleRadians), -d * cos(angleRadians), d)
        self.b.camera.setHpr(angleDegrees, -40, 0)

        return Task.cont


if __name__=="__main__":
    W=Wrapper()
    while True:
        W.b.taskMgr.step()

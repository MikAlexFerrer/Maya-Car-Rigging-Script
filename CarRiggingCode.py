from maya import cmds
from functools import partial
import math

# Final
class ReactiveUI:
    # meant to be overiden
    state = {}
    
    def __init__(self, name, title, size):
        if cmds.window(name, ex=True):
            cmds.deleteUI(name, window=True)
            
        self.window = cmds.window(name, title=title, widthHeight=size, sizeable=False)
        
        cmds.columnLayout(columnWidth=250, adjustableColumn=True, rowSpacing=4)
        cmds.setParent( '..' )
        cmds.rowColumnLayout( numberOfColumns = 1) 
        
        self.buildWidgets()
        
    def show(self):
        cmds.showWindow( self.window )
        
    def setState(self, key, value):
        self.state[key][0]=value
        self.state[key][1]=True

        
    def sliderGrpValueUpdated(self, key, value):
        self.setState(key, value)
    
    def createFloatSliderGrp(self, key, label, extralabel, minValue, maxValue, value, field=True, step=1):
        name = cmds.floatSliderGrp( field=field, label=label, minValue=minValue, maxValue=maxValue, value=value, extraLabel=extralabel,step=step, dc=partial(self.sliderGrpValueUpdated, key))

        return name

    def createRows(self, key, label, minValue, maxValue, value, field=True, step=1):
        name = cmds.rowColumnLayout( field=field, label=label, minValue=minValue, maxValue=maxValue, value=value, step=step, dc=partial(self.sliderGrpValueUpdated, key) )
        
        return name
        


class CarModifierUI(ReactiveUI):
    state = {
        'Volante': [0, False],
        'IzquierdaPuertas': [0, False],
        'DerechaPuertas': [0, False],
        'IzquierdaVidrios': [0, False],
        'DerechaVidrios': [0, False],
        'IzquierdaLlantasDelanteras': [0, False],
        'DerechaLlantasDelanteras': [0, False],
        'IzquierdaLlantasTraseras': [0, False],
        'DerechaLlantasTraseras': [0, False],
        'IzquierdaSteerLlantasDelanteras': [0, False],
        'DerechaSteerLlantasDelanteras': [0, False],
        'GeneralSuspension': [0, False],
        'SuspensionesDelanteras': [0, False],
        'SuspensionesTraseras': [0, False],
        'IzquierdaVentanasDelanteras': [0, False],
        'DerechaVentanasDelanteras': [0, False],
        'IzquierdaSuspensionesDelanteras': [0, False],
        'DerechaSuspensionesDelanteras': [0, False],
        'IzquierdaSuspensionesTraseras': [0, False],
        'DerechaSuspensionesTraseras': [0, False],
    }
        
    def buildWidgets(self):
        cmds.setParent('..')
        cmds.text( label='Steering wheel', align='center', w = 1060 )
        cmds.rowColumnLayout(adjustableColumn = 1, numberOfRows = 1) 
        self.createFloatSliderGrp(key='Volante', label='Turn Left', extralabel = 'Turn Right', minValue=-480, maxValue=480, value=self.state['Volante'][0])
        
        cmds.setParent('..')
        cmds.separator(height = 10)
        cmds.rowColumnLayout(adjustableColumn = 1, numberOfRows = 1) 
        cmds.text( label='Steer', align='center', w = 1060 )
        cmds.setParent('..')
        cmds.rowColumnLayout(adjustableColumn = 3, numberOfColumns = 2) 
        cmds.text( label='Left wheel', align='center', w = 630)
        cmds.text( label='Right wheel', align='center', w = 240)
        cmds.setParent('..')
        cmds.rowColumnLayout(adjustableColumn = 2, numberOfColumns = 2, h = 20) 
        self.createFloatSliderGrp(key='IzquierdaSteerLlantasDelanteras', label='Left', extralabel = 'Right', minValue=-45, maxValue=45, value=self.state['IzquierdaSteerLlantasDelanteras'][0])
        self.createFloatSliderGrp(key='DerechaSteerLlantasDelanteras', label='Left', extralabel = 'Right', minValue=-45, maxValue=45, value=self.state['DerechaSteerLlantasDelanteras'][0])

        cmds.setParent('..')
        cmds.separator(height = 10)
        cmds.text( label='Front doors', align='center', w = 1060 )
        cmds.setParent('..')
        cmds.rowColumnLayout(adjustableColumn = 2, numberOfColumns = 2) 
        cmds.text( label='Left', align='center', w = 630)
        cmds.text( label='Right', align='center', w = 240)
        cmds.setParent('..')
        cmds.rowColumnLayout(adjustableColumn = 2, numberOfColumns = 2) 
        self.createFloatSliderGrp(key='IzquierdaPuertas', label='Open', extralabel = 'Close', minValue=-60, maxValue=0, value=self.state['IzquierdaPuertas'][0])
        self.createFloatSliderGrp(key='DerechaPuertas', label='Close', extralabel = 'Open', minValue=0, maxValue=60, value=self.state['DerechaPuertas'][0])

        cmds.setParent('..')
        cmds.separator(height = 10)
        cmds.text( label='Front windows', align='center', w = 1060  )
        cmds.setParent('..')
        cmds.rowColumnLayout(adjustableColumn = 3, numberOfColumns = 2) 
        cmds.text( label='Left', align='center', w = 630)
        cmds.text( label='Right', align='center', w = 240)
        cmds.setParent('..')
        cmds.rowColumnLayout(adjustableColumn = 2, numberOfColumns = 2) 
        self.createFloatSliderGrp(key='IzquierdaVidrios', label='Open', extralabel = 'Close', minValue=-10, maxValue=0, value=self.state['IzquierdaVidrios'][0])
        self.createFloatSliderGrp(key='DerechaVidrios', label='Open', extralabel = 'Close', minValue=0, maxValue=10, value=self.state['DerechaVidrios'][0])
        
        cmds.setParent('..')
        cmds.separator(height = 10)
        cmds.rowColumnLayout(adjustableColumn = 2, numberOfColumns = 1) 
        cmds.text( label='Suspension', align='center' , w = 1060 )
        cmds.setParent('..')
        cmds.rowColumnLayout(adjustableColumn = 1, numberOfColumns = 1) 
        self.createFloatSliderGrp(key='GeneralSuspension', label='Lower', extralabel = 'Higher', minValue=-4, maxValue=4, value=self.state['GeneralSuspension'][0])

        cmds.setParent('..')
        cmds.separator(height = 10)
        cmds.rowColumnLayout(adjustableColumn = 2, numberOfColumns = 1) 
        cmds.setParent('..')
        cmds.text( label='Front suspension', align='center', w = 1060  )
        cmds.rowColumnLayout(adjustableColumn = 1, numberOfColumns = 1) 
        self.createFloatSliderGrp(key='SuspensionesDelanteras', label='Lower', extralabel = 'Higher', minValue=-4, maxValue=4, value=self.state['SuspensionesDelanteras'][0])
        cmds.setParent('..')
        cmds.rowColumnLayout(adjustableColumn = 3, numberOfColumns = 2) 
        cmds.text( label='Left Wheel', align='center', w = 630)
        cmds.text( label='Right Wheel', align='center', w = 240)
        cmds.setParent('..')
        cmds.rowColumnLayout(adjustableColumn = 2, numberOfColumns = 2) 
        self.createFloatSliderGrp(key='IzquierdaSuspensionesDelanteras', label='Lower', extralabel = 'Higher', minValue=-4, maxValue=4, value=self.state['IzquierdaSuspensionesDelanteras'][0])
        self.createFloatSliderGrp(key='DerechaSuspensionesDelanteras', label='Lower', extralabel = 'Higher', minValue=-4, maxValue=4, value=self.state['DerechaSuspensionesDelanteras'][0])
        

        cmds.setParent('..')
        cmds.separator(height = 10)
        cmds.rowColumnLayout(adjustableColumn = 2, numberOfColumns = 1) 
        cmds.text( label='Back suspension', align='center', w = 1060 )
        cmds.setParent('..')
        cmds.rowColumnLayout(adjustableColumn = 1, numberOfColumns = 1) 
        self.createFloatSliderGrp(key='SuspensionesTraseras', label='Lower', extralabel = 'Higher', minValue=-4, maxValue=4, value=self.state['SuspensionesTraseras'][0])
        cmds.setParent('..')
        cmds.rowColumnLayout(adjustableColumn = 3, numberOfColumns = 2) 
        cmds.text( label='Left Wheel', align='center', w = 630)
        cmds.text( label='Right Wheel', align='center', w = 240)
        cmds.setParent('..')
        cmds.rowColumnLayout(adjustableColumn = 2, numberOfColumns = 2) 
        self.createFloatSliderGrp(key='IzquierdaSuspensionesTraseras', label='Lower', extralabel = 'Higher', minValue=-4, maxValue=4, value=self.state['IzquierdaSuspensionesTraseras'][0])
        self.createFloatSliderGrp(key='DerechaSuspensionesTraseras', label='Lower', extralabel = 'Higher', minValue=-4, maxValue=4, value=self.state['DerechaSuspensionesTraseras'][0])
        
        cmds.setParent('..')
        cmds.separator(height = 10)
        cmds.text( label='Front turning', align='center', w = 1060  )
        cmds.setParent('..')
        cmds.rowColumnLayout(adjustableColumn = 3, numberOfColumns = 2) 
        cmds.text( label='Left', align='center', w = 630)
        cmds.text( label='Right', align='center', w = 240)
        cmds.setParent('..')
        cmds.rowColumnLayout(adjustableColumn = 2, numberOfColumns = 2) 
        self.createFloatSliderGrp(key='IzquierdaLlantasDelanteras', label='', extralabel = '', minValue=0, maxValue=360, value=self.state['IzquierdaLlantasDelanteras'][0])
        self.createFloatSliderGrp(key='DerechaLlantasDelanteras', label='', extralabel = '', minValue=0, maxValue=360, value=self.state['DerechaLlantasDelanteras'][0])

        cmds.setParent('..')
        cmds.separator(height = 10)
        cmds.text( label='Back turning', align='center', w = 1060  )
        cmds.setParent('..')
        cmds.rowColumnLayout(adjustableColumn = 3, numberOfColumns = 2) 
        cmds.text( label='Left', align='center', w = 630)
        cmds.text( label='Right', align='center', w = 240)
        cmds.setParent('..')
        cmds.rowColumnLayout(adjustableColumn = 2, numberOfColumns = 2) 
        self.createFloatSliderGrp(key='IzquierdaLlantasTraseras', label='', extralabel = '', minValue=0, maxValue=360, value=self.state['IzquierdaLlantasTraseras'][0])
        self.createFloatSliderGrp(key='DerechaLlantasTraseras', label='', extralabel = '', minValue=0, maxValue=360, value=self.state['DerechaLlantasTraseras'][0])



    def setState(self, *args):
        super().setState(*args)
        
        self.executeOrders()
        
    def clean(self):
        cmds.delete("%s*" % self.state['groupName'])
        
    def executeOrders(self, *args):
        if (self.state['Volante'][1]):
            self.state['Volante'][1] = False
            self.modifyCarSteeringWheel(self.state['Volante'][0])  
        
        elif (self.state['IzquierdaSteerLlantasDelanteras'][1] or self.state['DerechaSteerLlantasDelanteras'][1]):
            self.state['IzquierdaSteerLlantasDelanteras'][1] = False
            self.state['DerechaSteerLlantasDelanteras'][1] = False
            self.modifyCarFrontWheelsRotate(self.state['IzquierdaSteerLlantasDelanteras'][0], self.state['DerechaSteerLlantasDelanteras'][0])  

        elif (self.state['IzquierdaPuertas'][1] or self.state['DerechaPuertas'][1]):
            self.modifyCarFrontDoors(self.state['IzquierdaPuertas'][0], self.state['DerechaPuertas'][0]) 
            self.state['IzquierdaPuertas'][1] = False
            self.state['DerechaPuertas'][1] = False
        
        elif (self.state['GeneralSuspension'][1]):
            self.modifyCarSuspension(self.state['GeneralSuspension'][0])
            self.state['GeneralSuspension'][1] = False

        elif (self.state['SuspensionesDelanteras'][1]):
            self.modifyCarFrontSuspension(self.state['SuspensionesDelanteras'][0])
            self.state['SuspensionesDelanteras'][1] = False

        elif (self.state['IzquierdaVidrios'][1] or self.state['DerechaVidrios'][1]):
            self.modifyCarFrontWindows(self.state['IzquierdaVidrios'][0], self.state['DerechaVidrios'][0]) 
            self.state['IzquierdaVidrios'][1] = False
            self.state['DerechaVidrios'][1] = False

        elif (self.state['IzquierdaSuspensionesDelanteras'][1] or self.state['DerechaSuspensionesDelanteras'][1]):
            self.modifyCarFrontSuspensionWheels(self.state['IzquierdaSuspensionesDelanteras'][0], self.state['DerechaSuspensionesDelanteras'][0]) 
            self.state['IzquierdaSuspensionesDelanteras'][1] = False
            self.state['DerechaSuspensionesDelanteras'][1] = False

        elif (self.state['SuspensionesTraseras'][1]):
            self.modifyCarBackSuspension(self.state['SuspensionesTraseras'][0])
            self.state['SuspensionesTraseras'][1] = False

        elif (self.state['IzquierdaSuspensionesTraseras'][1] or self.state['DerechaSuspensionesTraseras'][1]):
            self.modifyCarBackSuspensionWheels(self.state['IzquierdaSuspensionesTraseras'][0], self.state['DerechaSuspensionesTraseras'][0])
            self.state['IzquierdaSuspensionesTraseras'][1] = False
            self.state['DerechaSuspensionesTraseras'][1] = False
        
        elif (self.state['IzquierdaLlantasDelanteras'][1] or self.state['DerechaLlantasDelanteras'][1]):
            self.modifyCarFrontWheels(self.state['IzquierdaLlantasDelanteras'][0], self.state['DerechaLlantasDelanteras'][0])
            self.state['IzquierdaLlantasDelanteras'][1] = False
            self.state['DerechaLlantasDelanteras'][1] = False

        elif (self.state['IzquierdaLlantasTraseras'][1] or self.state['DerechaLlantasTraseras'][1]):
            self.modifyCarBackWheels(self.state['IzquierdaLlantasTraseras'][0], self.state['DerechaLlantasTraseras'][0])
            self.state['IzquierdaLlantasTraseras'][1] = False
            self.state['DerechaLlantasTraseras'][1] = False
        
        
    def modifyCarSteeringWheel(self, steering):
        cmds.rotate(-65-(math.fabs(50*(math.sin(math.radians(steering/2))))), 25*(-math.sin(math.radians(steering))), steering, 'steering_wheel')
        cmds.rotate(0, -steering/10, 0, 'left_front_tire')
        cmds.rotate(0, -steering/10, 0, 'right_front_tire')
    
    def modifyCarFrontWheelsRotate(self, left, right):
        cmds.rotate(0, -left, 0, 'left_front_tire')
        cmds.rotate(0, -right, 0, 'right_front_tire')
    
    def modifyCarFrontDoors(self, left, right):
        cmds.rotate(0, left, 0, 'left_door')
        cmds.rotate(0, right, 0, 'right_door')

    def modifyCarSuspension(self, suspension):
        cmds.move(0, suspension/100, 0, 'Car')
        cmds.move(0, -suspension/100, 0, 'tires')

    def modifyCarFrontSuspension(self, front):
        cmds.move(0, front/100, 0, 'front_tires')
        cmds.move(0, front/100, 0, 'front_suspension')
        cmds.rotate(front/4, 0, 0, 'Car')

    def modifyCarFrontSuspensionWheels(self, left, right):
        cmds.move(0, right/100, 0, 'right_front_tire')
        cmds.move(0, left/100, 0, 'left_front_tire')

    def modifyCarBackSuspension(self, back):
        cmds.move(0, back/100, 0, 'back_tires')
        cmds.move(0, back/100, 0, 'back_suspension')
        cmds.rotate(-back/4, 0, 0, 'Car')

    def modifyCarBackSuspensionWheels(self, left, right):
        cmds.move(0, right/100, 0, 'right_back_tire')
        cmds.move(0, left/100, 0, 'left_back_tire')
    
    def modifyCarFrontWheels(self, left, right):
        cmds.rotate(left, 0, 0, 'left_front_tire')
        cmds.rotate(right, 0, 0, 'right_front_tire')

    def modifyCarBackWheels(self, left, right):
        cmds.rotate(left, 0, 0, 'left_back_tire')
        cmds.rotate(right, 0, 0, 'right_back_tire')
    
    def modifyCarFrontWindows(self, left, right):
        cmds.setAttr( "left_door.Left_Window", left )
        cmds.setAttr( "right_door.Right_Window", right )

        
ui = CarModifierUI('CarModifierUI', "Car Rigging", (900, 730))
ui.show()

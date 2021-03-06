__author__ = 'Usuario'

import win32com.client as com
import os

Vissim = []


def load(filename):
    global Vissim
    # Connecting the COM Server => Open a new Vissim Window:
    Vissim = com.Dispatch("Vissim.Vissim")
    # If you have installed multiple Vissim Versions, you can open a specific Vissim version adding the bit
    # Version (32 or 64bit) and Version number
    # Vissim = com.Dispatch("Vissim.Vissim-32.600") # Vissim 6 - 32 bit
    # Vissim = com.Dispatch("Vissim.Vissim-64.600") # Vissim 6 - 64 bit
    # Vissim = com.Dispatch("Vissim.Vissim-32.700") # Vissim 7 - 32 bit
    # Vissim = com.Dispatch("Vissim.Vissim-64.700") # Vissim 7 - 64 bit
    Path_of_COM_example_network = os.getcwd()
    # 'C:\\Users\\Public\\Documents\\PTV Vision\\PTV Vissim 7\\Examples Training\\COM\\Basic Commands\\'

    # Load a Vissim Network:
    Filename = os.path.join(Path_of_COM_example_network, filename + '.inpx')
    # you can read network(elements) additionally, in this case set "flag_read_additionally" to true
    flag_read_additionally = False
    Vissim.LoadNet(Filename, flag_read_additionally)
    # Load a Layout:
    Filename = os.path.join(Path_of_COM_example_network, filename + '.layx')
    Vissim.LoadLayout(Filename)
    defaultvalues()
    return Vissim


def defaultvalues():
    global Vissim

    random_seed = 42 #42
    Vissim.Simulation.SetAttValue('RandSeed', random_seed)

    Sim_break_at = 60 # Simulationsecond [s]
    Vissim.Simulation.SetAttValue('SimBreakAt', Sim_break_at)

    end_of_simulation = 1000  # Simulationsecond[s]
    Vissim.Simulation.SetAttValue('SimPeriod', end_of_simulation)

    Vissim.Simulation.SetAttValue('NumRuns', 1)

    # Set maximum speed:
    Vissim.Simulation.SetAttValue('UseMaxSimSpeed', True)

    Vissim.Simulation.SetAttValue('SimSpeed', 10) # 10 => 10 Sim.sec. / s

def getvehicles(signal):
    lstvehicle = []

    signalhead = Vissim.Net.SignalHeads.ItemByKey(signal)
    link_no = signalhead.Lane.Link.AttValue("No")

    allvehicles = Vissim.Net.Links.ItemByKey(link_no).Vehs
    for v in allvehicles:
        if signalhead.AttValue("Pos") > v.AttValue("Pos"):
            if signalhead.AttValue("Pos") - 50 <= v.AttValue("Pos"):
                lstvehicle.append(v)
                #print v.AttValue("No")
    return lstvehicle

def getvehicleswithdistance(signal, distance):
    lstvehicle = []

    signalhead = Vissim.Net.SignalHeads.ItemByKey(signal)
    link_no = signalhead.Lane.Link.AttValue("No")

    allvehicles = Vissim.Net.Links.ItemByKey(link_no).Vehs
    for v in allvehicles:
        if signalhead.AttValue("Pos") > v.AttValue("Pos"):
            if signalhead.AttValue("Pos") - distance <= v.AttValue("Pos"):
                lstvehicle.append(v)
                #print v.AttValue("No")
    return lstvehicle

def runseconds(sec):
    global Vissim
    stoptime = sec + Vissim.Simulation.SimulationSecond
    Vissim.Simulation.SetAttValue('SimBreakAt', stoptime)
    Vissim.Simulation.RunContinuous()
    #print Vissim.Simulation.SimulationSecond

def RunSteps(num):
    global Vissim
    for i in range(num):
         Vissim.Simulation.RunSingleStep()
         print Vissim.Simulation.SimulationSecond

def waitforcars():
    global Vissim
    lanes = [(2, 6), (7, 3)]

    totalprincipalcars = len(getvehicleswithdistance(lanes[0][0], -40)) + len(getvehicleswithdistance(lanes[0][1],-40))
    totalsecundariacars = len(getvehicleswithdistance(lanes[1][0], -26)) + len(getvehicleswithdistance(lanes[1][1],-26))
    totalcars = totalprincipalcars + totalsecundariacars
    threshold = 0
    while totalcars > 0:
        runseconds(1)
        threshold += 1
        totalprincipalcars = len(getvehicleswithdistance(lanes[0][0], -40)) + len(getvehicleswithdistance(lanes[0][1],-40))
        totalsecundariacars = len(getvehicleswithdistance(lanes[1][0], -26)) + len(getvehicleswithdistance(lanes[1][1],-26))
        totalcars = totalprincipalcars + totalsecundariacars

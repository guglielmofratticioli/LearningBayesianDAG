from typing import AnyStr
from Graph import Node, Graph
import Visualizer
import random
from Dataset import Dataset, Example
from Learning import Score , Learn , QuickLearn

LOW2 = 0    
NORMAL2 = 1
NORMAL = 0
ESOPHA = 1
ONESID = 2
LOW3 = 0
NORMAL3 = 1
HIGH3 = 2
ZERO4 = 0
LOW4 = 1
NORMAL4 = 2
HIGH4 = 3
TRUE = 1
FALSE = 0

def ALMSampler(graph) : 
    HISTORY =   graph.nodes[0]
    CVP =       graph.nodes[1]
    PCWP =      graph.nodes[2]
    HYPOVOLEMIA =graph.nodes[3]
    LVEOVOLUME = graph.nodes[4]
    LVFAILURE =  graph.nodes[5]
    STROKEVOLUME =  graph.nodes[6]
    ERRLOWOUTPUT =  graph.nodes[7]
    HRBP =  graph.nodes[8]
    HREKG     =  graph.nodes[9]
    ERRCAUTE = graph.nodes[10]
    HRSAT =  graph.nodes[11]
    INSYFFANESTH =  graph.nodes[12]
    ANAPHYLAXIS =  graph.nodes[13]
    TPR =  graph.nodes[14]
    EXPCO = graph.nodes[15]
    KINKEDTUBE =  graph.nodes[16]
    MINVOL =  graph.nodes[17]
    FIO2 = graph.nodes[18]
    PVSAT = graph.nodes[19]
    SA02 =  graph.nodes[20]
    PAP =  graph.nodes[21]
    PULMEMBOLUS =  graph.nodes[22]
    SHUNT =  graph.nodes[23]
    INTUBATION =  graph.nodes[24]
    PRESS =  graph.nodes[25]
    DISCONNECT =  graph.nodes[26]
    MINVOLSET = graph.nodes[27]
    VENTMACH =  graph.nodes[28]
    VENTTUBE =  graph.nodes[29]
    VENTLUNG =  graph.nodes[30]
    VENTALV =  graph.nodes[31]
    ARTCO2 =  graph.nodes[32]
    CATECHOL = graph.nodes[33]
    HR =  graph.nodes[34]
    CO =  graph.nodes[35]
    BP = graph.nodes[36]

    lvfail =  random.choices( population=[ TRUE ,FALSE ] , weights= [ LVFAILURE.table.get('SELF')[0], LVFAILURE.table.get('SELF')[1] ] )
    hypovelmia = random.choices( population=[ TRUE ,FALSE ] , weights= [ HYPOVOLEMIA.table.get('SELF')[0], HYPOVOLEMIA.table.get('SELF')[1] ] )
    errlowout = random.choices( population=[ TRUE ,FALSE ] , weights= [ ERRLOWOUTPUT.table.get('SELF')[0], ERRLOWOUTPUT.table.get('SELF')[1] ] ) 
    errcauter = random.choices( population=[ TRUE ,FALSE ] , weights= [ ERRCAUTE.table.get('SELF')[0], ERRCAUTE.table.get('SELF')[1] ] )
    insyffan =  random.choices( population=[ TRUE ,FALSE ] , weights= [ INSYFFANESTH.table.get('SELF')[0], INSYFFANESTH.table.get('SELF')[1] ] )
    pulmemb =   random.choices( population=[ TRUE ,FALSE ] , weights= [ PULMEMBOLUS.table.get('SELF')[0], PULMEMBOLUS.table.get('SELF')[1] ] )
    intuv =     random.choices( population=[ NORMAL ,ESOPHA,ONESID ] , weights= [ INTUBATION.table.get('SELF')[0], INTUBATION.table.get('SELF')[1] , INTUBATION.table.get('SELF')[2] ] )
    discon =    random.choices( population=[ TRUE ,FALSE ] , weights= [ DISCONNECT.table.get('SELF')[0], DISCONNECT.table.get('SELF')[1] ] )
    minvolset = random.choices( population=[ LOW3 ,NORMAL3,HIGH3 ] , weights= [ MINVOLSET.table.get('SELF')[0], MINVOLSET.table.get('SELF')[1],MINVOLSET.table.get('SELF')[2] ]  )
    kinkedtube =  random.choices( population=[ TRUE ,FALSE ] , weights= [ KINKEDTUBE.table.get('SELF')[0], KINKEDTUBE.table.get('SELF')[1] ] )
    anaphylaxis =  random.choices( population=[ TRUE ,FALSE ] , weights= [ ANAPHYLAXIS.table.get('SELF')[0], ANAPHYLAXIS.table.get('SELF')[1] ] )
    fio2 = random.choices( population=[ TRUE ,FALSE ] , weights= [ FIO2.table.get('SELF')[0], FIO2.table.get('SELF')[1] ] )
    
    history =  random.choices( population=[ TRUE ,FALSE ] ,                 weights= [ HISTORY.table.get(lvfail[0])[0], HISTORY.table.get(lvfail[0])[1] ] )
    lveovolume =  random.choices( population=[ LOW3 ,NORMAL3, HIGH3 ] ,     weights= [ LVEOVOLUME.table.get((hypovelmia[0],lvfail[0]))[0], LVEOVOLUME.table.get((hypovelmia[0],lvfail[0]))[1], LVEOVOLUME.table.get((hypovelmia[0],lvfail[0]))[2]  ] )
    pcwp = random.choices( population=[ LOW3 ,NORMAL3, HIGH3 ] ,            weights= [ PCWP.table.get(lveovolume[0])[0], PCWP.table.get(lveovolume[0])[1], PCWP.table.get(lveovolume[0])[2] ] )
    cvp = random.choices( population=[ LOW3 ,NORMAL3, HIGH3 ] ,             weights= [ CVP.table.get(lveovolume[0])[0], CVP.table.get(lveovolume[0])[1], CVP.table.get(lveovolume[0])[2] ] )
    strokevoulme = random.choices( population=[ LOW3 ,NORMAL3, HIGH3 ] ,    weights= [ STROKEVOLUME.table.get((hypovelmia[0],lvfail[0]))[0], STROKEVOLUME.table.get((hypovelmia[0],lvfail[0]))[1], STROKEVOLUME.table.get((hypovelmia[0],lvfail[0]))[2] ] )
    tpr = random.choices( population=[ LOW3 ,NORMAL3, HIGH3 ] ,             weights= [ TPR.table.get(anaphylaxis[0])[0], TPR.table.get(anaphylaxis[0])[1], TPR.table.get(anaphylaxis[0])[2] ] )
    pap = random.choices( population=[ LOW3 ,NORMAL3, HIGH3 ] ,             weights= [ PAP.table.get(pulmemb[0])[0], PAP.table.get(pulmemb[0])[1], PAP.table.get(pulmemb[0])[2] ] )
    shunt = random.choices( population=[ LOW2 ,NORMAL2 ] ,                  weights= [ SHUNT.table.get((intuv[0], pulmemb[0]))[0], SHUNT.table.get((intuv[0], pulmemb[0]))[1] ] )
    ventmach = random.choices( population=[ ZERO4 ,LOW4, NORMAL4, HIGH4 ] , weights= [ VENTMACH.table.get(minvolset[0])[0], VENTMACH.table.get(minvolset[0])[1], VENTMACH.table.get(minvolset[0])[2], VENTMACH.table.get(minvolset[0])[3]  ] )
    venttube = random.choices( population=[ ZERO4 ,LOW4, NORMAL4, HIGH4 ] , weights= [ VENTTUBE.table.get((discon[0],ventmach[0]))[0], VENTTUBE.table.get((discon[0],ventmach[0]))[1], VENTTUBE.table.get((discon[0],ventmach[0]))[2], VENTTUBE.table.get((discon[0],ventmach[0]))[3]  ] )
    ventlung = random.choices( population=[ ZERO4 ,LOW4, NORMAL4, HIGH4 ] , weights= [ VENTLUNG.table.get((intuv[0],kinkedtube[0],venttube[0]))[0], VENTLUNG.table.get((intuv[0],kinkedtube[0],venttube[0]))[1], VENTLUNG.table.get((intuv[0],kinkedtube[0],venttube[0]))[2], VENTLUNG.table.get((intuv[0],kinkedtube[0],venttube[0]))[3]  ] )
    ventalv  = random.choices( population=[ ZERO4 ,LOW4, NORMAL4, HIGH4 ] , weights= [ VENTALV.table.get((intuv[0],ventlung[0]))[0], VENTALV.table.get((intuv[0],ventlung[0]))[1], VENTALV.table.get((intuv[0],ventlung[0]))[2], VENTALV.table.get((intuv[0],ventlung[0]))[3]  ] )
    press = random.choices( population=[ ZERO4 ,LOW4, NORMAL4, HIGH4 ] ,    weights= [ PRESS.table.get((intuv[0],kinkedtube[0],venttube[0]))[0], PRESS.table.get((intuv[0],kinkedtube[0],venttube[0]))[1], PRESS.table.get((intuv[0],kinkedtube[0],venttube[0]))[2], PRESS.table.get((intuv[0],kinkedtube[0],venttube[0]))[3] ] )
    minvol = random.choices( population=[ ZERO4 ,LOW4, NORMAL4, HIGH4 ] ,   weights= [ MINVOL.table.get((intuv[0],ventlung[0]))[0], MINVOL.table.get((intuv[0],ventlung[0]))[1], MINVOL.table.get((intuv[0],ventlung[0]))[2], MINVOL.table.get((intuv[0],ventlung[0]))[3] ] )
    pvsat = random.choices( population=[ LOW3 ,NORMAL3, HIGH3 ] ,           weights= [ PVSAT.table.get((fio2[0],ventalv[0]))[0], PVSAT.table.get((fio2[0],ventalv[0]))[1], PVSAT.table.get((fio2[0],ventalv[0]))[2]  ] )
    sao2 = random.choices( population=[ LOW3 ,NORMAL3, HIGH3 ] ,            weights= [ SA02.table.get((pvsat[0],shunt[0]))[0], SA02.table.get((pvsat[0],shunt[0]))[1], SA02.table.get((pvsat[0],shunt[0]))[2]  ] )
    artcol2 =random.choices( population=[ LOW3 ,NORMAL3, HIGH3 ] ,          weights= [ ARTCO2.table.get(ventalv[0])[0], ARTCO2.table.get(ventalv[0])[1], ARTCO2.table.get(ventalv[0])[2]  ] )
    expcol2 = random.choices( population=[ ZERO4 ,LOW4, NORMAL4, HIGH4 ] ,  weights= [ EXPCO.table.get((artcol2[0],ventlung[0]))[0], EXPCO.table.get((artcol2[0],ventlung[0]))[1], EXPCO.table.get((artcol2[0],ventlung[0]))[2], EXPCO.table.get((artcol2[0],ventlung[0]))[3]  ] )
    catechol = random.choices( population=[ TRUE ,FALSE ] ,                 weights= [ CATECHOL.table.get((artcol2[0],insyffan[0],sao2[0],tpr[0]))[0], CATECHOL.table.get((artcol2[0],insyffan[0],sao2[0],tpr[0]))[1]  ] )
    hr = random.choices( population=[ LOW3 ,NORMAL3, HIGH3 ] ,              weights= [ HR.table.get(catechol[0])[0], HR.table.get(catechol[0])[1], HR.table.get(catechol[0])[2]  ] )
    hrbp = random.choices( population=[ LOW3 ,NORMAL3, HIGH3 ] ,            weights= [ HRBP.table.get((errlowout[0],hr[0]))[0], HRBP.table.get((errlowout[0],hr[0]))[1], HRBP.table.get((errlowout[0],hr[0]))[2]  ] )
    hrekg = random.choices( population=[ LOW3 ,NORMAL3, HIGH3 ] ,           weights= [ HREKG.table.get((errcauter[0],hr[0]))[0], HRBP.table.get((errcauter[0],hr[0]))[1], HRBP.table.get((errcauter[0],hr[0]))[2]  ] )
    hrsat = random.choices( population=[ LOW3 ,NORMAL3, HIGH3 ] ,           weights= [ HRSAT.table.get((errcauter[0],hr[0]))[0], HRSAT.table.get((errcauter[0],hr[0]))[1], HRSAT.table.get((errcauter[0],hr[0]))[2]  ] )
    co = random.choices( population=[ LOW3 ,NORMAL3, HIGH3 ] ,              weights= [ CO.table.get((hr[0],strokevoulme[0]))[0], CO.table.get((hr[0],strokevoulme[0]))[1], CO.table.get((hr[0],strokevoulme[0]))[2]  ] )
    bp = random.choices( population=[ LOW3 ,NORMAL3, HIGH3 ] ,              weights= [ BP.table.get((co[0],tpr[0]))[0], BP.table.get((co[0],tpr[0]))[1], BP.table.get((co[0],tpr[0]))[2]  ] )

    return Example([ HISTORY,
        CVP, 
        PCWP, 
        HYPOVOLEMIA,
        LVEOVOLUME, 
        LVFAILURE, 
        STROKEVOLUME, 
        ERRLOWOUTPUT, 
        HRBP, 
        HREKG,         
        ERRCAUTE,
        HRSAT, 
        INSYFFANESTH, 
        ANAPHYLAXIS, 
        TPR, 
        EXPCO,
        KINKEDTUBE, 
        MINVOL, 
        FIO2,
        PVSAT,
        SA02, 
        PAP, 
        PULMEMBOLUS, 
        SHUNT, 
        INTUBATION,  
        PRESS, 
        DISCONNECT, 
        MINVOLSET,
        VENTMACH, 
        VENTTUBE, 
        VENTLUNG, 
        VENTALV, 
        ARTCO2, 
        CATECHOL,
        HR, 
        CO, 
        BP
    ] , [
        history[0],
        cvp[0],
        pcwp[0],
        hypovelmia[0],
        lveovolume[0],
        lvfail[0],
        strokevoulme[0],
        errlowout[0],
        hrbp[0],
        hrekg[0],
        errcauter[0],
        hrsat[0],
        insyffan[0],
        anaphylaxis[0],
        tpr[0],
        expcol2[0],
        kinkedtube[0],
        minvol[0],
        fio2[0],
        pvsat[0],
        sao2[0],
        pap[0],
        pulmemb[0],
        shunt[0],
        intuv[0],
        press[0],
        discon[0],
        minvolset[0],
        ventmach[0],
        venttube[0],
        ventlung[0],
        ventalv[0],
        artcol2[0],
        catechol[0],
        hr[0],
        co[0],
        bp[0] ])

def buildALMGraph():

    HISTORY = Node(label=1, domine=2, name="HISTORY")
    CVP = Node(label=2, domine=3, name="CVP")
    PCWP = Node(label=3, domine=3, name="PCWP")
    HYPOVOLEMIA = Node(label=4, domine=2, name="HYPOVOLEMIA")
    LVEOVOLUME = Node(label=5, domine=3, name="LVEOVOLUME")
    LVFAILURE = Node(label=6, domine=2, name="LVFAILURE")
    STROKEVOLUME = Node(label=7, domine=3, name="STROKEVOLUME")
    ERRLOWOUTPUT = Node(label=8, domine=2, name="ERRLOWOUTPUT")
    HRBP = Node(label=9, domine=3, name="HRBP")
    HREKG = Node(label=10, domine=3, name="HREKG")
    ERRCAUTER = Node(label=11, domine=2, name="ERRCAUTER")
    HRSAT = Node(label=12, domine=3, name="HRSAT")
    INSYFFANESTH = Node(label=13, domine=2, name="INSYFFANESTH")
    ANAPHYLAXIS = Node(label=14, domine=2, name="ANAPHYLAXIS")
    TPR = Node(label=15, domine=3, name="TPR")
    EXPCO2 = Node(label=16, domine=4, name="EXPCO2")
    KINKEDTUBE = Node(label=17, domine=2, name="KINKEDTUBE")
    MINVOL = Node(label=18, domine=4, name="MINVOL")
    FIO2 = Node(label=19, domine=2, name="FIO2")
    PVSAT = Node(label=20, domine=3, name="PVSAT")
    SA02 = Node(label=21, domine=3, name="SA02")
    PAP = Node(label=22, domine=3, name="PAP")
    PULMEMBOLUS = Node(label=23, domine=2, name="PULMEMBOLUS")
    SHUNT = Node(label=24, domine=2, name="SHUNT")
    INTUBATION = Node(label=25, domine=3, name="INTUVATION")
    PRESS = Node(label=26, domine=4, name="PRESS")
    DISCONNECT = Node(label=27, domine=2, name="DISCONNECT")
    MINVOLSET = Node(label=28, domine=3, name="MINVOLSET")
    VENTMACH = Node(label=29, domine=4, name="VENTMACH")
    VENTTUBE = Node(label=30, domine=4, name="VENTTUBE")
    VENTLUNG = Node(label=31, domine=4, name="VENTLUNG")
    VENTALV = Node(label=32, domine=4, name="VENTALV")
    ARTCO2 = Node(label=33, domine=3, name="ARTCO2")
    CATECHOL = Node(label=34, domine=2, name="CATECHOL")
    HR = Node(label=35, domine=3, name="HR")
    CO = Node(label=36, domine=3, name="CO")
    BP = Node(label=37, domine=3, name="BP")

    HISTORY.table[TRUE] = [0.9, 0, 1]
    HISTORY.table[FALSE] = [0.01, 0, 99]

    CVP.table[LOW3] =    [0.95, 0.04, 0.01]
    CVP.table[NORMAL3] = [ 0.04, 0.95, 0.0]
    CVP.table[HIGH3] =   [ 0.01, 0.29, 0.70]

    PCWP.table[LOW3]        = [ 0.95,0.04,0.01] 
    PCWP.table[NORMAL3]     = [0.04,0.95,0.01] 
    PCWP.table[HIGH3]       = [0.01,0.04,0.95]

    HYPOVOLEMIA.table['SELF']     = [0.2,0.8]

    LVEOVOLUME.table[(TRUE, TRUE)]    = [0.95, 0.04, 0.01]
    LVEOVOLUME.table[(FALSE, TRUE)]   = [0.98, 0.01, 0.01]
    LVEOVOLUME.table[(TRUE, FALSE)]   = [0.01, 0.09, 0.90]
    LVEOVOLUME.table[(FALSE, FALSE)]  = [ 0.05, 0.90, 0.05]
    

    LVFAILURE.table['SELF']  = [0.05, 0.95]

    STROKEVOLUME.table[(TRUE, TRUE)]     =  [0.98, 0.01, 0.01] 
    STROKEVOLUME.table[(FALSE, TRUE)]    =  [0.95, 0.04, 0.01]  
    STROKEVOLUME.table[(TRUE, FALSE)]    =  [0.50, 0.49, 0.01]
    STROKEVOLUME.table[(FALSE, FALSE)]   =  [ 0.05, 0.90, 0.05]

    ERRLOWOUTPUT.table['SELF']    = [0.05, 0.95] 

    HRBP.table[(TRUE, LOW3)]      =  [0.98, 0.01, 0.01]  
    HRBP.table[(FALSE, LOW3)]     =  [ 0.40, 0.59, 0.01]  
    HRBP.table[(TRUE, NORMAL3)]   =  [ 0.3, 0.4, 0.3]  
    HRBP.table[(FALSE, NORMAL3)]  =  [ 0.98, 0.01, 0.0]   
    HRBP.table[(TRUE, HIGH3)]     =  [ 0.01, 0.98, 0.01]  
    HRBP.table[(FALSE, HIGH3)]    =  [0.01, 0.01, 0.98]    
  
    HREKG.table[(TRUE, LOW3)]     =  [ 0.3333333, 0.3333333, 0.3333333]         
    HREKG.table[(FALSE, LOW3)]    =  [ 0.3333333, 0.3333333, 0.3333333]   
    HREKG.table[(TRUE, NORMAL3)]  =  [ 0.3333333, 0.3333333, 0.3333333]   
    HREKG.table[(FALSE, NORMAL3)] =  [ 0.98, 0.01, 0.0]       
    HREKG.table[(TRUE, HIGH3)]    =  [ 0.01, 0.98, 0.01]   
    HREKG.table[(FALSE, HIGH3)]   =  [ 0.01, 0.01, 0.98]       

    ERRCAUTER.table['SELF']   =  [0.1, 0.9]

    HRSAT.table[(TRUE, LOW3)]     = [0.3333333, 0.3333333, 0.3333333]
    HRSAT.table[(FALSE, LOW3)]    = [ 0.3333333, 0.3333333, 0.3333333]
    HRSAT.table[(TRUE, NORMAL3)]  = [0.3333333, 0.3333333, 0.3333333]
    HRSAT.table[(FALSE, NORMAL3)]  = [ 0.98, 0.01, 0.01]
    HRSAT.table[(TRUE, HIGH3)]    = [ 0.01, 0.98, 0.01]
    HRSAT.table[(FALSE, HIGH3)]   = [ 0.01, 0.01, 0.98]
 
    INSYFFANESTH.table['SELF']    = [0.1, 0.9]
 
    ANAPHYLAXIS.table['SELF']     = [0.01, 0.99]         

    TPR.table[TRUE]     =  [0.98, 0.01, 0.01]
    TPR.table[FALSE]    =  [ 0.3, 0.4, 0.3]

    EXPCO2.table[(LOW3, ZERO4)]       =  [0.97, 0.01, 0.01, 0.01]
    EXPCO2.table[(NORMAL3, ZERO4)]    =  [ 0.01, 0.97, 0.01, 0.01]
    EXPCO2.table[(HIGH3, ZERO4)]      =  [ 0.01, 0.97, 0.01, 0.01]
    EXPCO2.table[(LOW3, LOW4)]        =  [0.01, 0.97, 0.01, 0.01]
    EXPCO2.table[(NORMAL3, LOW4)]     =  [ 0.97, 0.01, 0.01, 0.01]
    EXPCO2.table[(HIGH3, LOW4)]       =  [0.01, 0.01, 0.97, 0.01]
    EXPCO2.table[(LOW3, NORMAL4)]     =  [ 0.01, 0.01, 0.97, 0.01]
    EXPCO2.table[(NORMAL3, NORMAL4)]  =  [ 0.01, 0.01, 0.97, 0.01]
    EXPCO2.table[(HIGH3, NORMAL4 )]   =  [ 0.97, 0.01, 0.01, 0.01]
    EXPCO2.table[(LOW3, HIGH4)]       =  [ 0.01, 0.01, 0.01, 0.97]
    EXPCO2.table[(NORMAL3, HIGH4 )]   =  [ 0.01, 0.01, 0.01, 0.97]
    EXPCO2.table[(HIGH3, HIGH4)]      =  [ 0.01, 0.01, 0.01, 0.97]

    KINKEDTUBE.table['SELF']      = [0.04, 0.96]

    MINVOL.table[(NORMAL, ZERO4)]      =  [0.97, 0.01, 0.01, 0.01]
    MINVOL.table[(ESOPHA, LOW4)]       =  [ 0.01, 0.97, 0.01, 0.01]
    MINVOL.table[(ONESID, NORMAL4)]    =  [0.01, 0.01, 0.97, 0.01]  
    MINVOL.table[(NORMAL, HIGH4)]      =  [0.01, 0.01, 0.01, 0.97]
    MINVOL.table[(ESOPHA, ZERO4)]      =  [0.97, 0.01, 0.01, 0.01]
    MINVOL.table[(ONESID, LOW4)]       =  [ 0.60, 0.38, 0.01, 0.01]
    MINVOL.table[(NORMAL, NORMAL4)]    =  [ 0.50, 0.48, 0.01, 0.01]   
    MINVOL.table[(ESOPHA, HIGH4)]      =  [ 0.50, 0.48, 0.01, 0.01]   
    MINVOL.table[(ONESID, ZERO4)]      =  [ 0.97, 0.01, 0.01, 0.01]
    MINVOL.table[(NORMAL, LOW4)]       =  [0.01, 0.97, 0.01, 0.01]
    MINVOL.table[(ESOPHA, NORMAL4)]    =  [ 0.01, 0.01, 0.97, 0.01]   
    MINVOL.table[(ONESID, HIGH4)]      =  [ 0.01, 0.01, 0.01, 0.97]     

    FIO2.table['SELF']  = [0.05, 0.95]

    PVSAT.table[(LOW2, ZERO4)]       =  [ 1.0, 0.0, 0.0 ] 
    PVSAT.table[(NORMAL2, ZERO4)]    =  [ 0.99, 0.01, 0.00]    
    PVSAT.table[(LOW2, LOW4)]        =  [0.95, 0.04, 0.0]
    PVSAT.table[(NORMAL2, LOW4)]     =  [ 0.95, 0.04, 0.01]    
    PVSAT.table[(LOW2, NORMAL4)]     =  [1.0, 0.0, 0.0 ] 
    PVSAT.table[(NORMAL2, NORMAL4)]  =  [ 0.95, 0.04, 0.0]      
    PVSAT.table[(LOW2, HIGH4)]       =  [ 0.01, 0.95, 0.04]    
    PVSAT.table[(NORMAL2, HIGH4)]    =  [ 0.01, 0.01, 0.98]                   
        
    SA02.table[(LOW3, LOW2)]           =  [0.98, 0.01, 0.01]      
    SA02.table[(NORMAL3, LOW2)]     =  [ 0.01, 0.98, 0.01]              
    SA02.table[(HIGH3, LOW2)]          =  [ 0.01, 0.01, 0.98]       
    SA02.table[(LOW3, NORMAL2)] =  [98, 0.01, 0.01 ]                
    SA02.table[(NORMAL3, NORMAL2)]        =  [ 0.98, 0.01, 0.01]                       
    SA02.table[(HIGH3, NORMAL2)]       =  [0.69, 0.30, 0.01 ]                     


    PAP.table[TRUE]     =   [ 0.01, 0.19, 0.80]
    PAP.table[FALSE]    =   [ 0.05, 0.90, 0.05]

    PULMEMBOLUS.table['SELF']       =   [0.01, 0.99]

    SHUNT.table[(NORMAL, TRUE)]     =   [0.1, 0.9]   
    SHUNT.table[(ESOPHA, TRUE)]     =   [ 0.1, 0.9]   
    SHUNT.table[(ONESID, TRUE)]     =   [ 0.01, 0.99]       
    SHUNT.table[(NORMAL, FALSE)]    =   [ 0.95, 0.05] 
    SHUNT.table[(ESOPHA, FALSE)]    =   [ 0.95, 0.] 
    SHUNT.table[(ONESID, FALSE)]    =   [ 0.05, 0.95] 

    INTUBATION.table['SELF']     =   [0.92, 0.03, 0.05]

    PRESS.table[(NORMAL, TRUE, ZERO4)]     = [ 0.97, 0.01, 0.01, 0.01]                             
    PRESS.table[(ESOPHA, TRUE, ZERO4)]     = [ 0.01, 0.30, 0.49, 0.20]          
    PRESS.table[(ONESID, TRUE, ZERO4)]     = [ 0.01, 0.01, 0.08, 0.90]          
    PRESS.table[(NORMAL, FALSE, ZERO4)]    = [ 0.01, 0.01, 0.01, 0.97]          
    PRESS.table[(ESOPHA, FALSE, ZERO4)]    = [ 0.97, 0.01, 0.01, 0.01]          
    PRESS.table[(ONESID, FALSE, ZERO4)]    = [ 0.10, 0.84, 0.05, 0.01]          
    PRESS.table[(NORMAL, TRUE, LOW4)]      = [0.05, 0.25, 0.25, 0.45]      
    PRESS.table[(ESOPHA, TRUE, LOW4)]      = [ 0.01, 0.15, 0.25, 0.59]      
    PRESS.table[(ONESID, TRUE, LOW4)]      = [ 0.97, 0.01, 0.01, 0.01]      
    PRESS.table[(NORMAL, FALSE, LOW4)]     = [0.01, 0.29, 0.30, 0.40]          
    PRESS.table[(ESOPHA, FALSE, LOW4)]     = [ 0.01, 0.01, 0.08, 0.90]          
    PRESS.table[(ONESID, FALSE, LOW4)]     = [ 0.01, 0.01, 0.01, 0.97]          
    PRESS.table[(NORMAL, TRUE, NORMAL4)]   = [ 0.97, 0.01, 0.01, 0.01]          
    PRESS.table[(ESOPHA, TRUE, NORMAL4)]   = [ 0.01, 0.97, 0.01, 0.01]          
    PRESS.table[(ONESID, TRUE, NORMAL4)]   = [ 0.01, 0.01, 0.97, 0.01]          
    PRESS.table[(NORMAL, FALSE, NORMAL4)]  = [ 0.01, 0.01, 0.01, 0.97]
    PRESS.table[(ESOPHA, FALSE, NORMAL4)]  = [ 0.97, 0.01, 0.01, 0.0]
    PRESS.table[(ONESID, FALSE, NORMAL4)]  = [ 0.40, 0.58, 0.01, 0.01]
    PRESS.table[(NORMAL, TRUE, HIGH4)]     = [0.20, 0.75, 0.04, 0.01]
    PRESS.table[(ESOPHA, TRUE, HIGH4)]     = [ 0.20, 0.70, 0.09, 0.01]
    PRESS.table[(ONESID, TRUE, HIGH4)]     = [ 0.97, 0.01, 0.01, 0.01]
    PRESS.table[(NORMAL, FALSE, HIGH4)]    = [ 0.01, 0.90, 0.08, 0.01]
    PRESS.table[(ESOPHA, FALSE, HIGH4)]    = [ 0.01, 0.01, 0.38, 0.60]
    PRESS.table[(ONESID, FALSE, HIGH4)]    = [ 0.01, 0.01, 0.01, 0.97]          

    DISCONNECT.table['SELF']        = [0.1, 0.9]

    MINVOLSET.table['SELF']         = [0.05, 0.90, 0.05]

    VENTMACH.table[LOW3]            =[ 0.05, 0.93, 0.01, 0.01]
    VENTMACH.table[NORMAL3]         =[ 0.05, 0.01, 0.93, 0.01]
    VENTMACH.table[HIGH3]           =[ 0.05, 0.01, 0.01, 0.93]

    VENTTUBE.table[(TRUE, ZERO4)]     = [0.97, 0.01, 0.01, 0.01]
    VENTTUBE.table[(FALSE, ZERO4)]    = [ 0.97, 0.01, 0.01, 0.01]
    VENTTUBE.table[(TRUE, LOW4)]      = [0.97, 0.01, 0.01, 0.01]
    VENTTUBE.table[(FALSE, LOW4)]     = [0.97, 0.01, 0.01, 0.01]
    VENTTUBE.table[(TRUE, NORMAL4)]   = [  0.97, 0.01, 0.01, 0.01]
    VENTTUBE.table[(FALSE, NORMAL4)]  = [ 0.01, 0.97, 0.01, 0.01]
    VENTTUBE.table[(TRUE, HIGH4)]     = [0.01, 0.01, 0.97, 0.01]
    VENTTUBE.table[(FALSE, HIGH4)]    = [ 0.01, 0.01, 0.01, 0.97]

    VENTLUNG.table[(NORMAL, TRUE, ZERO4)]     =[0.97, 0.01, 0.01, 0.01]
    VENTLUNG.table[(ESOPHA, TRUE, ZERO4)]     =[ 0.95, 0.03, 0.01, 0.01]
    VENTLUNG.table[(ONESID, TRUE, ZERO4)]     =[ 0.40, 0.58, 0.01, 0.01]
    VENTLUNG.table[(NORMAL, FALSE, ZERO4)]    =[ 0.30, 0.68, 0.01, 0.01]
    VENTLUNG.table[(ESOPHA, FALSE, ZERO4)]    =[ 0.97, 0.01, 0.01, 0.01]
    VENTLUNG.table[(ONESID, FALSE, ZERO4)]    =[ 0.97, 0.01, 0.01, 0.01]
    VENTLUNG.table[(NORMAL, TRUE, LOW4)]      =[0.97, 0.01, 0.01, 0.01]
    VENTLUNG.table[(ESOPHA, TRUE, LOW4)]      =[ 0.97, 0.01, 0.01, 0.01]
    VENTLUNG.table[(ONESID, TRUE, LOW4)]      =[ 0.97, 0.01, 0.01, 0.01]
    VENTLUNG.table[(NORMAL, FALSE, LOW4)]     =[0.95, 0.03, 0.01, 0.01]
    VENTLUNG.table[(ESOPHA, FALSE, LOW4)]     =[ 0.50, 0.48, 0.01, 0.01]
    VENTLUNG.table[(ONESID, FALSE, LOW4)]     =[ 0.30, 0.68, 0.01, 0.01]
    VENTLUNG.table[(NORMAL, TRUE, NORMAL4)]   =[ 0.97, 0.01, 0.01, 0.01]
    VENTLUNG.table[(ESOPHA, TRUE, NORMAL4)]   =[ 0.01, 0.97, 0.01, 0.01]
    VENTLUNG.table[(ONESID, TRUE, NORMAL4)]   =[ 0.01, 0.01, 0.97, 0.01]
    VENTLUNG.table[(NORMAL, FALSE, NORMAL4)]   =[ 0.01, 0.01, 0.01, 0.97]
    VENTLUNG.table[(ESOPHA, FALSE, NORMAL4)]   =[ 0.97, 0.01, 0.01, 0.01]
    VENTLUNG.table[(ONESID, FALSE, NORMAL4)]   =[ 0.97, 0.01, 0.01, 0.01]
    VENTLUNG.table[(NORMAL, TRUE, HIGH4)]     =[0.97, 0.01, 0.01, 0.01]
    VENTLUNG.table[(ESOPHA, TRUE, HIGH4)]     =[ 0.97, 0.01, 0.01, 0.01]
    VENTLUNG.table[(ONESID, TRUE, HIGH4)]     =[0.97, 0.01, 0.01, 0.01]
    VENTLUNG.table[(NORMAL, FALSE, HIGH4)]    =[ 0.01, 0.97, 0.01, 0.01]
    VENTLUNG.table[(ESOPHA, FALSE, HIGH4)]    =[ 0.01, 0.01, 0.97, 0.01]
    VENTLUNG.table[(ONESID, FALSE, HIGH4)]    =[ 0.01, 0.01, 0.01, 0.97]       



    VENTALV.table[(NORMAL, ZERO4)]    = [ 0.97, 0.01, 0.01, 0.01]
    VENTALV.table[(ESOPHA, LOW4)]     = [ 0.01, 0.97, 0.01, 0.01]
    VENTALV.table[(ONESID, NORMAL4)]  = [ 0.01, 0.01, 0.97, 0.01]
    VENTALV.table[(NORMAL, HIGH4)]    = [0.01, 0.01, 0.01, 0.97]
    VENTALV.table[(ESOPHA, ZERO4)]    = [ 0.97, 0.01, 0.01, 0.01]
    VENTALV.table[(ONESID, LOW4)]     = [ 0.01, 0.97, 0.01, 0.01]
    VENTALV.table[(NORMAL, NORMAL4)]  = [ 0.01, 0.01, 0.97, 0.01]
    VENTALV.table[(ESOPHA, HIGH4)]    = [ 0.01, 0.01, 0.01, 0.97]
    VENTALV.table[(ONESID, ZERO4)]    = [ 0.97, 0.01, 0.01, 0.01]
    VENTALV.table[(NORMAL, LOW4)]     = [ 0.03, 0.95, 0.01, 0.01]
    VENTALV.table[(ESOPHA, NORMAL4)]  = [ 0.01, 0.94, 0.04, 0.01]
    VENTALV.table[(ONESID, HIGH4)]    = [ 0.01, 0.88, 0.10, 0.01]

    ARTCO2.table[ZERO4]     = [ 0.01, 0.01, 0.98]
    ARTCO2.table[LOW4]      = [0.01, 0.01, 0.98]
    ARTCO2.table[NORMAL4]   = [ 0.04, 0.92, 0.04]
    ARTCO2.table[HIGH4]     = [ 0.90, 0.09, 0.01]

    CATECHOL.table[(LOW3, TRUE, LOW3, LOW3)]          = [0.01, 0.99]
    CATECHOL.table[(NORMAL3, FALSE, LOW3, LOW3)]      = [ 0.01, 0.99]
    CATECHOL.table[(HIGH3, TRUE, LOW3, LOW3)]         = [ 0.01, 0.99]
    CATECHOL.table[(LOW3, FALSE, LOW3, LOW3)]         = [ 0.01, 0.99]
    CATECHOL.table[(NORMAL3, TRUE, LOW3, LOW3)]       = [ 0.01, 0.99]
    CATECHOL.table[(HIGH3, FALSE, LOW3, LOW3)]        = [ 0.01, 0.99]
    CATECHOL.table[(LOW3, TRUE, NORMAL3, LOW3)]       = [ 0.01, 0.99]
    CATECHOL.table[(NORMAL3, FALSE, NORMAL3, LOW3)]   = [ 0.01, 0.99]
    CATECHOL.table[(HIGH3, TRUE, NORMAL3, LOW3)]      = [ 0.01, 0.99]
    CATECHOL.table[(LOW3, FALSE, NORMAL3, LOW3)]      = [ 0.01, 0.99]
    CATECHOL.table[(NORMAL3, TRUE, NORMAL3, LOW3)]    = [ 0.01, 0.99]
    CATECHOL.table[(HIGH3, FALSE, NORMAL3, LOW3)]     = [ 0.01, 0.99]
    CATECHOL.table[(LOW3, TRUE, HIGH3, LOW3)]         = [ 0.01, 0.99]
    CATECHOL.table[(NORMAL3, FALSE, HIGH3, LOW3)]     = [ 0.01, 0.99]
    CATECHOL.table[(HIGH3, TRUE, HIGH3, LOW3)]        = [ 0.01, 0.99]
    CATECHOL.table[(LOW3, FALSE, HIGH3, LOW3)]        = [ 0.05, 0.95]
    CATECHOL.table[(NORMAL3, TRUE, HIGH3, LOW3)]      = [ 0.05, 0.95]
    CATECHOL.table[(HIGH3, FALSE, HIGH3, LOW3)]       = [ 0.01, 0.99]
    CATECHOL.table[(LOW3, TRUE, LOW3, NORMAL3)]       = [ 0.01, 0.99]
    CATECHOL.table[(NORMAL3, FALSE, LOW3, NORMAL3)]   = [ 0.01, 0.99]
    CATECHOL.table[(HIGH3, TRUE, LOW3, NORMAL3)]      = [ 0.01, 0.99]
    CATECHOL.table[(LOW3, FALSE, LOW3, NORMAL3)]      = [ 0.05, 0.95]
    CATECHOL.table[(NORMAL3, TRUE, LOW3, NORMAL3)]    = [ 0.05, 0.95]
    CATECHOL.table[(HIGH3, FALSE, LOW3, NORMAL3)]     = [ 0.01, 0.99]
    CATECHOL.table[(LOW3, TRUE, NORMAL3, NORMAL3)]    = [ 0.05, 0.95]
    CATECHOL.table[(NORMAL3, FALSE, NORMAL3, NORMAL3)]= [ 0.05, 0.95]
    CATECHOL.table[(HIGH3, TRUE, NORMAL3, NORMAL3)]   = [ 0.01, 0.99]
    CATECHOL.table[(LOW3, FALSE, NORMAL3, NORMAL3)]   = [ 0.05, 0.95]
    CATECHOL.table[(NORMAL3, TRUE, NORMAL3, NORMAL3)] = [ 0.05, 0.95]
    CATECHOL.table[(HIGH3, FALSE, NORMAL3, NORMAL3)]  = [ 0.01, 0.99]
    CATECHOL.table[(LOW3, TRUE, HIGH3, NORMAL3)]      = [ 0.05, 0.95]
    CATECHOL.table[(NORMAL3, FALSE, HIGH3, NORMAL3)]  = [ 0.05, 0.95]
    CATECHOL.table[(HIGH3, TRUE, HIGH3, NORMAL3)]     = [ 0.01, 0.99]
    CATECHOL.table[(LOW3, FALSE, HIGH3, NORMAL3)]     = [ 0.05, 0.95]
    CATECHOL.table[(NORMAL3, TRUE, HIGH3, NORMAL3)]   = [ 0.05, 0.95]
    CATECHOL.table[(HIGH3, FALSE, HIGH3, NORMAL3)]    = [ 0.01, 0.99]
    CATECHOL.table[(LOW3, TRUE, LOW3, HIGH3)]         = [0.7, 0.3]
    CATECHOL.table[(NORMAL3, FALSE, LOW3, HIGH3)]     = [ 0.7, 0.3]
    CATECHOL.table[(HIGH3, TRUE, LOW3, HIGH3)]        = [0.1, 0.9]
    CATECHOL.table[(LOW3, FALSE, LOW3, HIGH3)]        = [ 0.7, 0.3]
    CATECHOL.table[(NORMAL3, TRUE, LOW3, HIGH3)]      = [ 0.7, 0.3]
    CATECHOL.table[(HIGH3, FALSE, LOW3, HIGH3)]       = [ 0.1, 0.9]
    CATECHOL.table[(LOW3, TRUE, NORMAL3, HIGH3)]      = [ 0.7, 0.3]
    CATECHOL.table[(NORMAL3, FALSE, NORMAL3, HIGH3)]  = [ 0.7, 0.3]
    CATECHOL.table[(HIGH3, TRUE, NORMAL3, HIGH3)]     = [ 0.1, 0.9]
    CATECHOL.table[(LOW3, FALSE, NORMAL3, HIGH3)]     = [ 0.95, 0.05]
    CATECHOL.table[(NORMAL3, TRUE, NORMAL3, HIGH3)]   = [ 0.99, 0.01]
    CATECHOL.table[(HIGH3, FALSE, NORMAL3, HIGH3)]    = [ 0.3, 0.7]
    CATECHOL.table[(LOW3, TRUE, HIGH3, HIGH3)]        = [0.95, 0.05]
    CATECHOL.table[(NORMAL3, FALSE, HIGH3, HIGH3)]    = [ 0.99, 0.01]
    CATECHOL.table[(HIGH3, TRUE, HIGH3, HIGH3)]       = [ 0.3, 0.7]
    CATECHOL.table[(LOW3, FALSE, HIGH3, HIGH3)]       = [ 0.95, 0.05]
    CATECHOL.table[(NORMAL3, TRUE, HIGH3, HIGH3)]     = [ 0.99, 0.01]
    CATECHOL.table[(HIGH3, FALSE, HIGH3, HIGH3)]      = [ 0.3, 0.7]

    HR.table[LOW2]      = [ 0.05, 0.90, 0.0]
    HR.table[NORMAL2]   = [0.01, 0.09, 0.90]

    CO.table[(LOW3   ,LOW3)]      =  [ 0.98, 0.01, 0.01]
    CO.table[(NORMAL3,LOW3)]      =  [ 0.95, 0.04, 0.01]
    CO.table[(HIGH3  ,LOW3)]      =  [ 0.80, 0.19, 0.01]
    CO.table[(LOW3   ,NORMAL3)]   =  [ 0.95, 0.04, 0.01]
    CO.table[(NORMAL3,NORMAL3)]   =  [ 0.04, 0.95, 0.01]
    CO.table[(HIGH3  ,NORMAL3)]   =  [ 0.01, 0.04, 0.95]
    CO.table[(LOW3   ,HIGH3)]     =  [ 0.30, 0.69, 0.01]
    CO.table[(NORMAL3,HIGH3)]     =  [ 0.01, 0.30, 0.69]
    CO.table[(HIGH3  ,HIGH3)]     =  [ 0.01, 0.01, 0.98]

    BP.table[(LOW3   ,LOW3)]      =  [ 0.98, 0.01, 0.01]
    BP.table[(NORMAL3,LOW3)]      =  [ 0.98, 0.01, 0.01]
    BP.table[(HIGH3  ,LOW3)]      =  [ 0.90, 0.09, 0.01]
    BP.table[(LOW3   ,NORMAL3)]   =  [ 0.98, 0.01, 0.01]
    BP.table[(NORMAL3,NORMAL3)]   =  [ 0.10, 0.85, 0.05]
    BP.table[(HIGH3  ,NORMAL3)]   =  [ 0.05, 0.20, 0.75]
    BP.table[(LOW3   ,HIGH3)]     =  [ 0.3, 0.6, 0.1]
    BP.table[(NORMAL3,HIGH3)]     =  [ 0.05, 0.40, 0.55]
    BP.table[(HIGH3  ,HIGH3)]     =  [ 0.01, 0.09, 0.90]
    
    nodes = [
        HISTORY,
        CVP, 
        PCWP, 
        HYPOVOLEMIA,
        LVEOVOLUME, 
        LVFAILURE, 
        STROKEVOLUME, 
        ERRLOWOUTPUT, 
        HRBP, 
        HREKG,         
        ERRCAUTER,
        HRSAT, 
        INSYFFANESTH, 
        ANAPHYLAXIS, 
        TPR, 
        EXPCO2,
        KINKEDTUBE, 
        MINVOL, 
        FIO2,
        PVSAT,
        SA02, 
        PAP, 
        PULMEMBOLUS, 
        SHUNT, 
        INTUBATION,  
        PRESS, 
        DISCONNECT, 
        MINVOLSET,
        VENTMACH, 
        VENTTUBE, 
        VENTLUNG, 
        VENTALV, 
        ARTCO2, 
        CATECHOL,
        HR, 
        CO, 
        BP
        ]

    return Graph(nodes)
        
def connectALMFathers(graph):
    HISTORY =   graph.nodes[0]
    CVP =       graph.nodes[1]
    PCWP =      graph.nodes[2]
    HYPOVOLEMIA =graph.nodes[3]
    LVEOVOLUME =graph.nodes[4]
    LVFAILURE =  graph.nodes[5]
    STROKEVOLUME =  graph.nodes[6]
    ERRLOWOUTPUT =  graph.nodes[7]
    HRBP =  graph.nodes[8]
    HREKG     =  graph.nodes[9]
    ERRCAUTE = graph.nodes[10]
    HRSAT =  graph.nodes[11]
    INSYFFANESTH =  graph.nodes[12]
    ANAPHYLAXIS =  graph.nodes[13]
    TPR =  graph.nodes[14]
    EXPCO = graph.nodes[15]
    KINKEDTUBE =  graph.nodes[16]
    MINVOL =  graph.nodes[17]
    FIO2 = graph.nodes[18]
    PVSAT = graph.nodes[19]
    SA02 =  graph.nodes[20]
    PAP =  graph.nodes[21]
    PULMEMBOLUS =  graph.nodes[22]
    SHUNT =  graph.nodes[23]
    INTUBATION =  graph.nodes[24]
    PRESS =  graph.nodes[25]
    DISCONNECT =  graph.nodes[26]
    MINVOLSET = graph.nodes[27]
    VENTMACH =  graph.nodes[28]
    VENTTUBE =  graph.nodes[29]
    VENTLUNG =  graph.nodes[30]
    VENTALV =  graph.nodes[31]
    ARTCO2 =  graph.nodes[32]
    CATECHOL = graph.nodes[33]
    HR =  graph.nodes[34]
    CO =  graph.nodes[35]
    BP = graph.nodes[36]

    HISTORY.fathers = [LVFAILURE]
    CVP.fathers = [LVEOVOLUME]
    PCWP.fathers = [LVEOVOLUME]
    HYPOVOLEMIA.fathers = []
    LVEOVOLUME.fathers = [HYPOVOLEMIA, LVFAILURE]
    LVFAILURE.fathers = []
    STROKEVOLUME.fathers = [HYPOVOLEMIA, LVFAILURE]
    ERRLOWOUTPUT.fathers = []
    HRBP.fathers = [ERRLOWOUTPUT, HR]
    HREKG.fathers = [ERRCAUTE,HR]        
    ERRCAUTE.fathers = []
    HRSAT.fathers = [ERRCAUTE,HR]
    INSYFFANESTH.fathers = []
    ANAPHYLAXIS.fathers = []
    TPR.fathers = [ANAPHYLAXIS]
    EXPCO.fathers = [ARTCO2,VENTLUNG]
    KINKEDTUBE.fathers = []
    MINVOL.fathers = [INTUBATION,VENTLUNG]
    FIO2.fathers = []
    PVSAT.fathers = [FIO2,VENTALV]
    SA02.fathers = [PVSAT, SHUNT]
    PAP.fathers = [PULMEMBOLUS]
    PULMEMBOLUS.fathers = []
    SHUNT.fathers = [INTUBATION,PULMEMBOLUS]
    INTUBATION.fathers = [] 
    PRESS.fathers = [INTUBATION, KINKEDTUBE, VENTTUBE]
    DISCONNECT.fathers = []
    MINVOLSET.fathers = []
    VENTMACH.fathers = [MINVOLSET]
    VENTTUBE.fathers = [DISCONNECT, VENTMACH]
    VENTLUNG.fathers = [INTUBATION, KINKEDTUBE, VENTTUBE]
    VENTALV.fathers = [INTUBATION, VENTLUNG]
    ARTCO2.fathers = [VENTALV]
    CATECHOL.fathers = [ARTCO2, INSYFFANESTH , SA02]
    HR.fathers = [CATECHOL]
    CO.fathers = [HR,STROKEVOLUME]
    BP.fathers = [CO, TPR]
    
    HISTORY.sons = []   
    CVP.sons = []
    PCWP.sons = []
    HYPOVOLEMIA.sons = [STROKEVOLUME,LVEOVOLUME]
    LVEOVOLUME.sons = [PCWP,CVP]
    LVFAILURE.sons = [HISTORY,LVEOVOLUME,STROKEVOLUME]
    STROKEVOLUME.sons = [CO]
    ERRLOWOUTPUT.sons = [HRBP]
    HRBP.sons = []
    HREKG.sons = []        
    ERRCAUTE.sons = [HRSAT,HREKG]
    HRSAT.sons = []
    INSYFFANESTH.sons = [CATECHOL]
    ANAPHYLAXIS.sons = [TPR]
    TPR.sons = [BP]
    EXPCO.sons = []
    KINKEDTUBE.sons = [PRESS,VENTLUNG]
    MINVOL.sons = []
    FIO2.sons = [PVSAT]
    PVSAT.sons = [SA02]
    SA02.sons = [CATECHOL]
    PAP.sons = []
    PULMEMBOLUS.sons = [PAP,SHUNT]
    SHUNT.sons = [SA02]
    INTUBATION.sons = [SHUNT,VENTLUNG,PRESS]
    PRESS.sons = []
    DISCONNECT.sons = [VENTTUBE]
    MINVOLSET.sons = [VENTMACH]
    VENTMACH.sons = [VENTTUBE]
    VENTTUBE.sons = [VENTLUNG,PRESS]
    VENTLUNG.sons = [MINVOL]
    VENTALV.sons = [PVSAT,ARTCO2]
    ARTCO2.sons = [CATECHOL,EXPCO]
    CATECHOL.sons = [HR]
    HR.sons = [CO,HRBP,HREKG,HRSAT]
    CO.sons = [BP]
    BP.sons = []
    
actual = buildALMGraph()
connectALMFathers(actual)


graph = buildALMGraph()
examples = [] 

for i in range(100) : 
   e = ALMSampler(graph)
   examples.append(e)
   print(e.values)

datas = Dataset(graph.nodes,examples)

print("Score of the actual Alarm Model")
print(Score(actual, datas))
Visualizer.printdot(actual)
Visualizer.printpng()
learnt = Learn(graph, datas)
#learnt = QuickLearn(graph, datas)
print( " Score of the learnt Alarm model  ")
print(learnt[1])
Visualizer.printdot(learnt[0])
Visualizer.printpng()

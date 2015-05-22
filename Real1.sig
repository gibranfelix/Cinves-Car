<?xml version="1.0" encoding="UTF-8"?>
<sc id="1" name="nuevo sem" frequency="1" steps="0" defaultIntergreenMatrix="0">
  <signaldisplays>
    <display id="1" name="Red" state="RED">
      <patterns>
        <pattern pattern="MINUS" color="#FF0000" isBold="true" />
      </patterns>
    </display>
    <display id="2" name="Red/Amber" state="REDAMBER">
      <patterns>
        <pattern pattern="FRAME" color="#CCCC00" isBold="true" />
        <pattern pattern="SLASH" color="#CC0000" isBold="false" />
        <pattern pattern="MINUS" color="#CC0000" isBold="false" />
      </patterns>
    </display>
    <display id="3" name="Green" state="GREEN">
      <patterns>
        <pattern pattern="FRAME" color="#00CC00" isBold="true" />
        <pattern pattern="SOLID" color="#00CC00" isBold="false" />
      </patterns>
    </display>
    <display id="4" name="Amber" state="AMBER">
      <patterns>
        <pattern pattern="FRAME" color="#CCCC00" isBold="true" />
        <pattern pattern="SLASH" color="#CCCC00" isBold="false" />
      </patterns>
    </display>
    <display id="5" name="Flashing Green" state="FLASHING_GREEN">
      <patterns>
        <pattern pattern="FRAME" color="#00CC00" isBold="true" />
        <pattern pattern="SECONDS" color="#00CC00" isBold="true" />
      </patterns>
    </display>
    <display id="8" name="Flashing Red" state="FLASHING_RED">
      <patterns>
        <pattern pattern="FRAME" color="#FF0000" isBold="true" />
        <pattern pattern="SECONDS" color="#FF0000" isBold="true" />
      </patterns>
    </display>
  </signaldisplays>
  <signalsequences>
    <signalsequence id="3" name="Red-Red/Amber-Green-Amber">
      <state display="1" isFixedDuration="false" isClosed="true" defaultDuration="1000" />
      <state display="2" isFixedDuration="true" isClosed="true" defaultDuration="1000" />
      <state display="3" isFixedDuration="false" isClosed="false" defaultDuration="5000" />
      <state display="4" isFixedDuration="true" isClosed="true" defaultDuration="3000" />
    </signalsequence>
    <signalsequence id="6" name="Red-Green-Flashing Green">
      <state display="1" isFixedDuration="false" isClosed="true" defaultDuration="1000" />
      <state display="3" isFixedDuration="false" isClosed="false" defaultDuration="5000" />
      <state display="5" isFixedDuration="true" isClosed="false" defaultDuration="4000" />
    </signalsequence>
    <signalsequence id="7" name="Red-Green-Amber">
      <state display="1" isFixedDuration="false" isClosed="true" defaultDuration="1000" />
      <state display="3" isFixedDuration="false" isClosed="false" defaultDuration="5000" />
      <state display="4" isFixedDuration="true" isClosed="true" defaultDuration="3000" />
    </signalsequence>
    <signalsequence id="14" name="Red-Green-Flashing Red">
      <state display="1" isFixedDuration="false" isClosed="true" defaultDuration="1000" />
      <state display="3" isFixedDuration="false" isClosed="false" defaultDuration="5000" />
      <state display="8" isFixedDuration="true" isClosed="true" defaultDuration="1000" />
    </signalsequence>
  </signalsequences>
  <sgs>
    <sg id="1" name="Primaria" defaultSignalSequence="3" underEPICSControl="true">
      <defaultDurations>
        <defaultDuration display="1" duration="1000" />
      </defaultDurations>
      <EPICSTrafficDemands />
    </sg>
    <sg id="2" name="Secundaria" defaultSignalSequence="3" underEPICSControl="true">
      <defaultDurations />
      <EPICSTrafficDemands />
    </sg>
    <sg id="3" name="Peatones" defaultSignalSequence="6" underEPICSControl="true">
      <defaultDurations>
        <defaultDuration display="1" duration="1000" />
        <defaultDuration display="3" duration="5000" />
        <defaultDuration display="5" duration="8000" />
      </defaultDurations>
      <EPICSTrafficDemands />
    </sg>
  </sgs>
  <dets />
  <messagePointPairs />
  <intergreenmatrices />
  <progs>
    <prog id="1" cycletime="108000" switchpoint="0" offset="0" intergreens="0" fitness="0.000000" vehicleCount="0" name="Signal program 1">
      <sgs>
        <sg sg_id="1" signal_sequence="7">
          <cmds>
            <cmd display="3" begin="0" />
            <cmd display="1" begin="60000" />
          </cmds>
          <fixedstates>
            <fixedstate display="4" duration="3000" />
          </fixedstates>
        </sg>
        <sg sg_id="2" signal_sequence="7">
          <cmds>
            <cmd display="3" begin="60000" />
            <cmd display="1" begin="90000" />
          </cmds>
          <fixedstates>
            <fixedstate display="4" duration="3000" />
          </fixedstates>
        </sg>
        <sg sg_id="3" signal_sequence="14">
          <cmds>
            <cmd display="3" begin="90000" />
            <cmd display="1" begin="106000" />
          </cmds>
          <fixedstates>
            <fixedstate display="8" duration="1000" />
          </fixedstates>
        </sg>
      </sgs>
    </prog>
  </progs>
  <stages />
  <interstageProgs />
  <stageProgs />
  <dailyProgLists />
</sc>
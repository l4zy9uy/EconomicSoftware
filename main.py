# Budget at Completion
import os

bac = -1.0
# Planned Value
pv = -1.0
# Actual Cost
ac = -1.0
# Earned Value
ev = -1.0

while bac < 0.0:
    bac = float(input("Enter Budget at Completion (BAC): "))
    if bac > 0.0:
        break
    else:
        print("Invalid BAC")

while pv < 0.0 or pv > bac:
    pv = float(input("Enter Planning Value (PV): "))
    if 0.0 < pv <= bac:
        break
    else:
        print("Invalid PV")

while ev < 0.0 or ev > bac:
    ev = float(input("Enter Earned Value (EV): "))
    if 0.0 < ev <= bac:
        break
    else:
        print("Invalid EV")


while ac < 0.0:
    ac = float(input("Enter Actual Cost (AC): "))
    if 0.0 < ac:
        break
    else:
        print("Invalid AC")

# Cost variance
cv = ev - ac
cvPercent = cv / ev * 100.0
# Cost Performance Indicator
cpi = ev / ac
# Schedule Performance Indicator
spi = ev / pv
# Schedule Variance
sv = ev -pv
# To Complete Cost Performance Indicator
tcpi = (bac-ev) / (bac-ac)
# To Complete Schedule Performance Indicator
tspi = (bac-ev) / (bac-pv)
# Estimation at Completion
eac = ac + (bac - ev) / cpi
# Variance at completion
vac = bac - eac
# Completed Planned percent
cpPercent = pv / bac * 100.0
# Completed Actual percent
caPercent = ac / eac * 100.0

print(f"CV: {cv}",
      f"CV percent: {cvPercent}",
      f"CPI: {cpi}",
      f"SPI: {spi}",
      f"SV: {sv}",
      f"TCPI: {tcpi}",
      f"TSPI: {tspi}",
      f"EAC: {eac}",
      f"VAC: {vac}",
      f"CPPercent: {cpPercent}",
      f"CAPercent: {caPercent}",
      sep=os.linesep)


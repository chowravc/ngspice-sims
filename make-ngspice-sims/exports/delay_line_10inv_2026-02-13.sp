* NGSPICE Inverter Delay Chain
* 2026-02-13

.include 14nfetHP.nmos
.include 14pfetHP.pmos

* Voltage Sources
vrail vdd 0 dc=0.8
vsig  v0_2 0 pulse(0 0.8 50p 1p 1p 50p  100p 1)

* Circuit Elements
vm0 vdd v0_3 dc=0
np1 v1_1 v0_2 v0_3 v0_3 pmos TFIN=8n L=16n NFIN=12 NRS=1 NRD=1 D=16n
nn1 v1_1 v0_2 0   0   nmos TFIN=8n L=16n NFIN=24 NRS=1 NRD=1 D=16n

r1 v1_1 v1_2 100
c1 v1_2 0    3f

vm1 vdd v1_3 dc=0
np2 v2_1 v1_2 v1_3 v1_3 pmos TFIN=8n L=16n NFIN=12 NRS=1 NRD=1 D=16n
nn2 v2_1 v1_2 0   0   nmos TFIN=8n L=16n NFIN=24 NRS=1 NRD=1 D=16n

r2 v2_1 v2_2 100
c2 v2_2 0    3f

vm2 vdd v2_3 dc=0
np3 v3_1 v2_2 v2_3 v2_3 pmos TFIN=8n L=16n NFIN=12 NRS=1 NRD=1 D=16n
nn3 v3_1 v2_2 0   0   nmos TFIN=8n L=16n NFIN=24 NRS=1 NRD=1 D=16n

r3 v3_1 v3_2 100
c3 v3_2 0    3f

vm3 vdd v3_3 dc=0
np4 v4_1 v3_2 v3_3 v3_3 pmos TFIN=8n L=16n NFIN=12 NRS=1 NRD=1 D=16n
nn4 v4_1 v3_2 0   0   nmos TFIN=8n L=16n NFIN=24 NRS=1 NRD=1 D=16n

r4 v4_1 v4_2 100
c4 v4_2 0    3f

vm4 vdd v4_3 dc=0
np5 v5_1 v4_2 v4_3 v4_3 pmos TFIN=8n L=16n NFIN=12 NRS=1 NRD=1 D=16n
nn5 v5_1 v4_2 0   0   nmos TFIN=8n L=16n NFIN=24 NRS=1 NRD=1 D=16n

r5 v5_1 v5_2 100
c5 v5_2 0    3f

vm5 vdd v5_3 dc=0
np6 v6_1 v5_2 v5_3 v5_3 pmos TFIN=8n L=16n NFIN=12 NRS=1 NRD=1 D=16n
nn6 v6_1 v5_2 0   0   nmos TFIN=8n L=16n NFIN=24 NRS=1 NRD=1 D=16n

r6 v6_1 v6_2 100
c6 v6_2 0    3f

vm6 vdd v6_3 dc=0
np7 v7_1 v6_2 v6_3 v6_3 pmos TFIN=8n L=16n NFIN=12 NRS=1 NRD=1 D=16n
nn7 v7_1 v6_2 0   0   nmos TFIN=8n L=16n NFIN=24 NRS=1 NRD=1 D=16n

r7 v7_1 v7_2 100
c7 v7_2 0    3f

vm7 vdd v7_3 dc=0
np8 v8_1 v7_2 v7_3 v7_3 pmos TFIN=8n L=16n NFIN=12 NRS=1 NRD=1 D=16n
nn8 v8_1 v7_2 0   0   nmos TFIN=8n L=16n NFIN=24 NRS=1 NRD=1 D=16n

r8 v8_1 v8_2 100
c8 v8_2 0    3f

vm8 vdd v8_3 dc=0
np9 v9_1 v8_2 v8_3 v8_3 pmos TFIN=8n L=16n NFIN=12 NRS=1 NRD=1 D=16n
nn9 v9_1 v8_2 0   0   nmos TFIN=8n L=16n NFIN=24 NRS=1 NRD=1 D=16n

r9 v9_1 v9_2 100
c9 v9_2 0    3f

vm9 vdd v9_3 dc=0
np10 v10_1 v9_2 v9_3 v9_3 pmos TFIN=8n L=16n NFIN=12 NRS=1 NRD=1 D=16n
nn10 v10_1 v9_2 0   0   nmos TFIN=8n L=16n NFIN=24 NRS=1 NRD=1 D=16n

c10 v10_1 0   1f

* Transient Analysis
.tran 1f  150p

* Control Language Script
.control
pre_osdi ../lib/ngspice/BSIMCMG.osdi
set xbrushwidth=3
run

* Save Data
wrdata delay_line_10inv_2026-02-13_output.txt time v(v0_2) v(v1_1) v(v1_2) v(v2_1) v(v2_2) v(v3_1) v(v3_2) v(v4_1) v(v4_2) v(v5_1) v(v5_2) v(v6_1) v(v6_2) v(v7_1) v(v7_2) v(v8_1) v(v8_2) v(v9_1) v(v9_2) v(v10_1) i(vm0) i(vm1) i(vm2) i(vm3) i(vm4) i(vm5) i(vm6) i(vm7) i(vm8) i(vm9)

.endc
.end
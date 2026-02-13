import os
import datetime

def main(models, vdd, vsnl_params, n_inv, pmos_params, nmos_params, Ric, Cic, Cload, sim_params, plot=False):

    # Store all data lines
    lines = []

    # Header lines
    date = datetime.date.today().isoformat()
    lines.append(f"* NGSPICE Inverter Delay Chain\n* {date}\n")

    # Model include statements
    lines.append(f".include {models[0]}\n.include {models[1]}\n")

    # Voltage sources
    lines.append('* Voltage Sources')
    lines.append(f"vrail vdd 0 dc={vdd}")
    lines.append("vsig  v0_2 0 pulse({} {} {} {} {} {} {} {})\n".format(*vsnl_params))

    # Populate circuit elements
    lines.append('* Circuit Elements')
    for i in range(n_inv):

        # Measurement sources
        lines.append(f"vm{i} vdd v{i}_3 dc=0")

        # MOSFETs
        lines.append(f"np{i+1} v{i+1}_1 v{i}_2 v{i}_3 v{i}_3 pmos "+"TFIN={} L={} NFIN={} NRS={} NRD={} D={}".format(*nmos_params))
        lines.append(f"nn{i+1} v{i+1}_1 v{i}_2 0   0   nmos "    +"TFIN={} L={} NFIN={} NRS={} NRD={} D={}\n".format(*pmos_params))

        # Interconnects and output load
        if i != (n_inv - 1):
            # Interconnects
            lines.append(f"r{i+1} v{i+1}_1 v{i+1}_2 {Ric}")
            lines.append(f"c{i+1} v{i+1}_2 0    {Cic}\n")
        else:
            # Load capacitor
            lines.append(f"c{i+1} v{i+1}_1 0   {Cload}\n")

    # Simulation params
    lines.append('* Transient Analysis')
    lines.append(".tran {} {}\n".format(*sim_params))

    # Control lines
    lines.append('* Control Language Script')
    lines.append('.control\npre_osdi ../lib/ngspice/BSIMCMG.osdi\nset xbrushwidth=3\nrun\n')

    # Saving data
    lines.append('* Save Data')
    v_columns = ' '.join([f"v(v{i+1}_1) v(v{i+1}_2)" for i in range(n_inv-1)]) + f" v(v{n_inv}_1)"
    i_columns = ' '.join([f"i(vm{i})" for i in range(n_inv)])
    lines.append(f"wrdata delay_line_{n_inv}inv_{date}_output.txt time v(v0_2) {v_columns} {i_columns}\n")

    # If plot
    if plot:
        # lines.append(f"plot v(v01) {v_columns}\n")
        lines.append(f"plot {i_columns}\n")

    # End lines
    lines.append('.endc\n.end')

    # Join string and save
    full_string = '\n'.join(lines)
    os.makedirs('exports', exist_ok=True)
    fname = f"exports/delay_line_{n_inv}inv_{date}.sp"
    with open(fname, 'w') as f:
        f.write(full_string)
    print(f"Saved {fname}.")

if __name__ == '__main__':

    # FET models being used: ['*.nmos', *.pmos']
    models = ['14nfetHP.nmos', '14pfetHP.pmos']

    # Rail voltage
    vdd = 0.8 # V

    # Input signal voltage params
    # ['Vinit', 'Vfin', 'tdelay', 'trise', 'tfall', 'pulsewidth', 'period', 'npulses']
    vsnl_params = ['0', '0.8', '50p', '1p', '1p', '50p',' 100p', '1']

    # Number of inverters
    n_inv = 10

    # NMOS, PMOS params
    # ['TFIN', 'L', 'NFIN', 'NRS', 'NRD', 'D']
    nmos_params = ['8n', '16n', '12', '1', '1', '16n']
    pmos_params = ['8n', '16n', '24', '1', '1', '16n']

    # Other circuit params
    Ric = '100' # interconnect resistance, Ohm
    Cic = '3f'  # interconnect capacitance, F
    Cload = '1f' # load capacitance, F

    # Simulation params
    # ['timestep', 'sim_time']
    sim_params = ['1f',' 150p']

    main(models, vdd, vsnl_params, n_inv, pmos_params, nmos_params, Ric, Cic, Cload, sim_params)
import networkx as nx
import os
import re

def parse_lef(lef_file):
    cell_info = {}
    with open(lef_file, 'r') as file:
        for line in file:
            if line.startswith('MACRO'):
                current_macro = line.split()[1]
                cell_info[current_macro] = {'pins': {}, 'size': (0, 0)}
            elif line.startswith('SIZE'):
                dimensions = line.split()
                cell_info[current_macro]['size'] = (float(dimensions[1]), float(dimensions[3]))
            elif line.startswith('PIN'):
                current_pin = line.split()[1]
                cell_info[current_macro]['pins'][current_pin] = {}
    return cell_info

def parse_def(def_file):
    G = nx.Graph()
    current_section = None

    with open(def_file, 'r') as file:
        current_net = None
        for line in file:
            line = line.strip()
            if line.startswith('COMPONENTS'):
                current_section = 'COMPONENTS'
            elif line.startswith('NETS'):
                current_section = 'NETS'
                current_net = None
            elif current_section == 'COMPONENTS':
                if line.startswith('-'):
                    parts = line.split()
                    if len(parts) >= 3:
                        cell_id = parts[1]
                        cell_type = parts[2]
                        G.add_node(cell_id, cell_type=cell_type)
            elif current_section == 'NETS':
                if line.startswith('-'):
                    parts = line.split()
                    if len(parts) >= 2:
                        current_net = parts[1]
                elif current_net:
                    parts = re.findall(r'\(([^)]+)\)', line)
                    for i in range(len(parts) - 1):
                        src_parts = parts[i].split()
                        dest_parts = parts[i + 1].split()
                        if len(src_parts) > 0 and len(dest_parts) > 0:
                            src = src_parts[0]
                            dest = dest_parts[0]
                            G.add_edge(src, dest, net=current_net)
    return G

def parse_guide(guide_file):
    guides = {}
    current_net = None

    with open(guide_file, 'r') as file:
        for line in file:
            line = line.strip()
            if line.startswith('net'):
                parts = line.split()
                if len(parts) > 1:
                    current_net = parts[1]
                    guides[current_net] = []
                else:
                    current_net = None
            elif current_net:
                guides[current_net].append(line)

    return guides

def load_ispd_data(base_dir):
    lef_file = os.path.join(base_dir, "ispd19_sample.input.lef")
    idef_file = os.path.join(base_dir, "ispd19_sample.input.def")
    guide_file = os.path.join(base_dir, "ispd19_sample.input.guide")

    cell_info = parse_lef(lef_file)
    G = parse_def(idef_file)
    guides = parse_guide(guide_file)

    return G, cell_info, guides

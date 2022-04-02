"""Running label propagation."""
import json
from model import LabelPropagator
from param_parser import parameter_parser
from print_and_read import graph_reader, argument_printer

def create_and_run_model(args):
    """
    Method to run the model.
    :param args: Arguments object.
    """
    graph = graph_reader(args.input)
    model = LabelPropagator(graph, args)
    model.do_a_series_of_propagations()
#influence of nodes with DNSD
    print("################################################################################################")
    influence = model.DNSD(graph)
    for k, v in sorted(influence.items(), key=lambda x: x[1]):
        print("Node Influence of %s = %s" % (k, v))
    print("################################################################################################")

if __name__ == "__main__":
    communaute = {}
    args = parameter_parser()
    argument_printer(args)
    create_and_run_model(args)
    with open(args.assignment_output) as json_data:
        data_dict = json.load(json_data)
        node = data_dict.keys()
        label = data_dict.values()
        total_label = []
        for l in label:
            if type(l) in (list, tuple, dict, str):
                for k in l:
                    if k not in total_label:
                        total_label.append(k)
            else:
                if l not in total_label:
                    total_label.append(l)
        print("Le nombre total des nodes=", len(node))
        print("Le nombre total de communauté = ", len(total_label))
        print("Les lebels des communautés sont ", total_label)
        for c in range(len(total_label)):
            key_list = []
            print("La communautes C", c, "de label", total_label[c], "est:")
            for k, val in data_dict.items():
                if type(val) in (list, tuple, dict, str):
                    for j in val:
                        if total_label[c] == j:
                            key_list.append(k)
                else:
                    if total_label[c] == val:
                        key_list.append(k)
            print(key_list)


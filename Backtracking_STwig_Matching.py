import copy

from Graph_Format import Graph_Format
import networkx as nx
from collections import OrderedDict

# def permute(list, s):
#     if list == 1:
#         return s
#     else:
#         return [ y + x
#                  for y in permute(1, s)
#                  for x in permute(list - 1, s)
#                  ]
#
# print(permute(1, ["a","b","c"]))
# print(permute(2, ["a","b","c"]))

# class Backtracking_STwig_Matching:
#     partial_solution = []
#     query_stwig_dict = {}
#     current_node = None
#     data_graph = None

    # def match_stwig_backtracking(query_stwig, query_stwig_as_labels, data_graph, index, solution):
    # # Cate o lista cu noduri din graf pentru fiecare tip de nod din STwig. Atunci lucram doar cu cateva liste.
    #
    #
    # # Verificam daca exista solutie
    # #   Cum returnam mai multe solutii? Cum facem intoarcerea?
    # # Punem criteriul de validitate
    # # In caz de validitate, apelam din nou si construim astfel solutia
    #
    #
    #     # if solution == [[]] or len(solution[1]) == len(query_stwig[1]):
    #     print("\n------------------------------")
    #     print("Input solution: " + str(solution))
    #     # Verficam daca am gasit o solutie completa.
    #     # if len(solution) > 1:
    #
    #     if is_valid(solution, query_stwig):
    #         cs = copy.deepcopy(solution)
    #         print("Complete solution: " + str(cs))
    #         complete_solutions.append(cs)
    #         print("Intermediary complete list: ")
    #         for c in complete_solutions:
    #             print(c)
    #         solution = back(solution, -1)
    #         print("Solution without last element: " + str(solution))
    #         print("Passing it on...")
    #         index = index - 2
    #         # new_leaf = find_valid_leaf_with_label(query_stwig_as_labels[3], solution, data_graph)
    #         # print("new_leaf: " + str(new_leaf))
    #         match_stwig_backtracking(query_stwig, query_stwig_as_labels, data_graph, index, solution)
    #
    #     else:
    #         if solution in complete_solutions:
    #             print("Already found.")
    #             print(back(solution, -2))
    #             solution = copy.deepcopy(back(solution, -2))
    #             # leaf_labels = copy.deepcopy(query_stwig_as_labels[1:])
    #             query_stwig_as_labels = copy.deepcopy(query_stwig_1_as_labels_source)
    #             match_stwig_backtracking(query_stwig, query_stwig_as_labels, data_graph, 1, solution)
    #
    #         # Pentru radacina STwig-ului:
    #         if len(solution) == 0:
    #             # print(len(solution))
    #             for root in data_graph.nodes():
    #                 # print("root: " + str(root))
    #                 if data_graph.node[root]['label'] == query_stwig_as_labels[0]: # Avem un root al unei solutii
    #                     solution.insert(0,root)
    #                     print("root: " + str(query_stwig[0]))
    #                     print("root label: " + str(query_stwig_as_labels[0]))
    #                     # solution.append([])
    #                     print("-solution start: " + str(solution))
    #                     # match_stwig_backtracking(query_stwig, query_stwig_as_labels, data_graph, index, solution)
    #                     break
    #
    #
    #                     # La urma vom sterge radacina, si vom intra din nou pe ramura aceasta.
    #                     # Trebuie facut ca sa nu ia aceeasi radacina din nou.
    #
    #         # Pentru O FRUNZA STwig-ului:
    #         if len(solution) >= 1:
    #             if len(solution[1:]) < len(query_stwig[1:]):
    #
    #                 print("query_stwig_as_labels: ")
    #                 print(query_stwig_as_labels)
    #                 leaf_labels = copy.deepcopy(query_stwig_as_labels[1:])
    #                 print("leaf_labels: ")
    #                 print(leaf_labels)
    #
    #                 # if len(solution[1:]) > 0:
    #                 if len(leaf_labels) > 0:
    #                     solution_leafs_number = len(solution[1:])
    #                     print("solution_leafs_number: ")
    #                     print(solution_leafs_number)
    #                     print("leaf_labels without already found node labels: ")
    #                     new_list_leaf_labels = leaf_labels[solution_leafs_number:]
    #                     print(new_list_leaf_labels)
    #                     if len(new_list_leaf_labels) > 0:
    #                         leaf_label = new_list_leaf_labels[0]
    #                         print("leaf_label")
    #                         print(leaf_label)
    #
    #                     else:
    #                         leaf_label = leaf_labels[0]
    #
    #                 print("leaf label for next valid leaf: ")
    #                 print(leaf_label)
    #                 print("label list for next iteration: ")
    #                 del leaf_labels[0]
    #                 print(leaf_labels)
    #
    #
    #                 print("query_stwig_as_labels for next iteration: MUST BE EQUAL WITH ABOVE LIST")
    #                 # query_stwig_as_labels.remove(leaf_label)
    #
    #                 position_for_replacement = query_stwig_1_as_labels_source.index(query_stwig_as_labels[0])
    #                 position_for_replacement = position_for_replacement + 1
    #                 print("position_for_replacement: ")
    #                 print(position_for_replacement)
    #                 del query_stwig_as_labels[0]
    #
    #
    #                 print(query_stwig_as_labels[1:])
    #                 valid_leaf = find_valid_leaf_with_label(leaf_label, solution, data_graph, position_for_replacement)
    #
    #                 print("valid_leaf: " + str(valid_leaf))
    #                 solution.append(valid_leaf)
    #                 # print(solution)
    #
    #                 # Trece la urmatoarea frunza
    #                 # solution[1] = solution[1][:3] # .append(valid_root)
    #                 print("Solution before next rec call: " + str(solution))
    #                 if index <= len(query_stwig_as_labels)-1:
    #                     index = index + 1
    #                     print("index: " + str(index))
    #                     match_stwig_backtracking(query_stwig, query_stwig_as_labels, data_graph, index, solution)
    #                 else:
    #                     print("Found first solution. Must pass it on.")
    #                     print("Refreshed query_stwig_1_as_labels: ")
    #                     query_stwig_1_as_labels = copy.deepcopy(query_stwig_1_as_labels_source)
    #                     print(query_stwig_1_as_labels)
    #                     match_stwig_backtracking(query_stwig, query_stwig_1_as_labels, data_graph, index, solution)
    #
    #
    #
    #
    #                 # leaf_label = query_stwig_1_as_labels[1][0]
    #                 # print("leaf_label selectat: " + str(leaf_label))
    #                 #
    #                 # for leaf in data_graph.nodes():
    #                 #     print("--leaf: " + str(leaf))
    #                 #     if data_graph.node[leaf]['label'] == leaf_label: # and leaf not in solution[1]: # Avem un nod te tipul unui leaf
    #                 #         # print("---leaf label: " + str(leaf_label))
    #                 #         # print("Same label")
    #                 #         if data_graph.has_edge(solution[0], leaf): # Verificam daca este vecinatate de ordinul 1
    #                 #         #     # print("----Is neighbor.")
    #                 #
    #                 #             solution[1].append(leaf)
    #                 #             # solution[1].append(leaf_label)
    #                 #             # print("     solution[1]: " + str(solution[1]))
    #                 #             print("     partial solution: " + str(solution))
    #                         #
    #                         #     solution[1] = solution[1][:1] # Cu asta putem face intoarcerea
    #
    #                                 # for i in range(1, len(query_stwig_1[1])):
    #                                 #     print(i)
    #                                 #     solution[1] = solution[1][:i]
    #                                 #     print(solution[1])
    #                                 # index = index + 1
    #                                 # match_stwig_backtracking(query_stwig, query_stwig_as_labels, data_graph, index, solution)
    #                             # else:
    #                             #     break
    #                                 # return solution
    #
    # def find_valid_leaf_with_label(leaf_label, solution, data_graph, position):
    #     valid_leafs_for_position = []
    #
    #     print("find_valid_leaf_with_label execution: ")
    #     # print(len(data_graph.nodes()))
    #     print("     leaf_label: " + leaf_label)
    #     # print(data_graph.has_node('3301'))
    #         # print(leaf)
    #         # print(type(leaf))
    #
    #     if len(complete_solutions) == 0:
    #         for leaf in data_graph.nodes():
    #
    #             # print("FIRST VALIDATION IF")
    #             if data_graph.node[leaf]['label'] == leaf_label:  # and leaf not in solution[1]: # Avem un nod te tipul unui leaf
    #                     print("     " + str(leaf) + " " + str(leaf_label))
    #
    #                     # if data_graph.has_edge(solution[0], leaf):  # Verificam daca este vecinatate de ordinul 1
    #                     if leaf in data_graph.neighbors(solution[0]):
    #                         # print("YES")
    #                         print("find_valid_leaf_with_label execution end on FIRST VALIDATION IF ")
    #
    #                         return leaf
    #
    #
    #     # Aici vine solutia fara ultimul element dupa gasirea primei solutii complete
    #     if len(complete_solutions) != 0:
    #         print("     SECOND VALIDATION IF - USED WHEN WE ALREADY HAD A COMPLETE SOLUTION")
    #         print("         complete_solutions until this iteration: ")
    #         print("         " + str(complete_solutions))
    #         for c_sol in complete_solutions:
    #             print("completed solution selected for comparison: ")
    #             print("     " + str(c_sol))
    #             # print("     " + str(c_sol[-1]))
    #             for leaf in data_graph.nodes():
    #                 # print(leaf)
    #                 # if leaf == c_sol[-1]:
    #                     # print("^---leaf already used")
    #
    #                 if leaf != c_sol[position]:
    #                     print("leaf from completed solution selected for comparison : ")
    #                     print(c_sol[position])
    #                     print(leaf)
    #                     print("^---leaf is different than the one in the complete solutions")
    #                     print("    and its label is: " + str(data_graph.node[leaf]['label']))
    #                     print("    The current selected leaf label is: " + str(leaf_label))
    #
    #                     if data_graph.node[leaf]['label'] == leaf_label:  # and leaf not in solution[1]: # Avem un nod te tipul unui leaf
    #                         if leaf in data_graph.neighbors(solution[0]):
    #                             print("     RETURNED VALID LEAF: " + str(leaf))
    #                             return leaf
    #                             # if leaf not in valid_leafs_for_position:
    #                             #     valid_leafs_for_position.append(leaf)
    #                             #     print("    APPENDED LEAF TO VALID LEAFS FOR POSITION: " + str(leaf))
    #
    #         # valid_leafs_for_position.sort()
    #         # print("valid_leafs_for_position: ")
    #         # print(valid_leafs_for_position)
    #         # leaf_to_return = valid_leafs_for_position[-1]
    #         # del valid_leafs_for_position[-1]
    #         # print("find_valid_leaf_with_label execution end on SECOND VALIDATION IF ")
    #         # return leaf_to_return
    #
    #
    # def back(solution, pos):
    #     to_del = copy.deepcopy(solution)
    #     to_del = to_del[:pos]
    #     # del to_del[pos]
    #     # print("sol_aux: ")
    #     # print(solution)
    #     return to_del
    #
    # def is_valid(solution, query_stwig):
    #     if len(solution[1:]) == len(query_stwig[1:]):
    #         # print(solution[1][:2])
    #         if solution not in complete_solutions:
    #             return True

    #---------------------------------------------------

    # def __init__(self, partial_solution, query_stwig_dict, current_node, data_graph):
    #     self.partial_solution = partial_solution
    #     self.query_stwig_dict = query_stwig_dict
    #     self.current_node = current_node
    #     self.data_graph = data_graph

def is_joinable(node, partial_solution, data_graph, query_stwig_as_dict):
    if len(partial_solution) <= len(list(query_stwig_as_dict.items())):
        if node not in partial_solution:
            if node in list(nx.ego_graph(data_graph, list(query_stwig_as_dict.keys())[0], radius=1, center=True, undirected=True, distance=None).nodes()):
                if data_graph.node[node]['label'] == query_stwig_as_dict[list(query_stwig_as_dict.keys())[len(partial_solution)]]:
                    return True
    return False

def update_state(node):
    c_node = copy.deepcopy(node)
    p_solution.append(c_node)
    return p_solution

def restore_state(partial_solution):
    del partial_solution[-1]
    p_solution = copy.deepcopy(partial_solution)
    print(p_solution)
    # return partial_solution

def next_query_vertex(current_node, query_stwig_dict):
    if current_node == []:
        return list(query_stwig_dict.keys())[0]
    current_node_pos = list(query_stwig_dict.keys()).index(current_node)
    next_node_pos = current_node_pos + 1
    try:
        return list(query_stwig_dict.keys())[next_node_pos]
    except IndexError:
        print("No more elements after this one in dict.")

def subgraph_search(partial_solution, query_stwig_dict, current_node, data_graph):
    if len(partial_solution) == len(list(query_stwig_dict.items())):
        # if partial_solution not in complete_solutions:
        c_sol = copy.deepcopy(partial_solution)
        complete_solutions.append(c_sol)
        # return partial_solution
        # partial_solution = []
        # candidate = []
        # subgraph_search(partial_solution, query_stwig_dict, candidate, data_graph)

    # if len(partial_solution) < len(list(query_stwig_dict.items())):
    else:
        candidate = next_query_vertex(current_node, query_stwig_dict)
        print("Candidate: ")
        print(candidate)
        if is_joinable(candidate, partial_solution, data_graph, query_stwig_dict):
            print("IS JOINABLE")
            partial_solution = copy.deepcopy(update_state(candidate))
            print("PARTIAL SOLUTION: ")
            print(partial_solution)
            subgraph_search(partial_solution, query_stwig_dict, candidate, data_graph)
            restore_state(partial_solution)

# # Cream graful de 1000 de muchii.
# # Il inseram in NetworkX
# # Adaugam label-urile nodurilor
#
# # Inseram in graful nx graful RI
# graph_format = Graph_Format("Homo_sapiens_udistr_32.gfd")
# graph_format.create_graph_from_RI_file()
# nx_ri_graph = graph_format.get_graph()
# # print(nx_ri_graph.nodes())
# # print(list(nx_ri_graph.edges())[2])
#
# # Noduri pentru 1000 de muchii, apoi 1000 muchii.
#
# # Cream un graf nou cu 1000 de muchii din graful RI
# nx_ri_graph_1000edges = nx.Graph()
# # nodes_for_1000_edges =
# nx_ri_graph_1000edges.add_edges_from(list(nx_ri_graph.edges())[:1000])
# # nodes_and_labels_dict = {}
# nodes_for_selected_1000_edges = list(nx_ri_graph_1000edges.nodes())
#
# aux_graph = nx.Graph()
# for node in nodes_for_selected_1000_edges:
#     aux_graph.add_node(node, label=nx_ri_graph.node[node]['label'])
# # for n in aux_graph.nodes(data=True):
# #     print(n)
# aux_graph.add_edges_from(list(nx_ri_graph.edges())[:1000])
# print("Number of graph edges: " + str(len(aux_graph.edges())))
# print("Nodes and labels of nodes: " + str(aux_graph.nodes(data=True)))
# print("Number of nodes: " + str(len(aux_graph.nodes(data=True))))
#
# graph_for_bactracking_search = aux_graph
# data_graph = aux_graph
#
#
# query_stwig_1 = ['1773', '1488', '1898', '2285']
# print("Query STwig: " + str(query_stwig_1))
# # Label-ul radacinii
# root_label = graph_for_bactracking_search.node[query_stwig_1[0]]['label']
# # Label-urile vecinilor din lista
# neighbor_labels = []
# for n in query_stwig_1[1:]:
#     neighbor_labels.append(graph_for_bactracking_search.node[n]['label'])
#
# query_stwig_1_as_labels = []
# query_stwig_1_as_labels.append(root_label)
# for nl in neighbor_labels:
#     query_stwig_1_as_labels.append(nl)
# print("query_stwig_1_as_labels: " + str(query_stwig_1_as_labels))


# Graf data foarte mic, 10 noduri, 4 label-uri.

small_graph = nx.Graph()
small_graph_nodes = [1,2,3,4,5,6,7,8,9,10]
# Sortarea ascendenta la string este diferita de cea a de la tipul int
small_graph_nodes.sort()
small_graph_edges = [[1, 2], [1, 3], [5, 6], [5, 7], [1, 6], [1, 7], [1, 10]]
small_graph.add_nodes_from(small_graph_nodes)
small_graph.add_edges_from(small_graph_edges)
node_attr = ["a", "b", "c", "d", "a", "b", "c", "d", "a", "b"]
node_attr_dict = dict(zip(sorted(small_graph.nodes()), node_attr))
print(node_attr_dict.items())
nx.set_node_attributes(small_graph, node_attr_dict, 'label')
print(small_graph.nodes(data=True))
print(small_graph.edges())

query_stwig_1 = [1, 2, 3]
print("Query STwig: " + str(query_stwig_1))
# Label-ul radacinii
root_label = small_graph.node[query_stwig_1[0]]['label']
# Label-urile vecinilor din lista
neighbor_labels = []
for n in query_stwig_1[1:]:
    neighbor_labels.append(small_graph.node[n]['label'])

query_stwig_1_as_labels = []
query_stwig_1_as_labels.append(root_label)
for nl in neighbor_labels:
    query_stwig_1_as_labels.append(nl)
print("query_stwig_1_as_labels: " + str(query_stwig_1_as_labels))
print()
query_stwig_1_as_labels_source = copy.deepcopy(query_stwig_1_as_labels)

query_stwig1_dict = OrderedDict(zip(query_stwig_1, query_stwig_1_as_labels_source))
print("query_stwig1_dict: ")
print(query_stwig1_dict.items())
print()
p_solution = []
complete_solutions = []
subgraph_search(p_solution, query_stwig1_dict, [], small_graph)
# complete_solutions = []
# b = Backtracking_STwig_Matching()
# b.subgraph_search([], query_stwig1_dict, [], small_graph)

# print(list(query_stwig1_dict.keys())[0])
# print(query_stwig1_dict[1])
# current_node_pos = list(query_stwig1_dict.keys()).index(2)
# print(current_node_pos)
# next_node_pos = current_node_pos + 1
# print(next_node_pos)
# print("Next element:")
# print(next_query_vertex(2, query_stwig1_dict))
# print(is_joinable(3, [1,2], small_graph, query_stwig1_dict))



# print("Backtracking start: ")
# complete_solutions = []
# match_stwig_backtracking(query_stwig_1, query_stwig_1_as_labels, small_graph, 1, [])
# print("\nComplete solutions list: ")
# for c in complete_solutions:
#     print(c)


# r = '1773'
# solution = [r, []]
# leaf_sol = []
# leaf_label = query_stwig_1_as_labels[1][0]
# for leaf_label in query_stwig_1_as_labels[1]:
#
#     print("leaf_label selectat: " + str(leaf_label))
#     for leaf in data_graph.nodes():
#         # print("--leaf: " + str(leaf))
#         if data_graph.node[leaf]['label'] == leaf_label:  # and leaf not in solution[1]: # Avem un nod te tipul unui leaf
#             print("     " + str(leaf))
#             # print("---leaf label: " + str(leaf_label))
#             if data_graph.has_edge(solution[0], leaf):  # Verificam daca este vecinatate de ordinul 1
#                 solution[1].append(leaf)
#                 # solution[1] = leaf_sol
#                 print("     ^---Is neighbor => " + str(solution))

        #         solution[1].append(leaf)
        #         # solution[1].append(leaf_label)
        #         # print("     solution[1]: " + str(solution[1]))
        #         print("     partial solution: " + str(solution))





# root_label_nodes_dict = {}
# for node in graph_for_bactracking_search.nodes():
#     if graph_for_bactracking_search.node[node]['label'] == query_stwig_1_as_labels[0]:
#         root_label_nodes_dict[query_stwig_1_as_labels[0]] = node
#
#
# leaf_labels_nodes_dict = {}
# if len(query_stwig_1_as_labels[1]) == 1:
#     leaf_label_1_nodes = []
#
#     for node in graph_for_bactracking_search.nodes():
#         if graph_for_bactracking_search.node[node]['label'] == query_stwig_1_as_labels[1][0]:
#             leaf_label_1_nodes.append(node)
#     leaf_labels_nodes_dict[query_stwig_1_as_labels[1][0]] = leaf_label_1_nodes
#
# elif len(query_stwig_1_as_labels[1]) == 2:
#     leaf_label_1_nodes = []
#     leaf_label_2_nodes = []
#     for node in graph_for_bactracking_search.nodes():
#         if graph_for_bactracking_search.node[node]['label'] == query_stwig_1_as_labels[1][0]:
#             leaf_label_1_nodes.append(node)
#         elif graph_for_bactracking_search.node[node]['label'] == query_stwig_1_as_labels[1][1]:
#             leaf_label_2_nodes.append(node)
#     leaf_labels_nodes_dict[query_stwig_1_as_labels[1][0]] = leaf_label_1_nodes
#     leaf_labels_nodes_dict[query_stwig_1_as_labels[1][1]] = leaf_label_2_nodes
#
#
# elif len(query_stwig_1_as_labels[1]) == 3:
#     leaf_label_1_nodes = []
#     leaf_label_2_nodes = []
#     leaf_label_3_nodes = []
#     for node in graph_for_bactracking_search.nodes():
#         if graph_for_bactracking_search.node[node]['label'] == query_stwig_1_as_labels[1][0]:
#             leaf_label_1_nodes.append(node)
#         elif graph_for_bactracking_search.node[node]['label'] == query_stwig_1_as_labels[1][1]:
#             leaf_label_2_nodes.append(node)
#         elif graph_for_bactracking_search.node[node]['label'] == query_stwig_1_as_labels[1][2]:
#             leaf_label_3_nodes.append(node)
#     leaf_labels_nodes_dict[query_stwig_1_as_labels[1][0]] = leaf_label_1_nodes
#     leaf_labels_nodes_dict[query_stwig_1_as_labels[1][1]] = leaf_label_2_nodes
#     leaf_labels_nodes_dict[query_stwig_1_as_labels[1][2]] = leaf_label_3_nodes
#
#
# elif len(query_stwig_1_as_labels[1]) == 4:
#     leaf_label_1_nodes = []
#     leaf_label_2_nodes = []
#     leaf_label_3_nodes = []
#     leaf_label_4_nodes = []
#     for node in graph_for_bactracking_search.nodes():
#         if graph_for_bactracking_search.node[node]['label'] == query_stwig_1_as_labels[1][0]:
#             leaf_label_1_nodes.append(node)
#         elif graph_for_bactracking_search.node[node]['label'] == query_stwig_1_as_labels[1][1]:
#             leaf_label_2_nodes.append(node)
#         elif graph_for_bactracking_search.node[node]['label'] == query_stwig_1_as_labels[1][2]:
#             leaf_label_3_nodes.append(node)
#         elif graph_for_bactracking_search.node[node]['label'] == query_stwig_1_as_labels[1][3]:
#             leaf_label_4_nodes.append(node)
#     leaf_labels_nodes_dict[query_stwig_1_as_labels[1][0]] = leaf_label_1_nodes
#     leaf_labels_nodes_dict[query_stwig_1_as_labels[1][1]] = leaf_label_2_nodes
#     leaf_labels_nodes_dict[query_stwig_1_as_labels[1][2]] = leaf_label_3_nodes
#     leaf_labels_nodes_dict[query_stwig_1_as_labels[1][3]] = leaf_label_4_nodes



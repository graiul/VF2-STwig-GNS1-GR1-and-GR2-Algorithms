from Graph_File_Generator import Graph_File_Generator
from DB_Access_Test import DB_Access_Test
from Dataset_Operator import Dataset_Operator
from STwig_Algorithm import STwig_Algorithm
from VF2Algorithm import VF2Algorithm
from neo4j_test_2 import neo4j_test_2
import os
from multiprocessing import Pool, Process, Manager

from timeit import default_timer as timer

from functools import partial

def main():
    menu = [
        ["\n\n1. Graph generator tool"],
        ["2. Insert Zhao Sun data into db"],
        ["21. Insert RI data into db"],
        ["22. Insert small graph data into db"],
        ["3. Delete data from db"],
        ["4. View graph data - single thread"],
        ["5. View graph data - multi-threaded"],
        ["6. View graph data - multi-process"],
        ["7. Run MatchSTwig"],
        ["8. Run STwig_Order_Selection"],
        ["9. Run MatchSTwig per STwig generated by STwig_Order_Selection"],
        ["91. Run MatchSTwig *one process per STwig* generated by STwig_Order_Selection; unfiltered results"],
        ["92. Run MatchSTwig *one process per STwig* generated by STwig_Order_Selection; filtered results"],
        ["93. Small graph: Run MatchSTwig *one process per STwig* generated by STwig_Order_Selection; filtered results"],
        ["10. Query graph zhaosun split prototype, single threaded"],
        ["11. Configure db"],
        ["12. VF2 Algorithm"],
        ["0. Exit"]
    ]
    print()
    for m in menu:
        print(m)
    while(True):

        option = int(input('\nPlease choose option: '))
        # option = 12



        if option == 2:
            # node_dataset_url = str(input('\nDataset nodes URL: '))
            node_dataset_url = "https://raw.githubusercontent.com/room229/graph_datasets/master/ZhaoSun_Data_Graph_Nodes.csv"
            # edge_dataset_url = str(input('\nDataset edges URL: '))
            edge_dataset_url = "https://raw.githubusercontent.com/room229/graph_datasets/master/ZhaoSun_Data_Graph_Edges.csv"
            leader_core_bolt_address = str(input('\nLeader core bolt address: '))
            username = str(input('\nUsername of core: '))
            passwd = str(input('\nPassword of core: '))
            dataset_operator = Dataset_Operator(node_dataset_url, edge_dataset_url, leader_core_bolt_address, username, passwd)
            dataset_operator.insert_nodes_zhao_sun()
            dataset_operator.insert_edges_zhao_sun()
            print()
            for m in menu:
                print(m)

        elif option == 21:
            # node_dataset_url = str(input('\nDataset nodes URL: '))
            node_dataset_url = "https://raw.githubusercontent.com/room229/graph_datasets/master/RI_data_graph_nodes.csv"
            # edge_dataset_url = str(input('\nDataset edges URL: '))
            edge_dataset_url = "https://raw.githubusercontent.com/room229/graph_datasets/master/RI_data_graph_edges.csv"
            leader_core_bolt_address = str(input('\nLeader core bolt address: '))
            username = str(input('\nUsername of core: '))
            passwd = str(input('\nPassword of core: '))
            dataset_operator = Dataset_Operator(node_dataset_url, edge_dataset_url, leader_core_bolt_address, username, passwd)
            dataset_operator.insert_nodes_RI()
            option = str(input('\nStart inserting edges? (y/n): '))
            if option == "y":
                dataset_operator.insert_edges_RI()
            print()
            for m in menu:
                print(m)

        elif option == 22:
            node_dataset_url = "https://raw.githubusercontent.com/room229/graph_datasets/master/10_node_graph_nodes.csv"
            edge_dataset_url = "https://raw.githubusercontent.com/room229/graph_datasets/master/10_node_graph_edges.csv"
            # leader_core_bolt_address = str(input('\nLeader core bolt address: '))
            leader_core_bolt_address = "http://localhost:7474/"
            # username = str(input('\nUsername of core: '))
            username = "neo4j"
            # passwd = str(input('\nPassword of core: '))
            passwd = "changeme"
            dataset_operator = Dataset_Operator(node_dataset_url, edge_dataset_url, leader_core_bolt_address, username, passwd)
            dataset_operator.insert_nodes_small_graph()
            dataset_operator.insert_edges_small_graph()
            print()
            for m in menu:
                print(m)

        elif option == 3:
            leader_core_bolt_address = str(input('\nLeader core bolt address: '))
            username = str(input('\nUsername of core: '))
            passwd = str(input('\nPassword of core: '))
            dataset_operator = Dataset_Operator(None, None, leader_core_bolt_address, username, passwd)
            dataset_operator.delete_data_from_db()
            print()
            for m in menu:
                print(m)

        elif option == 4:
            print("\n================= Option 4 commencing... =================")
            test = DB_Access_Test()
            test.single_thread_access_to_one_read_replica()
            print("\n============== End of Option 4 execution =================")
            print()
            for m in menu:
                print(m)

        elif option == 5:
            print("\n================= Option 5 commencing... =================")
            test = DB_Access_Test()
            test.run_test_multiple_threads()
            print("\n============== End of Option 5 execution =================")
            print()
            for m in menu:
                print(m)

        elif option == 6:
            print("\n================= Option 6 commencing... =================")
            db = DB_Access_Test()
            queries = ["MATCH (n) RETURN n", "MATCH (n) RETURN n", "MATCH (n) RETURN n"]
            p = Pool(3)
            print("Pool result:")
            # res = p.map(foo.work, queries)
            start_time = timer()
            res = p.map(db.multiple_processes_access_to_one_read_replica, queries)
            total_time_sec = timer() - start_time
            total_time_millis = total_time_sec * 1000
            # print(res)
            for r in res:
                for rr in r:
                    print(rr)
                print()
            p.close()
            print()
            print('\x1b[0;30;45m' + 'DB_Access_Test multiple procs exec time: ' + str(
                total_time_millis) + ' ms' + '\x1b[0m')

            print("\n============== End of Option 6 execution =================")
            print()
            for m in menu:
                print(m)

        elif option == 7:
            print("\n================= Option 7 commencing... =================")
            # q = ['a', ['b', 'c']]
            # q = ['b', ['a', 'd', 'e']]
            q = ['d', ['c', 'f', 'e']]
            query_graph_gen = Graph_File_Generator()
            query_graph = query_graph_gen.gen_zhaosun_query_graph()
            test2 = neo4j_test_2(query_graph)
            print("Searcing given STwigs from query graph in the data graph: ")
            start_time = timer()
            STwig_matches = test2.MatchSTwig(q)
            total_time_sec = timer() - start_time
            total_time_millis = total_time_sec * 1000
            print("\nSTwigs from data graph corresponding to the query STwig given: ")
            for match in STwig_matches:
                print(match)
            print('\x1b[0;30;45m' + 'Match STwig exec time: ' + str(
                total_time_millis) + ' ms' + '\x1b[0m')
            print("\n============== End of Option 7 execution =================")

        elif option == 8:
            print("\n================= Option 8 commencing... =================")
            print("STwig_Order_Selection: ")
            query_graph_gen = Graph_File_Generator()
            query_graph = query_graph_gen.gen_zhaosun_query_graph()
            test2 = neo4j_test_2(query_graph)

            start_time = timer()
            stwigs = test2.STwig_Order_Selection()
            total_time_sec = timer() - start_time
            total_time_millis = total_time_sec * 1000
            for t in stwigs:
                print(t)

            print()
            print('\x1b[0;30;45m' + 'STwig Order Selection exec time: ' + str(
                total_time_millis) + ' ms' + '\x1b[0m')
            print("\n============== End of Option 8 execution =================")
            print()
            for m in menu:
                print(m)

        elif option == 9:
            print("\n================= Option 9 commencing... =================")
            query_graph_gen = Graph_File_Generator()
            query_graph = query_graph_gen.gen_zhaosun_query_graph()
            test2 = neo4j_test_2(query_graph)

            start_time = timer()
            stwigs = test2.STwig_Order_Selection()

            print("stwigs:")
            print(stwigs)
            print("labels of stwigs:")
            print(query_graph.nodes(data=True))
            total_time_sec = timer() - start_time
            total_time_millis = total_time_sec * 1000
            # for t in stwigs:
            iteration_number = stwigs.index(stwigs[0])
            print("--------Iteration number: " + str(iteration_number) + str("-----------"))


            # test2.STwig_query_root = stwigs[0][0]

            test2.STwig_query_neighbor_labels = stwigs[0][1]

            # print("stwigs[0]:" + str(stwigs[0]))
            matches = test2.MatchSTwig(stwigs[0], iteration_number)
            test2.matches_dict[repr(stwigs[0])] = matches
            # print("matches for Iteration 0:")
            # print(matches)

            print("Matches dictionary: ")
            print("First key: ")
            print(list(test2.matches_dict.keys())[0])
            print('\x1b[0;30;45m' + "First values attached to the first key; matches: " + '\x1b[0m')
            for match in list(test2.matches_dict.values())[0]:
                print('\x1b[0;30;45m' + str(match) + '\x1b[0m')
            print("--------Iteration end-----------------")

            for t in stwigs[1:]:
                iteration_number = stwigs.index(t)
                print("--------Iteration number: " + str(iteration_number) + str("-----------"))
                test2.STwig_query_root = t[0]
                test2.STwig_query_neighbor_labels = t[1]
                matches = test2.MatchSTwig(t, iteration_number)
                # test2.matches_dict[repr(t)] = matches
                print("--------Iteration end-----------------")

            # print("STwig list:")
            # print(test2.stwig_list)

            print()
            print('\x1b[0;30;45m' + 'STwig Order Selection exec time: ' + str(
                total_time_millis) + ' ms' + '\x1b[0m')
            print("\n============== End of Option 9 execution =================")

        elif option == 91:
            print("\n================= Option 91 commencing... =================")
            query_graph_gen = Graph_File_Generator()
            query_graph = query_graph_gen.gen_zhaosun_query_graph()
            test2 = neo4j_test_2(query_graph)

            start_time = timer()
            stwigs = test2.STwig_Order_Selection()

            # Initiem un process pool cu numarul de procese egal cu cel al STwig-urilor generate de STwig_Order_Selection
            pool = Pool(len(stwigs))
            print("Pool: " + str(pool))
            # Avem un dictionar care va stoca rezultatele fiecarui process.
            # Acest dictionar este o zona de memorie comuna al proceselor, iar ordinea cheilor(ordinea in care
            # stocam datele de iesire) nu conteaza.
            # Va trebui sa punem o bariera, astfel incat atunci cand fiecare proces cauta in dictionar,
            # toate procesele trebuie sa fi pus deja rezultatele lor in el.

            manager = Manager()
            process_dict = manager.dict()
            # pool.


            # Pentru fiecare proces rulam o metoda de gasire al matches pentru un singur STwig
            # Avem doua cazuri: primul STwig care trebuie cautat cu totul in graful data
            # si urmatoarele, dar care vor fi bounded de primul, deci radacinile lor sunt deja stabilite.
            test2.STwig_query_neighbor_labels = stwigs[0][1]
            # db.match_finding_process(stwigs[0], 0, test2)
            db = DB_Access_Test()

            return_dict = manager.dict()
            # func = partial(db.match_finding_process, [stwigs[0]])
            # res = pool.map(db.match_finding_process, [stwigs[0]])
            # print(res)

            process = Process(target=db.match_finding_process, args=(stwigs[0], return_dict, ))
            process.start()
            process.join()
            print(return_dict.values())

            jobs = []

            for t in stwigs[1:]:
                process = Process(target=db.match_finding_process, args=(t, return_dict, ))
                jobs.append(process)

            for j in jobs:
                j.start()
                j.join()
                print(return_dict.values())

            # for t in stwigs[1:]:
            #     iteration_number = stwigs.index(t)
            #     print("--------Iteration number: " + str(iteration_number) + str("-----------"))
            #     test2.STwig_query_root = t[0]
            #     test2.STwig_query_neighbor_labels = t[1]
            #     matches = test2.MatchSTwig(t, iteration_number)
            #     # test2.matches_dict[repr(t)] = matches
            #     print("--------Iteration end-----------------")

            print("\n============== End of Option 91 execution =================")

        elif option == 92:
            print("\n================= Option 92 commencing... =================")
            query_graph_gen = Graph_File_Generator()
            # query_graph = query_graph_gen.gen_zhaosun_query_graph()
            query_graph = query_graph_gen.gen_RI_query_graph()
            print(query_graph.nodes(data=True))

            manager = Manager()
            return_dict = manager.dict()
            used_stwigs = manager.list()
            STwig_query_neighbor_labels = manager.list()

            STwig_algorithm = STwig_Algorithm(query_graph, return_dict, used_stwigs, STwig_query_neighbor_labels)
            stwigs = STwig_algorithm.STwig_Order_Selection()
            print("stwigs: " + str(stwigs))
            db = DB_Access_Test()


            # process = Process(target=db.match_finding_process_filtered, args=(stwigs[0], return_dict, STwig_query_neighbor_labels, query_graph, iter_num, ))
            # process.start()
            # process.join()

            jobs = []

            # for t in stwigs[1:]:
            for t in stwigs:
                iter_num = stwigs.index(t)
                process = Process(target=db.match_finding_process_filtered, args=(t, return_dict, STwig_query_neighbor_labels, query_graph, iter_num, used_stwigs, ))
                jobs.append(process)


            for j in jobs:
                j.start()
                j.join()

            print("Results from multiprocessing: ")
            for item in return_dict.items():
                print(item)



            print("\n============== End of Option 92 execution =================")

        elif option == 93:
            print("\n================= Option 93 commencing... =================")
            query_graph_gen = Graph_File_Generator()
            # query_graph = query_graph_gen.gen_zhaosun_query_graph()
            query_graph = query_graph_gen.gen_small_graph_query_graph()
            print(query_graph.nodes(data=True))

            manager = Manager()
            return_dict = manager.dict()
            used_stwigs = manager.list()
            STwig_query_neighbor_labels = manager.list()

            STwig_algorithm = STwig_Algorithm(query_graph, return_dict, used_stwigs, STwig_query_neighbor_labels)
            stwigs = STwig_algorithm.STwig_Order_Selection()
            print("stwigs: " + str(stwigs))
            db = DB_Access_Test()

            jobs = []

            for t in stwigs:
                iter_num = stwigs.index(t)
                process = Process(target=db.match_finding_process_filtered, args=(t, return_dict, STwig_query_neighbor_labels, query_graph, iter_num, used_stwigs, ))
                jobs.append(process)

            for j in jobs:
                j.start()
                j.join()

            print("Results from multiprocessing: ")
            for item in return_dict.values():
                for i in item:
                    print(i)



            print("\n============== End of Option 93 execution =================")

        elif option == 10:
            print("\n================= Option 10 commencing... =================")
            # print("Are these the query graph STWIGS?")
            query_graph_gen = Graph_File_Generator()
            query_graph = query_graph_gen.gen_zhaosun_query_graph()
            test2 = neo4j_test_2()
            query_graph_gen = Graph_File_Generator()
            query_graph = query_graph_gen.gen_zhaosun_query_graph()
            splits = test2.Query_Graph_Split(query_graph)
            for s in splits:
                print(str(splits))
            print("\n============== End of Option 10 execution =================")

        elif option == 11:
            file = "notepad.exe neo4j_db\\docker-compose.yml"
            os.system(file)

        elif option == 12:
            print("\nVF2 Algorithm: ")

            # TRANSFORMA IN INT DIN STR IN CREAREA GRAFULUI NX! - Facut.

            # M = [["0", "0"]]  # Test de corectitudine. Ar trebui sa dea un M in care toate match-urile sa aiba elemente egale, practic sa imi returneze toate nodurile query asociate cu ele insasi.
            # M = [["0", "1173"]] # Test al timpului de executie.
            # vf2 = VF2Algorithm(M, 'graph_to_RI_db.txt', 'Homo_sapiens_udistr_32.gfd', 'RI')

            # M = [["1","1"]]
            # M = [['1','5']]
            # M = [["1","9"]]
            # print(M)

            M = []

            # vf2 = VF2Algorithm(M, 'small_query_graph_VF2.txt', 'small_data_graph_VF2.txt', 'RI')
            # vf2.subGraphSearch(M)

            results = []

            if len(M) == 0:
                print("\nRoots: ")
                vf2 = VF2Algorithm(M, 'small_query_graph_VF2.txt', 'small_data_graph_VF2.txt', 'RI')
                roots = vf2.subGraphSearch(M)[1]
                print()
                print(roots)
                print("Selected root: ")
                for root in roots:
                    print(root)
                    M = [["1",str(root)]]
                    print("M = " + str(M))
                    vf2 = VF2Algorithm(M, 'small_query_graph_VF2.txt', 'small_data_graph_VF2.txt', 'RI')
                    vf2.subGraphSearch(M)
                    # vf2 = None
                    results.append(list(vf2.results_dict.items()))

                print("\nFinal results: ")
                for result in results:
                    print(result)

        elif option == 0:
            exit(code=0)

if __name__ == '__main__':
    main()
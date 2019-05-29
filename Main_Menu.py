from Graph_File_Generator import Graph_File_Generator
from DB_Access_Test import DB_Access_Test
from Dataset_Operator import Dataset_Operator
from neo4j_test_2 import neo4j_test_2
import os
from multiprocessing import Pool
from timeit import default_timer as timer

def main():
    menu = [
        ["\n\n1. Graph generator tool"],
        ["2. Insert data into db"],
        ["3. Delete data from db"],
        ["4. View graph data - single thread"],
        ["5. View graph data - multi-threaded"],
        ["6. View graph data - multi-process"],
        ["7. Run MatchSTwig"],
        ["8. Run STwig_Order_Selection"],
        ["9. Query graph zhaosun split prototype, single threaded"],
        ["10. Configure db"],
        ["0. Exit"]
    ]
    print()
    for m in menu:
        print(m)
    while(True):
        option = int(input('\nPlease choose option: '))
        if option == 2:
            # node_dataset_url = str(input('\nDataset nodes URL: '))
            node_dataset_url = "https://raw.githubusercontent.com/room229/graph_datasets/master/ZhaoSun_Data_Graph_Nodes.csv"
            # edge_dataset_url = str(input('\nDataset edges URL: '))
            edge_dataset_url = "https://raw.githubusercontent.com/room229/graph_datasets/master/ZhaoSun_Data_Graph_Edges.csv"
            leader_core_bolt_address = str(input('\nLeader core bolt address: '))
            username = str(input('\nUsername of core: '))
            passwd = str(input('\nPassword of core: '))
            dataset_operator = Dataset_Operator(node_dataset_url, edge_dataset_url, leader_core_bolt_address, username, passwd)
            dataset_operator.insert_nodes()
            dataset_operator.insert_edges()
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
            start_time = timer()
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
            q = ['a', ['b', 'c']]
            query_graph_gen = Graph_File_Generator()
            query_graph = query_graph_gen.gen_zhaosun_query_graph()
            test2 = neo4j_test_2(query_graph)
            print("Searcing given STwigs from query graph in the data graph: ")
            STwigs = test2.MatchSTwig(q)
            print("\nSTwigs from data graph corresponding to the query STwig given: ")
            for stwig in STwigs:
                print(stwig)
            print("\n============== End of Option 7 execution =================")

        elif option == 8:
            print("\n================= Option 8 commencing... =================")
            print("STwig_Order_Selection: ")
            query_graph_gen = Graph_File_Generator()
            query_graph = query_graph_gen.gen_zhaosun_query_graph()
            test2 = neo4j_test_2(query_graph)
            for t in test2.STwig_Order_Selection():
                print(t)
            print("\n============== End of Option 8 execution =================")
            print()
            for m in menu:
                print(m)

        elif option == 9:
            print("\n================= Option 9 commencing... =================")
            # print("Are these the query graph STWIGS?")
            query_graph_gen = Graph_File_Generator()
            query_graph = query_graph_gen.gen_zhaosun_query_graph()
            test2 = neo4j_test_2()
            query_graph_gen = Graph_File_Generator()
            query_graph = query_graph_gen.gen_zhaosun_query_graph()
            splits = test2.Query_Graph_Split(query_graph)
            for s in splits:
                print(str(splits))
            print("\n============== End of Option 9 execution =================")

        elif option == 10:
            file = "notepad.exe neo4j_db\\docker-compose.yml"
            os.system(file)



        elif option == 0:
            exit(code=0)

if __name__ == '__main__':
    main()
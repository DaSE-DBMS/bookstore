from fe.bench.workload import Workload
from fe.bench.session import Session


def run_bench():
    wl = Workload()
    wl.gen_database()
    ss = Session(wl)
    ss.gen_procedure()

    sessions = []
    for i in range(0, wl.session):
        ss = Session(wl)
        sessions.append(ss)

    for ss in sessions:
        ss.run()

    for ss in sessions:
        ss.join()


#if __name__ == "__main__":
#    run_bench()
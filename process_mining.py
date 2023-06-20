import pm4py

# Load the event log
event_log = pm4py.read_xes("event_log.xes")

# Discover a process model using the Alpha Miner algorithm
process_model = pm4py.discovery.alpha_miner.apply(event_log)

# Visualize the process model
pm4py.visualization.process_tree.view(process_model)

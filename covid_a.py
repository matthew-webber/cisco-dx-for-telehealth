from helpers.endpoint_helpers import MockDataDaemon
from endpoints.factories import EndpointFactory
from data.teleport_data import TeleportProvisioner
import time
from multiprocessing.pool import ThreadPool

if __name__ == '__main__':

    # todo TEST if running this when a DX is on gets the proper online vs mock object (run, reboot + run)
    #
    all_data = MockDataDaemon().pull_all_data()
    endpoint_ips = [endpoint['ip'] for endpoint in all_data]

    # endpoint_ips = [
    #     '10.27.200.140',  # my DX
    #     '10.33.100.145',  # DX-PATIENT 10 live but "offline"
    #     '10.33.112.74',  # NS-02 LIVE!!!!!!
    #     '10.33.114.35',  # telepod
    #     '10.33.48.18',  # triage
    #     '10.33.121.109',  # DX-5C-02
    # ]

    all_data = MockDataDaemon().pull_all_data()
    endpoint_ips = [endpoint['ip'] for endpoint in all_data]

    factory = EndpointFactory(endpoint_ips[:5])
    factory.process_queue(multiprocessor=True)  # sort endpoints into online / offline queues
    package = factory.package_endpoints()  # process queues and put into endpoint container

    provisioner = TeleportProvisioner()  # create provisioner to outfit endpoints for Teleport work
    provisioner.typify(package.online + package.offline)  # add Teleport types / roles to endpoints

    """for pretty printing"""
    lengths = [len(ep.name) for ep in package.online]
    long_name = max(lengths)

    for endpoint in package.online:  # currently, online providers are the only endpoints that get directives
        provisioner.add_directives(endpoint)  # add directives depending on role + type
        favorites = provisioner.define_favorites(endpoint)  # create favorites "to-be-added" to endpoint
        # print(favorites, f' for {endpoint.name}, {endpoint.type}')
        if favorites:
            endpoint.collect_favorites(package.online + package.offline, favorites)
            print(
                f"\t{endpoint.name}{'.' * (long_name - len(endpoint.name))}.. ({len(endpoint._favorites)}) favorites, ({len(endpoint.directives)}) directives")

    print(f"\n{len(package.online)} Teleports are locked and loaded!")

    print(f'Main done in {round(time.perf_counter(), 2)}')

'''        
    
   
# todo refresh offline endpoints to see if they're online again instead of having to run the whole thing over again

'''
'''
    print("\nSorting + packaging endpoints...")
    package = factory.package_endpoints()  # process queues and put into endpoint container
    print("\nCreating TeleportProvisioner...")
    provisioner = TeleportProvisioner()  # create provisioner to outfit endpoints for Teleport work
    print("Provisioning endpoints with types/roles...")
    provisioner.typify(package.online + package.offline)  # add Teleport types / roles to endpoints
    print("Provisioning endpoints with directives/favorites...\n")

    myDX = package.online[-1]

# todo refresh offline endpoints to see if they're online again instead of having to run the whole thing over again

'''
'''
Wishlist:

1. Refresh "offline" endpoints
        
        Pull up a list of offline endpoints ("status check") and then choose to refresh either all ("refresh all") or 
        refresh a specific endpoint ("refresh <index of endpoint from status check list>").  The objects would be
        checked again and moved from offline > online if necessary.
        
2. Check for conflicts b/t .csv file and live endpoint data

        Compare / contrast the data associated with an IP address across the .csv file and the data in a live endpoint.
        If a discrepancy is found, print the discrepancy and ask user if they want to update the .csv file or the
        endpoint itself using API calls (feel like this would be rare because the .csv is likely to be the inaccurate
        one).
        
'''
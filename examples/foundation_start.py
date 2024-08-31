#!/usr/bin/env python

from foundation.utils import Workers
import argparse

parser = argparse.ArgumentParser(description="Start an HCI worker.")
parser.add_argument(
    '-a', '--advertise_addr', default=None, help="Advertise address."
)
args = parser.parse_args()


# ----------------------------------------------------------------------
def main():
    """"""
    workers = Workers(swarm_advertise_addr=args.advertise_addr)
    workers.stop_all_workers()

#     # Basic services
#     workers.swarm.start_ntp(restart=True)
#     workers.swarm.start_jupyterlab(restart=True)
#     # workers.swarm.start_kafka(restart=True)
#     # workers.swarm.start_kafka_logs(restart=True)
#     workers.swarm.start_timescaledb(restart=True)
#     # workers.swarm.delete_volume('timescaledb-service-volume')
#
#
#
#     # Basic workers
#     workers.start_worker(
#         'chaski_root', service_name='chaski_root', port=51110, restart=True
#     )
#
#     # workers.start_worker(
#     #     'main_app', service_name='main_app', port=51101, restart=True
#     # )
#
#     workers.start_worker(
#         'timescaledb_api',
#         service_name='timescaledb_api',
#         image='djangorun',
#         endpoint='/timescaledbapp/',
#         port=51102,
#         restart=True,
#     )
#
#     workers.start_worker('kafka2api', service_name='kafka2api')
#
#
#     workers.start_worker('chaski_root', service_name='chaski_root', port=51110, restart=True)
#     workers.start_worker('chaski_ca', service_name='chaski_ca', port=51111, restart=True)
#     workers.start_worker('chaski_remote', service_name='chaski_ca', port=51112, restart=True)
#     workers.start_worker('chaski2api', service_name='chaski2api', port=51113, restart=True)

    workers.start_worker('chaski_root', service_name='chaski_root', port=51110, restart=True)


if __name__ == '__main__':
    main()

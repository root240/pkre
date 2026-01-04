
import argparse
from .crypto import sha256
from .analysis import shannon_entropy, keyspace

def main():
    p = argparse.ArgumentParser(prog="pkre")
    sub = p.add_subparsers(dest="cmd")

    e = sub.add_parser("entropy")
    e.add_argument("hexdata")

    k = sub.add_parser("keyspace")
    k.add_argument("bits", type=int)

    h = sub.add_parser("hash")
    h.add_argument("text")

    args = p.parse_args()

    if args.cmd == "entropy":
        data = bytes.fromhex(args.hexdata)
        print(shannon_entropy(data))
    elif args.cmd == "keyspace":
        print(keyspace(args.bits))
    elif args.cmd == "hash":
        print(sha256(args.text.encode()))
    else:
        p.print_help()

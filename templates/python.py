#!/usr/bin/python3
from argparse import ArgumentParser as ap


if __name__ == "__main__":
	parser=ap()
	parser.add_argument("--list","-l", action="store_true", help="List Database")
	args=parser.parse_args()




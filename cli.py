#!/usr/bin/env python3
import argparse
import os
import shoebox

def init():
	dir = os.getcwd()

	if shoebox.is_repo(dir):
		print("Already in a repo: {}".format(dir))
		return False
	

def status():
	dir = os.getcwd()

	if not shoebox.is_repo(dir):
		print("You are not inside a shoebox repository.")
		print("Use \"shoebox init\" to create one at {}".format(os.getcwd()))
	else:
		print("You are inside a shoebox repository.")

if __name__ == "__main__":
	parser = argparse.ArgumentParser(
			description="Archive system to manage the lifecycle of data snapshots.")
	parser.add_argument("command", type=str, default="status",
			help="command to execute", nargs="?",
			choices=["status", "init"])

	args = parser.parse_args()
	
	if args.command == "status":
		status()
	elif args.command == "init":
		init()

#!/usr/bin/env python
# coding:UTF-8

import os
import sys
import argparse


def main():
	# parse arg
	parser = argparse.ArgumentParser()
	parser.add_argument("no", help="The No. of leetcode problem starting from 0", type=int)
	args = parser.parse_args()
	if args.no <= 0:
		print "The No. of leetcode problem must larger than 0!"
		return
	leetcodeNo = args.no

	# dynamic import solution
	FILE_SEP = "_"
	bHasModule = False
	cwd = os.path.abspath(os.path.dirname(__file__))
	for file in os.listdir(cwd):
		bIsDir = os.path.isdir(os.path.join(cwd, file))
		bHasModule = file.startswith("%s%s" % (leetcodeNo, FILE_SEP))
		if bIsDir and bHasModule:
			SolutionModule = __import__("%s.Solution" % file, globals(), locals(), ["Solution"])
			SolutionClass = getattr(SolutionModule, "Solution")
			oSolution = SolutionClass()
			oSolution.test()
			break
	if not bHasModule:
		print "no leetcode problem %s!" % leetcodeNo

if __name__ == '__main__':
	main()

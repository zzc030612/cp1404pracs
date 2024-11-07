"""Prac 7, task 'More Guitars!'"""
from prac_07.guitar import Guitar


def main():
    guitars = []
    with open('guitars.csv', 'r') as in_file:
        for line in in_file:
            parts = line.strip().split(',')
            guitar = Guitar(parts[0], parts[1], parts[2])
            guitars.append(guitar)

main()

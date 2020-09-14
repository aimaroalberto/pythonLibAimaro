import argparse

def ciaone():
    print("ciano")

parser = argparse.ArgumentParser(prog = None,#'The name of the program (default: sys.argv[0])',
                                 #usage = 'The string describing the program usage (default: generated from arguments added to parser)',
                                 description = 'Text to display before the argument help (default: none)',
                                 epilog = 'Text to display after the argument help (default: none)',
                                 parents = [],#'A list of ArgumentParser objects whose arguments should also be included',
                                 formatter_class = argparse.RawDescriptionHelpFormatter,# A class for customizing the help output', class argparse.RawDescriptionHelpFormatter
                                                                                                #class argparse.RawTextHelpFormatter
                                                                                                #class argparse.ArgumentDefaultsHelpFormatter
                                                                                                #class argparse.MetavarTypeHelpFormatter
                                 prefix_chars = '-',#- The set of characters that prefix optional arguments (default: ‘-‘)',
                                fromfile_prefix_chars = None, #The set of characters that prefix files from which additional arguments should be read (default: None)',
                                argument_default = None, #The global default value for arguments (default: None)',
                                add_help = True)#Add a -h/--help option to the parser (default: True)

parser.add_argument('integers', metavar='N', type=int, nargs='+',
                    help='an integer for the accumulator')
parser.add_argument('--sum', dest='accumulate', action='store_const',
                    const=sum, default=max,
                    help='sum the integers (default: find the max)')
parser.add_argument('--prod', dest='prodciaone', action='store_const',
                    const=ciaone, default=print,
                    help='sum the integers (default: find the max)')

parser.add_argument('--param', metavar= 'N',dest='variables', type=int, nargs='+',
                    help='sum the integers (default: find the max)')

args = parser.parse_args()
print(args.accumulate(args.integers))
print(args.accumulate(args.variables))
args.prodciaone()




def var():
    cassate(5)
    #il ciccone dietro casa è il mio mostro
    list.append()

def cassate(arg):
    print(arg)



